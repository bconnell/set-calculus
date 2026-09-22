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
    Evidence,
    Intent,
    IntentStatus,
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
from generative_governance_engine.engine import plan_path


class EngineTests(unittest.TestCase):
    def base_intent(self) -> Intent:
        return Intent(
            intent_id="INT-1",
            version=1,
            objective="Make feature ready.",
            acceptance_criteria=(
                Requirement("AC-1", "ready", True),
            ),
            invariants=(
                Requirement("INV-1", "data_preserved", True),
            ),
        )

    def authority(self) -> Authority:
        return Authority((AuthorityRule("agent", "set-ready", "feature"),))

    def ready_transform(self) -> Transform:
        return Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )

    def test_incomplete_executes_to_completed(self):
        result = run(
            self.base_intent(),
            self.authority(),
            State({"ready": False, "data_preserved": True}),
            (self.ready_transform(),),
        )
        self.assertEqual(Resolution.COMPLETED, result.resolution)
        self.assertTrue(result.state.facts["ready"])

    def test_missing_authority_blocks(self):
        result = run(
            self.base_intent(),
            Authority(),
            State({"ready": False, "data_preserved": True}),
            (self.ready_transform(),),
        )
        self.assertEqual(Resolution.BLOCKED, result.resolution)

    def test_uncertain_required_state_is_unresolved(self):
        state = State(
            {"ready": False, "data_preserved": True},
            uncertain=frozenset({"ready"}),
        )
        resolution = resolve(
            self.base_intent(),
            self.authority(),
            state,
            transforms=(self.ready_transform(),),
        )
        self.assertEqual(Resolution.UNRESOLVED, resolution)

    def test_superseded_intent_is_superseded(self):
        intent = Intent(
            intent_id="INT-1",
            version=1,
            objective="Old objective.",
            acceptance_criteria=(Requirement("AC-1", "ready", True),),
            status=IntentStatus.SUPERSEDED,
        )
        self.assertEqual(
            Resolution.SUPERSEDED,
            resolve(intent, self.authority(), State({"ready": True})),
        )

    def test_contradictory_intent_fails(self):
        intent = Intent(
            intent_id="INT-BAD",
            version=1,
            objective="Contradiction.",
            acceptance_criteria=(Requirement("AC-1", "mode", "A"),),
            invariants=(Requirement("INV-1", "mode", "B"),),
        )
        self.assertEqual(
            Resolution.FAILED,
            resolve(intent, Authority(), State({"mode": "A"})),
        )

    def test_invariant_breaking_transform_is_not_admissible(self):
        transform = Transform(
            "T-BAD",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True, "data_preserved": False},
        )
        self.assertFalse(
            admissible(
                self.base_intent(),
                self.authority(),
                State({"ready": False, "data_preserved": True}),
                transform,
            )
        )

    def test_completion_requires_current_evidence(self):
        intent = self.base_intent()
        state = State({"ready": True, "data_preserved": True}, version=2)
        stale = (Evidence("AC-1", state_version=1, proven=True, provenance="old"),)
        self.assertEqual(
            Resolution.UNRESOLVED,
            resolve(intent, self.authority(), state, stale),
        )
        current = observe(intent, state)
        self.assertEqual(
            Resolution.COMPLETED,
            resolve(intent, self.authority(), state, current),
        )

    def test_dependency_aware_planner_executes_prerequisite_first(self):
        intent = self.base_intent()
        authority = Authority((
            AuthorityRule("agent", "prepare", "feature"),
            AuthorityRule("agent", "set-ready", "feature"),
        ))
        prepare = Transform(
            "T-PREPARE",
            "agent",
            "prepare",
            "feature",
            effects={"prepared": True},
        )
        ready = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
            depends_on=("T-PREPARE",),
        )
        path = plan_path(
            intent,
            authority,
            State({"ready": False, "data_preserved": True}),
            (ready, prepare),
        )
        self.assertEqual(("T-PREPARE", "T-READY"), tuple(t.transform_id for t in path))

    def test_blocked_precondition_recovers_through_non_goal_transform(self):
        intent = self.base_intent()
        authority = Authority((
            AuthorityRule("agent", "repair", "feature"),
            AuthorityRule("agent", "set-ready", "feature"),
        ))
        recover = Transform(
            "T-RECOVER",
            "agent",
            "repair",
            "feature",
            effects={"dependency_ok": True},
        )
        ready = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
            preconditions=(Requirement("P-1", "dependency_ok", True),),
        )
        result = run(
            intent,
            authority,
            State({
                "ready": False,
                "data_preserved": True,
                "dependency_ok": False,
            }),
            (ready, recover),
        )
        self.assertEqual(Resolution.COMPLETED, result.resolution)
        self.assertIn("apply:T-RECOVER", result.trace)
        self.assertIn("apply:T-READY", result.trace)

    def test_no_recovery_path_remains_blocked(self):
        ready = Transform(
            "T-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
            preconditions=(Requirement("P-1", "dependency_ok", True),),
        )
        result = run(
            self.base_intent(),
            self.authority(),
            State({
                "ready": False,
                "data_preserved": True,
                "dependency_ok": False,
            }),
            (ready,),
        )
        self.assertEqual(Resolution.BLOCKED, result.resolution)

    def test_tie_breaking_prefers_shorter_path(self):
        intent = self.base_intent()
        authority = Authority((
            AuthorityRule("agent", "*", "feature"),
        ))
        direct = Transform(
            "T-Z-DIRECT",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
        )
        prep = Transform(
            "T-A-PREP",
            "agent",
            "prepare",
            "feature",
            effects={"prepared": True},
        )
        indirect = Transform(
            "T-A-READY",
            "agent",
            "set-ready",
            "feature",
            effects={"ready": True},
            depends_on=("T-A-PREP",),
        )
        path = plan_path(
            intent,
            authority,
            State({"ready": False, "data_preserved": True}),
            (prep, indirect, direct),
        )
        self.assertEqual(("T-Z-DIRECT",), tuple(t.transform_id for t in path))

    def test_tie_breaking_prefers_greater_delta_reduction(self):
        intent = Intent(
            intent_id="INT-MULTI",
            version=1,
            objective="Satisfy two requirements.",
            acceptance_criteria=(
                Requirement("AC-1", "a", True),
                Requirement("AC-2", "b", True),
            ),
        )
        authority = Authority((AuthorityRule("agent", "*", "feature"),))
        one = Transform(
            "T-A",
            "agent",
            "one",
            "feature",
            effects={"a": True},
        )
        two = Transform(
            "T-Z",
            "agent",
            "two",
            "feature",
            effects={"a": True, "b": True},
        )
        selected = plan_next(
            intent,
            authority,
            State({"a": False, "b": False}),
            (one, two),
        )
        self.assertEqual("T-Z", selected.transform_id)

    def test_tie_breaking_is_lexicographic_after_equal_cost_and_gain(self):
        intent = self.base_intent()
        authority = Authority((AuthorityRule("agent", "*", "feature"),))
        alpha = Transform(
            "T-ALPHA",
            "agent",
            "set-ready-a",
            "feature",
            effects={"ready": True},
        )
        beta = Transform(
            "T-BETA",
            "agent",
            "set-ready-b",
            "feature",
            effects={"ready": True},
        )
        selected = plan_next(
            intent,
            authority,
            State({"ready": False, "data_preserved": True}),
            (beta, alpha),
        )
        self.assertEqual("T-ALPHA", selected.transform_id)


if __name__ == "__main__":
    unittest.main()
