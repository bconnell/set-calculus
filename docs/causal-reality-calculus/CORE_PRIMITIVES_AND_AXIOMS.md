# Causal Reality Calculus

## 1. Definition

Causal Reality Calculus (CRC) is a specialization of Set Calculus for representing, transforming, and resolving causally related states of reality.

It inherits the general Set Calculus:

```text
SC =
<Set, Member, Relationship, State, Transform, Resolution, Provenance>
```

CRC adds the minimum causal structure required to distinguish:

- where a transformation occurs;
- when it occurs;
- under which causal conditions it is valid;
- how measurable structure is attached to it;
- whether one realization may validly project into another.

The initial specialization is:

```text
CRC =
SC + <Context, Carrier, Metric, Temporal, Authority>
```

Expanded:

```text
CRC =
<Set, Member, Relationship, State, Transform, Resolution, Provenance,
 Context, Carrier, Metric, Temporal, Authority>
```

---

# 2. Inherited Set Calculus Primitives

## Set

A bounded collection or structure participating in causal resolution.

A Set may represent:

- an active causal field;
- a collection of events;
- a carrier domain;
- a state space;
- a problem-local grid.

## Member

An occurrence participating in a Set.

In CRC, a Member may represent:

- an event;
- a causal transformation occurrence;
- an active cell;
- a realized state element.

## Relationship

A typed relation among Members, Sets, States, or Transforms.

Examples:

```text
precedes(a,b)
causes(a,b)
adjacent(a,b)
bridge(A,B)
depends(T1,T2)
```

Causality is therefore a specialized Relationship rather than a new primitive.

## State

The condition of a causal structure at a particular resolution boundary.

```text
S_t
```

State may include:

- realized properties;
- carrier;
- metric coordinates;
- Temporal position;
- orientation;
- authority version;
- unresolved relations.

## Transform

A mapping from one State into another:

```text
T : S_t -> S_(t+1)
```

A Transform represents causal change.

Not every state difference implies that a known Transform caused it.

## Resolution

The explicit outcome of evaluating a causal structure.

CRC may specialize Resolution into states such as:

```text
EXACT
PROJECTABLE
RECALCULATE
UNRESOLVED
INVALID
CLOSED
```

These are domain-specific Resolution outcomes, not new root primitives.

## Provenance

The lineage establishing how a causal claim, realization, metric, or Resolution was produced.

Provenance may include:

- source State;
- applied Transform;
- metric receipt;
- bridge receipt;
- authority source;
- prior realizations;
- observation history.

---

# 3. CRC-Specific Primitives

## Context

A Context defines the active causal boundary within which membership, relationships, transforms, and resolution are evaluated.

```text
C
```

Membership is therefore contextual:

```text
Member(x,S,C)
```

A thing may participate in one causal Context without participating in another.

Context establishes:

```text
resolved reality = reality within an explicit boundary
```

## Carrier

A Carrier is the substrate or representational domain in which a realization exists.

```text
K
```

A realization is not fully identified merely by its semantic type.

Its Carrier participates in identity:

```text
Identity(x) includes Carrier(x)
```

Carrier equality is distinct from semantic similarity.

## Metric

Metric supplies measurable structure.

```text
M
```

A Metric maps permitted relationships into quantities according to an explicitly defined metric structure.

Conceptually:

```text
M_K(x,y) -> value
```

A Metric is distinct from:

- identity;
- address;
- ordering;
- rank;
- symbolic label.

Therefore:

```text
Address != Measure
```

## Temporal

Temporal represents causal position in time-like ordering.

```text
tau
```

Temporal may contain:

```text
epoch
phase
ancestry
precedence
validity interval
```

Temporal is richer than a scalar timestamp.

Two otherwise similar realizations may be causally distinct when:

```text
tau_1 != tau_2
```

## Authority

Authority establishes which rules, metrics, transformations, bridges, or causal claims are valid within a Context.

```text
A
```

Examples:

```text
AuthorizedMetric(A,M)
AuthorizedBridge(A,B12)
AuthorizedTransform(A,T)
```

