#!/usr/bin/env python3
"""Repository-wide candidate audit for Core 0.1 G1 legacy-state cleanup.

This tool does not decide canonical mathematical meaning and does not mark G1
as passed. It finds text patterns named by the G1 release gate and classifies
matches conservatively for human review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".py"}
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}

CONTROL_PATHS = {
    "CORE_0.1_COMPLETENESS_CHECKLIST.md",
    "CORE_0.1_COMPLETENESS_CHECKLIST.yaml",
    "docs/audits/CORE_0.1_G1_CONSISTENCY_AUDIT.md",
    "scripts/audit_core_g1_consistency.py",
}

HISTORICAL_MARKERS = (
    "historical",
    "superseded",
    "obsolete",
    "legacy",
    "checkpoint supersedes",
    "this checkpoint supersedes",
)


@dataclass(frozen=True)
class Rule:
    rule_id: str
    label: str
    patterns: tuple[str, ...]


@dataclass(frozen=True)
class Finding:
    rule_id: str
    label: str
    path: str
    line: int
    classification: str
    excerpt: str


RULES = (
    Rule(
        "G1-THREE-STATE-ADMISSIBILITY",
        "three-state admissibility as canonical",
        (
            r"Adm\([^)]*\)\s*∈\s*\{\s*ADMISSIBLE,\s*INADMISSIBLE,\s*UNRESOLVED\s*\}",
            r"\|\s*⊗A\s*\|\s*ADMISSIBLE\s*\|\s*UNRESOLVED\s*\|\s*INADMISSIBLE\s*\|",
            r"BoundaryCompatible\([^)]*\)\s*∈\s*\{\s*ADMISSIBLE,\s*INADMISSIBLE,\s*UNRESOLVED\s*\}",
        ),
    ),
    Rule(
        "G1-FIVE-WITNESS",
        "five-witness boundary model",
        (
            r"\bAll five witness types\b",
            r"\ball five VALID\b",
            r"witness_type\s*∈\s*\{\s*STATE,\s*CONTEXT,\s*AUTHORITY,\s*INVARIANT,\s*PROVENANCE\s*\}",
        ),
    ),
    Rule(
        "G1-IDENTITY-IN-STATE",
        "IDENTITY inside State relation",
        (
            r"STATE\s*->\s*identity\s*/\s*compatibility\s*/\s*authorized projection",
            r"relation_type\s*∈\s*\{\s*IDENTITY,\s*COMPATIBILITY,\s*PROJECTION\s*\}",
        ),
    ),
    Rule(
        "G1-NEGATIVE-EXHAUSTION",
        "negative-exhaustion requirement",
        (
            r"\brequires?\s+(?:prior\s+)?negative exhaustion\b",
            r"\bnegative exhaustion\s+(?:is\s+)?required\b",
            r"\bmust\s+(?:first\s+)?(?:eliminate|exhaust)\s+negative alternatives\b",
        ),
    ),
    Rule(
        "G1-OBSOLETE-BOUNDARY-AGGREGATION",
        "obsolete boundary aggregation",
        (
            r"E_B\s*=\s*<\s*W_state,\s*W_context,\s*W_authority,\s*W_invariant,\s*W_provenance\s*>",
            r"ValidateBoundary\(E_B\)\s*=\s*ValidateWitness\(W_state\)\s*⊗A\s*ValidateWitness\(W_context\)\s*⊗A\s*ValidateWitness\(W_authority\)\s*⊗A\s*ValidateWitness\(W_invariant\)\s*⊗A\s*ValidateWitness\(W_provenance\)",
        ),
    ),
    Rule(
        "G1-THREE-VALUED-WITNESS-VALIDATION",
        "three-valued witness-validation return type",
        (
            r"ValidateWitness\(W\)\s*->\s*\{\s*VALID,\s*INVALID,\s*UNRESOLVED\s*\}",
            r"The typed validator returns VALID, INVALID, or UNRESOLVED",
        ),
    ),
    Rule(
        "EXTRA-THREE-VALUED-ENTAILMENT",
        "three-valued entailment superseded by four-state entailment",
        (
            r"##\s+14\.5\s+Three-valued entailment",
            r"Entail\(R_t,R_u\)\s*∈\s*\{\s*ENTAILS,\s*DOES_NOT_ENTAIL,\s*UNRESOLVED\s*\}",
        ),
    ),
)


def iter_text_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def context_excerpt(text: str, line: int, radius: int = 5) -> str:
    lines = text.splitlines()
    start = max(0, line - 1 - radius)
    end = min(len(lines), line + radius)
    return "\n".join(lines[start:end]).strip()


def heading_scope(text: str, line: int) -> str:
    """Return the active Markdown heading ancestry for a source line."""
    lines = text.splitlines()
    if not lines:
        return ""

    index = min(max(line - 1, 0), len(lines) - 1)
    by_level: dict[int, str] = {}

    for candidate in reversed(lines[: index + 1]):
        match = re.match(r"^(#{1,6})\s+(.+)$", candidate)
        if not match:
            continue

        level = len(match.group(1))
        if level not in by_level:
            by_level[level] = candidate.strip()

        if level == 1:
            break

    return "\n".join(by_level[level] for level in sorted(by_level))


def classify(path: str, text: str, line: int, excerpt: str) -> str:
    if path in CONTROL_PATHS:
        return "CONTROL_REFERENCE"

    scope = "\n".join((heading_scope(text, line), excerpt)).lower()
    if any(marker in scope for marker in HISTORICAL_MARKERS):
        return "MARKED_HISTORICAL"

    return "REVIEW_REQUIRED"


def audit(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    flags = re.IGNORECASE | re.MULTILINE

    for path in sorted(iter_text_files(root)):
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for rule in RULES:
            seen: set[tuple[int, str]] = set()
            for pattern in rule.patterns:
                for match in re.finditer(pattern, text, flags):
                    line = line_number(text, match.start())
                    excerpt = context_excerpt(text, line)
                    key = (line, excerpt)
                    if key in seen:
                        continue
                    seen.add(key)
                    findings.append(
                        Finding(
                            rule_id=rule.rule_id,
                            label=rule.label,
                            path=rel,
                            line=line,
                            classification=classify(rel, text, line, excerpt),
                            excerpt=excerpt,
                        )
                    )

    return sorted(
        findings,
        key=lambda item: (item.path, item.line, item.rule_id),
    )


def summary(findings: list[Finding]) -> dict[str, int]:
    counts = {
        "REVIEW_REQUIRED": 0,
        "MARKED_HISTORICAL": 0,
        "CONTROL_REFERENCE": 0,
    }
    for finding in findings:
        counts[finding.classification] += 1
    return counts


def print_text(findings: list[Finding]) -> None:
    counts = summary(findings)
    print("Core 0.1 G1 consistency candidate audit")
    print(f"review_required={counts['REVIEW_REQUIRED']}")
    print(f"marked_historical={counts['MARKED_HISTORICAL']}")
    print(f"control_reference={counts['CONTROL_REFERENCE']}")
    print()

    for finding in findings:
        print(
            f"[{finding.classification}] "
            f"{finding.rule_id} {finding.path}:{finding.line}"
        )
        print(f"  {finding.label}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of scripts/.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit structured JSON instead of the text summary.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero when unmarked review-required findings exist.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    findings = audit(root)
    counts = summary(findings)

    if args.json:
        print(
            json.dumps(
                {
                    "root": str(root),
                    "summary": counts,
                    "findings": [asdict(item) for item in findings],
                },
                indent=2,
                sort_keys=True,
            )
        )
    else:
        print_text(findings)

    if args.strict and counts["REVIEW_REQUIRED"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
