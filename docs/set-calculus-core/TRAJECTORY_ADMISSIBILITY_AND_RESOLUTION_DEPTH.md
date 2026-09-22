# Trajectory Admissibility and Resolution Depth

## Status

Working Set Math formalization.

This document captures the current formal development of:

- trajectory admissibility;
- admissibility composition;
- boundary compatibility;
- representation structures;
- resolution depth;
- depth-indexed requirement sets;
- requirement entailment across depth.

It does not change the stable architecture. These objects are formal structures developed within the existing Set Calculus framework.

---

# 1. Trajectories

A trajectory is an ordered alternating sequence of States and Transforms:

```text
π = <s0, T1, s1, T2, ..., Tn, sn>
```

where:

```text
si = State
Ti = Transform
```

Trajectory length is not identical to resolution depth.

```text
trajectory length
!=
resolution depth
```

A long trajectory may repeat the same structural distinction and therefore add little or no resolution depth.

---

# 2. Trajectory Admissibility

Define:

```text
Adm(π | C,A)
∈ {
  ADMISSIBLE,
  INADMISSIBLE,
  UNRESOLVED
}
```

where:

```text
C = active Context / resolution boundary
A = active Authority / rule set
```

The trajectory is admissible when every State, Relationship, Transform, constraint, and provenance dependency needed by the path composes validly under the active Context and Authority.

Equivalent set notation:

```text
Π_adm(C,A)
=
{ π | Adm(π | C,A) = ADMISSIBLE }
```

## 2.1 Minimum admissibility axioms

### Axiom TA-1: Membership Validity

Every object participating materially in the trajectory must belong to, or be explicitly related to, the active Context.

```text
Adm(π | C,A) = ADMISSIBLE
=>
∀x ∈ π:
Member(x,C)
∨ Relates(x,C)
```

### Axiom TA-2: Transform Applicability

Every Transform must be applicable to the State from which it is taken.

```text
Ti : s_(i-1) -> si
=>
Applicable(Ti, s_(i-1) | C,A)
```

Therefore:

```text
defined(Ti)
!=
applicable(Ti, s_(i-1))
```

### Axiom TA-3: Sequential Composability

Adjacent trajectory segments must share a compatible intermediate State.

```text
Ti : s_(i-1) -> si
T_(i+1) : si -> s_(i+1)
```

requires:

```text
Output(Ti)
compatible-with
Input(T_(i+1))
```

Thus:

```text
functional sequence
!-> admissible trajectory
```

without a valid boundary.

### Axiom TA-4: Constraint Preservation

Every materially required invariant must be preserved unless an explicit authorized change permits alteration.

Let:

```text
I(C,A)
```

be the active invariant set.

Then:

```text
Adm(π | C,A) = ADMISSIBLE
=>
∀Ti ∈ π,
∀i ∈ RequiredInvariants(Ti):
Preserve(Ti,i)
∨ AuthorizedChange(Ti,i,C,A)
```

### Axiom TA-5: Provenance Continuity

Every materially relevant resolved State along an admissible trajectory must remain traceable to the State and Transform that produced it.

```text
Traceable(
  si <- Ti <- s_(i-1)
)
```

for all required trajectory steps.

Compactly:

```text
trajectory continuity
requires
provenance continuity
```

### Axiom TA-6: No Invented Resolution

A required unresolved bridge, relation, metric, authority, or transition must remain unresolved.

```text
required(x)
∧ unresolved(x)
=>
Adm(π | C,A) = UNRESOLVED
```

It must not be silently promoted to:

```text
ADMISSIBLE
```

This preserves:

```text
Unresolved != Unknown
```

and prevents path completion by assumption.

---

# 3. Admissibility Composition Algebra

Let:

```text
π1 = <s0, ..., sk>
π2 = <sk', ..., sn>
```

and let:

```text
π1 ⊕ π2
```

denote ordered trajectory concatenation.

Define the admissibility status composition operator:

```text
⊗A
```

with the table:

| ⊗A | ADMISSIBLE | UNRESOLVED | INADMISSIBLE |
|---|---:|---:|---:|
| **ADMISSIBLE** | ADMISSIBLE | UNRESOLVED | INADMISSIBLE |
| **UNRESOLVED** | UNRESOLVED | UNRESOLVED | INADMISSIBLE |
| **INADMISSIBLE** | INADMISSIBLE | INADMISSIBLE | INADMISSIBLE |