Authority does not create reality. It defines the recognized rule boundary under which CRC may resolve it.

---

# 4. Derived Constructs

The following remain derived.

## Event

```text
Event = Member + State + Temporal
```

## Causal Relation

```text
CausalRelation subset Relationship
```

## Bridge

```text
Bridge(K1,K2) subset Relationship
```

## Coordinate

A coordinate is a representation produced under a Metric or addressing scheme.

It is not primitive.

## Orientation

Orientation is a State property.

## Mirror

Mirror is a Transform.

```text
M(T,S) = (S,T)
```

where defined.

## Causal Path

A causal path is an ordered Relationship/Transform sequence:

```text
P = <x0,T1,x1,T2,...,xn>
```

## Realization

A realization is a resolved Member-State within Context, Carrier, Temporal, Metric, and Authority boundaries.

One useful form is:

```text
R_x = <x,C,K,M,tau,A,S,P>
```

where `P` is Provenance.

---

# 5. Foundational Axioms

## Axiom 1: Contextual Reality

All causal resolution occurs within an explicit Context.

```text
Resolve(x) => Resolve(x | C)
```

There is no assumption that a resolved relation in `C1` remains valid in `C2`.

## Axiom 2: Contextual Membership

Membership is Context-dependent.

```text
x in S | C1
```

does not imply:

```text
x in S | C2
```

Prior-problem membership cannot silently enter a new active causal Set.

## Axiom 3: Composite Identity

Causal identity is multidimensional.

A realization cannot be identified solely by name or semantic type.

At minimum:

```text
Identity(x) =
<Type, Carrier, Metric, Temporal, Orientation, Authority>
```

where relevant to the active domain.

If a materially identity-bearing component changes, direct identity reuse is invalid.

## Axiom 4: Address-Measure Separation

An addressing, indexing, ranking, or naming system does not automatically define measurable distance.

```text
Address(x) != Metric(x)
Rank(x,y) !-> Distance(x,y)
```

unless an explicit authorized Metric establishes that mapping.

## Axiom 5: Grounded Metric

A quantitative causal claim requires an applicable authorized Metric.

```text
Measure(x,y)
=> exists M:
   Authorized(M)
   and Applicable(M,x,y)
```

No metric value may be manufactured merely because coordinates are available.

## Axiom 6: Causal Transform Grounding

A State transition alone does not prove causation.

```text
S_t != S_(t+1)
```

does not imply an authoritative causal Transform is known.

A causal Transform requires an explicit valid relationship or rule grounding it.

## Axiom 7: Explicit Projection

A realization on one Carrier cannot be projected to another merely because semantic labels match.

```text
x@K1 !-> x@K2
```

Projection requires an explicit admissible Bridge:

```text
Projection(K1 -> K2)
=> AuthorizedBridge(K1,K2)
```

## Axiom 8: Preservation Must Be Declared

A Transform may preserve some properties while changing others.

For property `p`:

```text
p(S_t) = p(S_(t+1))
```

cannot be assumed merely because other properties are preserved.

Each Transform has a preservation signature:

```text
Preserve(T) = {p1,p2,...}
Change(T)   = {q1,q2,...}
```

## Axiom 9: Transform Non-Projection

A property produced by a Transform cannot automatically be projected backward.

```text
property(T(x)) !-> property(x)
```

unless an explicit inverse or preservation relationship establishes it.

## Axiom 10: Temporal Distinction

Temporal difference may distinguish otherwise structurally identical realizations.

```text
x_tau1 != x_tau2
```

when Temporal position participates materially in identity.

Previous realization does not automatically imply current realization.

## Axiom 11: Precedence Is Not Reversibility

If:

```text
a < b
```

then:

```text
b < a
```

does not follow.

Likewise:

```text
T : S_a -> S_b
```

does not imply that an inverse causal Transform exists.

## Axiom 12: Symmetry Is Not Causal Inversion

Geometric or representational symmetry does not establish reversible causation.

```text
Mirror(x) != CausalInverse(x)
```

unless an explicit causal inverse relationship exists.

## Axiom 13: Provenance Persistence

