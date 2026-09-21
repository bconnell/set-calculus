# Intent-Driven Generative Math: Axioms and Laws

This document defines the formal axioms and derived laws of Intent-Driven Generative Math (IDGM).

IDGM is a specialization of general Set Calculus:

```text
IDGM = Set Calculus + Intent + Authority + Evidence
```

It inherits:

```text
Set
Member
Relationship
State
Transform
Resolution
Provenance
```

and adds:

```text
Intent
Authority
Evidence
```

Completion is not primitive:

```text
Completion = Resolution(COMPLETED)
```

The operational kernel is IASTER:

```text
Intent -> Authority -> State -> Transform -> Evidence -> Resolution
```

---

# 1. Formal Domain

Let:

```text
I  = Intent
A  = Authority
S  = State
T  = Transform
E  = Evidence
R  = Resolution
P  = Provenance
```

Define the generative context:

```text
G = <I,A,S,E,P>
```

Define the resolution operator:

```text
rho(G) -> R
```

where:

```text
R in {
  COMPLETED,
  INCOMPLETE,
  BLOCKED,
  UNRESOLVED,
  SUPERSEDED,
  FAILED
}
```

Define semantic Intent-State delta:

```text
D(I,S) = { r in Requirements(I) | S does not satisfy r }
```

The delta is semantic rather than textual.

---

# 2. Foundational Axioms

## Axiom 1: Intent Distinction

Intent and State are distinct objects.

```text
Intent = what should become true
State  = what is true
```

Therefore:

```text
I != S
```

in general.

A change in Intent does not imply a change in State.

A change in State does not imply a change in Intent.

---

## Axiom 2: State Transformability

A Transform maps one State to another:

```text
T : S_t -> S_(t+1)
```

A Transform may preserve State:

```text
T(S) = S
```

or modify it.

---

## Axiom 3: Authority-Bounded Transformation

A Transform is admissible only when authority permits that operation over the affected object, scope, and time boundary.

```text
Admissible(T) -> Authorized(A,T)
```

Authorization is operation-specific.

```text
Authorized(read) !-> Authorized(write)
Authorized(write) !-> Authorized(delete)
Authorized(local_change) !-> Authorized(publication)
```

---

## Axiom 4: Current-State Primacy

Execution is governed by current valid State rather than stale remembered State.

If:

```text
Observed(S_t)
```

conflicts with:

```text
Remembered(S_(t-k))
```

for a materially relevant boundary, the current observed State governs execution.

---

## Axiom 5: Evidence-Claim Specificity

Evidence proves only claims within its valid proof boundary.

```text
E |- q
```

does not imply:

```text
E |- r
```

unless a valid relationship establishes that implication.

Examples:

```text
BuildPass     !-> RuntimeCorrect
Screenshot    !-> SemanticCorrect
SingleSuccess !-> LifecycleReliable
```

---

## Axiom 6: Explicit Resolution

The system must resolve explicitly rather than silently inventing certainty.

If the available structure is insufficient to determine a valid result:

```text
rho(G) = UNRESOLVED
```

rather than fabricating a resolved value.

---

## Axiom 7: Provenance Persistence

Every material Resolution should retain enough Provenance to determine the Inputs, Relationships, Transforms, and Evidence that produced it.

A Transform does not erase origin merely because State changed.

---

# 3. Invariant Laws

## Law 1: Invariant Preservation

For any invariant `q` required by Intent:

```text
q(S_t) = true
```

an admissible Transform must preserve:

```text
q(T(S_t)) = true
```

unless the current authoritative Intent explicitly changes that invariant and Authority permits that change.

---

## Law 2: Invariant Violation Blocks Completion

If any required invariant is false:

```text
exists q in Invariants(I) such that q(S) = false
```

then:

```text
rho(G) != COMPLETED
```

---

## Law 3: Invariant Non-Projection

A property produced by a Transform is not assumed to have been a property of the unresolved input.

```text
property(T(x)) !-> property(x)
```

unless an explicit relationship establishes backward implication.

---

## Law 4: Protected Invariant Persistence

Inherited mandatory protections cannot be silently removed by ordinary implementation choice.

Examples include:

```text
user-data preservation
credential protection
privacy
repository integrity
destructive-history safety
legal constraints
high-impact external-state boundaries
```

Changing one of these requires explicit governing Authority, not merely Transform convenience.

---

# 4. Composition Laws

## Law 5: Sequential Composition

For composable Transforms:

```text
T1 : S0 -> S1
T2 : S1 -> S2
```

their composition is:

```text
(T2 o T1)(S0) = S2
```

Composition is valid only if each intermediate boundary remains admissible.

```text
Admissible(T2 o T1)
requires
Admissible(T1)
and Admissible(T2 | S1)
```

---

## Law 6: Authority Is Not Automatically Compositional

Even when two individual Transforms are valid as functions:

```text
T1
T2
```

their composition is not automatically authorized.

