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


---

# 18. Admissible Concatenation Closure Theorem

## Theorem

Given trajectory segments `π1` and `π2`:

```text
Adm(π1 | C,A) = ADMISSIBLE
Adm(π2 | C,A) = ADMISSIBLE
BoundaryCompatible(π1,π2 | C,A) = ADMISSIBLE
```

then:

```text
Adm(π1 ⊕ π2 | C,A) = ADMISSIBLE
```

Compactly:

```text
ADMISSIBLE
⊕
ADMISSIBLE
+
ADMISSIBLE boundary
=>
ADMISSIBLE concatenation
```

Using the admissibility composition algebra:

```text
Adm(π1 ⊕ π2 | C,A)
=
Adm(π1 | C,A)
⊗A
BoundaryCompatible(π1,π2 | C,A)
⊗A
Adm(π2 | C,A)
```

and:

```text
ADMISSIBLE ⊗A ADMISSIBLE = ADMISSIBLE
```

the final reduction follows once the proof obligations are discharged.

## 18.1 Proof obligations

Define:

```text
PO(π1,π2 | C,A)
=
<
  PO_segment1,
  PO_segment2,
  PO_state,
  PO_context,
  PO_authority,
  PO_invariant,
  PO_provenance,
  PO_transform
>
```

Required obligations:

1. `Adm(π1 | C,A) = ADMISSIBLE`
2. `Adm(π2 | C,A) = ADMISSIBLE` under its entry conditions
3. `StateCompat = ADMISSIBLE`
4. `ContextCompat = ADMISSIBLE`
5. `AuthorityCompat = ADMISSIBLE`
6. `InvariantCompat = ADMISSIBLE`
7. `ProvenanceCompat = ADMISSIBLE`
8. the first Transform of `π2` is applicable to the actual boundary State

Inference rule:

```text
Adm(π1) = ADMISSIBLE
Adm(π2) = ADMISSIBLE
StateCompat = ADMISSIBLE
ContextCompat = ADMISSIBLE
AuthorityCompat = ADMISSIBLE
InvariantCompat = ADMISSIBLE
ProvenanceCompat = ADMISSIBLE
CrossBoundaryTransformApplicable = ADMISSIBLE
---------------------------------------------------
Adm(π1 ⊕ π2) = ADMISSIBLE
```

## 18.2 Failure and unresolved counterparts

If any required proof obligation is INADMISSIBLE:

```text
∃p ∈ PO : p = INADMISSIBLE
=>
Adm(π1 ⊕ π2) = INADMISSIBLE
```

If no proof obligation is INADMISSIBLE and at least one is UNRESOLVED:

```text
∀p ∈ PO : p != INADMISSIBLE
∧
∃p ∈ PO : p = UNRESOLVED
=>
Adm(π1 ⊕ π2) = UNRESOLVED
```

## 18.3 Finite concatenation closure

For:

```text
Π = π1 ⊕ π2 ⊕ ... ⊕ πn
```

if all segments are ADMISSIBLE and every accumulated-prefix boundary is ADMISSIBLE, then:

```text
Adm(Π | C,A) = ADMISSIBLE
```

The accumulated-prefix qualification matters because earlier segments may contribute materially relevant invariants, authority history, Context transitions, or provenance dependencies.

---

# 19. Boundary Evidence Object

Define the minimum boundary evidence bundle:

```text
E_B(π1,π2)
=
<
  E_state,
  E_context,
  E_authority,
  E_invariant,
  E_provenance
>
```

A boundary may resolve ADMISSIBLE only when all required evidence components are sufficient and valid.

Minimal object shape:

```text
BoundaryEvidence = {
    source_segment,
    target_segment,
    boundary_state,
    state_evidence,
    context_evidence,
    authority_evidence,
    invariant_evidence,
    provenance_evidence,
    evidence_status
}
```

with:

```text
evidence_status
∈ {
  COMPLETE,
  INCOMPLETE,
  CONTRADICTED
}
```

Evidence status is distinct from admissibility status.

```text
evidence status
!=
admissibility status
```

## 19.1 State evidence

```text
E_state = {
    terminal_state_of_π1,
    initial_state_requirement_of_π2,
    relation_between_them,
    witness
}
```

The witness establishes IDENTITY, COMPATIBILITY, or authorized PROJECTION.

