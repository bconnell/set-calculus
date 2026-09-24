#!/usr/bin/env python3
"""Validate Core 0.1 E1 initial-family coverage against the repository README."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

COVERAGE_PATH = Path("docs/dependency-map/CORE_0.1_E1_COVERAGE.json")
COVERAGE_SCHEMA_PATH = Path("docs/dependency-map/CORE_0.1_E1_COVERAGE.schema.json")
INVENTORY_PATH = Path("docs/dependency-map/CORE_0.1_DEPENDENCY_INVENTORY.json")
README_PATH = Path("docs/dependency-map/README.md")
VALID_STATUSES = {"REPRESENTED", "OPEN_GAP"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_initial_families(readme: str) -> list[str]:
    lines = readme.splitlines()
    try:
        start = lines.index("## Initial concept families") + 1
    except ValueError as exc:
        raise ValueError("missing Initial concept families heading") from exc

    families: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        stripped = line.strip()
        if stripped.startswith("- "):
            families.append(stripped[2:].strip())

    if not families:
        raise ValueError("initial concept-family list is empty")
    return families


def validate(
    coverage: dict[str, Any],
    inventory: dict[str, Any],
    readme_text: str,
    root: Path | None = None,
) -> list[str]:
    errors: list[str] = []

    try:
        source_families = read_initial_families(readme_text)
    except ValueError as exc:
        return [str(exc)]

    if len(source_families) != len(set(source_families)):
        errors.append("README initial concept-family list contains duplicates")

    targets = coverage.get("targets", [])
    target_names = [target.get("name", "") for target in targets]

    if len(target_names) != len(set(target_names)):
        errors.append("coverage map contains duplicate target names")

    if target_names != source_families:
        missing = [name for name in source_families if name not in target_names]
        extra = [name for name in target_names if name not in source_families]
        if missing:
            errors.append("coverage targets missing README families: " + ", ".join(missing))
        if extra:
            errors.append("coverage targets not present in README list: " + ", ".join(extra))
        if not missing and not extra:
            errors.append("coverage target order differs from README initial-family order")

    node_ids = {node.get("id") for node in inventory.get("nodes", [])}
    for target in targets:
        name = target.get("name", "<missing>")
        status = target.get("status")
        mapped = target.get("node_ids", [])

        if status not in VALID_STATUSES:
            errors.append(f"{name}: invalid coverage status {status!r}")
        if not mapped:
            errors.append(f"{name}: node_ids must not be empty")
        if len(mapped) != len(set(mapped)):
            errors.append(f"{name}: duplicate node_ids")
        for node_id in mapped:
            if node_id not in node_ids:
                errors.append(f"{name}: unknown inventory node {node_id!r}")
        if not str(target.get("rationale", "")).strip():
            errors.append(f"{name}: missing rationale")

    if coverage.get("source_list_path") != README_PATH.as_posix():
        errors.append("source_list_path must point to docs/dependency-map/README.md")
    if coverage.get("source_heading") != "Initial concept families":
        errors.append("source_heading must be Initial concept families")
    if coverage.get("status") != "PROVISIONAL_RESEARCH":
        errors.append("coverage status must remain PROVISIONAL_RESEARCH")

    if root is not None:
        if not (root / COVERAGE_SCHEMA_PATH).is_file():
            errors.append(f"missing coverage schema: {COVERAGE_SCHEMA_PATH.as_posix()}")
        else:
            try:
                schema = load_json(root / COVERAGE_SCHEMA_PATH)
            except json.JSONDecodeError as exc:
                errors.append(f"coverage schema is invalid JSON: {exc}")
            else:
                version_const = (
                    schema.get("properties", {})
                    .get("schema_version", {})
                    .get("const")
                )
                if version_const != coverage.get("schema_version"):
                    errors.append("coverage schema_version does not match schema const")

    return errors


def run_self_tests(
    coverage: dict[str, Any],
    inventory: dict[str, Any],
    readme_text: str,
) -> list[str]:
    failures: list[str] = []

    missing_target = copy.deepcopy(coverage)
    missing_target["targets"] = missing_target["targets"][:-1]
    errs = validate(missing_target, inventory, readme_text)
    if not any("missing README families" in error for error in errs):
        failures.append("self-test failed: missing coverage target was not detected")

    unknown_node = copy.deepcopy(coverage)
    unknown_node["targets"][0]["node_ids"] = ["node_that_does_not_exist"]
    errs = validate(unknown_node, inventory, readme_text)
    if not any("unknown inventory node" in error for error in errs):
        failures.append("self-test failed: unknown mapped node was not detected")

    duplicate_target = copy.deepcopy(coverage)
    duplicate_target["targets"].append(copy.deepcopy(duplicate_target["targets"][0]))
    errs = validate(duplicate_target, inventory, readme_text)
    if not any("duplicate target names" in error for error in errs):
        failures.append("self-test failed: duplicate target was not detected")

    bad_order = copy.deepcopy(coverage)
    bad_order["targets"][0], bad_order["targets"][1] = (
        bad_order["targets"][1],
        bad_order["targets"][0],
    )
    errs = validate(bad_order, inventory, readme_text)
    if not any("order differs" in error for error in errs):
        failures.append("self-test failed: README-order drift was not detected")

    return failures


def summarize(coverage: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    targets = coverage.get("targets", [])
    represented = sum(1 for target in targets if target.get("status") == "REPRESENTED")
    open_gaps = sum(1 for target in targets if target.get("status") == "OPEN_GAP")
    mapped_nodes = {
        node_id
        for target in targets
        for node_id in target.get("node_ids", [])
    }
    return {
        "coverage_errors": len(errors),
        "coverage_targets": len(targets),
        "represented_targets": represented,
        "open_gap_targets": open_gaps,
        "mapped_node_count": len(mapped_nodes),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root.",
    )
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    coverage = load_json(root / COVERAGE_PATH)
    inventory = load_json(root / INVENTORY_PATH)
    readme_text = (root / README_PATH).read_text(encoding="utf-8")

    errors = validate(coverage, inventory, readme_text, root)
    self_test_failures = (
        run_self_tests(coverage, inventory, readme_text)
        if args.self_test
        else []
    )
    result = summarize(coverage, errors)
    result["errors"] = errors
    result["self_test_failures"] = self_test_failures

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("Core 0.1 E1 initial-family coverage audit")
        print(f"coverage_errors={result['coverage_errors']}")
        print(f"coverage_targets={result['coverage_targets']}")
        print(f"represented_targets={result['represented_targets']}")
        print(f"open_gap_targets={result['open_gap_targets']}")
        print(f"mapped_node_count={result['mapped_node_count']}")
        if args.self_test:
            print(f"self_test_failures={len(self_test_failures)}")
        for error in errors:
            print(f"ERROR: {error}")
        for failure in self_test_failures:
            print(f"SELF_TEST_ERROR: {failure}")

    return 1 if errors or self_test_failures else 0


if __name__ == "__main__":
    sys.exit(main())
