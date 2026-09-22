import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from generative_governance_engine import (
    Authority,
    AuthorityRule,
    Intent,
    Requirement,
    Resolution,
    State,
    Transform,
    admissible,
    observe,
    plan_next,
    resolve,
    run,
)
from generative_governance_engine.engine import apply_transform


class EngineContractTests(unittest.TestCase):
    def intent(self) -> Intent:
        return Intent(
            intent_id="INT-CONTRACT",
            version=1,
            objective="Reach ready without losing protected data.",
            acceptance_criteria=(Requirement("AC-READY", "ready", True),),
            invariants=(Requirement("INV-DATA", "data_preserved", True),),
        )

    def authority(self) -> Authority:
        return Authority((AuthorityRule("agent", "*", "feature"),))

    def test_conflicting_acceptance_criteria_fail_consistency(self):
        intent = Intent(
            intent_id="INT-CONFLICT",
            version=1,
            objective="Contradictory acceptance state.",
            acceptance_criteria=(
                Requirement("AC-A", "mode", "A"),
                Requirement("AC-B", "mode", "B"),
            ),
        )

        self.assertEqual(
            Resolution.FAILED,
            resolve(intent, self.authority(), State({"mode": "A"})),
        )

    def test_transform_may_repair_an_invariant_that_is_already_false(self):
        repair = Transform(
            "T-REPAIR",
            "agent",
            "repair",
            "feature",
            effects={"data_preserved": True},
        )
        state = State({"ready": False, "data_preserved": False})

        self.assertTrue(admissible(self.intent(), self.authority(), state, repair))

    def test_plan_next_respects_max_depth_for_dependency_recovery(self):
        prepare = Transform(
            "T-PREPARE",
            "agent",
            "prepare",
            "feature",
            effects={"prepared": True},
        )
        finish = Transform(
            "T-FINISH",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
            depends_on=("T-PREPARE",),
        )
        state = State({"ready": False, "data_preserved": True})

        self.assertIsNone(
            plan_next(
                self.intent(),
                self.authority(),
                state,
                (finish, prepare),
                max_depth=1,
            )
        )
        selected = plan_next(
            self.intent(),
            self.authority(),
            state,
            (finish, prepare),
            max_depth=2,
        )
        self.assertIsNotNone(selected)
        self.assertEqual("T-PREPARE", selected.transform_id)

    def test_completed_dependency_in_state_allows_dependent_transform(self):
        finish = Transform(
            "T-FINISH",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
            depends_on=("T-PREPARE",),
        )
        state = State(
            {"ready": False, "data_preserved": True},
            completed_transforms=frozenset({"T-PREPARE"}),
        )

        selected = plan_next(
            self.intent(),
            self.authority(),
            state,
            (finish,),
        )
        self.assertIsNotNone(selected)
        self.assertEqual("T-FINISH", selected.transform_id)

    def test_apply_transform_records_exact_state_transition(self):
        transform = Transform(
            "T-READY",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
        )
        state = State(
            {"ready": False, "data_preserved": True},
            version=4,
            uncertain=frozenset({"ready", "remote"}),
            completed_transforms=frozenset({"T-PREPARE"}),
        )

        changed = apply_transform(
            self.intent(),
            self.authority(),
            state,
            transform,
        )

        self.assertEqual(5, changed.version)
        self.assertTrue(changed.facts["ready"])
        self.assertTrue(changed.facts["data_preserved"])
        self.assertEqual(frozenset({"remote"}), changed.uncertain)
        self.assertEqual(
            frozenset({"T-PREPARE", "T-READY"}),
            changed.completed_transforms,
        )

    def test_observe_emits_only_satisfied_acceptance_with_current_provenance(self):
        intent = Intent(
            intent_id="INT-EVIDENCE",
            version=1,
            objective="Observe satisfied claims.",
            acceptance_criteria=(
                Requirement("AC-A", "a", True),
                Requirement("AC-B", "b", True),
            ),
        )
        state = State({"a": True, "b": False}, version=9)

        evidence = observe(intent, state, provenance="contract-test")

        self.assertEqual(1, len(evidence))
        self.assertEqual("AC-A", evidence[0].claim_id)
        self.assertEqual(9, evidence[0].state_version)
        self.assertTrue(evidence[0].proven)
        self.assertEqual("contract-test", evidence[0].provenance)

    def test_run_preserves_input_and_records_transition_versions(self):
        prepare = Transform(
            "T-PREPARE",
            "agent",
            "prepare",
            "feature",
            effects={"prepared": True},
        )
        finish = Transform(
            "T-FINISH",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
            depends_on=("T-PREPARE",),
        )
        initial = State({"ready": False, "data_preserved": True})

        result = run(
            self.intent(),
            self.authority(),
            initial,
            (finish, prepare),
        )

        self.assertEqual(Resolution.COMPLETED, result.resolution)
        self.assertEqual(0, initial.version)
        self.assertFalse(initial.facts["ready"])
        self.assertEqual(2, result.state.version)
        self.assertEqual(
            frozenset({"T-PREPARE", "T-FINISH"}),
            result.state.completed_transforms,
        )
        self.assertEqual(1, len(result.evidence))
        self.assertEqual(result.state.version, result.evidence[0].state_version)
        self.assertTrue(any(item.startswith("plan:") for item in result.trace))
        self.assertIn("apply:T-PREPARE cost:1.000 risk:0.000", result.trace)
        self.assertIn("apply:T-FINISH cost:1.000 risk:0.000", result.trace)
        self.assertEqual(
            "state:2 resolution:COMPLETED",
            result.trace[-1],
        )

    def test_max_steps_returns_canonical_final_state_resolution(self):
        prepare = Transform(
            "T-PREPARE",
            "agent",
            "prepare",
            "feature",
            effects={"prepared": True},
        )
        finish = Transform(
            "T-FINISH",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
            depends_on=("T-PREPARE",),
        )
        initial = State({"ready": False, "data_preserved": True})

        result = run(
            self.intent(),
            self.authority(),
            initial,
            (finish, prepare),
            max_steps=1,
        )

        self.assertEqual(Resolution.INCOMPLETE, result.resolution)
        self.assertEqual(1, result.state.version)
        self.assertEqual(frozenset({"T-PREPARE"}), result.state.completed_transforms)
        self.assertEqual((), result.evidence)
        self.assertEqual("state:1 resolution:INCOMPLETE", result.trace[-2])
        self.assertEqual("max steps exhausted", result.trace[-1])

    def test_last_allowed_transform_can_complete(self):
        finish = Transform(
            "T-FINISH",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
        )
        initial = State({"ready": False, "data_preserved": True})

        result = run(
            self.intent(),
            self.authority(),
            initial,
            (finish,),
            max_steps=1,
        )

        self.assertEqual(Resolution.COMPLETED, result.resolution)
        self.assertEqual(1, result.state.version)
        self.assertEqual(frozenset({"T-FINISH"}), result.state.completed_transforms)
        self.assertEqual(1, len(result.evidence))
        self.assertEqual(result.state.version, result.evidence[0].state_version)
        self.assertEqual("state:1 resolution:COMPLETED", result.trace[-1])
        self.assertNotIn("max steps exhausted", result.trace)


if __name__ == "__main__":
    unittest.main()