## 19.2 Context evidence

```text
E_context = {
    source_context,
    target_context,
    context_relation,
    transition_witness
}
```

The transition witness establishes sameness or an authorized Context transition and records the materially relevant scope that survives.

## 19.3 Authority evidence

```text
E_authority = {
    source_authority,
    target_authority,
    accepted_output,
    authorized_next_transform,
    authority_transition_witness
}
```

It must establish outgoing validity, target acceptance, and authorization of the next Transform.

## 19.4 Invariant evidence

```text
E_invariant = {
    required_boundary_invariants,
    observed_or_derived_values,
    preservation_witnesses,
    authorized_changes
}
```

For every `i ∈ I_boundary`, evidence must establish preservation or authorized change.

## 19.5 Provenance evidence

```text
E_provenance = {
    source_provenance,
    boundary_evidence_provenance,
    target_provenance_requirements,
    composition_witness
}
```

It must establish traceability, target acceptance, and defined provenance composition.

---

# 20. Minimal Typed Boundary Witness Schemas

## 20.1 State Witness

```text
StateWitness = {
    source_state,
    target_state_requirement,
    relation_type,
    relation_evidence
}
```

where:

```text
relation_type ∈ {
  IDENTITY,
  COMPATIBILITY,
  PROJECTION
}
```

Valid iff the witness refers to the actual terminal and entry States and the evidence establishes the declared relation, including required bridge conditions for projection.

## 20.2 Context Witness

```text
ContextWitness = {
    source_context,
    target_context,
    transition_type,
    transition_evidence,
    preserved_scope
}
```

where:

```text
transition_type ∈ {
  SAME_CONTEXT,
  CONTEXT_TRANSITION
}
```

Valid iff the actual trajectory Contexts are identified, sameness or authorized transition is established, and every materially required State, Relationship, invariant, and provenance dependency survives.

## 20.3 Authority Witness

```text
AuthorityWitness = {
    source_authority,
    target_authority,
    output_validity_evidence,
    acceptance_evidence,
    next_transform,
    transform_authorization
}
```

Valid iff:

```text
ValidUnder(TerminalState(π1),source_authority)
∧
Accepts(target_authority,TerminalState(π1))
∧
Authorized(next_transform,target_authority)
```

and any Authority transition is explicitly supported.

## 20.4 Invariant Witness

```text
InvariantWitness = {
    invariant,
    requirement_source,
    boundary_value_or_state,
    disposition,
    evidence
}
```

where:

```text
disposition ∈ {
  PRESERVED,
  AUTHORIZED_CHANGE
}
```

and:

```text
InvariantWitnessSet
=
{ witness_i | i ∈ I_boundary }
```

The set is valid only if every required invariant has a valid witness.

## 20.5 Provenance Witness

```text
ProvenanceWitness = {
    source_lineage,
    terminal_state_reference,
    boundary_evidence_reference,
    target_provenance_requirements,
    composition_rule,
    composition_result
}
```

Valid iff required lineage is traceable, accepted by the target segment, and composable into a provenance result that preserves all materially required lineage.

---

# 21. Common Witness Envelope

All five witness types share a common outer form:

```text
WitnessEnvelope<W> = {
    witness_type,
    claim,
    subject,
    boundary_reference,
    evidence,
    evidence_provenance,
    rule_basis,
    dependencies,
    contradictions,
    status,
    resolution_record,
    payload : W
}
```

where:

```text
witness_type ∈ {
  STATE,
  CONTEXT,
  AUTHORITY,
  INVARIANT,
  PROVENANCE
}
```

and:

```text
status ∈ {
  VALID,
  INVALID,
  UNRESOLVED
}
```

The envelope is uniform; the typed payload preserves the specific mathematics of each compatibility relation.

## 21.1 Common envelope semantics

`claim` is the exact proposition the witness attempts to establish.

`subject` identifies the concrete objects referenced by that claim.

`boundary_reference` identifies the actual concatenation boundary and prevents witness reuse against an unrelated boundary.

`evidence` stores the material supporting the claim.

`evidence_provenance` records source, method, version/time, and producing rule or Authority.

`rule_basis` records the formal rule under which the evidence is supposed to establish the claim.

`dependencies` records prerequisite witnesses or propositions.

`contradictions` records known evidence against the claim.

