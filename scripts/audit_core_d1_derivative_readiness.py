#!/usr/bin/env python3
"""Audit D1 derivative compatibility readiness without manufacturing Set Calculus semantics."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

RECORD_PATH = Path("docs/conventional-calculus/examples/derivative/record.json")
SCHEMA_PATH = Path("docs/conventional-calculus/COMPATIBILITY_RECORD.schema.json")
CHECKLIST_PATH = Path("CORE_0.1_COMPLETENESS_CHECKLIST.md")
COMPATIBILITY_README_PATH = Path("docs/conventional-calculus/README.md")
EXAMPLE_README_PATH = Path("docs/conventional-calculus/examples/derivative/README.md")

EXPECTED_STATEMENT = "f(x)=x^2"
EXPECTED_RESULT = "f'(x)=2x"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def conventional_baseline() -> str:
    """Differentiate x^2 as a coefficient vector [0, 0, 1]."""
    coefficients = [0, 0, 1]
    derivative = [
        exponent * coefficient
        for exponent, coefficient in enumerate(coefficients)
        if exponent > 0
    ]
    if derivative != [0, 2]:
        raise AssertionError(f"unexpected derivative coefficients: {derivative}")
    return EXPECTED_RESULT


def validate(record: dict[str, Any], root: Path | None = None) -> list[str]:
    errors: list[str] = []

    if record.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if record.get("example_id") != "D1-derivative-x-squared":
        errors.append("unexpected D1 example_id")
    if record.get("checklist_gate") != "D1":
        errors.append("checklist_gate must be D1")
    if record.get("gate_claim") != "NOT_ASSERTED":
        errors.append("contributor record must not assert D1 PASS")

    conventional = record.get("conventional", {})
    if conventional.get("statement") != EXPECTED_STATEMENT:
        errors.append(
            f"conventional statement must remain {EXPECTED_STATEMENT}"
        )
    if conventional.get("result") != EXPECTED_RESULT:
        errors.append(f"conventional result must remain {EXPECTED_RESULT}")
    if conventional_baseline() != conventional.get("result"):
        errors.append("executable conventional baseline disagrees with record")
    if not str(conventional.get("verification", "")).strip():
        errors.append("conventional verification text is missing")

    artifact_status = record.get("artifact_status")
    set_calculus = record.get("set_calculus", {})
    representation_status = set_calculus.get("representation_status")
    representation = set_calculus.get("representation")
    transform_status = set_calculus.get("transform_resolution_status")
    transform_resolution = set_calculus.get("transform_resolution")
    mapped = record.get("mapped_conventional_result")
    equivalence = record.get("equivalence")
    blocking_reason = record.get("blocking_reason")

    if artifact_status == "BLOCKED_PENDING_CANONICAL_MAPPING":
        if representation_status != "MISSING_CANONICAL_SPEC":
            errors.append(
                "blocked record must mark representation as MISSING_CANONICAL_SPEC"
            )
        if representation is not None:
            errors.append("blocked record must not contain a Set Calculus representation")
        if transform_status != "MISSING_CANONICAL_SPEC":
            errors.append(
                "blocked record must mark transform/resolution as MISSING_CANONICAL_SPEC"
            )
        if transform_resolution is not None:
            errors.append(
                "blocked record must not contain transform/resolution semantics"
            )
        if mapped is not None:
            errors.append("blocked record must not claim a mapped conventional result")
        if equivalence != "UNDETERMINED":
            errors.append("blocked record equivalence must remain UNDETERMINED")
        if not str(blocking_reason or "").strip():
            errors.append("blocked record requires an explicit blocking_reason")
    elif artifact_status == "CANDIDATE_MAPPING":
        if representation_status != "CANDIDATE" or not isinstance(
            representation, dict
        ):
            errors.append(
                "candidate mapping requires a non-null candidate representation"
            )
        if transform_status != "CANDIDATE" or not isinstance(
            transform_resolution, dict
        ):
            errors.append(
                "candidate mapping requires non-null candidate transform/resolution"
            )
        if mapped != EXPECTED_RESULT:
            errors.append(
                "candidate D1 mapping must preserve the valid conventional result"
            )
        if equivalence != "EQUIVALENT":
            errors.append("candidate D1 mapping must classify as EQUIVALENT")
    else:
        errors.append(f"unsupported artifact_status: {artifact_status!r}")

    provenance = record.get("provenance", [])
    if not provenance:
        errors.append("compatibility record must preserve provenance")

    if root is not None:
        required_paths = [
            RECORD_PATH,
            SCHEMA_PATH,
            CHECKLIST_PATH,
            COMPATIBILITY_README_PATH,
            EXAMPLE_README_PATH,
        ]
        for path in required_paths:
            if not (root / path).is_file():
                errors.append(f"required D1 readiness path missing: {path.as_posix()}")

        if (root / CHECKLIST_PATH).is_file():
            checklist = (root / CHECKLIST_PATH).read_text(encoding="utf-8")
            if EXPECTED_STATEMENT not in checklist:
                errors.append("D1 checklist no longer contains expected statement")
            if EXPECTED_RESULT not in checklist:
                errors.append("D1 checklist no longer contains expected result")

        for item in provenance:
            path_text = item.get("path")
            if not path_text or not (root / path_text).is_file():
                errors.append(
                    f"provenance path does not exist: {path_text!r}"
                )

        if (root / SCHEMA_PATH).is_file():
            try:
                schema = load_json(root / SCHEMA_PATH)
            except json.JSONDecodeError as exc:
                errors.append(f"compatibility schema is invalid JSON: {exc}")
            else:
                version_const = (
                    schema.get("properties", {})
                    .get("schema_version", {})
                    .get("const")
                )
                if version_const != record.get("schema_version"):
                    errors.append(
                        "record schema_version does not match schema const"
                    )

        if (root / EXAMPLE_README_PATH).is_file():
            example_readme = (root / EXAMPLE_README_PATH).read_text(
                encoding="utf-8"
            )
            if "not asserted" not in example_readme.lower():
                errors.append(
                    "D1 readiness README must state that the gate claim is not asserted"
                )
            if "blocked" not in example_readme.lower():
                errors.append(
                    "D1 readiness README must state the current blocked condition"
                )

    return errors


def run_self_tests(record: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    wrong_result = copy.deepcopy(record)
    wrong_result["conventional"]["result"] = "f'(x)=3x"
    errs = validate(wrong_result)
    if not any("conventional result" in error for error in errs):
        failures.append(
            "self-test failed: changed conventional result was not detected"
        )

    false_pass = copy.deepcopy(record)
    false_pass["gate_claim"] = "PASS"
    errs = validate(false_pass)
    if not any("must not assert D1 PASS" in error for error in errs):
        failures.append("self-test failed: false D1 PASS was not detected")

    fake_blocked_mapping = copy.deepcopy(record)
    fake_blocked_mapping["mapped_conventional_result"] = EXPECTED_RESULT
    errs = validate(fake_blocked_mapping)
    if not any("must not claim a mapped" in error for error in errs):
        failures.append(
            "self-test failed: blocked record mapping claim was not detected"
        )

    wrong_candidate = copy.deepcopy(record)
    wrong_candidate["artifact_status"] = "CANDIDATE_MAPPING"
    wrong_candidate["set_calculus"]["representation_status"] = "CANDIDATE"
    wrong_candidate["set_calculus"]["representation"] = {"placeholder": True}
    wrong_candidate["set_calculus"]["transform_resolution_status"] = "CANDIDATE"
    wrong_candidate["set_calculus"]["transform_resolution"] = {
        "placeholder": True
    }
    wrong_candidate["mapped_conventional_result"] = "f'(x)=3x"
    wrong_candidate["equivalence"] = "DIFFERENT"
    errs = validate(wrong_candidate)
    if not any("must preserve the valid conventional result" in error for error in errs):
        failures.append(
            "self-test failed: incompatible candidate mapping was not detected"
        )

    missing_provenance = copy.deepcopy(record)
    missing_provenance["provenance"] = []
    errs = validate(missing_provenance)
    if not any("preserve provenance" in error for error in errs):
        failures.append("self-test failed: missing provenance was not detected")

    return failures


def summarize(record: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    set_calculus = record.get("set_calculus", {})
    return {
        "d1_readiness_errors": len(errors),
        "conventional_baseline_verified": conventional_baseline()
        == record.get("conventional", {}).get("result"),
        "artifact_status": record.get("artifact_status"),
        "gate_claim": record.get("gate_claim"),
        "representation_status": set_calculus.get("representation_status"),
        "transform_resolution_status": set_calculus.get(
            "transform_resolution_status"
        ),
        "mapped_result_present": record.get("mapped_conventional_result")
        is not None,
        "provenance_entries": len(record.get("provenance", [])),
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
    record = load_json(root / RECORD_PATH)
    errors = validate(record, root)
    self_test_failures = run_self_tests(record) if args.self_test else []

    result = summarize(record, errors)
    result["errors"] = errors
    result["self_test_failures"] = self_test_failures

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("Core 0.1 D1 derivative compatibility readiness audit")
        print(f"d1_readiness_errors={result['d1_readiness_errors']}")
        print(
            "conventional_baseline_verified="
            f"{int(result['conventional_baseline_verified'])}"
        )
        print(f"artifact_status={result['artifact_status']}")
        print(f"gate_claim={result['gate_claim']}")
        print(f"representation_status={result['representation_status']}")
        print(
            "transform_resolution_status="
            f"{result['transform_resolution_status']}"
        )
        print(
            "mapped_result_present="
            f"{int(result['mapped_result_present'])}"
        )
        print(f"provenance_entries={result['provenance_entries']}")
        if args.self_test:
            print(f"self_test_failures={len(self_test_failures)}")
        for error in errors:
            print(f"ERROR: {error}")
        for failure in self_test_failures:
            print(f"SELF_TEST_ERROR: {failure}")

    return 1 if errors or self_test_failures else 0


if __name__ == "__main__":
    sys.exit(main())
