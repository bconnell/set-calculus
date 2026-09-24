#!/usr/bin/env python3
"""Validate the Core 0.1 canonical path index without asserting gate completion."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

INDEX_PATH = Path("docs/set-calculus-core/CORE_0.1_PATH_INDEX.md")
ENTRY_POINTS = (
    Path("README.md"),
    Path("SCOPE.md"),
    Path("docs/set-calculus-core/README.md"),
)
INDEX_LINK_TOKEN = "CORE_0.1_PATH_INDEX.md"
VALID_STATUSES = {"PRESENT", "MISSING_REQUIRED"}

REQUIRED_CATEGORIES = {
    "Core release gate",
    "Core terminology",
    "Active Core formalization",
    "Provenance policy",
    "Machine-readable provenance catalog",
    "Conventional compatibility workspace",
    "Canonical conformance fixtures",
    "Derivative round trip",
    "Definite-integral round trip",
    "First-order ODE round trip",
    "Compatibility report",
}


@dataclass(frozen=True)
class Entry:
    category: str
    status: str
    path: str
    gate_relation: str


def parse_index(text: str) -> list[Entry]:
    entries: list[Entry] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            continue

        category, status, path_cell, relation = cells
        if category in {"Category", "---"} or status == "---":
            continue

        match = re.fullmatch(r"`([^`]+)`", path_cell)
        if not match:
            continue

        entries.append(
            Entry(
                category=category,
                status=status,
                path=match.group(1),
                gate_relation=relation,
            )
        )
    return entries


def validate(root: Path) -> dict[str, object]:
    errors: list[str] = []
    index_file = root / INDEX_PATH

    if not index_file.is_file():
        return {
            "errors": [f"missing index: {INDEX_PATH.as_posix()}"],
            "present_entries": 0,
            "missing_required_entries": 0,
            "entry_points_linked": 0,
            "entry_points_total": len(ENTRY_POINTS),
        }

    entries = parse_index(index_file.read_text(encoding="utf-8"))
    by_category: dict[str, Entry] = {}

    for entry in entries:
        if entry.category in by_category:
            errors.append(f"duplicate category: {entry.category}")
        else:
            by_category[entry.category] = entry

        if entry.status not in VALID_STATUSES:
            errors.append(
                f"invalid status for {entry.category}: {entry.status}"
            )
            continue

        candidate = root / entry.path
        exists = candidate.exists()

        if entry.status == "PRESENT" and not exists:
            errors.append(
                f"PRESENT path does not exist: {entry.category} -> {entry.path}"
            )

        if entry.status == "MISSING_REQUIRED" and exists:
            errors.append(
                "MISSING_REQUIRED path now exists; update the index: "
                f"{entry.category} -> {entry.path}"
            )

    missing_categories = sorted(REQUIRED_CATEGORIES - set(by_category))
    for category in missing_categories:
        errors.append(f"required navigation category omitted: {category}")

    linked = 0
    for entry_point in ENTRY_POINTS:
        full_path = root / entry_point
        if not full_path.is_file():
            errors.append(f"missing G2 entry point: {entry_point.as_posix()}")
            continue

        content = full_path.read_text(encoding="utf-8")
        if INDEX_LINK_TOKEN not in content:
            errors.append(
                f"entry point does not link to canonical path index: "
                f"{entry_point.as_posix()}"
            )
        else:
            linked += 1

    present = sum(1 for entry in entries if entry.status == "PRESENT")
    missing = sum(
        1 for entry in entries if entry.status == "MISSING_REQUIRED"
    )

    return {
        "errors": errors,
        "present_entries": present,
        "missing_required_entries": missing,
        "entry_points_linked": linked,
        "entry_points_total": len(ENTRY_POINTS),
        "entries": [asdict(entry) for entry in entries],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable validation output.",
    )
    args = parser.parse_args()

    result = validate(args.root.resolve())

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("Core 0.1 G2 canonical path-index audit")
        print(f"index_errors={len(result['errors'])}")
        print(f"present_entries={result['present_entries']}")
        print(
            "missing_required_entries="
            f"{result['missing_required_entries']}"
        )
        print(
            "entry_points_linked="
            f"{result['entry_points_linked']}/"
            f"{result['entry_points_total']}"
        )
        for error in result["errors"]:
            print(f"ERROR: {error}")

    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
