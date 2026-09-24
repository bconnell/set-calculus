#!/usr/bin/env python3
"""Validate the provisional E2 dependency-class example table."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

GRAPH_PATH = Path("docs/dependency-map/001-conventional-calculus-prerequisite-graph.md")
VALID_CLASSES = {
    "HARD",
    "STRONG",
    "SUPPORTING",
    "HISTORICAL/CURRICULAR",
}
EXPECTED_EXAMPLE_EDGES = {
    "limits -> derivative definition",
    "definite integral -> Fundamental Theorem",
    "basic integration -> separable first-order ODEs",
    "power series -> series solutions of ODEs",
    "linear algebra -> eigenvalue solution of ODE systems",
    "Calc III as a whole -> first-order ODEs",
    "multivariable calculus -> PDE methods",
}
EXPECTED_NON_DEPENDENCY = "vector calculus -> ordinary first-order ODEs"


def parse_table(lines: list[str], start: int, columns: int) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines[start:]:
        if not line.startswith("|"):
            if rows:
                break
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != columns:
            continue
        if all(set(cell) <= {"-", ":"} for cell in cells):
            continue
        rows.append(cells)
    return rows


def find_line(lines: list[str], text: str) -> int:
    for index, line in enumerate(lines):
        if line.strip() == text:
            return index + 1
    return -1


def validate(root: Path) -> dict[str, object]:
    errors: list[str] = []
    graph = root / GRAPH_PATH
    if not graph.is_file():
        return {
            "errors": [f"missing graph: {GRAPH_PATH.as_posix()}"],
            "classified_edges": 0,
            "non_dependency_observations": 0,
        }

    lines = graph.read_text(encoding="utf-8").splitlines()

    class_marker = (
        "Example provisional classifications normalized to the Core 0.1 "
        "E2 vocabulary:"
    )
    class_start = find_line(lines, class_marker)
    if class_start < 0:
        errors.append("missing normalized provisional classification marker")
        class_rows: list[list[str]] = []
    else:
        class_rows = parse_table(lines, class_start, 3)

    if class_rows and class_rows[0][0] == "Dependency":
        class_rows = class_rows[1:]

    seen: set[str] = set()
    for row in class_rows:
        dependency, edge_class, rationale = row
        if dependency in seen:
            errors.append(f"duplicate dependency row: {dependency}")
        seen.add(dependency)

        if edge_class not in VALID_CLASSES:
            errors.append(
                f"invalid E2 class for {dependency}: {edge_class}"
            )

        if not rationale:
            errors.append(f"missing rationale for {dependency}")

    missing_edges = sorted(EXPECTED_EXAMPLE_EDGES - seen)
    extra_edges = sorted(seen - EXPECTED_EXAMPLE_EDGES)
    for edge in missing_edges:
        errors.append(f"expected provisional edge missing: {edge}")
    for edge in extra_edges:
        errors.append(f"unexpected provisional edge in normalized table: {edge}")

    non_dep_marker = "Explicit non-dependency observation:"
    non_dep_start = find_line(lines, non_dep_marker)
    if non_dep_start < 0:
        errors.append("missing explicit non-dependency section")
        non_dep_rows: list[list[str]] = []
    else:
        non_dep_rows = parse_table(lines, non_dep_start, 3)

    if non_dep_rows and non_dep_rows[0][0] == "Relationship tested":
        non_dep_rows = non_dep_rows[1:]

    matching_non_dep = [
        row
        for row in non_dep_rows
        if row[0] == EXPECTED_NON_DEPENDENCY
    ]
    if len(matching_non_dep) != 1:
        errors.append(
            "expected exactly one vector-calculus/first-order-ODE "
            "non-dependency observation"
        )
    elif matching_non_dep[0][1] != "NONE":
        errors.append(
            "non-dependency observation must retain result NONE outside "
            "the E2 dependency-class table"
        )

    return {
        "errors": errors,
        "classified_edges": len(class_rows),
        "non_dependency_observations": len(non_dep_rows),
        "valid_classes": sorted(VALID_CLASSES),
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
        help="Emit machine-readable output.",
    )
    args = parser.parse_args()

    result = validate(args.root.resolve())

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("Dependency E2 provisional-class vocabulary audit")
        print(f"class_errors={len(result['errors'])}")
        print(f"classified_edges={result['classified_edges']}")
        print(
            "non_dependency_observations="
            f"{result['non_dependency_observations']}"
        )
        for error in result["errors"]:
            print(f"ERROR: {error}")

    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
