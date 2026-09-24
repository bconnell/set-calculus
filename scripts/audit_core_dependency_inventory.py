#!/usr/bin/env python3
"""Validate the Core 0.1 machine-readable dependency inventory."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

INVENTORY_PATH = Path("docs/dependency-map/CORE_0.1_DEPENDENCY_INVENTORY.json")
SCHEMA_PATH = Path("docs/dependency-map/CORE_0.1_DEPENDENCY_INVENTORY.schema.json")

REQUIRED_CLASSES = {
    "HARD",
    "STRONG",
    "SUPPORTING",
    "HISTORICAL/CURRICULAR",
}
CONSTRAINT_CLASSES = {"HARD", "STRONG"}
NON_CONSTRAINT_CLASSES = {"SUPPORTING", "HISTORICAL/CURRICULAR"}
VALID_BASES = {"EXPLICIT_GRAPH", "EXPLICIT_NARRATIVE", "WORKING_INFERENCE"}
VALID_ROOT_KINDS = {
    "FOUNDATIONAL_ROOT",
    "PARALLEL_DOMAIN_ROOT",
    "UNRESOLVED_SOURCE_GAP",
}


def load_inventory(root: Path) -> dict[str, Any]:
    return json.loads((root / INVENTORY_PATH).read_text(encoding="utf-8"))


def derive_layers(data: dict[str, Any]) -> tuple[list[list[str]], list[str]]:
    teaching_nodes = {
        node["id"]
        for node in data.get("nodes", [])
        if node.get("include_in_teaching_layers") is True
    }

    indegree = {node_id: 0 for node_id in teaching_nodes}
    adjacency: dict[str, list[str]] = defaultdict(list)

    for edge in data.get("edges", []):
        if edge.get("order_constraint") is not True:
            continue

        source = edge.get("from")
        target = edge.get("to")
        if source not in teaching_nodes or target not in teaching_nodes:
            continue

        adjacency[source].append(target)
        indegree[target] += 1

    remaining = set(teaching_nodes)
    layers: list[list[str]] = []

    while remaining:
        layer = sorted(node_id for node_id in remaining if indegree[node_id] == 0)
        if not layer:
            return layers, sorted(remaining)

        layers.append(layer)
        for node_id in layer:
            remaining.remove(node_id)
            for target in adjacency[node_id]:
                indegree[target] -= 1

    return layers, []


def validate_inventory(
    data: dict[str, Any],
    root: Path | None = None,
) -> list[str]:
    errors: list[str] = []

    allowed_classes = set(data.get("allowed_classes", []))
    if allowed_classes != REQUIRED_CLASSES:
        errors.append(
            "allowed_classes must exactly match the Core E2 vocabulary: "
            + ", ".join(sorted(REQUIRED_CLASSES))
        )

    policy = data.get("topology_policy", {})
    if set(policy.get("constraint_classes", [])) != CONSTRAINT_CLASSES:
        errors.append("topology_policy.constraint_classes must be HARD and STRONG")
    if set(policy.get("non_constraint_classes", [])) != NON_CONSTRAINT_CLASSES:
        errors.append(
            "topology_policy.non_constraint_classes must be SUPPORTING and "
            "HISTORICAL/CURRICULAR"
        )

    nodes = data.get("nodes", [])
    node_ids: list[str] = [node.get("id", "") for node in nodes]
    node_id_set = set(node_ids)

    if len(node_ids) != len(node_id_set):
        errors.append("duplicate node id detected")
    if "" in node_id_set:
        errors.append("node id must not be empty")

    node_by_id = {node.get("id"): node for node in nodes if node.get("id")}

    edges = data.get("edges", [])
    edge_ids: list[str] = [edge.get("id", "") for edge in edges]
    if len(edge_ids) != len(set(edge_ids)):
        errors.append("duplicate edge id detected")
    if "" in set(edge_ids):
        errors.append("edge id must not be empty")

    edge_pairs: set[tuple[str, str]] = set()
    for edge in edges:
        edge_id = edge.get("id", "<missing>")
        source = edge.get("from")
        target = edge.get("to")
        edge_class = edge.get("class")
        order_constraint = edge.get("order_constraint")
        basis = edge.get("basis")

        if source not in node_id_set:
            errors.append(f"{edge_id}: unknown source node {source!r}")
        if target not in node_id_set:
            errors.append(f"{edge_id}: unknown target node {target!r}")
        if source == target:
            errors.append(f"{edge_id}: self-dependency is not allowed")

        pair = (source, target)
        if pair in edge_pairs:
            errors.append(f"duplicate dependency pair detected: {source} -> {target}")
        edge_pairs.add(pair)

        if edge_class not in REQUIRED_CLASSES:
            errors.append(f"{edge_id}: invalid class {edge_class!r}")

        expected_constraint = edge_class in CONSTRAINT_CLASSES
        if order_constraint is not expected_constraint:
            errors.append(
                f"{edge_id}: order_constraint={order_constraint!r} does not match "
                f"class {edge_class!r}"
            )

        if basis not in VALID_BASES:
            errors.append(f"{edge_id}: invalid basis {basis!r}")

        if not str(edge.get("source_anchor", "")).strip():
            errors.append(f"{edge_id}: missing source_anchor")
        if not str(edge.get("rationale", "")).strip():
            errors.append(f"{edge_id}: missing rationale")

        if order_constraint is True:
            source_node = node_by_id.get(source, {})
            target_node = node_by_id.get(target, {})
            if source_node.get("include_in_teaching_layers") is not True:
                errors.append(
                    f"{edge_id}: constraining source is excluded from teaching layers"
                )
            if target_node.get("include_in_teaching_layers") is not True:
                errors.append(
                    f"{edge_id}: constraining target is excluded from teaching layers"
                )

    non_dependencies = data.get("non_dependencies", [])
    nondep_ids = [item.get("id", "") for item in non_dependencies]
    if len(nondep_ids) != len(set(nondep_ids)):
        errors.append("duplicate non-dependency id detected")

    nondep_pairs: set[tuple[str, str]] = set()
    for item in non_dependencies:
        item_id = item.get("id", "<missing>")
        source = item.get("from")
        target = item.get("to")
        pair = (source, target)

        if source not in node_id_set:
            errors.append(f"{item_id}: unknown non-dependency source {source!r}")
        if target not in node_id_set:
            errors.append(f"{item_id}: unknown non-dependency target {target!r}")
        if item.get("result") != "NONE":
            errors.append(f"{item_id}: non-dependency result must be NONE")
        if pair in nondep_pairs:
            errors.append(f"duplicate non-dependency pair detected: {source} -> {target}")
        nondep_pairs.add(pair)
        if pair in edge_pairs:
            errors.append(
                f"{item_id}: pair is both a dependency edge and a non-dependency: "
                f"{source} -> {target}"
            )
        if not str(item.get("source_anchor", "")).strip():
            errors.append(f"{item_id}: missing source_anchor")
        if not str(item.get("rationale", "")).strip():
            errors.append(f"{item_id}: missing rationale")

    open_questions = data.get("open_questions", [])
    question_ids = [item.get("id", "") for item in open_questions]
    if len(question_ids) != len(set(question_ids)):
        errors.append("duplicate open-question id detected")

    for item in open_questions:
        item_id = item.get("id", "<missing>")
        related_nodes = item.get("related_nodes", [])
        if not related_nodes:
            errors.append(f"{item_id}: open question has no related_nodes")
        for node_id in related_nodes:
            if node_id not in node_id_set:
                errors.append(f"{item_id}: unknown related node {node_id!r}")
        if not str(item.get("question", "")).strip():
            errors.append(f"{item_id}: missing question text")
        if not str(item.get("reason", "")).strip():
            errors.append(f"{item_id}: missing reason")

    layers, cyclic_nodes = derive_layers(data)
    if cyclic_nodes:
        errors.append(
            "cycle detected among teaching-order constraints; unresolved nodes: "
            + ", ".join(cyclic_nodes)
        )

    teaching_nodes = {
        node["id"]
        for node in nodes
        if node.get("include_in_teaching_layers") is True
    }

    incoming = {node_id: 0 for node_id in teaching_nodes}
    for edge in edges:
        if edge.get("order_constraint") is True and edge.get("to") in incoming:
            incoming[edge["to"]] += 1
    actual_roots = {node_id for node_id, count in incoming.items() if count == 0}

    declared_roots = data.get("declared_roots", [])
    declared_root_ids = [item.get("node", "") for item in declared_roots]
    if len(declared_root_ids) != len(set(declared_root_ids)):
        errors.append("duplicate declared root detected")

    for item in declared_roots:
        node_id = item.get("node")
        if node_id not in teaching_nodes:
            errors.append(f"declared root is not a teaching-layer node: {node_id!r}")
        if item.get("kind") not in VALID_ROOT_KINDS:
            errors.append(
                f"declared root {node_id!r} has invalid kind {item.get('kind')!r}"
            )
        if not str(item.get("rationale", "")).strip():
            errors.append(f"declared root {node_id!r} is missing rationale")

    declared_root_set = set(declared_root_ids)
    if actual_roots != declared_root_set:
        missing = sorted(actual_roots - declared_root_set)
        extra = sorted(declared_root_set - actual_roots)
        if missing:
            errors.append(
                "undeclared teaching-order roots detected: " + ", ".join(missing)
            )
        if extra:
            errors.append(
                "declared roots have incoming constraints: " + ", ".join(extra)
            )

    if not cyclic_nodes:
        flattened = [node_id for layer in layers for node_id in layer]
        if len(flattened) != len(set(flattened)):
            errors.append("a teaching node appears in more than one derived layer")
        if set(flattened) != teaching_nodes:
            errors.append("derived layers do not cover every teaching-layer node")

    source_document = data.get("source_document")
    if root is not None:
        if not source_document or not (root / source_document).is_file():
            errors.append(f"source_document does not exist: {source_document!r}")
        if not (root / SCHEMA_PATH).is_file():
            errors.append(f"schema file does not exist: {SCHEMA_PATH.as_posix()}")
        else:
            try:
                schema = json.loads(
                    (root / SCHEMA_PATH).read_text(encoding="utf-8")
                )
            except json.JSONDecodeError as exc:
                errors.append(f"schema file is invalid JSON: {exc}")
            else:
                if schema.get("properties", {}).get("schema_version", {}).get(
                    "const"
                ) != data.get("schema_version"):
                    errors.append(
                        "schema_version does not match the schema const value"
                    )

    return errors


def run_self_tests(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    duplicate_id = copy.deepcopy(data)
    duplicate_id["edges"].append(copy.deepcopy(duplicate_id["edges"][0]))
    duplicate_errors = validate_inventory(duplicate_id)
    if not any("duplicate edge id" in error for error in duplicate_errors):
        failures.append("self-test failed: duplicate edge id was not detected")

    duplicate_pair = copy.deepcopy(data)
    duplicate = copy.deepcopy(duplicate_pair["edges"][0])
    duplicate["id"] = "e998"
    duplicate_pair["edges"].append(duplicate)
    duplicate_pair_errors = validate_inventory(duplicate_pair)
    if not any(
        "duplicate dependency pair" in error
        for error in duplicate_pair_errors
    ):
        failures.append("self-test failed: duplicate edge pair was not detected")

    bad_class = copy.deepcopy(data)
    bad_class["edges"][0]["class"] = "SOFT"
    bad_class_errors = validate_inventory(bad_class)
    if not any("invalid class" in error for error in bad_class_errors):
        failures.append("self-test failed: invalid class was not detected")

    cycle = copy.deepcopy(data)
    cycle["edges"].append(
        {
            "id": "e999",
            "from": "second_order_odes",
            "to": "functions_algebra_trigonometry",
            "class": "HARD",
            "order_constraint": True,
            "basis": "EXPLICIT_GRAPH",
            "source_anchor": "self-test",
            "rationale": "Synthetic cycle used only by validator self-test.",
        }
    )
    cycle_errors = validate_inventory(cycle)
    if not any("cycle detected" in error for error in cycle_errors):
        failures.append("self-test failed: cycle was not detected")

    root_drift = copy.deepcopy(data)
    root_drift["edges"] = [
        edge for edge in root_drift["edges"] if edge["id"] != "e001"
    ]
    root_errors = validate_inventory(root_drift)
    if not any("undeclared teaching-order roots" in error for error in root_errors):
        failures.append("self-test failed: root drift was not detected")

    contradictory = copy.deepcopy(data)
    contradictory["non_dependencies"].append(
        {
            "id": "n999",
            "from": "functions_algebra_trigonometry",
            "to": "limits",
            "result": "NONE",
            "source_anchor": "self-test",
            "rationale": "Synthetic contradiction used only by validator self-test.",
        }
    )
    contradictory_errors = validate_inventory(contradictory)
    if not any(
        "both a dependency edge and a non-dependency" in error
        for error in contradictory_errors
    ):
        failures.append(
            "self-test failed: dependency/non-dependency contradiction was not detected"
        )

    return failures


def summary(data: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    edges = data.get("edges", [])
    layers, cyclic_nodes = derive_layers(data)
    return {
        "inventory_errors": len(errors),
        "node_count": len(data.get("nodes", [])),
        "teaching_node_count": sum(
            1
            for node in data.get("nodes", [])
            if node.get("include_in_teaching_layers") is True
        ),
        "edge_count": len(edges),
        "constraining_edges": sum(
            1 for edge in edges if edge.get("order_constraint") is True
        ),
        "supporting_edges": sum(
            1 for edge in edges if edge.get("class") == "SUPPORTING"
        ),
        "historical_edges": sum(
            1
            for edge in edges
            if edge.get("class") == "HISTORICAL/CURRICULAR"
        ),
        "non_dependencies": len(data.get("non_dependencies", [])),
        "layer_count": len(layers) if not cyclic_nodes else None,
        "root_count": len(data.get("declared_roots", [])),
        "open_questions": len(data.get("open_questions", [])),
        "cyclic_nodes": cyclic_nodes,
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
        help="Emit structured JSON validation output.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run synthetic validator mutations that must be rejected.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    data = load_inventory(root)
    errors = validate_inventory(data, root)

    self_test_failures: list[str] = []
    if args.self_test:
        self_test_failures = run_self_tests(data)

    result = summary(data, errors)
    result["errors"] = errors
    result["self_test_failures"] = self_test_failures

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("Core 0.1 dependency inventory audit")
        print(f"inventory_errors={result['inventory_errors']}")
        print(f"node_count={result['node_count']}")
        print(f"teaching_node_count={result['teaching_node_count']}")
        print(f"edge_count={result['edge_count']}")
        print(f"constraining_edges={result['constraining_edges']}")
        print(f"supporting_edges={result['supporting_edges']}")
        print(f"historical_edges={result['historical_edges']}")
        print(f"non_dependencies={result['non_dependencies']}")
        print(f"layer_count={result['layer_count']}")
        print(f"root_count={result['root_count']}")
        print(f"open_questions={result['open_questions']}")
        if args.self_test:
            print(f"self_test_failures={len(self_test_failures)}")
        for error in errors:
            print(f"ERROR: {error}")
        for failure in self_test_failures:
            print(f"SELF_TEST_ERROR: {failure}")

    return 1 if errors or self_test_failures else 0


if __name__ == "__main__":
    sys.exit(main())
