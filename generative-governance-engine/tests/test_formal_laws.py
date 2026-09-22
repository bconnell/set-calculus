import itertools
import os
import random
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
    IntentStatus,
    Requirement,
    Resolution,
    State,
    Transform,
    admissible,
    observe,
    plan_next,
    plan_path,
    resolve,
    run,
)
from generative_governance_engine.engine import apply_transform, semantic_delta


class FormalLawRegressionTests(unittest.TestCase):
    def base_intent(self) -> Intent:
        return Intent(
            intent_id="INT-LAWS",
            version=1,
            objective="Reach ready while preserving data.",
            acceptance_criteria=(Requirement("AC-READY", "ready", True),),
            invariants=(Requirement("INV-DATA", "data_preserved", True),),
        )

    def wildcard_authority(self) -> Authority:
        return Authority((AuthorityRule("agent", "*", "feature"),))

    def test_planner_is_deterministic_across_transform_input_order(self):
        intent = self.base_intent()
        authority = self.wildcard_authority()
        state = State({"ready": False, "data_preserved": True})
        alpha = Transform(
            "T-ALPHA",
            "agent",
            "set-ready-alpha",
            "feature",
            effects={"ready": True},
            base_cost=2.0,
        )
        beta = Transform(
            "T-BETA",
            "agent",
            "set-ready-beta",
            "feature",
            effects={"ready": True},
            base_cost=2.0,
        )
        gamma = Transform(
            "T-GAMMA",
            "agent",
            "set-ready-gamma",
            "feature",
            effects={"ready": True},
            base_cost=3.0,
        )

        for ordering in itertools.permutations((alpha, beta, gamma)):
            with self.subTest(ordering=tuple(t.transform_id for t in ordering)):
                path = plan_path(intent, authority, state, ordering)
                self.assertEqual(("T-ALPHA",), tuple(t.transform_id for t in path))

    def test_generated_direct_candidates_obey_cost_then_id_ordering(self):
        rng = random.Random(0x1D6D)
        intent = self.base_intent()
        authority = self.wildcard_authority()
        state = State({"ready": False, "data_preserved": True})

        for case in range(100):
            candidates = []
            for index in range(6):
                candidates.append(
                    Transform(
                        f"T-{case:03d}-{index:02d}",
                        "agent",
                        f"op-{index}",
                        "feature",
                        effects={"ready": True},
                        base_cost=float(rng.randint(0, 6)),
                        risk_penalty=float(rng.randint(0, 4)),
                    )
                )

            expected = min(
                candidates,
                key=lambda item: (item.effective_cost, item.transform_id),
            )
            rng.shuffle(candidates)
            selected = plan_next(intent, authority, state, candidates)

            with self.subTest(case=case):
                self.assertIsNotNone(selected)
                self.assertEqual(expected.transform_id, selected.transform_id)

    def test_completion_is_a_fixpoint_under_stable_inputs(self):
        intent = self.base_intent()
        authority = self.wildcard_authority()
        state = State({"ready": True, "data_preserved": True}, version=7)
        evidence = observe(intent, state)

        for _ in range(50):
            self.assertEqual(
                Resolution.COMPLETED,
                resolve(intent, authority, state, evidence),
            )

    def test_unrelated_state_change_preserves_completion_with_fresh_evidence(self):
        intent = self.base_intent()
        authority = self.wildcard_authority()
        state = State({"ready": True, "data_preserved": True}, version=3)

        self.assertEqual(
            Resolution.COMPLETED,
            resolve(intent, authority, state, observe(intent, state)),
        )

        changed = state.with_effects({"diagnostic_note": "unchanged boundary"})
        self.assertEqual(
            Resolution.COMPLETED,
            resolve(intent, authority, changed, observe(intent, changed)),
        )

    def test_apply_transform_rejects_missing_authority(self):
        intent = self.base_intent()
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )
        state = State({"ready": False, "data_preserved": True})

        with self.assertRaises(PermissionError):
            apply_transform(intent, Authority(), state, transform)

    def test_noop_is_not_selected_over_direct_progress(self):
        intent = self.base_intent()
        authority = self.wildcard_authority()
        state = State({"ready": False, "data_preserved": True})
        noop = Transform(
            "T-NOOP",
            "agent",
            "inspect",
            "feature",
            effects={"diagnostic_note": "observed"},
        )
        progress = Transform(
            "T-PROGRESS",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )

        selected = plan_next(intent, authority, state, (noop, progress))
        self.assertIsNotNone(selected)
        self.assertEqual("T-PROGRESS", selected.transform_id)

    def test_noop_only_candidate_does_not_create_false_progress(self):
        intent = self.base_intent()
        authority = self.wildcard_authority()
        state = State({"ready": False, "data_preserved": True})
        noop = Transform(
            "T-NOOP",
            "agent",
            "inspect",
            "feature",
            effects={"diagnostic_note": "observed"},
        )

        self.assertIsNone(plan_next(intent, authority, state, (noop,)))

    def test_dependency_path_is_stable_across_input_order(self):
        intent = self.base_intent()
        authority = self.wildcard_authority()
        state = State({"ready": False, "data_preserved": True})
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
        irrelevant = Transform(
            "T-IRRELEVANT",
            "agent",
            "inspect",
            "feature",
            effects={"note": "not progress"},
        )

        for ordering in itertools.permutations((prepare, finish, irrelevant)):
            with self.subTest(ordering=tuple(t.transform_id for t in ordering)):
                path = plan_path(intent, authority, state, ordering)
                self.assertEqual(
                    ("T-PREPARE", "T-FINISH"),
                    tuple(t.transform_id for t in path),
                )

    def test_consistent_duplicate_requirement_key_remains_consistent(self):
        intent = Intent(
            intent_id="INT-DUPLICATE",
            version=1,
            objective="Allow the same requirement on both boundaries.",
            acceptance_criteria=(Requirement("AC-READY", "ready", True),),
            invariants=(Requirement("INV-READY", "ready", True),),
        )
        state = State({"ready": True})

        self.assertEqual(
            Resolution.COMPLETED,
            resolve(intent, self.wildcard_authority(), state, observe(intent, state)),
        )

    def test_superseded_intent_rejects_transform_admissibility(self):
        intent = Intent(
            intent_id="INT-OLD",
            version=1,
            objective="Old objective.",
            acceptance_criteria=(Requirement("AC-READY", "ready", True),),
            status=IntentStatus.SUPERSEDED,
        )
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )

        self.assertFalse(
            admissible(
                intent,
                self.wildcard_authority(),
                State({"ready": False}),
                transform,
            )
        )

    def test_completed_state_requires_no_planning_path(self):
        intent = self.base_intent()
        state = State({"ready": True, "data_preserved": True})
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )

        self.assertEqual(
            (),
            plan_path(intent, self.wildcard_authority(), state, (transform,)),
        )

    def test_zero_planner_depth_cannot_produce_path(self):
        intent = self.base_intent()
        state = State({"ready": False, "data_preserved": True})
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )

        self.assertEqual(
            (),
            plan_path(
                intent,
                self.wildcard_authority(),
                state,
                (transform,),
                max_depth=0,
            ),
        )

    def test_satisfied_acceptance_with_broken_invariant_fails(self):
        intent = self.base_intent()
        state = State({"ready": True, "data_preserved": False})

        self.assertEqual(
            Resolution.FAILED,
            resolve(intent, self.wildcard_authority(), state, observe(intent, state)),
        )

    def test_unmet_intent_without_transform_catalog_is_incomplete(self):
        intent = self.base_intent()
        state = State({"ready": False, "data_preserved": True})

        self.assertEqual(
            Resolution.INCOMPLETE,
            resolve(intent, self.wildcard_authority(), state),
        )

    def test_run_respects_zero_planner_depth_during_resolution(self):
        intent = self.base_intent()
        state = State({"ready": False, "data_preserved": True})
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )

        result = run(
            intent,
            self.wildcard_authority(),
            state,
            (transform,),
            planner_max_depth=0,
        )

        self.assertEqual(Resolution.BLOCKED, result.resolution)
        self.assertEqual(
            ("state:0 resolution:BLOCKED",),
            result.trace,
        )

    def test_zero_step_run_is_explicitly_unresolved(self):
        intent = self.base_intent()
        state = State({"ready": False, "data_preserved": True})
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )

        result = run(
            intent,
            self.wildcard_authority(),
            state,
            (transform,),
            max_steps=0,
        )

        self.assertEqual(Resolution.UNRESOLVED, result.resolution)
        self.assertIn("max steps exceeded", result.trace)

    def test_requirement_evaluation_preserves_uncertainty(self):
        requirement = Requirement("AC-READY", "ready", True)
        state = State(
            {"ready": True},
            uncertain=frozenset({"ready"}),
        )

        self.assertIsNone(requirement.evaluate(state))

    def test_selected_progress_does_not_increase_semantic_delta(self):
        intent = self.base_intent()
        authority = self.wildcard_authority()
        state = State({"ready": False, "data_preserved": True})
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )

        selected = plan_next(intent, authority, state, (transform,))
        self.assertIsNotNone(selected)
        next_state = apply_transform(intent, authority, state, selected)

        self.assertLessEqual(
            len(semantic_delta(intent, next_state)),
            len(semantic_delta(intent, state)),
        )


if __name__ == "__main__":
    unittest.main()