`resolution_record` records how validation was performed and why the resulting status was assigned.

---

# 22. Uniform Witness Validation Algorithm

Define:

```text
ValidateWitness(W)
-> {
  VALID,
  INVALID,
  UNRESOLVED
}
```

Validation proceeds uniformly until typed payload validation.

## Step 1: Schema validity

```text
if !SchemaValid(W):
    return INVALID
```

Malformed evidence is not the same as absent evidence.

## Step 2: Boundary applicability

If the witness positively refers to the wrong boundary or wrong subjects:

```text
return INVALID
```

If applicability cannot yet be established:

```text
return UNRESOLVED
```

## Step 3: Claim completeness

A precise typed claim must be present.

Missing claim:

```text
return INVALID
```

Unresolved identity or typing required by the claim:

```text
return UNRESOLVED
```

## Step 4: Provenance validity

Known broken, false, or disallowed provenance:

```text
return INVALID
```

Incomplete but potentially recoverable provenance:

```text
return UNRESOLVED
```

Thus:

```text
missing provenance
!=
invalid provenance
```

## Step 5: Dependency resolution

For every dependency:

```text
INVALID dependency
-> INVALID

no INVALID dependency
+ at least one UNRESOLVED dependency
-> UNRESOLVED
```

otherwise validation continues.

## Step 6: Contradiction check

A valid contradiction that disproves the claim:

```text
return INVALID
```

An unresolved contradiction:

```text
return UNRESOLVED
```

Supporting evidence cannot silently erase contradictory evidence.

## Step 7: Typed payload validation

Dispatch by `witness_type`:

```text
STATE
-> identity / compatibility / authorized projection

CONTEXT
-> same Context / authorized transition + preserved scope

AUTHORITY
-> outgoing validity + target acceptance + next-Transform authorization

INVARIANT
-> preserved / authorized change

PROVENANCE
-> traceability + acceptance + composability
```

The typed validator returns VALID, INVALID, or UNRESOLVED.

## Step 8: Resolution record

The validator records the boundary, claim, examined dependencies, contradiction results, typed validation result, final status, and validator provenance.

Validation itself is therefore reconstructible.

## 22.1 Universal witness validity law

For any boundary witness `W`:

```text
Valid(W)
iff
SchemaValid(W)
∧ BoundaryApplicable(W)
∧ ClaimSpecified(W)
∧ ProvenanceValid(W)
∧ DependenciesValid(W)
∧ NoValidContradiction(W)
∧ TypedPayloadProvesClaim(W)
```

INCOMPLETE required evidence produces UNRESOLVED unless a positive violation has already been established.

## 22.2 Aggregate boundary validation

Let:

```text
E_B =
<
  W_state,
  W_context,
  W_authority,
  W_invariant,
  W_provenance
>
```

Then:

```text
ValidateBoundary(E_B)
=
ValidateWitness(W_state)
⊗A
ValidateWitness(W_context)
⊗A
ValidateWitness(W_authority)
⊗A
ValidateWitness(W_invariant)
⊗A
ValidateWitness(W_provenance)
```

under the mapping:

```text
VALID       -> ADMISSIBLE
INVALID     -> INADMISSIBLE
UNRESOLVED  -> UNRESOLVED
```

Therefore:

```text
all five VALID
-> BoundaryCompatible = ADMISSIBLE

any INVALID
-> BoundaryCompatible = INADMISSIBLE

otherwise
-> BoundaryCompatible = UNRESOLVED
```

---

# 23. Anchor Checkpoint: Boundary-Proof Layer

At this checkpoint the Set Math thread has moved from path validity into explicit proof-carrying boundary composition.

The current dependency chain is:

```text
Trajectory
-> Trajectory Admissibility
-> Boundary Compatibility
-> Boundary Evidence
-> Typed Boundary Witnesses
-> Common Witness Envelope
-> Uniform Witness Validation
-> Admissible Concatenation Closure
-> Reachability
-> Resolution Depth
```

The current minimum proof principle is:

```text
no admissible concatenation
without admissible segments
+ admissible boundary

no admissible boundary
without sufficient typed evidence

no sufficient typed evidence
without valid provenance-bearing witnesses
```

Epistemic status:

- Concatenation closure theorem: **working theorem**
- Closure proof obligations: **working proof obligations**
- Boundary Evidence Object: **working formal definition**
- Typed witness schemas: **working formal definitions**
- Common Witness Envelope: **working formal definition**
- Uniform validation algorithm: **working validation procedure**
- External novelty/equivalence claims: **not established**


---

# 24. Identity Witness Correction

Identity is a separate boundary compatibility obligation from State.

Canonical distinction:

```text
IdentityCompat
!=
StateCompat
```

Identity answers what continues across the boundary.

State answers what condition that continuing object is in.

Boundary compatibility therefore expands to:

```text
BoundaryCompatible
=
IdentityCompat
⊗A StateCompat
⊗A ContextCompat
⊗A AuthorityCompat
⊗A InvariantCompat
⊗A ProvenanceCompat
```

and the boundary evidence object becomes:

```text
E_B =
<
  E_identity,
  E_state,
  E_context,
  E_authority,
  E_invariant,
  E_provenance
>
```

The witness discriminator expands to:

```text
witness_type ∈ {
  IDENTITY,
  STATE,
  CONTEXT,
  AUTHORITY,
  INVARIANT,
  PROVENANCE
}
```

## 24.1 IdentityWitnessPayload

```text
IdentityWitnessPayload {
    source_identity        : IdentityRef          [1, non-null]
    target_identity        : IdentityRef          [1, non-null]
    identity_relation      : IdentityRelation     [1, non-null]
    identity_basis         : EvidenceRef          [1, non-null]
    preserved_properties   : IdentityPropertyRef  [0..*, non-null elements]
    transformed_properties : IdentityTransformRef [0..*, non-null elements]
}
```

where:

```text
IdentityRelation =
    SAME_IDENTITY
  | CONTINUOUS_IDENTITY
  | DERIVED_IDENTITY
  | PROJECTED_IDENTITY
```

Canonical identity distinctions:

```text
same state
!=
same identity

different state
!-> different identity

DerivedFrom(x,y)
!-> x = y
```

## 24.2 Identity payload validity

Define:

```text
IdentityPayloadValid(W_id)
```

iff:

```text
CardinalityValid(W_id)
∧
IdentityApplicable(W_id)
∧
RelationEvidenceValid(W_id)
∧
PreservationCoverageValid(W_id)
∧
TransformConsistency(W_id)
```

### Cardinality

Required singular fields must occur exactly once and be non-null.

```text
count(source_identity)     = 1
count(target_identity)     = 1
count(identity_relation)   = 1
count(identity_basis)      = 1
```

Collections may contain zero or more non-null members.

A type, cardinality, or forbidden-null violation is INVALID rather than UNRESOLVED.

### Boundary applicability

```text
source_identity
=
BoundarySourceIdentity(π1)
```

and:

```text
target_identity
=
BoundaryTargetIdentityRequirement(π2)
```

A positively wrong identity is INVALID.

An identity not yet resolved is UNRESOLVED unless partial resolution is available under the rules below.

### Relation-specific evidence

`SAME_IDENTITY` requires evidence establishing identity equality.

`CONTINUOUS_IDENTITY` requires evidence establishing identity continuity plus complete coverage of materially required identity properties.

`DERIVED_IDENTITY` requires evidence establishing `DerivedFrom(target,source)` and required inherited-property coverage.

`PROJECTED_IDENTITY` requires evidence establishing authorized identity projection, required bridge validity, and required projected-property coverage.

### Preservation coverage

Let:

```text
I_req
=
RequiredIdentityProperties(
  π1,
  π2,
  identity_relation
)
```

and:

```text
I_pres =
set(preserved_properties)

I_trans =
set(transformed_properties)
```

Then complete coverage requires:

```text
I_req
⊆
I_pres
∪ AuthorizedTransformCoverage(I_trans)
```

A known required-property loss without authorized transformation is INVALID.

Unresolved coverage with some positively established coverage may become PARTIAL.

### Transformation consistency

```text
∀x ∈ transformed_properties:
AuthorizedForRelation(
  x,
  identity_relation
)
```

A known contradiction is INVALID.

Unknown compatibility remains unresolved or partial depending on the amount of positively resolved structure.

---

# 25. Partial Resolution State

PARTIAL is a first-class resolution state throughout the Set Math layer.

Canonical distinction:

```text
PARTIAL
!=
UNRESOLVED
```

Define:

> **Partial Resolution** is a resolution state in which at least one materially required obligation has resolved, at least one materially required obligation remains unresolved, and no decisive invalidating obligation has resolved negatively.

The generic four-state pattern is:

```text
RESOLVED_POSITIVE
PARTIAL
UNRESOLVED
RESOLVED_NEGATIVE
```

Domain-specific forms include:

```text
Witness Validation:
VALID
PARTIAL
UNRESOLVED
INVALID

Trajectory Admissibility:
ADMISSIBLE
PARTIALLY_ADMISSIBLE
UNRESOLVED
INADMISSIBLE

Requirement Entailment:
ENTAILS
PARTIALLY_ENTAILS
UNRESOLVED
DOES_NOT_ENTAIL

Evidence Sufficiency:
SUFFICIENT
PARTIALLY_SUFFICIENT
INCOMPLETE
CONTRADICTED
```

The conceptual ladder is:

```text
Unknown
!=
Unresolved
!=
Partially Resolved
!=
Resolved
```

## 25.1 Four-valued admissibility composition

The admissibility composition algebra becomes:

| ⊗A | ADMISSIBLE | PARTIAL | UNRESOLVED | INADMISSIBLE |
|---|---:|---:|---:|---:|
| **ADMISSIBLE** | ADMISSIBLE | PARTIAL | UNRESOLVED | INADMISSIBLE |
| **PARTIAL** | PARTIAL | PARTIAL | PARTIAL | INADMISSIBLE |
| **UNRESOLVED** | UNRESOLVED | PARTIAL | UNRESOLVED | INADMISSIBLE |
| **INADMISSIBLE** | INADMISSIBLE | INADMISSIBLE | INADMISSIBLE | INADMISSIBLE |

Important cases:

```text
PARTIAL ⊗A UNRESOLVED
=
PARTIAL
```

because positive resolution already exists.

```text
UNRESOLVED ⊗A UNRESOLVED
=
UNRESOLVED
```

because no positive partial resolution has yet been established.

```text
x ⊗A INADMISSIBLE
=
INADMISSIBLE
```

for any final admissibility claim where the negative obligation is decisive.

## 25.2 Uniform validation aggregation

For a validation object with materially required obligations, let:

```text
resolved_positive = number resolved positively
unresolved        = number not yet resolved
resolved_negative = number decisively violated
required_total    = total materially required obligations
```

Then:

```text
if resolved_negative > 0:
    -> INVALID

else if resolved_positive = required_total:
    -> VALID

else if resolved_positive > 0
     and unresolved > 0:
    -> PARTIAL

else:
    -> UNRESOLVED
```

The same pattern maps to the domain-specific names for admissibility, entailment, and evidence sufficiency.

## 25.3 Identity validation with PARTIAL

For example:

```text
identity relation established
+ some required identity properties proven preserved
+ at least one required identity property unresolved
+ no required property proven invalid
=
PARTIAL
```

Thus an unresolved remainder no longer erases known resolved structure.

---

# 26. Anchor Checkpoint: Six-Witness Four-State Boundary Model

At this checkpoint the boundary-proof layer has two material corrections:

1. **Identity is independent of State**, producing six typed boundary witnesses.
2. **PARTIAL is a first-class resolution state**, producing four-valued resolution across validation, admissibility, evidence, and entailment.

Current boundary witness set:

```text
Identity
State
Context
Authority
Invariant
Provenance
```

Current resolution model:

```text
positive
partial
unresolved
negative
```

Current dependency chain:

```text
Trajectory
-> Trajectory Admissibility
-> Boundary Compatibility
-> Six-Dimension Boundary Evidence
-> Typed Boundary Witnesses
-> Common Witness Envelope
-> Four-State Witness Validation
-> Admissible / Partially Admissible Concatenation
-> Reachability
-> Resolution Depth
```

Canonical checkpoint laws:

```text
IdentityCompat != StateCompat

PARTIAL != UNRESOLVED

known resolved structure
must not be erased
by unresolved remainder
```

Epistemic status:

- Identity Witness: **working formal definition**
- Identity payload validation: **working validation predicate**
- Partial Resolution: **working canonical resolution state**
- Four-valued composition: **working algebra**
- Six-witness boundary model: **working boundary formalization**
- External novelty/equivalence claims: **not established**
