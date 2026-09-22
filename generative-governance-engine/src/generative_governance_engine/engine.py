from __future__ import annotations

import heapq
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


def _dependencies_hold(transform: Transform, state: State) -> bool:
    return all(
        dependency in state.completed_transforms
        for dependency in transform.depends_on
    )


def _preserves_invariants(intent: Intent, state: State, transform: Transform) -> bool:
    projected = state.with_effects(transform.effects, transform.transform_id)
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
        and _dependencies_hold(transform, state)
        and _preconditions_hold(transform, state)
        and _preserves_invariants(intent, state, transform)
    )


def _delta_size(intent: Intent, state: State) -> int:
    return len(semantic_delta(intent, state))


def _state_signature(
    state: State,
) -> tuple[tuple[tuple[str, str], ...], tuple[str, ...], tuple[str, ...]]:
    facts = tuple(sorted((key, repr(value)) for key, value in state.facts.items()))
    return (
        facts,
        tuple(sorted(state.uncertain)),
        tuple(sorted(state.completed_transforms)),
    )


def _simulate(state: State, transform: Transform) -> State:
    return state.with_effects(transform.effects, transform.transform_id)


def path_cost(path: Iterable[Transform]) -> float:
    return sum(transform.effective_cost for transform in path)


def plan_path(
    intent: Intent,
    authority: Authority,
    state: State,
    transforms: Iterable[Transform],
    *,
    max_depth: int = 12,
) -> tuple[Transform, ...]:
    """Return the deterministic lowest-cost admissible path that reduces delta.

    Intermediate dependency or recovery transforms may be selected even when
    they do not directly reduce Intent-State delta.

    Candidate success paths are ordered by:
      1. lowest total effective cost (base cost + risk penalty);
      2. greatest semantic-delta reduction;
      3. fewest transforms;
      4. lexicographically smallest transform-id path.
    """
    transforms = tuple(sorted(transforms, key=lambda item: item.transform_id))
    initial_delta = _delta_size(intent, state)
    if initial_delta == 0:
        return ()

    # Queue items:
    # (path_cost, path_length, path_ids, state, path)
    queue: list[
        tuple[
            float,
            int,
            tuple[str, ...],
            State,
            tuple[Transform, ...],
        ]
    ] = [(0.0, 0, (), state, ())]

    # Lowest discovered cost for a concrete state signature. Equal-cost states
    # may still compete deterministically through path ids in the queue.
    best_cost: dict[
        tuple[tuple[tuple[str, str], ...], tuple[str, ...], tuple[str, ...]],
        float,
    ] = {_state_signature(state): 0.0}

    successes: list[
        tuple[
            float,
            int,
            int,
            tuple[str, ...],
            tuple[Transform, ...],
        ]
    ] = []

    while queue:
        current_cost, current_depth, path_ids, current_state, path = heapq.heappop(queue)

        if current_depth >= max_depth:
            continue

        for transform in transforms:
            if transform.transform_id in current_state.completed_transforms:
                continue
            if not admissible(intent, authority, current_state, transform):
                continue

            next_state = _simulate(current_state, transform)
            next_path = (*path, transform)
            next_ids = (*path_ids, transform.transform_id)
            next_cost = current_cost + transform.effective_cost
            next_depth = current_depth + 1
            next_delta = _delta_size(intent, next_state)

            if next_delta < initial_delta:
                reduction = initial_delta - next_delta
                successes.append(
                    (
                        next_cost,
                        -reduction,
                        next_depth,
                        next_ids,
                        next_path,
                    )
                )
                continue

            signature = _state_signature(next_state)
            prior_cost = best_cost.get(signature)
            if prior_cost is None or next_cost <= prior_cost:
                best_cost[signature] = next_cost
                heapq.heappush(
                    queue,
                    (
                        next_cost,
                        next_depth,
                        next_ids,
                        next_state,
                        next_path,
                    ),
                )

    if not successes:
        return ()

    successes.sort(key=lambda item: (item[0], item[1], item[2], item[3]))
    return successes[0][4]


def plan_next(
    intent: Intent,
    authority: Authority,
    state: State,
    transforms: Iterable[Transform],
    *,
    max_depth: int = 12,
) -> Transform | None:
    path = plan_path(
        intent,
        authority,
        state,
        transforms,
        max_depth=max_depth,
    )
    return path[0] if path else None


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
    return state.with_effects(transform.effects, transform.transform_id)


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
    *,
    planner_max_depth: int = 12,
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
        if (
            plan_next(
                intent,
                authority,
                state,
                transforms,
                max_depth=planner_max_depth,
            )
            is None
        ):
            return Resolution.BLOCKED

    return Resolution.INCOMPLETE


def run(
    intent: Intent,
    authority: Authority,
    initial_state: State,
    transforms: Iterable[Transform],
    *,
    max_steps: int = 100,
    planner_max_depth: int = 12,
) -> GovernanceResult:
    transforms = tuple(transforms)
    state = initial_state
    trace: list[str] = []

    for _ in range(max_steps):
        evidence = observe(intent, state)
        resolution = resolve(
            intent,
            authority,
            state,
            evidence,
            transforms,
            planner_max_depth=planner_max_depth,
        )
        trace.append(f"state:{state.version} resolution:{resolution.value}")

        if resolution is not Resolution.INCOMPLETE:
            if resolution is Resolution.BLOCKED:
                trace.append("no admissible recovery/progress path")
            return GovernanceResult(
                resolution=resolution,
                state=state,
                evidence=evidence,
                trace=tuple(trace),
            )

        path = plan_path(
            intent,
            authority,
            state,
            transforms,
            max_depth=planner_max_depth,
        )

        trace.append(
            "plan:"
            + "->".join(transform.transform_id for transform in path)
            + f" cost:{path_cost(path):.3f}"
        )

        transform = path[0]
        trace.append(
            f"apply:{transform.transform_id} "
            f"cost:{transform.base_cost:.3f} "
            f"risk:{transform.risk_penalty:.3f}"
        )
        state = apply_transform(intent, authority, state, transform)

    evidence = observe(intent, state)
    resolution = resolve(
        intent,
        authority,
        state,
        evidence,
        transforms,
        planner_max_depth=planner_max_depth,
    )
    trace.append(f"state:{state.version} resolution:{resolution.value}")

    if resolution is Resolution.INCOMPLETE:
        trace.append("max steps exhausted")
    elif resolution is Resolution.BLOCKED:
        trace.append("no admissible recovery/progress path")

    return GovernanceResult(
        resolution=resolution,
        state=state,
        evidence=evidence,
        trace=tuple(trace),
    )