Every resolved causal realization must preserve sufficient Provenance to determine materially relevant:

```text
source
context
carrier
metric
Temporal state
authority
transform
bridge
prior realization
```

A Transform may alter State without erasing causal ancestry.

## Axiom 14: Explicit Unresolved State

Insufficient causal information resolves to an explicit unresolved condition.

```text
InsufficientInformation => UNRESOLVED
```

It must never be converted into an invented causal relationship.

## Axiom 15: Fail-Closed Authority

If the governing causal rule, Metric, Carrier relation, or Bridge is absent or ambiguous, CRC does not manufacture one.

```text
NoAuthority => NoAuthorizedResolution
```

The appropriate Resolution may therefore be:

```text
UNRESOLVED
RECALCULATE
INVALID
```

depending on domain semantics.

---

# 6. Locality Law

## Locality Conservation

For a Context `C`:

```text
S_C = {x | Member(x,C)}
```

A Transform operating on `C` must not introduce unrelated members from `C'` without an explicit Relationship.

```text
x in C'
and !Relates(x,C)
=> x not-in T(C)
```

This generalizes prevention of stale cross-problem membership.

---

# 7. Causal Path Composition

Suppose:

```text
T1 : S0 -> S1
T2 : S1 -> S2
```

Then:

```text
T2 o T1 : S0 -> S2
```

is a valid causal composition only when:

1. `S1` is compatible between both Transforms;
2. Context remains valid;
3. Carrier transitions are authorized;
4. required Metric relationships remain valid;
5. Temporal ordering is valid;
6. required invariants survive;
7. Provenance is composable.

Functional composability alone does not imply causal composability.

---

# 8. Causal Resolution Algebra

CRC initially supports:

```text
R_CRC = {
  EXACT,
  PROJECTABLE,
  RECALCULATE,
  UNRESOLVED,
  INVALID,
  CLOSED
}
```

## EXACT

The requested realization matches the complete causal identity boundary.

## PROJECTABLE

No exact realization exists, but a certified admissible Bridge permits projection.

## RECALCULATE

A prior realization exists but cannot safely be reused or projected.

## UNRESOLVED

Insufficient information exists to determine the causal result.

## INVALID

The proposed realization violates a governing causal invariant, authority, metric, or relationship.

## CLOSED

The causal path has resolved to a valid terminal boundary for the active Context.

These are specializations of the general Set Calculus `Resolution` primitive.

---

# 9. Canonical CRC Identity

A useful first canonical key is:

```text
K_CRC(x) =
<Type, Context, Carrier, Metric, Temporal, Orientation, AuthorityVersion>
```

Provenance is attached to the realization rather than necessarily participating directly in lookup identity.

Direct reuse requires equality across all identity dimensions declared material for the domain.

---

# 10. Canonical CRC Pipeline

The initial execution model is:

```text
Reality input
    -> establish Context
    -> identify Members
    -> resolve Relationships
    -> bind Carrier
    -> bind Temporal state
    -> establish authorized Metric
    -> apply admissible Transform
    -> preserve / update Provenance
    -> resolve
```

Formally:

```text
<C,K,M,tau,A,S,P>
  --T-->
<C',K',M',tau',A',S',P'>
```

subject to the causal axioms above.

---

# 11. Minimal Specialization

## General Set Calculus

```text
Set
Member
Relationship
State
Transform
Resolution
Provenance
```

## Causal Reality Calculus adds

```text
Context
Carrier
Metric
Temporal
Authority
```

## Derived

```text
Event
Causal Relation
Bridge
Coordinate
Orientation
Mirror
Causal Path
Realization
Certificate
Causal Identity Key
```

Therefore:

```text
CRC =
SC + Context + Carrier + Metric + Temporal + Authority
```

The important boundary is that Cause is not a primitive. Cause is a typed Relationship supported by Context, Temporal ordering, Authority, Provenance, and whatever domain conditions establish that causal relationship.


---

# 12. Source-Derived CRC Extensions

The following extensions are merged from **SRC-CTE-V6-20260909**. They are generalized into CRC form while preserving source provenance.

