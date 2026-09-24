#!/usr/bin/env python3
"""Validate the Core 0.1 E3 teaching hypothesis against the dependency inventory."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from audit_core_dependency_inventory import derive_layers, load_inventory, validate_inventory

HYPOTHESIS_PATH = Path("docs/dependency-map/CORE_0.1_E3_TEACHING_HYPOTHESIS.json")
HYPOTHESIS_SCHEMA_PATH = Path("docs/dependency-map/CORE_0.1_E3_TEACHING_HYPOTHESIS.schema.json")

EXPECTED_WITHIN_STAGE = "UNORDERED_NOT_MATHEMATICALLY_FORCED"
EXPECTED_STATUS = "PROVISIONAL_HYPOTHESIS"
EXPECTED_GATE_CLAIM = "NOT_ASSERTED"


def load_hypothesis(root: Path) -> dict[str, Any]:
    return json.loads((root / HYPOTHESIS_PATH).read_text(encoding="utf-8"))


def validate(
    hypothesis: dict[str, Any],
    inventory: dict[str, Any],
    root: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_inventory(inventory, root))

    layers, cyclic_nodes = derive_layers(inventory)
    if cyclic_nodes:
        errors.append(
            "cannot validate E3 hypothesis while inventory contains a cycle: "
            + ", ".join(cyclic_nodes)
        )
        return errors

    if hypothesis.get("status") != EXPECTED_STATUS:
        errors.append("E3 hypothesis status must remain PROVISIONAL_HYPOTHESIS")
    if hypothesis.get("gate_claim") != EXPECTED_GATE_CLAIM:
        errors.append("E3 hypothesis gate_claim must remain NOT_ASSERTED")

    policy = hypothesis.get("derivation_policy", {})
    if set(policy.get("constraining_classes", [])) != {"HARD", "STRONG"}:
        errors.append("E3 constraining classes must be exactly HARD and STRONG")
    if set(policy.get("non_constraining_classes", [])) != {
        "SUPPORTING",
        "HISTORICAL/CURRICULAR",
    }:
        errors.append(
            "E3 non-constraining classes must be SUPPORTING and "
            "HISTORICAL/CURRICULAR"
        )
    if policy.get("within_stage_ordering") != EXPECTED_WITHIN_STAGE:
        errors.append(
            "E3 policy must keep within-stage order explicitly non-forced"
        )
    if policy.get("course_bundle_policy") != "EXCLUDED_FROM_TEACHING_STAGES":
        errors.append("E3 course-bundle policy must exclude curricular containers")

    stages = hypothesis.get("stages", [])
    if [stage.get("stage") for stage in stages] != list(range(len(stages))):
        errors.append("E3 stage numbers must be contiguous and zero-based")

    if len(stages) != len(layers):
        errors.append(
            f"E3 stage count {len(stages)} differs from derived layer count {len(layers)}"
        )

    seen_nodes: list[str] = []
    stage_by_node: dict[str, int] = {}

    for index, stage in enumerate(stages):
        if stage.get("within_stage_ordering") != EXPECTED_WITHIN_STAGE:
            errors.append(
                f"stage {index}: within-stage ordering must remain non-forced"
            )

        node_ids = stage.get("node_ids", [])
        if len(node_ids) != len(set(node_ids)):
            errors.append(f"stage {index}: duplicate node id detected")

        seen_nodes.extend(node_ids)
        for node_id in node_ids:
            if node_id in stage_by_node:
                errors.append(
                    f"node appears in more than one stage: {node_id}"
                )
            stage_by_node[node_id] = index

        if index < len(layers) and set(node_ids) != set(layers[index]):
            missing = sorted(set(layers[index]) - set(node_ids))
            extra = sorted(set(node_ids) - set(layers[index]))
            if missing:
                errors.append(
                    f"stage {index}: missing derived nodes: " + ", ".join(missing)
                )
            if extra:
                errors.append(
                    f"stage {index}: contains nodes not in derived layer: "
                    + ", ".join(extra)
                )

    teaching_nodes = {
        node["id"]
        for node in inventory.get("nodes", [])
        if node.get("include_in_teaching_layers") is True
    }
    if set(seen_nodes) != teaching_nodes:
        omitted = sorted(teaching_nodes - set(seen_nodes))
        extra = sorted(set(seen_nodes) - teaching_nodes)
        if omitted:
            errors.append("E3 hypothesis omits teaching nodes: " + ", ".join(omitted))
        if extra:
            errors.append(
                "E3 hypothesis includes non-teaching nodes: " + ", ".join(extra)
            )

    excluded = set(hypothesis.get("excluded_curricular_containers", []))
    expected_excluded = {
        node["id"]
        for node in inventory.get("nodes", [])
        if node.get("family") == "CURRICULAR_CONTAINER"
    }
    if excluded != expected_excluded:
        errors.append(
            "excluded curricular containers do not match inventory containers"
        )
    leaked = sorted(excluded & set(seen_nodes))
    if leaked:
        errors.append(
            "curricular containers leaked into teaching stages: " + ", ".join(leaked)
        )

    for edge in inventory.get("edges", []):
        if edge.get("order_constraint") is not True:
            continue

        source = edge.get("from")
        target = edge.get("to")
        if source not in teaching_nodes or target not in teaching_nodes:
            continue

        source_stage = stage_by_node.get(source)
        target_stage = stage_by_node.get(target)
        if source_stage is None or target_stage is None:
            continue

        if source_stage >= target_stage:
            errors.append(
                f"{edge.get('id')}: constraining edge does not point forward "
                f"({source} stage {source_stage} -> {target} stage {target_stage})"
            )

    inventory_question_ids = {
        item.get("id") for item in inventory.get("open_questions", [])
    }
    referenced_questions = set(hypothesis.get("unresolved_questions", []))
    if referenced_questions != inventory_question_ids:
        errors.append(
            "E3 unresolved_questions must exactly mirror inventory open-question ids"
        )

    notes = hypothesis.get("hypothesis_notes", [])
    note_ids = [item.get("id", "") for item in notes]
    if len(note_ids) != len(set(note_ids)):
        errors.append("duplicate E3 hypothesis-note id detected")
    if not any(item.get("kind") == "DERIVED_CONSTRAINT" for item in notes):
        errors.append("E3 hypothesis must include at least one DERIVED_CONSTRAINT note")
    if not any(item.get("kind") == "TEACHING_HYPOTHESIS" for item in notes):
        errors.append("E3 hypothesis must include at least one TEACHING_HYPOTHESIS note")

    if root is not None:
        if not (root / HYPOTHESIS_SCHEMA_PATH).is_file():
            errors.append(
                f"missing E3 schema: {HYPOTHESIS_SCHEMA_PATH.as_posix()}"
            )
        else:
            try:
                schema = json.loads(
                    (root / HYPOTHESIS_SCHEMA_PATH).read_text(encoding="utf-8")
                )
            except json.JSONDecodeError as exc:
                errors.append(f"E3 schema is invalid JSON: {exc}")
            else:
                version_const = (
                    schema.get("properties", {})
                    .get("schema_version", {})
                    .get("const")
                )
                if version_const != hypothesis.get("schema_version"):
                    errors.append(
                        "E3 hypothesis schema_version does not match schema const"
                    )

    return errors


def run_self_tests(
    hypothesis: dict[str, Any],
    inventory: dict[str, Any],
) -> list[str]:
    failures: list[str] = []

    moved = copy.deepcopy(hypothesis)
    moved["stages"][0]["node_ids"].append(
        moved["stages"][1]["node_ids"].pop(0)
    )
    errs = validate(moved, inventory)
    if not any("derived nodes" in error or "not in derived layer" in error for error in errs):
        failures.append("self-test failed: wrong-stage node was not detected")

    duplicated = copy.deepcopy(hypothesis)
    duplicated["stages"][1]["node_ids"].append(
        duplicated["stages"][0]["node_ids"][0]
    )
    errs = validate(duplicated, inventory)
    if not any("more than one stage" in error for error in errs):
        failures.append("self-test failed: duplicate staged node was not detected")

    ordered = copy.deepcopy(hypothesis)
    ordered["stages"][0]["within_stage_ordering"] = "ORDERED"
    errs = validate(ordered, inventory)
    if not any("within-stage ordering" in error for error in errs):
        failures.append("self-test failed: forced within-stage order was not detected")

    leaked = copy.deepcopy(hypothesis)
    leaked["stages"][0]["node_ids"].append("calc_iii_course_bundle")
    errs = validate(leaked, inventory)
    if not any("curricular containers leaked" in error for error in errs):
        failures.append("self-test failed: curricular-container leak was not detected")

    reversed_edge = copy.deepcopy(hypothesis)
    source = "functions_algebra_trigonometry"
    target = "limits"
    source_stage = next(
        index
        for index, stage in enumerate(reversed_edge["stages"])
        if source in stage["node_ids"]
    )
    target_stage = next(
        index
        for index, stage in enumerate(reversed_edge["stages"])
        if target in stage["node_ids"]
    )
    reversed_edge["stages"][source_stage]["node_ids"].remove(source)
    reversed_edge["stages"][target_stage]["node_ids"].remove(target)
    reversed_edge["stages"][source_stage]["node_ids"].append(target)
    reversed_edge["stages"][target_stage]["node_ids"].append(source)
    errs = validate(reversed_edge, inventory)
    if not any("does not point forward" in error for error in errs):
        failures.append("self-test failed: reversed dependency was not detected")

    return failures


def summarize(
    hypothesis: dict[str, Any],
    inventory: dict[str, Any],
    errors: list[str],
) -> dict[str, Any]:
    stages = hypothesis.get("stages", [])
    teaching_nodes = [
        node
        for node in inventory.get("nodes", [])
        if node.get("include_in_teaching_layers") is True
    ]
    constraining_edges = [
        edge
        for edge in inventory.get("edges", [])
        if edge.get("order_constraint") is True
    ]
    return {
        "e3_errors": len(errors),
        "stage_count": len(stages),
        "staged_node_count": sum(len(stage.get("node_ids", [])) for stage in stages),
        "teaching_node_count": len(teaching_nodes),
        "constraining_edge_count": len(constraining_edges),
        "excluded_curricular_containers": len(
            hypothesis.get("excluded_curricular_containers", [])
        ),
        "hypothesis_note_count": len(hypothesis.get("hypothesis_notes", [])),
        "unresolved_question_count": len(
            hypothesis.get("unresolved_questions", [])
        ),
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
    inventory = load_inventory(root)
    hypothesis = load_hypothesis(root)

    errors = validate(hypothesis, inventory, root)
    self_test_failures = (
        run_self_tests(hypothesis, inventory)
        if args.self_test
        else []
    )

    result = summarize(hypothesis, inventory, errors)
    result["errors"] = errors
    result["self_test_failures"] = self_test_failures

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("Core 0.1 E3 teaching-hypothesis audit")
        print(f"e3_errors={result['e3_errors']}")
        print(f"stage_count={result['stage_count']}")
        print(f"staged_node_count={result['staged_node_count']}")
        print(f"teaching_node_count={result['teaching_node_count']}")
        print(f"constraining_edge_count={result['constraining_edge_count']}")
        print(
            "excluded_curricular_containers="
            f"{result['excluded_curricular_containers']}"
        )
        print(f"hypothesis_note_count={result['hypothesis_note_count']}")
        print(
            "unresolved_question_count="
            f"{result['unresolved_question_count']}"
        )
        if args.self_test:
            print(f"self_test_failures={len(self_test_failures)}")
        for error in errors:
            print(f"ERROR: {error}")
        for failure in self_test_failures:
            print(f"SELF_TEST_ERROR: {failure}")

    return 1 if errors or self_test_failures else 0


if __name__ == "__main__":
    sys.exit(main())
