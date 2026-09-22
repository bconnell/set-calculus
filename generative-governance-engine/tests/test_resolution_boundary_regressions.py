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
    resolve,
    run,
)


class ResolutionBoundaryRegressionTests(unittest.TestCase):
    def authority(self) -> Authority:
        return Authority((AuthorityRule("agent", "*", "feature"),))

    def simple_intent(self) -> Intent:
        return Intent(
            intent_id="INT-BOUNDARY",
            version=1,
            objective="Reach ready.",
            acceptance_criteria=(Requirement("AC-READY", "ready", True),),
        )

    def test_final_allowed_transform_is_resolved_after_application(self):
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )

        result = run(
            self.simple_intent(),
            self.authority(),
            State({"ready": False}),
            (transform,),
            max_steps=1,
        )

        self.assertEqual(Resolution.COMPLETED, result.resolution)
        self.assertTrue(result.state.facts["ready"])
        self.assertEqual(1, result.state.version)
        self.assertEqual(1, len(result.evidence))
        self.assertEqual(result.state.version, result.evidence[0].state_version)
        self.assertEqual("state:1 resolution:COMPLETED", result.trace[-1])

    def test_zero_step_budget_preserves_incomplete_when_progress_is_known(self):
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )
        initial = State({"ready": False})

        result = run(
            self.simple_intent(),
            self.authority(),
            initial,
            (transform,),
            max_steps=0,
        )

        self.assertEqual(Resolution.INCOMPLETE, result.resolution)
        self.assertIs(result.state, initial)
        self.assertEqual(
            (
                "state:0 resolution:INCOMPLETE",
                "max steps exhausted",
            ),
            result.trace,
        )

    def test_zero_step_budget_preserves_blocked_when_no_path_exists(self):
        transform = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )
        initial = State({"ready": False})

        result = run(
            self.simple_intent(),
            Authority(),
            initial,
            (transform,),
            max_steps=0,
        )

        self.assertEqual(Resolution.BLOCKED, result.resolution)
        self.assertIs(result.state, initial)
        self.assertEqual(
            (
                "state:0 resolution:BLOCKED",
                "no admissible recovery/progress path",
            ),
            result.trace,
        )

    def test_resolution_probe_honors_requested_planner_depth(self):
        intent = self.simple_intent()
        state = State({"ready": False})
        transforms = []
        for index in range(1, 14):
            transform_id = f"T-{index:02d}"
            effects = {"ready": True} if index == 13 else {f"step_{index}": True}
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

        self.assertEqual(
            Resolution.BLOCKED,
            resolve(
                intent,
                self.authority(),
                state,
                transforms=tuple(transforms),
            ),
        )
        self.assertEqual(
            Resolution.INCOMPLETE,
            resolve(
                intent,
                self.authority(),
                state,
                transforms=tuple(transforms),
                planner_max_depth=13,
            ),
        )


if __name__ == "__main__":
    unittest.main()
