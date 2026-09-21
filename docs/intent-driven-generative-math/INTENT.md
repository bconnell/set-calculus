# Intent and Intent Delta

## Intent

Intent is the authoritative representation of the outcome currently being pursued.

A canonical Intent contains:

```text
Intent {
  intent_id
  version
  status
  provenance

  objective
  scope

  invariants
  acceptance_criteria
  non_goals
  constraints

  supersedes
  superseded_by

  authority_source

  created_at
  activated_at
  completed_at
}
```

## Identity

`intent_id` remains stable across clarification, refinement, correction, and compatible revision of the same logical objective.

A materially different objective should receive a new identity.

## Version

Every material authoritative change creates a new version.

```text
INT-042:v1
INT-042:v2
INT-042:v3
```

A version change is required when objective, scope, invariants, acceptance criteria, non-goals, constraints, or completion requirements materially change.

## Intent semantics

```text
Intent = what should become true
State  = what is true
```

Define the unresolved semantic delta:

```text
D(I,S) = { r in Requirements(I) | S does not satisfy r }
```

The delta is semantic rather than textual.

## Intent Delta

Intent changes through a specialized Transform:

```text
DeltaI : I_n -> I_(n+1)
```

Canonical delta classification:

```text
added
modified
removed
preserved
```

Recommended change classes:

```text
CLARIFICATION
CORRECTION
EXPANSION
REDUCTION
CONSTRAINT_CHANGE
ACCEPTANCE_CHANGE
SCOPE_CHANGE
PRIORITY_CHANGE
REPLACEMENT
ROLLBACK
```

## Delta propagation

A material Intent Delta may propagate into:

```text
DeltaI
  -> State reinspection
  -> Transform re-evaluation
  -> Evidence reclassification
  -> Resolution re-evaluation
```

Only the changed semantic boundary should cause changed execution, changed evidence, or reopened work.

## Supersession

Supersession is explicit and provenance-preserving.

```text
I_n --DeltaI--> I_(n+1)
```

A superseded Intent remains historically valid as provenance. It simply no longer governs current execution.

Compatible unchanged requirements survive revision unless explicitly replaced.
