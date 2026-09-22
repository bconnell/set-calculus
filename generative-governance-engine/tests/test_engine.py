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
    resolve,
    run,
)


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


if __name__ == "__main__":
    unittest.main()
