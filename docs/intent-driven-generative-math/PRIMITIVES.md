# Primitive Boundary

## General Set Calculus primitives

Intent-Driven Generative Math inherits the general Set Calculus primitive set:

```text
Set
Member
Relationship
State
Transform
Resolution
Provenance
```

Formally:

```text
SC = <Set, Member, Relationship, State, Transform, Resolution, Provenance>
```

These primitives remain domain-neutral.

## Added specialization primitives

Intent-Driven Generative Math adds only:

```text
Intent
Authority
Evidence
```

Therefore:

```text
IDGM = SC + <Intent, Authority, Evidence>
```

Expanded:

```text
IDGM =
<Set, Member, Relationship, State, Transform, Resolution, Provenance,
 Intent, Authority, Evidence>
```

## Why Completion is not primitive

Completion is a specialized Resolution outcome:

```text
Completion = Resolution(COMPLETED)
```

The same applies to INCOMPLETE, BLOCKED, UNRESOLVED, SUPERSEDED, and FAILED. They are resolution states in the generative domain.

## Derived constructs

The following are derived rather than foundational:

```text
Intent Delta
State Delta
Acceptance Criterion
Invariant
Non-goal
Constraint
Scope
Risk
Dependency
Failure Class
Completion Ledger
Planning Path
Evidence Class
Reopening
Maturity
```

Representative reductions:

```text
IntentDelta       = Transform(Intent)
AcceptanceCriterion = Member(Intent)
Completion        = Resolution(COMPLETED)
Reopening         = Transform(COMPLETED -> non-COMPLETED Resolution)
Dependency        = Relationship(Transform, Transform)
Invariant         = persistent constraint over valid States / Transforms
```

## IASTER kernel

The operational kernel selects six concepts:

```text
I = Intent       [specialized]
A = Authority    [specialized]
S = State        [general]
T = Transform    [general]
E = Evidence     [specialized]
R = Resolution   [general, domain-specialized outcomes]
```

Provenance remains transversal across the entire kernel.
