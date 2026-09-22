import inspect
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
    plan_next,
    plan_path,
    resolve,
    run,
)
from generative_governance_engine.engine import apply_transform


class VerificationContractTests(unittest.TestCase):
    def intent(self) -> Intent:
        return Intent(
            intent_id="INT-VERIFY",
            version=1,
            objective="Reach ready while preserving data.",
            acceptance_criteria=(Requirement("AC-READY", "ready", True),),
            invariants=(Requirement("INV-DATA", "data_preserved", True),),
        )

    def authority(self) -> Authority:
        return Authority((AuthorityRule("agent", "*", "feature"),))

    def test_resource_defaults_are_part_of_the_reference_contract(self):
        self.assertEqual(
            12,
            inspect.signature(plan_path).parameters["max_depth"].default,
        )
        self.assertEqual(
            12,
            inspect.signature(plan_next).parameters["max_depth"].default,
        )
        self.assertEqual(
            12,
            inspect.signature(resolve).parameters["planner_max_depth"].default,
        )
        run_parameters = inspect.signature(run).parameters
        self.assertEqual(100, run_parameters["max_steps"].default)
        self.assertEqual(12, run_parameters["planner_max_depth"].default)

    def dependency_chain(self, length: int) -> tuple[Transform, ...]:
        transforms = []
        for index in range(1, length + 1):
            transform_id = f"T-{index:02d}"
            effects = {"ready": True} if index == length else {f"step_{index}": True}
            depends_on = () if index == 1 else (f"T-{index - 1:02d}",)
            transforms.append(
                Transform(
                    transform_id,
                    "agent",
                    f"step-{index}",
                    "feature",
                    effects=effects,
                    depends_on=depends_on,
                )
            )
        return tuple(transforms)

    def test_resolve_uses_requested_planner_depth_for_feasibility(self):
        chain = self.dependency_chain(13)
        state = State({"ready": False, "data_preserved": True})

        self.assertEqual(
            Resolution.BLOCKED,
            resolve(
                self.intent(),
                self.authority(),
                state,
                (),
                chain,
            ),
        )
        self.assertEqual(
            Resolution.INCOMPLETE,
            resolve(
                self.intent(),
                self.authority(),
                state,
                (),
                chain,
                planner_max_depth=13,
            ),
        )

    def test_run_planner_depth_override_reaches_thirteen_step_path(self):
        chain = self.dependency_chain(13)
        state = State({"ready": False, "data_preserved": True})

        blocked = run(
            self.intent(),
            self.authority(),
            state,
            chain,
            max_steps=14,
        )
        self.assertEqual(Resolution.BLOCKED, blocked.resolution)
        self.assertEqual(0, blocked.state.version)

        completed = run(
            self.intent(),
            self.authority(),
            state,
            chain,
            max_steps=14,
            planner_max_depth=13,
        )
        self.assertEqual(Resolution.COMPLETED, completed.resolution)
        self.assertEqual(13, completed.state.version)
        self.assertEqual(
            frozenset(transform.transform_id for transform in chain),
            completed.state.completed_transforms,
        )

    def test_negative_cost_diagnostics_are_exact_and_actionable(self):
        with self.assertRaisesRegex(
            ValueError,
            r"^Transform base_cost must be non-negative\.$",
        ):
            Transform(
                "T-NEG-BASE",
                "agent",
                "bad",
                "feature",
                effects={},
                base_cost=-0.01,
            )

        with self.assertRaisesRegex(
            ValueError,
            r"^Transform risk_penalty must be non-negative\.$",
        ):
            Transform(
                "T-NEG-RISK",
                "agent",
                "bad",
                "feature",
                effects={},
                risk_penalty=-0.01,
            )

    def test_apply_transform_diagnostic_identifies_rejected_transform(self):
        transform = Transform(
            "T-DENIED",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )
        with self.assertRaisesRegex(
            PermissionError,
            r"^Transform 'T-DENIED' is not admissible\.$",
        ):
            apply_transform(
                self.intent(),
                Authority(),
                State({"ready": False, "data_preserved": True}),
                transform,
            )

    def test_low_cost_depth_limit_dead_end_does_not_hide_shallower_viable_path(self):
        cheap = Transform(
            "T-A-CHEAP",
            "agent",
            "cheap",
            "feature",
            effects={"cheap": True},
            base_cost=0.0,
        )
        expensive = Transform(
            "T-B-EXPENSIVE",
            "agent",
            "expensive",
            "feature",
            effects={"expensive": True},
            base_cost=10.0,
        )
        deep_dead_end = Transform(
            "T-C-DEEP",
            "agent",
            "deep",
            "feature",
            effects={"deep": True},
            preconditions=(Requirement("P-CHEAP", "cheap", True),),
            base_cost=0.0,
        )
        finish = Transform(
            "T-D-FINISH",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
            preconditions=(Requirement("P-EXPENSIVE", "expensive", True),),
            base_cost=0.0,
        )

        path = plan_path(
            self.intent(),
            self.authority(),
            State({"ready": False, "data_preserved": True}),
            (cheap, expensive, deep_dead_end, finish),
            max_depth=2,
        )

        self.assertEqual(
            ("T-B-EXPENSIVE", "T-D-FINISH"),
            tuple(item.transform_id for item in path),
        )

    def test_pruning_keeps_distinct_completed_transform_states_separate(self):
        dead_end = Transform(
            "T-A-DEAD",
            "agent",
            "dead",
            "feature",
            effects={"dead": True},
            base_cost=0.0,
        )
        viable = Transform(
            "T-B-VIABLE",
            "agent",
            "viable",
            "feature",
            effects={"viable": True},
            base_cost=5.0,
        )
        finish = Transform(
            "T-C-FINISH",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
            depends_on=("T-B-VIABLE",),
            base_cost=0.0,
        )

        selected = plan_next(
            self.intent(),
            self.authority(),
            State({"ready": False, "data_preserved": True}),
            (dead_end, viable, finish),
            max_depth=2,
        )

        self.assertIsNotNone(selected)
        self.assertEqual("T-B-VIABLE", selected.transform_id)

    def test_state_signature_preserves_order_dependent_fact_states(self):
        write_a = Transform(
            "T-A",
            "agent",
            "write-a",
            "feature",
            effects={"mode": "A"},
            base_cost=1.0,
        )
        write_b = Transform(
            "T-B",
            "agent",
            "write-b",
            "feature",
            effects={"mode": "B"},
            base_cost=1.0,
        )
        finish = Transform(
            "T-C",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
            preconditions=(Requirement("P-MODE-A", "mode", "A"),),
            depends_on=("T-A", "T-B"),
            base_cost=1.0,
        )

        path = plan_path(
            self.intent(),
            self.authority(),
            State({"ready": False, "data_preserved": True, "mode": "initial"}),
            (write_a, write_b, finish),
            max_depth=3,
        )

        self.assertEqual(
            ("T-B", "T-A", "T-C"),
            tuple(item.transform_id for item in path),
        )

    def test_run_reports_direct_blocked_resolution_without_false_progress_trace(self):
        transform = Transform(
            "T-READY",
            "agent",
            "finish",
            "feature",
            effects={"ready": True},
            preconditions=(Requirement("P-MISSING", "missing", True),),
        )
        initial = State({"ready": False, "data_preserved": True})

        result = run(
            self.intent(),
            self.authority(),
            initial,
            (transform,),
        )

        self.assertEqual(Resolution.BLOCKED, result.resolution)
        self.assertIs(result.state, initial)
        self.assertEqual((), result.evidence)
        self.assertEqual(
            ("state:0 resolution:BLOCKED",),
            result.trace,
        )

    def test_runtime_depth_block_preserves_current_state_and_evidence(self):
        transform = Transform(
            "T-READY",
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
            (transform,),
            planner_max_depth=0,
        )

        self.assertEqual(Resolution.BLOCKED, result.resolution)
        self.assertIs(result.state, initial)
        self.assertEqual((), result.evidence)
        self.assertEqual(
            (
                "state:0 resolution:INCOMPLETE",
                "no admissible recovery/progress path",
            ),
            result.trace,
        )

    def test_plan_trace_preserves_full_transform_order_and_cost(self):
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

        result = run(
            self.intent(),
            self.authority(),
            State({"ready": False, "data_preserved": True}),
            (finish, prepare),
        )

        self.assertIn(
            "plan:T-PREPARE->T-FINISH cost:2.000",
            result.trace,
        )


if __name__ == "__main__":
    unittest.main()
