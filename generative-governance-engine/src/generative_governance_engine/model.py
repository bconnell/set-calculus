from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping


class IntentStatus(str, Enum):
    ACTIVE = "ACTIVE"
    SUPERSEDED = "SUPERSEDED"


class Resolution(str, Enum):
    COMPLETED = "COMPLETED"
    INCOMPLETE = "INCOMPLETE"
    BLOCKED = "BLOCKED"
    UNRESOLVED = "UNRESOLVED"
    SUPERSEDED = "SUPERSEDED"
    FAILED = "FAILED"


@dataclass(frozen=True)
class Requirement:
    id: str
    key: str
    expected: Any
    description: str = ""

    def evaluate(self, state: "State") -> bool | None:
        if self.key in state.uncertain:
            return None
        return state.facts.get(self.key) == self.expected


@dataclass(frozen=True)
class Intent:
    intent_id: str
    version: int
    objective: str
    acceptance_criteria: tuple[Requirement, ...]
    invariants: tuple[Requirement, ...] = ()
    non_goals: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    status: IntentStatus = IntentStatus.ACTIVE
    supersedes: str | None = None


@dataclass(frozen=True)
class State:
    facts: Mapping[str, Any]
    version: int = 0
    uncertain: frozenset[str] = frozenset()

    def with_effects(self, effects: Mapping[str, Any]) -> "State":
        updated = dict(self.facts)
        updated.update(effects)
        uncertainty = set(self.uncertain)
        uncertainty.difference_update(effects.keys())
        return State(
            facts=updated,
            version=self.version + 1,
            uncertain=frozenset(uncertainty),
        )


@dataclass(frozen=True)
class AuthorityRule:
    actor: str
    operation: str
    scope: str

    def allows(self, actor: str, operation: str, scope: str) -> bool:
        return (
            (self.actor == "*" or self.actor == actor)
            and (self.operation == "*" or self.operation == operation)
            and (self.scope == "*" or self.scope == scope)
        )


@dataclass(frozen=True)
class Authority:
    rules: tuple[AuthorityRule, ...] = ()

    def allows(self, actor: str, operation: str, scope: str) -> bool:
        return any(rule.allows(actor, operation, scope) for rule in self.rules)


@dataclass(frozen=True)
class Transform:
    transform_id: str
    actor: str
    operation: str
    scope: str
    effects: Mapping[str, Any]
    preconditions: tuple[Requirement, ...] = ()
    description: str = ""


@dataclass(frozen=True)
class Evidence:
    claim_id: str
    state_version: int
    proven: bool
    provenance: str


@dataclass(frozen=True)
class GovernanceResult:
    resolution: Resolution
    state: State
    evidence: tuple[Evidence, ...]
    trace: tuple[str, ...] = field(default_factory=tuple)
