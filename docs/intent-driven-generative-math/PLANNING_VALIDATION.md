# Planning and Validation

Intent-Driven Generative Math uses the same primitives in two directions.

## Forward direction: planning

Planning asks:

```text
Given Intent, Authority, and Current State,
what admissible Transform path should occur next?
```

Define:

```text
D = I - S
```

as semantic difference, not literal subtraction.

Candidate Transforms are generated from the unresolved delta:

```text
T_candidates = GenerateTransforms(D,A,S)
```

The admissible subset satisfies:

```text
Authorized(T)
and InScope(T)
and ConstraintSafe(T)
and InvariantPreserving(T)
```

A plan is an ordered Transform path:

```text
Plan = <T1,T2,...,Tn>
```

whose execution is expected to reduce the unresolved semantic delta while preserving required invariants.

## Dependency and recovery planning

A valid plan may contain intermediate Transforms that do not directly reduce Intent-State delta when those Transforms establish dependencies, preconditions, authority conditions, or recoverability required by later advancing work.

For a Transform dependency:

```text
T1 < T2
```

T2 is not eligible until T1 has resolved its required boundary.

A planner may therefore derive:

```text
Recovery
  -> Prerequisite
  -> Advancing Transform
  -> Reduced Delta
```

without treating the intermediate work as goal completion.

## Cost-aware planning

Each Transform may carry a non-negative base cost and risk penalty:

```text
Cost(T) = BaseCost(T) + RiskPenalty(T)
```

For a path:

```text
P = <T1,T2,...,Tn>
```

define:

```text
Cost(P) = sum(Cost(T_i))
```

Cost and risk do not make an inadmissible Transform admissible. Authority, scope, constraints, and invariants are evaluated first.

Among admissible paths that reduce semantic delta, canonical deterministic selection is:

```text
1. lowest total effective path cost
2. greatest semantic-delta reduction
3. fewest Transforms
4. lexicographically smallest Transform-ID path
```

This permits a longer low-cost, low-risk path to outrank a shorter expensive or high-risk path.

Risk penalty is an explicit planning quantity, not an implicit permission rule:

```text
RiskPenalty(T) >= 0
```

A high risk penalty may make another admissible path preferable, but risk scoring alone does not revoke or grant Authority.

## Deterministic selection

For a fixed:

```text
Intent
Authority
State
Transform set
cost model
risk model
search boundary
```

the planner should return the same selected path.

Equal-value plans are resolved by the canonical ordering rather than iteration order, insertion order, randomness, or model preference.

## Backward direction: validation

Validation asks:

```text
Given the generated result,
does the resulting proven State satisfy current Intent?
```

A generated result is valid only to the extent supported by:

```text
Intent alignment
Authority
Current State
Transform admissibility
Evidence
Resolution
```

## Unified loop

```text
Intent
  -> Current State
  -> Semantic Delta
  -> Plan
  -> Transform
  -> New State
  -> Evidence
  -> Resolution
  -> Complete / Continue / Block / Investigate / Revise Intent
```

## Planning and validation symmetry

The same acceptance criteria and invariants used to generate a plan are used to validate its result.

This prevents a planner from optimizing toward one target while a validator judges against a different target.

Cost and risk influence path selection. They do not weaken the validation boundary required for Resolution.

## Generative work interpretation

The specialization therefore supports three linked functions:

```text
Planning
Controlled Transformation
Validation
```

A compact description is:

```text
Intent-directed generative work calculus
```

or:

```text
math for planning, governing, and validating generative work
```