```text
Authorized(T1)
and Authorized(T2)
!-> Authorized(T2 o T1)
```

when the composition crosses a new scope, publication, destructive, external-state, or other authority boundary.

---

## Law 7: Independent Transform Composition

If:

```text
T1 || T2
```

and they do not conflict in ownership or writes:

```text
Writes(T1) intersect Writes(T2) = empty
```

then they may be composed in either order when their semantics commute:

```text
T2(T1(S)) = T1(T2(S))
```

---

## Law 8: Dependency Ordering

If:

```text
T1 < T2
```

means T2 depends on T1, then:

```text
T2
```

must not be treated as admissible until the required output boundary of T1 is resolved.

---

## Law 9: Intent Delta Composition

For sequential Intent changes:

```text
I1 --Delta1--> I2 --Delta2--> I3
```

a composite delta may be derived:

```text
Delta(1,3) = Delta2 o Delta1
```

but original Deltas and their Provenance must remain available.

Composition must not erase intermediate authoritative history.

---

# 5. Monotonicity Laws

## Law 10: Progress Monotonicity

For a valid progress Transform:

```text
D(I,S_(t+1)) subseteq D(I,S_t)
```

Strong progress requires:

```text
D(I,S_(t+1)) proper-subset D(I,S_t)
```

provided no required invariant is violated.

---

## Law 11: Knowledge Monotonicity

A Transform that does not reduce Intent-State delta may still be productive if it increases reliable knowledge.

Let:

```text
K_t
```

be the set of justified current facts.

Then diagnostic progress may satisfy:

```text
K_t subset K_(t+1)
```

without changing:

```text
D(I,S)
```

---

## Law 12: Evidence Monotonicity Under Compatibility

If:

```text
E1 |- q
```

and new evidence `E2` is compatible with E1, then:

```text
E1 union E2 |- q
```

Evidence accumulation should preserve or strengthen justified claims unless later Evidence contradicts, invalidates, or makes stale the previous proof.

---

## Law 13: Non-Monotonicity Under Contradiction

If:

```text
E1 |- q
E2 |- not-q
```

then the system must not preserve q merely because it was established first.

Instead, the claim becomes subject to provenance, freshness, subject identity, and evidence-authority resolution.

A previously resolved claim may transition to:

```text
UNRESOLVED
```

or:

```text
FAILED
```

depending on the contradiction.

---

## Law 14: Completion Monotonicity Under Stable Inputs

If:

```text
rho(I,A,S,E,P) = COMPLETED
```

and no materially relevant component of:

```text
I, A, S, E, P
```

changes, then repeated evaluation remains:

```text
COMPLETED
```

This is the Completion fixpoint property.

---

## Law 15: Completion Is Not Globally Monotone

Completion may be invalidated by a material change in:

```text
Intent
State
Authority
Evidence
Provenance
```

Therefore:

```text
COMPLETED_t !-> COMPLETED_(t+1)
```

without stability of relevant inputs.

---

# 6. Conservation Laws

## Law 16: Provenance Conservation

For any valid Transform:

```text
P_(t+1)
```

must preserve sufficient ancestry to recover materially relevant:

```text
inputs
relationships
prior states
transforms
authority
evidence
resolution history
```

Information may be summarized, but required lineage must not be silently erased.

---

## Law 17: Unaffected Resolution Conservation

If an Intent Delta does not affect a requirement `r`, and the relevant State and Evidence remain valid, then:

```text
Resolution_(n+1)(r) = Resolution_n(r)
```

Therefore:

```text
UnrelatedChange !-> GlobalReopening
```

---

## Law 18: Valid Work Conservation

Let:

```text
W_t
```

be the set of valid completed work.

Absent invalidation:

```text
W_t subseteq W_(t+1)
```

Completed work is preserved unless:

```text
Intent changes materially
relevant State changes
Evidence becomes invalid or stale
a contradiction is discovered
the work is explicitly superseded
```

---

## Law 19: Unfinished Work Conservation

Let the active completion ledger contain item `l`.

Then:

```text
l_t -> empty
```

is invalid unless there is an explicit disposition:

```text
COMPLETED
DEFERRED
REPLACED
RETIRED
SUPERSEDED
FAILED
```

New work or priority changes must not cause unresolved work to disappear silently.

---

## Law 20: Intent History Conservation

When:

```text
I_n --DeltaI--> I_(n+1)
```

the newer Intent replaces governing authority but does not rewrite historical Intent.

```text
Supersession != historical erasure
```

---

## Law 21: Scope Conservation Under Narrow Change

A local change in one semantic boundary must not enlarge the affected work boundary without a dependency relationship establishing the need.

```text
LocalDelta -> LocalReevaluation
```

unless the affected element participates in a shared mechanism or dependency whose blast radius is broader.

---

# 7. Resolution Laws

## Law 22: Resolution Determinacy

For a fixed valid context:

```text
G = <I,A,S,E,P>
```

