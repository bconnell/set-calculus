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

    def test_default_planner_depth_stops_before_thirteen_step_path(self):
        chain = self.dependency_chain(13)
        state = State({"ready": False, "data_preserved": True})

        self.assertEqual(
            (),
            plan_path(self.intent(), self.authority(), state, chain),
        )
        self.assertIsNone(
            plan_next(self.intent(), self.authority(), state, chain),
        )

        explicit_path = plan_path(
            self.intent(),
            self.authority(),
            state,
            chain,
            max_depth=13,
        )
        self.assertEqual(13, len(explicit_path))
        self.assertEqual("T-01", explicit_path[0].transform_id)
        self.assertEqual("T-13", explicit_path[-1].transform_id)

    def test_run_planner_depth_override_can_widen_beyond_default(self):
        chain = self.dependency_chain(13)
        state = State({"ready": False, "data_preserved": True})

        blocked = run(
            self.intent(),
            self.authority(),
            state,
            chain,
        )
        self.assertEqual(Resolution.BLOCKED, blocked.resolution)

        completed = run(
            self.intent(),
            self.authority(),
            state,
            chain,
            planner_max_depth=13,
            max_steps=13,
        )
        self.assertEqual(Resolution.COMPLETED, completed.resolution)
        self.assertEqual(13, completed.state.version)

    def test_default_run_step_budget_is_observable_at_one_hundred_transforms(self):
        requirements = tuple(
            Requirement(f"AC-{index:03d}", f"done_{index}", True)
            for index in range(1, 102)
        )
        intent = Intent(
            intent_id="INT-BUDGET",
            version=1,
            objective="Complete 101 independent requirements.",
            acceptance_criteria=requirements,
        )
        transforms = tuple(
            Transform(
                f"T-{index:03d}",
                "agent",
                f"complete-{index}",
                "feature",
                effects={f"done_{index}": True},
                base_cost=0.0,
            )
            for index in range(1, 102)
        )
        initial = State(
            {f"done_{index}": False for index in range(1, 102)}
        )

        default_result = run(
            intent,
            self.authority(),
            initial,
            transforms,
        )
        self.assertEqual(Resolution.INCOMPLETE, default_result.resolution)
        self.assertEqual(100, default_result.state.version)
        self.assertEqual("max steps exhausted", default_result.trace[-1])

        extended_result = run(
            intent,
            self.authority(),
            initial,
            transforms,
            max_steps=101,
        )
        self.assertEqual(Resolution.COMPLETED, extended_result.resolution)
        self.assertEqual(101, extended_result.state.version)

    def test_resolve_with_catalog_uses_requested_planner_depth(self):
        chain = self.dependency_chain(13)
        state = State({"ready": False, "data_preserved": True})

        default_resolution = __import__(
            "generative_governance_engine",
            fromlist=["resolve"],
        ).resolve(
            self.intent(),
            self.authority(),
            state,
            (),
            chain,
        )
        self.assertEqual(Resolution.BLOCKED, default_resolution)

        widened_resolution = __import__(
            "generative_governance_engine",
            fromlist=["resolve"],
        ).resolve(
            self.intent(),
            self.authority(),
            state,
            (),
            chain,
            planner_max_depth=13,
        )
        self.assertEqual(Resolution.INCOMPLETE, widened_resolution)

    def test_step_exhaustion_can_finish_in_blocked_state(self):
        intent = Intent(
            intent_id="INT-PARTIAL",
            version=1,
            objective="Satisfy both requirements.",
            acceptance_criteria=(
                Requirement("AC-A", "a", True),
                Requirement("AC-B", "b", True),
            ),
        )
        transform = Transform(
            "T-A",
            "agent",
            "set-a",
            "feature",
            effects={"a": True},
        )
        initial = State({"a": False, "b": False})

        result = run(
            intent,
            self.authority(),
            initial,
            (transform,),
            max_steps=1,
        )

        self.assertEqual(Resolution.BLOCKED, result.resolution)
        self.assertEqual(1, result.state.version)
        self.assertTrue(result.state.facts["a"])
        self.assertFalse(result.state.facts["b"])
        self.assertEqual(
            (
                "state:0 resolution:INCOMPLETE",
                "plan:T-A cost:1.000",
                "apply:T-A cost:1.000 risk:0.000",
                "state:1 resolution:BLOCKED",
                "no admissible recovery/progress path",
            ),
            result.trace,
        )

    def test_post_budget_recheck_honors_widened_planner_depth(self):
        acceptance = (
            Requirement("AC-A", "a", True),
            Requirement("AC-B", "b", True),
        )
        intent = Intent(
            intent_id="INT-POST-BUDGET-DEPTH",
            version=1,
            objective="Satisfy A directly, then retain a 13-step path to B.",
            acceptance_criteria=acceptance,
        )

        direct_a = Transform(
            "T-00-A",
            "agent",
            "set-a",
            "feature",
            effects={"a": True},
            base_cost=0.0,
        )

        chain = []
        for index in range(1, 14):
            transform_id = f"T-B-{index:02d}"
            effects = {"b": True} if index == 13 else {f"b_step_{index}": True}
            depends_on = () if index == 1 else (f"T-B-{index - 1:02d}",)
            chain.append(
                Transform(
                    transform_id,
                    "agent",
                    f"b-step-{index}",
                    "feature",
                    effects=effects,
                    depends_on=depends_on,
                )
            )

        result = run(
            intent,
            self.authority(),
            State({"a": False, "b": False}),
            (direct_a, *chain),
            max_steps=1,
            planner_max_depth=13,
        )

        self.assertEqual(Resolution.INCOMPLETE, result.resolution)
        self.assertEqual(1, result.state.version)
        self.assertTrue(result.state.facts["a"])
        self.assertFalse(result.state.facts["b"])
        self.assertEqual("max steps exhausted", result.trace[-1])

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
            (
                "state:0 resolution:BLOCKED",
                "no admissible recovery/progress path",
            ),
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
                "state:0 resolution:BLOCKED",
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