Interpretation:

```text
ADMISSIBLE
= identity

UNRESOLVED
= uncertainty-preserving

INADMISSIBLE
= absorbing
```

Compact ordering:

```text
ADMISSIBLE < UNRESOLVED < INADMISSIBLE
```

with:

```text
a ⊗A b = max(a,b)
```

under the status ordering.

This ordering applies to status reduction, not truth value.

## 3.1 Concatenation law

```text
Adm(π1 ⊕ π2 | C,A)
=
Adm(π1 | C,A)
⊗A
BoundaryCompatible(π1,π2 | C,A)
⊗A
Adm(π2 | C,A)
```

Two individually admissible segments do not guarantee an admissible concatenation.

```text
ADMISSIBLE segment
+
ADMISSIBLE segment
!-> ADMISSIBLE concatenation
```

without an admissible boundary.

## 3.2 Identity law

Let:

```text
ε_s = <s>
```

be the zero-length trajectory at State `s`.

When `s` is valid in the active Context:

```text
Adm(ε_s | C,A) = ADMISSIBLE
```

and:

```text
ε ⊕ π = π
π ⊕ ε = π
```

subject to valid boundary compatibility.

## 3.3 Inadmissibility absorption

```text
Adm(π_i) = INADMISSIBLE
=>
Adm(π_1 ⊕ ... ⊕ π_i ⊕ ... ⊕ π_n)
= INADMISSIBLE
```

## 3.4 Unresolved propagation

If no segment or boundary is INADMISSIBLE and at least one is UNRESOLVED:

```text
Adm(π) = UNRESOLVED
```

Successful local validation cannot erase unresolved evidence.

## 3.5 Positive composition

```text
Adm(π1 ⊕ π2) = ADMISSIBLE
```

iff:

```text
Adm(π1) = ADMISSIBLE
∧ Adm(π2) = ADMISSIBLE
∧ BoundaryCompatible(π1,π2) = ADMISSIBLE
```

## 3.6 Associativity

For validly typed concatenations:

```text
(π1 ⊕ π2) ⊕ π3
=
π1 ⊕ (π2 ⊕ π3)
```

and:

```text
(a ⊗A b) ⊗A c
=
a ⊗A (b ⊗A c)
```

## 3.7 Ordered trajectory / symmetric status distinction

The status algebra is commutative:

```text
a ⊗A b = b ⊗A a
```

but trajectory concatenation is not:

```text
π1 ⊕ π2
!=
π2 ⊕ π1
```

## 3.8 Prefix law

```text
Adm(π_prefix) = INADMISSIBLE
=>
Adm(π_prefix ⊕ π_suffix) = INADMISSIBLE
```

but:

```text
Adm(π_prefix) = ADMISSIBLE
!-> Adm(π) = ADMISSIBLE
```

## 3.9 Monotonic failure

```text
Adm(π) = INADMISSIBLE
=>
Adm(π ⊕ σ) = INADMISSIBLE
```

UNRESOLVED is not permanently absorbing under later reconciliation:

```text
UNRESOLVED
-> ADMISSIBLE
```

or:

```text
UNRESOLVED
-> INADMISSIBLE
```

may occur when previously missing evidence resolves.

---

# 4. Boundary Compatibility

Define:

```text
BoundaryCompatible(π1,π2 | C,A)
∈ {
  ADMISSIBLE,
  INADMISSIBLE,
  UNRESOLVED
}
```

The boundary is admissible only when the outgoing condition of `π1` can validly become the incoming condition of `π2`.

Define:

```text
B(π1,π2 | C,A)
=
StateCompat
⊗A ContextCompat
⊗A AuthorityCompat
⊗A InvariantCompat
⊗A ProvenanceCompat
```

and:

```text
BoundaryCompatible(π1,π2 | C,A)
=
B(π1,π2 | C,A)
```

## 4.1 State compatibility

Let:

```text
s_out = TerminalState(π1)
s_in  = InitialState(π2)
```

State compatibility is ADMISSIBLE when:

```text
s_out = s_in
```

or an explicit valid compatibility/projection relation exists:

```text
CompatibleState(s_out,s_in)
```

or:

```text
Project(s_out -> s_in)
```

with all required bridge conditions satisfied.

Therefore:

```text
semantic similarity
!-> StateCompat
```

## 4.2 Context compatibility

