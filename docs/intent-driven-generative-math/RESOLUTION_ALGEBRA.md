# Formal Resolution Algebra

## Resolution state space

Let:

```text
R = {
  COMPLETED,
  INCOMPLETE,
  BLOCKED,
  UNRESOLVED,
  SUPERSEDED,
  FAILED
}
```

Define:

```text
rho(I,A,S,E,P) -> r
```

where `r in R` and `P` is provenance.

## Fundamental predicates

```text
Active(I)
Sat(I,S)
Provable(I,S,E)
Admissible(I,A,S)
Determinate(I,A,S,E)
Consistent(I,S)
```

Let `D(I,S)` be the unresolved semantic Intent-State delta.

## Canonical resolution function

```text
rho(I,A,S,E) =
  SUPERSEDED   if !Active(I)
  FAILED       if !Consistent(I,S) or resolution is proven impossible
  UNRESOLVED   if !Determinate(I,A,S,E)
  BLOCKED      if D != empty and !Admissible(I,A,S)
  COMPLETED    if D == empty and Provable(I,S,E)
  INCOMPLETE   otherwise
```

## COMPLETED

```text
COMPLETED iff
  Active(I)
  and Sat(I,S)
  and Provable(I,S,E)
  and Consistent(I,S)
```

Completion is conditionally terminal relative to the current Intent and relevant State/Evidence.

## INCOMPLETE

```text
INCOMPLETE iff
  Intent is active
  and requirements remain
  and at least one admissible path exists
  and the situation is determinate
```

## BLOCKED

```text
BLOCKED =
  known unresolved requirement
  + no current admissible Transform
```

Typical causes include missing authority, external dependency, unavailable resource, ownership conflict, required human decision, or high-impact boundary.

## UNRESOLVED

```text
UNRESOLVED iff
  the system lacks enough valid information
  to determine the current resolution condition
```

Unresolved is not unknown. It may retain constraints, provenance, candidate transforms, partial evidence, and possible resolution paths.

## SUPERSEDED

```text
SUPERSEDED iff
  the Intent is no longer authoritative
```

An earlier Intent may have been historically completed and later become superseded.

## FAILED

```text
FAILED iff
  the active Intent is internally inconsistent
  or required resolution is proven impossible
  under current governing conditions
```

FAILED is stronger than BLOCKED:

```text
BLOCKED = cannot proceed now
FAILED  = cannot resolve as currently defined
```

## Valid transitions

From INCOMPLETE:

```text
INCOMPLETE -> COMPLETED
INCOMPLETE -> BLOCKED
INCOMPLETE -> UNRESOLVED
INCOMPLETE -> FAILED
INCOMPLETE -> SUPERSEDED
INCOMPLETE -> INCOMPLETE
```

From BLOCKED:

```text
BLOCKED -> INCOMPLETE
BLOCKED -> COMPLETED
BLOCKED -> UNRESOLVED
BLOCKED -> FAILED
BLOCKED -> SUPERSEDED
BLOCKED -> BLOCKED
```

From UNRESOLVED:

```text
UNRESOLVED -> INCOMPLETE
UNRESOLVED -> BLOCKED
UNRESOLVED -> COMPLETED
UNRESOLVED -> FAILED
UNRESOLVED -> SUPERSEDED
UNRESOLVED -> UNRESOLVED
```

From COMPLETED:

```text
COMPLETED -> INCOMPLETE
COMPLETED -> UNRESOLVED
COMPLETED -> FAILED
COMPLETED -> SUPERSEDED
COMPLETED -> COMPLETED
```

SUPERSEDED is normally terminal for that Intent version.

FAILED is terminal for the unchanged Intent specification. Recovery normally requires a changed governing condition or a new Intent version.

## Orthogonal dimensions

The named resolution states can be derived from independent dimensions:

```text
Authority:    ACTIVE | SUPERSEDED
Determinacy:  DETERMINATE | UNRESOLVED
Feasibility:  FEASIBLE | BLOCKED | IMPOSSIBLE
Satisfaction: SATISFIED | UNSATISFIED
Proof:        PROVEN | UNPROVEN
```

Representative projection:

```text
ACTIVE + DETERMINATE + FEASIBLE + SATISFIED + PROVEN
  -> COMPLETED

ACTIVE + DETERMINATE + FEASIBLE + UNSATISFIED
  -> INCOMPLETE

ACTIVE + DETERMINATE + BLOCKED + UNSATISFIED
  -> BLOCKED

ACTIVE + UNRESOLVED
  -> UNRESOLVED

SUPERSEDED
  -> SUPERSEDED

ACTIVE + DETERMINATE + IMPOSSIBLE
  -> FAILED
```

## Algebra

```text
R_IDGM = <R, rho, ->, DeltaI>
```

where:

- `R` is the resolution state set;
- `rho` maps the current generative condition to a Resolution;
- `->` is the valid transition relation;
- `DeltaI` mutates the governing Intent and may force re-resolution.

## Resolution conservation

An unrelated Intent change must not invalidate unaffected resolution claims.

```text
UnrelatedChange !-> GlobalReopening
```

If the requirement, relevant State, and proof remain unchanged, the prior component resolution remains valid.
