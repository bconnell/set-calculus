from __future__ import annotations

from collections.abc import Iterable

from .model import (
    Authority,
    Evidence,
    GovernanceResult,
    Intent,
    IntentStatus,
    Requirement,
    Resolution,
    State,
    Transform,
)


def semantic_delta(intent: Intent, state: State) -> tuple[Requirement, ...]:
    return tuple(
        requirement
        for requirement in intent.acceptance_criteria
        if requirement.evaluate(state) is not True
    )


def _intent_is_consistent(intent: Intent) -> bool:
    expected_by_key: dict[str, object] = {}
    for requirement in (*intent.acceptance_criteria, *intent.invariants):
        if requirement.key in expected_by_key:
            if expected_by_key[requirement.key] != requirement.expected:
                return False
        else:
            expected_by_key[requirement.key] = requirement.expected
    return True


def _is_determinate(intent: Intent, state: State) -> bool:
    required_keys = {
        requirement.key
        for requirement in (*intent.acceptance_criteria, *intent.invariants)
    }
    return not bool(required_keys.intersection(state.uncertain))


def _preconditions_hold(transform: Transform, state: State) -> bool:
    return all(req.evaluate(state) is True for req in transform.preconditions)


def _preserves_invariants(intent: Intent, state: State, transform: Transform) -> bool:
    projected = state.with_effects(transform.effects)
    for invariant in intent.invariants:
        before = invariant.evaluate(state)
        after = invariant.evaluate(projected)
        if before is True and after is not True:
            return False
    return True


def admissible(
    intent: Intent,
    authority: Authority,
    state: State,
    transform: Transform,
) -> bool:
    if intent.status is not IntentStatus.ACTIVE:
        return False
    return (
        authority.allows(transform.actor, transform.operation, transform.scope)
        and _preconditions_hold(transform, state)
        and _preserves_invariants(intent, state, transform)
    )


def _delta_size(intent: Intent, state: State) -> int:
    return len(semantic_delta(intent, state))


def _advances(intent: Intent, state: State, transform: Transform) -> bool:
    before = _delta_size(intent, state)
    after = _delta_size(intent, state.with_effects(transform.effects))
    return after < before


def plan_next(
    intent: Intent,
    authority: Authority,
    state: State,
    transforms: Iterable[Transform],
) -> Transform | None:
    candidates = [
        transform
        for transform in transforms
        if admissible(intent, authority, state, transform)
        and _advances(intent, state, transform)
    ]
    if not candidates:
        return None

    def score(transform: Transform) -> tuple[int, str]:
        projected = state.with_effects(transform.effects)
        reduction = _delta_size(intent, state) - _delta_size(intent, projected)
        return (-reduction, transform.transform_id)

    return sorted(candidates, key=score)[0]


def apply_transform(
    intent: Intent,
    authority: Authority,
    state: State,
    transform: Transform,
) -> State:
    if not admissible(intent, authority, state, transform):
        raise PermissionError(
            f"Transform {transform.transform_id!r} is not admissible."
        )
    return state.with_effects(transform.effects)


def observe(
    intent: Intent,
    state: State,
    provenance: str = "deterministic-state-observation",
) -> tuple[Evidence, ...]:
    return tuple(
        Evidence(
            claim_id=requirement.id,
            state_version=state.version,
            proven=True,
            provenance=provenance,
        )
        for requirement in intent.acceptance_criteria
        if requirement.evaluate(state) is True
    )


def _criterion_is_proven(
    requirement: Requirement,
    state: State,
    evidence: Iterable[Evidence],
) -> bool:
    return any(
        item.claim_id == requirement.id
        and item.proven
        and item.state_version == state.version
        for item in evidence
    )


def resolve(
    intent: Intent,
    authority: Authority,
    state: State,
    evidence: Iterable[Evidence] = (),
    transforms: Iterable[Transform] | None = None,
) -> Resolution:
    evidence = tuple(evidence)

    if intent.status is not IntentStatus.ACTIVE:
        return Resolution.SUPERSEDED

    if not _intent_is_consistent(intent):
        return Resolution.FAILED

    if not _is_determinate(intent, state):
        return Resolution.UNRESOLVED

    delta = semantic_delta(intent, state)

    if not delta:
        invariants_hold = all(
            invariant.evaluate(state) is True for invariant in intent.invariants
        )
        if not invariants_hold:
            return Resolution.FAILED

        if all(
            _criterion_is_proven(requirement, state, evidence)
            for requirement in intent.acceptance_criteria
        ):
            return Resolution.COMPLETED
        return Resolution.UNRESOLVED

    if transforms is not None:
        transforms = tuple(transforms)
        if plan_next(intent, authority, state, transforms) is None:
            return Resolution.BLOCKED

    return Resolution.INCOMPLETE


def run(
    intent: Intent,
    authority: Authority,
    initial_state: State,
    transforms: Iterable[Transform],
    *,
    max_steps: int = 100,
) -> GovernanceResult:
    transforms = tuple(transforms)
    state = initial_state
    trace: list[str] = []

    for _ in range(max_steps):
        evidence = observe(intent, state)
        resolution = resolve(intent, authority, state, evidence, transforms)
        trace.append(f"state:{state.version} resolution:{resolution.value}")

        if resolution is not Resolution.INCOMPLETE:
            return GovernanceResult(
                resolution=resolution,
                state=state,
                evidence=evidence,
                trace=tuple(trace),
            )

        transform = plan_next(intent, authority, state, transforms)
        if transform is None:
            return GovernanceResult(
                resolution=Resolution.BLOCKED,
                state=state,
                evidence=evidence,
                trace=tuple(trace + ["no admissible advancing transform"]),
            )

        trace.append(f"apply:{transform.transform_id}")
        state = apply_transform(intent, authority, state, transform)

    evidence = observe(intent, state)
    return GovernanceResult(
        resolution=Resolution.UNRESOLVED,
        state=state,
        evidence=evidence,
        trace=tuple(trace + ["max steps exceeded"]),
    )
