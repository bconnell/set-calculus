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
    Requirement,
    State,
    Transform,
)


class ModelContractTests(unittest.TestCase):
    def test_state_with_effects_preserves_unaffected_state_and_records_transition(self):
        original = State(
            {"ready": False, "count": 2, "label": "original"},
            version=7,
            uncertain=frozenset({"ready", "external"}),
            completed_transforms=frozenset({"T-OLD"}),
        )

        changed = original.with_effects(
            {"ready": True, "count": 3},
            transform_id="T-NEW",
        )

        self.assertEqual(
            {"ready": False, "count": 2, "label": "original"},
            dict(original.facts),
        )
        self.assertEqual(7, original.version)
        self.assertEqual(frozenset({"ready", "external"}), original.uncertain)
        self.assertEqual(frozenset({"T-OLD"}), original.completed_transforms)

        self.assertEqual(
            {"ready": True, "count": 3, "label": "original"},
            dict(changed.facts),
        )
        self.assertEqual(8, changed.version)
        self.assertEqual(frozenset({"external"}), changed.uncertain)
        self.assertEqual(
            frozenset({"T-OLD", "T-NEW"}),
            changed.completed_transforms,
        )

    def test_state_with_effects_without_transform_id_does_not_record_none(self):
        original = State(
            {"ready": False},
            version=2,
            completed_transforms=frozenset({"T-OLD"}),
        )

        changed = original.with_effects({"ready": True})

        self.assertEqual(3, changed.version)
        self.assertEqual(frozenset({"T-OLD"}), changed.completed_transforms)
        self.assertNotIn(None, changed.completed_transforms)

    def test_authority_rule_requires_every_non_wildcard_dimension_to_match(self):
        rule = AuthorityRule("agent", "write", "feature")

        self.assertTrue(rule.allows("agent", "write", "feature"))
        cases = (
            ("other", "write", "feature"),
            ("agent", "read", "feature"),
            ("agent", "write", "other"),
            ("other", "read", "other"),
        )
        for actor, operation, scope in cases:
            with self.subTest(actor=actor, operation=operation, scope=scope):
                self.assertFalse(rule.allows(actor, operation, scope))

    def test_authority_rule_wildcards_are_dimension_local(self):
        self.assertTrue(
            AuthorityRule("*", "write", "feature").allows(
                "any-agent", "write", "feature"
            )
        )
        self.assertTrue(
            AuthorityRule("agent", "*", "feature").allows(
                "agent", "any-operation", "feature"
            )
        )
        self.assertTrue(
            AuthorityRule("agent", "write", "*").allows(
                "agent", "write", "any-scope"
            )
        )
        self.assertTrue(
            AuthorityRule("*", "*", "*").allows(
                "any-agent", "any-operation", "any-scope"
            )
        )
        self.assertFalse(
            AuthorityRule("*", "write", "feature").allows(
                "any-agent", "read", "feature"
            )
        )

    def test_authority_accepts_when_any_rule_matches(self):
        authority = Authority(
            (
                AuthorityRule("other", "read", "feature"),
                AuthorityRule("agent", "write", "feature"),
            )
        )
        self.assertTrue(authority.allows("agent", "write", "feature"))
        self.assertFalse(authority.allows("agent", "delete", "feature"))

    def test_zero_costs_are_valid_and_effective_cost_is_exact_sum(self):
        zero = Transform(
            "T-ZERO",
            "agent",
            "inspect",
            "feature",
            effects={},
            base_cost=0.0,
            risk_penalty=0.0,
        )
        priced = Transform(
            "T-PRICED",
            "agent",
            "inspect",
            "feature",
            effects={},
            base_cost=2.25,
            risk_penalty=1.5,
        )

        self.assertEqual(0.0, zero.effective_cost)
        self.assertEqual(3.75, priced.effective_cost)

    def test_requirement_missing_fact_is_false_not_uncertain(self):
        requirement = Requirement("REQ", "ready", True)
        self.assertFalse(requirement.evaluate(State({})))


if __name__ == "__main__":
    unittest.main()