the Resolution operator should return one canonical state:

```text
rho(G) in R
```

where:

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

---

## Law 23: Resolution Precedence

The canonical resolution decision order is:

```text
if !Active(I):
    SUPERSEDED

else if impossible or inconsistent:
    FAILED

else if not determinate:
    UNRESOLVED

else if unresolved requirements remain and no admissible transform exists:
    BLOCKED

else if all requirements are satisfied and sufficiently proven:
    COMPLETED

else:
    INCOMPLETE
```

---

## Law 24: Blocked/Failed Distinction

```text
BLOCKED
```

means:

```text
cannot proceed now
```

while:

```text
FAILED
```

means:

```text
cannot resolve as currently defined
```

BLOCKED may become INCOMPLETE or COMPLETED without changing Intent.

FAILED normally requires a change in governing conditions or Intent.

---

## Law 25: Supersession Orthogonality

SUPERSEDED is not a statement that the prior Resolution was incorrect.

A prior Intent may satisfy:

```text
HistoricalResolution(I_n) = COMPLETED
```

while also satisfying:

```text
CurrentResolution(I_n) = SUPERSEDED
```

because it no longer governs active work.

---

# 8. Planning Laws

## Law 26: Planning from Semantic Delta

Planning operates over:

```text
D(I,S)
```

rather than over Intent text alone.

Candidate Transforms must address unresolved semantic requirements or required supporting conditions.

---

## Law 27: Minimal Admissible Transform

Among valid candidate Transforms, prefer the smallest coherent Transform that advances resolution while preserving invariants and authority boundaries.

This is a partial-order preference rather than a universal scalar optimization.

---

## Law 28: No-Op Rejection

A Transform that:

```text
does not reduce D(I,S)
does not increase justified knowledge
does not resolve authority
does not repair evidence
does not restore recoverability
```

is non-progressing with respect to the current Intent.

Such a Transform should not be selected as productive work absent another explicit purpose.

---

## Law 29: Replanning Trigger

Replanning is required when a material change occurs in:

```text
Intent
Authority
Current State
Evidence validity
dependency structure
failure classification
```

Replanning should preserve unaffected valid work.

---

# 9. Evidence Laws

## Law 30: Evidence Freshness

Evidence must correspond to the State and candidate identity relevant to the claim.

If a materially relevant State transition occurs after Evidence is produced:

```text
E_t
```

then:

```text
E_t
```

must be re-evaluated before proving claims about:

```text
S_(t+1)
```

---

## Law 31: Evidence Provenance

Evidence without sufficient subject, source, candidate, or state identity cannot establish a claim requiring those identities.

---

## Law 32: Proof Boundary Conservation

Evidence may be reused across Intent versions only when the relevant proof boundary remains semantically unchanged.

Intent version mismatch alone does not invalidate Evidence.

Semantic mismatch does.

---

# 10. Failure and Recovery Laws

## Law 33: Failure-Owner Alignment

A detected failure must be classified before repair.

Representative classes:

```text
Product
Harness
Environment
Infrastructure
Authority
State
Evidence
Resource
```

Repair should target the owner of the failure.

```text
HarnessFailure !-> Modify(Product)
EnvironmentFailure !-> ProductRegression
```

---

## Law 34: Repeated-Failure Escalation

If repeated failures share the same architectural class or owner mechanism, repeated local repair should transition toward shared-mechanism audit.

```text
RepeatedSymptom + SharedMechanism -> SystemicAudit
```

---

## Law 35: Recovery Preserves Valid State

Recovery from failure must preserve unaffected valid work, Evidence, Provenance, and current authoritative Intent wherever possible.

Failure does not authorize arbitrary reset.

---

# 11. Algebraic Summary

The formal IDGM system is:

```text
IDGM =
<SC, Intent, Authority, Evidence>
```

with:

```text
SC =
<Set, Member, Relationship, State, Transform, Resolution, Provenance>
```

The runtime context is:

```text
G = <I,A,S,E,P>
```

Planning derives admissible Transform paths from semantic delta:

```text
Plan(I,A,S) -> <T1,T2,...,Tn>
```

Execution applies:

```text
T : S_t -> S_(t+1)
```

Evidence evaluates resulting claims:

```text
E |- q
```

Resolution classifies the current condition:

```text
rho(I,A,S,E,P) -> R
```

where:

```text
R in {
  COMPLETED,
  INCOMPLETE,
  BLOCKED,
  UNRESOLVED,
  SUPERSEDED,
  FAILED
}
```

The controlling conservation principle is:

```text
Only materially changed semantics should force changed execution,
changed evidence, or changed resolution.
```

The controlling progress principle is:

```text
Perform only admissible Transforms that advance Intent resolution,
increase justified knowledge, resolve authority, repair evidence,
or restore recoverability.
```

The controlling validation principle is:

```text
Claim only what current valid Evidence proves about current State
under current authoritative Intent.
```
