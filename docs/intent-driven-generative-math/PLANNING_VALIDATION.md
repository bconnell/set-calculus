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