Let:

```text
C1 = Context(π1)
C2 = Context(π2)
```

Context compatibility is ADMISSIBLE when:

```text
C1 = C2
```

or there is an authorized Context transition or explicit relation preserving materially required State.

```text
context change
!=
automatic continuity
```

## 4.3 Authority compatibility

Let:

```text
A1 = Authority(π1)
A2 = Authority(π2)
```

Authority compatibility requires that the outgoing State produced under `A1` remains validly acceptable at the entry to `π2` under `A2`.

A sufficient condition is:

```text
ValidUnder(s_out,A1)
∧ Accepts(A2,s_out)
∧ Authorized(T_(k+1),A2)
```

Thus:

```text
change of authority
!-> invalidity
```

but:

```text
change of authority
requires explicit compatibility
```

## 4.4 Invariant compatibility

Let:

```text
I_boundary
=
PreserveRelevant(I1,π2)
∪ RequiredAtEntry(I2)
```

Then:

```text
InvariantCompat = ADMISSIBLE
```

iff for every:

```text
i ∈ I_boundary
```

either:

```text
Holds(i,s_out)
```

or:

```text
AuthorizedChange(i)
```

establishes a valid transition before the invariant is required.

## 4.5 Provenance compatibility

Let:

```text
P1 = Provenance(π1)
P2 = ProvenanceRequirements(π2)
```

Provenance compatibility requires:

```text
Traceable(TerminalState(π1) <- π1)
```

plus acceptance and composability of the required lineage:

```text
AcceptsProvenance(π2,P1)
```

and:

```text
ComposeProv(P1,BoundaryEvidence,P2)
```

must be defined.

Known provenance destruction produces INADMISSIBLE when provenance is required.

Unavailable but potentially recoverable provenance produces UNRESOLVED.

```text
missing evidence
!=
evidence of invalidity
```

---

# 5. Representation Structure

Define a representation structure:

```text
G = <V, R, Σ, Φ, I, P>
```

where:

```text
V = representable objects / states
R = representable relations
Σ = representable state distinctions
Φ = supported transforms
I = preserved invariants / constraints
P = provenance structure
```

Define:

```text
Supports(G,t | C,A)
```

to mean:

> G can represent, distinguish, transform, preserve, reach, and reconstruct all information materially required to resolve through depth t under Context C and Authority A.

Resolution depth is not simply the number of executed steps.

```text
resolution depth
!=
trajectory length
```

---

# 6. Depth-Indexed Requirement Sets

Define:

```text
R_t =
<
  Rep_t,
  Dist_t,
  Trans_t,
  Inv_t,
  Reach_t,
  Prov_t
>
```

where:

```text
Rep_t   = representability requirements
Dist_t  = distinguishability requirements
Trans_t = transform-closure requirements
Inv_t   = invariant / constraint requirements
Reach_t = reachability requirements
Prov_t  = provenance requirements
```

Then:

```text
Supports(G,t | C,A)
iff
G ⊨ R_t
```

with:

```text
G ⊨ R_t
iff
G ⊨ Rep_t
∧ G ⊨ Dist_t
∧ G ⊨ Trans_t
∧ G ⊨ Inv_t
∧ G ⊨ Reach_t
∧ G ⊨ Prov_t
```

## 6.1 Incremental requirements

Let:

```text
ΔR_t
```

be the requirements introduced specifically at depth `t`.

The naive cumulative form is:

```text
R_t = R_(t-1) ∪ ΔR_t
```

but the preferred form is:

```text
R_t
=
PreserveRelevant(R_(t-1),t)
∪ ΔR_t
```

because a shallower requirement may later be legitimately discharged or replaced.

---

# 7. Representability Requirements

Define:

```text
Rep_t
=
{
  x :
  x must be representable
  to resolve through depth t
}
```

This may include:

```text
objects
states
relations
constraints
transforms
metadata
```

Depth growth:

```text
Rep_(t+1)
=
PreserveRelevant(Rep_t,t+1)
∪ NewObjects_(t+1)
∪ NewRelations_(t+1)
```

A previously represented object may disappear from the explicit representation only if its resolution obligation has been validly discharged or replaced.

---

# 8. Distinguishability Requirements

Define:

```text
Dist_t
=
{
  (x,y) :
  x and y must remain distinguishable
  through depth t
}
```

Then:

```text
(x,y) ∈ Dist_t
=>
Rep_G(x) != Rep_G(y)
```

Depth may expose distinctions that were unnecessary at shallower levels:

```text
depth increases
-> equivalence classes may split
```

A merge is legitimate only when equivalence has been established for all materially remaining resolution purposes.

---

# 9. Transform-Closure Requirements

Define:

```text
Trans_t
=
{
  T :
  T must be expressible and closed
  for resolution through depth t
}
```

For a required Transform:

```text
T : s_i -> s_j
```

the relevant input and output representations must remain valid.

Depth may introduce both new atomic Transforms and new composition requirements:

```text
Trans_t
=
AtomicTransforms_t
∪ CompositionRequirements_t
```

A deeper level may therefore fail even when every individual Transform exists if the required composition does not.

---

# 10. Constraint-Preservation Requirements

Define:

```text
Inv_t
=
{
  i :
  invariant or constraint i
  must hold through depth t
}
```

For every required Transform `T`:

```text
Preserve(T,i)
∨ AuthorizedChange(T,i)
```

must hold for each materially relevant invariant.

Depth may expose new constraints:

```text
Inv_(t+1)
=
PreserveRelevant(Inv_t,t+1)
∪ NewlyVisibleConstraints_(t+1)
```

Therefore:

```text
valid at depth t
!-> valid at depth t+1
```

---

# 11. Reachability Requirements

Define `Reach_t` as the set of required targets and boundary conditions that must be reachable by admissible trajectories at depth `t`.

One useful form is:

```text
Reach_t =
<
  RequiredTargets_t,
  RequiredBoundaryConditions_t,
  RequiredAdmissibility_t
>
```

For every required target `q`:

```text
∃π_q :
Adm(π_q | C,A) = ADMISSIBLE
∧ reaches(π_q,q)
```

Depth growth may add:

```text
NewTargetReachability
NewBoundaryConditions
NewAdmissibilityObligations
```

Structural representability alone does not establish reachability.

---

# 12. Provenance Requirements

Define:

```text
Prov_t
```

as the minimum provenance needed to reconstruct and validate all materially relevant resolution steps through depth `t`.

Depth growth normally extends provenance:

```text
Prov_(t+1)
=
PreserveRelevant(Prov_t,t+1)
∪ NewProvenanceEdges_(t+1)
```

Canonical rule:

```text
deeper resolution
requires provenance extension
not provenance replacement
```

unless explicit compression preserves all materially required reconstructibility.

---

# 13. Supported Resolution Depth

Define:

```text
Supports(G,t | C,A)
iff
Representable(G,t)
∧ Distinguishable(G,t)
∧ TransformClosed(G,t)
∧ ConstraintPreserving(G,t)
∧ Reachable(G,t | C,A)
∧ ProvenanceContinuous(G,t)
```

Then:

```text
t_max(G | C,A)
=
sup {
  t :
  Supports(G,t | C,A)
}
```

For discrete depth, define the first failure:

```text
t_fail
=
min {
  t :
  !Supports(G,t)
}
```

and where the cumulative-depth assumptions hold:

```text
t_max = t_fail - 1
```

Failure classes include:

```text
REPRESENTABILITY
DISTINGUISHABILITY
TRANSFORM_CLOSURE
CONSTRAINT_PRESERVATION
REACHABILITY
PROVENANCE
```

Two structures may therefore share the same `t_max` while failing for different structural reasons.

---

# 14. Requirement Entailment Across Depth

For:

```text
u <= t
```

define:

```text
R_t ⊨ R_u
```

to mean:

> every requirement that remains materially necessary from depth u is preserved, strictly strengthened, or legitimately replaced at depth t.

Componentwise:

```text
R_t ⊨ R_u
iff
Rep_t   ⊨ Rep_u
∧ Dist_t  ⊨ Dist_u
∧ Trans_t ⊨ Trans_u
∧ Inv_t   ⊨ Inv_u
∧ Reach_t ⊨ Reach_u
∧ Prov_t  ⊨ Prov_u
```

## 14.1 Preservation

A requirement is preserved when the same materially relevant obligation remains in force.

```text
Preserves(r_t,r_u)
=>
r_t ⊨ r_u
```

## 14.2 Strict strengthening

Define:

```text
r_t ≻ r_u
```

iff:

```text
r_t ⊨ r_u
∧
r_u !⊨ r_t
```

