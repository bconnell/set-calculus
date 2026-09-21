# Intent-Driven Generative Math

Intent-Driven Generative Math is a specialization of general Set Calculus for planning, governing, executing, and validating generative work.

It does not replace Set Calculus. It inherits the general transformation and resolution machinery and adds the domain primitives required when work is directed toward an intended outcome.

## General relationship

```text
Set Calculus
  -> structure
  -> relationship
  -> state
  -> transform
  -> resolution
  -> provenance

Intent-Driven Generative Math
  -> inherits Set Calculus
  -> adds Intent
  -> adds Authority
  -> adds Evidence
  -> specializes Resolution for generative work
```

A compact definition is:

```text
IDGM = Set Calculus + Intent + Authority + Evidence
```

Completion is not a primitive. It is a specialized Resolution state.

## Operational kernel

The runtime kernel is:

```text
Intent
  -> Authority
  -> State
  -> Transform
  -> Evidence
  -> Resolution
```

Abbreviation:

```text
IASTER
```

where State, Transform, Resolution, and Provenance are inherited from Set Calculus.

## Purpose

The specialization answers three linked questions:

1. Planning: what valid transforms should occur next?
2. Governance: which transforms are admissible under current authority, scope, constraints, and invariants?
3. Validation: does the resulting proven state satisfy the current authoritative Intent?

## Core loop

```text
Intent
  -> inspect current State
  -> calculate unresolved semantic delta
  -> select admissible Transform
  -> produce new State
  -> gather Evidence
  -> resolve
       COMPLETED
       INCOMPLETE
       BLOCKED
       UNRESOLVED
       SUPERSEDED
       FAILED
```

If Resolution is not terminal, the system continues, resolves a blocker, acquires information, repairs a failure, or applies an Intent change.

## Files

- `PRIMITIVES.md` - general vs specialized primitive boundary
- `INTENT.md` - first-class Intent and Intent Delta
- `EXECUTION_KERNEL.md` - IASTER planning / execution / validation loop
- `RESOLUTION_ALGEBRA.md` - formal resolution states and transitions
- `PLANNING_VALIDATION.md` - forward planning and backward validation

This directory is intentionally separate from `docs/set-calculus-core/`. The general calculus should remain domain-neutral.