## Axiom 16: Residual Primacy

**Source: SRC-CTE-V6-20260909, V3 §3; V6 §3**

A causal problem may be represented by a typed residual:

```text
R_i : X_i -> R_i_carrier
```

A Transform is productive relative to target residual `R_i` when it contracts that residual without violating protected boundaries:

```text
R_i(T(x)) < R_i(x)
```

Residual reduction in one Carrier does not authorize arithmetic with another Carrier.

## Axiom 17: Unknown Is Not Zero

**Source: SRC-CTE-V6-20260909, V6 §§15-19**

```text
UNKNOWN != 0
```

A parameter, bridge, floor, coefficient, or causal quantity that has not been established remains unresolved rather than silently receiving a neutral numeric value.

## Axiom 18: Unbridged Is Not Commensurable

**Source: SRC-CTE-V6-20260909, V6 §6**

For quantities in distinct Carriers:

```text
no certified bridge => no arithmetic combination
```

Semantic resemblance alone does not establish commensurability.

## Axiom 19: Protected-Floor Admissibility

**Source: SRC-CTE-V6-20260909, V5 §21; V6 §5**

A local causal improvement is admissible only when:

1. the target residual contracts;
2. no protected domain crosses below its declared floor;
3. no new externalized residual is created without explicit representation;
4. accepted loss remains visible under non-erasure.

## Axiom 20: Stage Conservation

**Source: SRC-CTE-V6-20260909, V5 §19; V6 §12**

If a mechanism or Carrier performs a necessary function for a live residual and no certified substitute exists:

```text
m |= R
R > 0
no certified substitute
=> m remains functionally necessary
```

Removing it transfers or externalizes the residual rather than closing it.

## Axiom 21: Stage Extinction

**Source: SRC-CTE-V6-20260909, V5 §20; V6 §12**

If:

```text
R = 0
```

and a mechanism carries no other live residual, continued compulsory extraction or exclusive claim through that mechanism creates a new residual.

The mechanism must extinguish, transform, or migrate to an explicit live function.

## Axiom 22: Causal History Non-Erasure

**Source: SRC-CTE-V6-20260909, V3 §§8-10**

```text
active residual -> 0
historical provenance != 0
```

Closure of an obligation and erasure of causal history are distinct.

## Axiom 23: Witness Requires Causal Participation

**Source: SRC-CTE-V6-20260909, V3 §§8-9**

```text
Witness(A,T) => CausalLoad(A,T) > 0
```

Proximity, prestige, ownership, funding alone, or later declaration do not establish causal participation.

## Axiom 24: Resource Authority Is Not Truth Authority

**Source: SRC-CTE-V6-20260909, V3 §7**

Resources may alter the feasible Transform set, but do not alter the admissible truth set merely by being supplied.

```text
Resources -> capability
Resources !-> truth sovereignty
```

## Axiom 25: Global Result / Local Realization Distinction

**Source: SRC-CTE-V6-20260909, V3 §§4-5**

```text
GeneralResult != LocalInstantiation
```

A globally reusable informational result may still require local matter, energy, compute, time, data, or labor for realization.

## Axiom 26: Calibration Provenance

**Source: SRC-CTE-V6-20260909, V6 §15**

Every empirical quantity used in causal resolution should carry:

```text
variable
unit
source
method
interval
date
domain
version
```

Uncalibrated quantities remain UNKNOWN.

---

# 13. Typed Board Construct

**Source: SRC-CTE-V6-20260909, V6 §2**

A bounded measurable causal domain may be represented as:

```text
TypedBoard =
<StateSpace,
 AdmissibleSet,
 Capacity,
 AbsorbedLoad,
 Leakage,
 Margin,
 ProtectedFloor,
 Observables,
 NativeUnitSystem>
```

A Typed Board is a derived CRC construct, not a primitive.

A board may not borrow units from another board merely to manufacture a scalar score.

---

# 14. Active Need Construct

**Source: SRC-CTE-V6-20260909, V6 §4**

For a scalar floor/margin board:

```text
Need_i(x) = positive_part(Floor_i - Margin_i(x))
```

```text
Need_i = 0
```

means only that this specific floor is not breached. It does not imply global closure.

---

# 15. Causal Leverage

**Source: SRC-CTE-V6-20260909, V3 §15; V6 §7**

For an admissible intervention `T_i^u` with resource amount `E_i(u) > 0`:

```text
L_(j<-i)(x;u) =
  [R_j(x) - R_j(T_i^u(x))] / E_i(u)
```

when measurements are commensurable in the same Carrier or validly bridged.

A graph-level leverage profile may remain vector-valued. A universal scalar is not required.

---

# 16. Reliability Profile

**Source: SRC-CTE-V6-20260909, V6 §8**

Reliability is represented as a profile:

```text
q_i =
<delivery,
 durability,
 repair,
 truth,
 closure,
 externalization,
 ...>
```

A domain-specific scalar projection is permitted only when the projection preserves information required by that decision.

---

# 17. Conditional Closure Laws

## Finite Strict-Descent Closure

**Source: SRC-CTE-V6-20260909, V6 §10**

For residuals already placed in a common nonnegative Carrier by certified bridges:

```text
V(x) = sum(w_j * R_j(x))
w_j > 0
```

If every accepted Transform preserves protected floors and:

```text
V(T(x)) <= V(x) - epsilon
```

for fixed `epsilon > 0` whenever `V(x) > V_floor`, then the process reaches `V <= V_floor` after finitely many accepted strict-decrease steps.

The theorem is conditional on the validity of bridges, floors, weights, and decrement assumptions.

## Lyapunov-Type Residual Contraction

**Source: SRC-CTE-V6-20260909, V6 §11**

If:

```text
V(x_(t+1)) - V(x_t) <= -alpha(V(x_t))
```

with `alpha(r) > 0` above the floor and zero on the admitted floor, the process cannot remain indefinitely in a compact region strictly above that floor.

This is a stability template, not a universal empirical claim.

---

# 18. Causal Stage Classification

**Source: SRC-CTE-V6-20260909, V5 §§14-18; V6 §14**

A Stage is a falsifiable classification over an explicitly scoped Context.

A valid Stage assignment includes:

```text
supporting evidence
live residual
current Carrier/mechanism
exit condition
falsifier
scope
time horizon
capacity layer
```

A Stage may move forward or backward when evidence changes.

---

# 19. Formal / Empirical Boundary

**Source: SRC-CTE-V6-20260909, V6 §§16-19**

CRC distinguishes:

```text
FORMAL-CLOSED
EMPIRICAL-CALIBRATION-PENDING
BRIDGE-REQUIRED
CONDITIONAL-THEOREM
UNKNOWN
```

A formally valid relation may still require empirical calibration before application to reality.

Missing values must not become invented constants. Missing Bridges must not become implicit conversions.

---

# 20. Source-Derived Operational Cycle

**Source: SRC-CTE-V6-20260909, V6 §17**

A measured CRC intervention may use:

```text
identify active Context / board
-> identify exact target residual
-> declare Carrier / unit / Metric
-> record floor, margin, uncertainty
-> identify protected neighboring domains
-> reject unsupported cross-carrier arithmetic
-> propose smallest admissible Transform
-> measure before
-> execute
-> measure after
-> compute supported local leverage
-> audit externalization and protected floors
-> certify contraction, reopen, or return UNKNOWN
-> update Stage only from evidence
-> preserve witness and calibration Provenance
```

This is a specialized measurable-intervention profile of the general CRC pipeline.

---

# 21. Provenance Note

Sections 12-20 incorporate generalized laws extracted from:

```text
SRC-CTE-V6-20260909
Causal Temporal Economics
Version 6 - Cumulative Edition
S. D. Bolduc
September 9, 2026
```

See `SOURCE_LEDGER.md` for source anchors.

The merge preserves the distinction among:

```text
source statement
generalized CRC law
CRC inference
empirical calibration
```

No generalized CRC form should be represented as a verbatim theorem of the source unless the source states it in that form.