The deeper requirement necessarily satisfies the shallower one but introduces additional obligation.

For whole requirement sets:

```text
R_t ≻ R_u
iff
R_t ⊨ R_u
∧
R_u !⊨ R_t
```

## 14.3 Legitimate replacement

Write:

```text
r_t ▷ r_u
```

when a deeper requirement legitimately replaces a shallower requirement.

This requires an admissible replacement witness `w` such that:

```text
Discharges(w,r_u)
∧ Establishes(w,r_t)
∧ PreservesResolutionMeaning(w,u->t)
∧ PreservesRequiredProvenance(w)
```

Then:

```text
r_t ⊨ r_u
```

even if `r_u` is no longer syntactically present.

Canonical rule:

```text
replacement
!=
deletion
```

and:

```text
old requirement may disappear syntactically
only if its resolution obligation survives semantically
```

## 14.4 Requirement transition status

For each shallower requirement:

```text
Status_t(r)
∈ {
  PRESERVED,
  STRENGTHENED,
  REPLACED,
  DROPPED_INVALIDLY,
  UNRESOLVED
}
```

Then:

```text
R_t ⊨ R_u
```

iff every materially relevant requirement in `R_u` is:

```text
PRESERVED
or
STRENGTHENED
or
REPLACED
```

and none is:

```text
DROPPED_INVALIDLY
or
UNRESOLVED
```

for a fully resolved entailment claim.

## 14.5 Three-valued entailment

Define:

```text
Entail(R_t,R_u)
∈ {
  ENTAILS,
  DOES_NOT_ENTAIL,
  UNRESOLVED
}
```

with:

```text
any invalid drop
-> DOES_NOT_ENTAIL

no invalid drop
+ at least one unresolved requirement transition
-> UNRESOLVED

all requirements preserved, strengthened, or validly replaced
-> ENTAILS
```

## 14.6 Entailment laws

### Reflexivity

```text
R_t ⊨ R_t
```

### Transitivity

If:

```text
R_t ⊨ R_u
```

and:

```text
R_u ⊨ R_v
```

then:

```text
R_t ⊨ R_v
```

provided all replacement witnesses compose validly.

### Resolution equivalence

Antisymmetry is not required.

Define:

```text
R_t ≡_R R_u
iff
R_t ⊨ R_u
∧
R_u ⊨ R_t
```

Distinct requirement structures may therefore be resolution-equivalent.

---

# 15. Strong Depth Laws

Where the depth system is cumulative and no shallower requirement has been legitimately discharged:

```text
Supports(G,t+1)
=>
Supports(G,t)
```

A failure at depth `t` propagates upward only while the failed requirement remains materially necessary:

```text
!Supports(G,t)
=>
!Supports(G,t+k)
```

for `k>0` only under continuing material necessity.

Thus:

```text
deeper
!= merely more requirements
```

Instead:

```text
deeper
=
preservation
+ possible strengthening
+ explicitly justified replacement
```

---

# 16. Current Compact Model

```text
Trajectory
-> Admissibility
-> Boundary Compatibility
-> Reachability

Representation Structure
-> Depth-Indexed Requirement Set R_t
-> Requirement Entailment
-> Supported Resolution Depth
```

and:

```text
representation
+ distinction
+ admissible transform
+ invariant preservation
+ reachability
+ provenance
=
supported resolution depth
```

The critical non-collapse rules are:

```text
trajectory length
!= resolution depth

can represent depth t
!= can resolve depth t

replacement
!= deletion

missing evidence
!= evidence of invalidity

ADMISSIBLE segment
+ ADMISSIBLE segment
!-> ADMISSIBLE concatenation
without boundary compatibility
```

---

# 17. Provenance and Epistemic Status

These formal definitions were developed in the active Set Math workstream and are recorded here as a working formalization.

Status:

- Trajectory admissibility relation: **working formal definition**
- Minimum admissibility axioms: **working axiom set**
- Three-valued admissibility composition: **working algebra**
- Boundary compatibility predicate: **working formal definition**
- Representation structure `G`: **working formal definition**
- Depth-indexed requirements `R_t`: **working formal definition**
- Requirement entailment `R_t ⊨ R_u`: **working formal definition**
- Resolution-depth support and failure classes: **working formal definition**
- Relationship to external standard mathematical frameworks: **not established by this document**

No claim of external novelty or equivalence to a standard formal system is made here.
