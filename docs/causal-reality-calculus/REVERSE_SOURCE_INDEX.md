# Causal Reality Calculus Reverse Source Index

This index reverses the CRC provenance matrix.

Instead of asking:

```text
Which source supports this CRC law?
```

it asks:

```text
What CRC laws were derived from this source passage?
```

It also records:

- one-to-many mappings, where one source passage supports multiple CRC laws;
- many-to-one mappings, where one CRC law depends on several passages;
- source passages extracted from the source but not yet promoted into CRC.

---

# Source

```text
Source ID: SRC-CTE-V6-20260909
Title: Causal Temporal Economics
Version: 6 - Cumulative Edition
Author: S. D. Bolduc
Series: CT Working Paper
Date: September 9, 2026
Source file: ct_temporal_economics_en_v6.pdf
```

---

# Interpretation Key

- **DIRECT**: CRC preserves essentially the same source proposition.
- **GENERALIZED**: CRC lifts a domain-specific source rule into broader causal form.
- **INFERRED**: CRC synthesizes multiple source passages into a new generalized rule.
- **UNMAPPED**: passage is tracked but has not yet been merged into a CRC law.

---

# Reverse Mapping

## SRC-PASSAGE-001: Residual as Primitive Economic Object

**Source location:** V3 §3, PDF p. 8, lines 175-185

**Source passage:**

> “Closure occurs when Ri(t) = 0 under the declared scope and verification standard.”

> “A productive action ... is defined by what it does to the residual: ΔRi < 0.”

### CRC mappings

1. **Axiom 16: Residual Primacy**
   - Interpretation: **GENERALIZED**
   - Mapping type: **direct source -> generalized CRC law**

2. **Causal Stage Classification**
   - Interpretation: **GENERALIZED**
   - Mapping type: **one-to-many**
   - Reason: stage assignment depends on identifying a live residual and its closure condition.

3. **Finite Strict-Descent Closure**
   - Interpretation: **INFERRED / FORMAL EXTENSION**
   - Mapping type: **one-to-many**
   - Reason: strict-descent closure is defined over residual functionals derived from the primitive residual concept.

---

## SRC-PASSAGE-002: Certified Closure Time

**Source location:** V3 §3, PDF p. 8, lines 195-200

**Source passage:**

> “The closure time of residual i is τi(t) = inf{s ≥ 0 : Ri(t + s) = 0} ...”

### CRC mappings

1. **Temporal as causal state dimension**
   - Interpretation: **GENERALIZED**
   - Existing CRC location: Core primitive `Temporal`

2. **Causal Stage Classification**
   - Interpretation: **GENERALIZED**
   - Reason: closure time is part of stage evidence and transition state.

### Mapping note

This source passage predates the CTE V6 merge and reinforces the CRC Temporal primitive. It is source support for an already-existing CRC primitive rather than a newly numbered source-derived axiom.

---

## SRC-PASSAGE-003: Public Knowledge Monotonicity

**Source location:** V3 §4, PDF p. 9

**Source passage:**

> “Once a general capability has been certified and released, it remains in the common knowledge base: Kt+1 ⊇ Kt.”

### CRC mappings

1. **Axiom 25: Global Result / Local Realization Distinction**
   - Interpretation: **GENERALIZED**
   - Mapping type: **partial support**

2. **Causal History Non-Erasure**
   - Interpretation: **INFERRED**
   - Mapping type: **many-to-one contributor**
   - Reason: persistent certified knowledge and persistent witness history share the non-erasure structure but are distinct objects.

### Unmapped remainder

The explicit monotone-commons law:

```text
K_(t+1) >= K_t
```

has **not yet been promoted into a standalone CRC law**.

Status: **UNMAPPED CANDIDATE**

---

## SRC-PASSAGE-004: Global Information / Local Instantiation Split

**Source location:** V3 §5, PDF pp. 9-10, lines 225-246

**Source passage:**

> “P = Pinformation ⊕ Pinstantiation.”

> “The first is global after certification; the second remains local and may remain scarce.”

### CRC mappings

1. **Axiom 25: Global Result / Local Realization Distinction**
   - Interpretation: **GENERALIZED**
   - Mapping type: **direct source -> generalized CRC law**

2. **Carrier primitive**
   - Interpretation: **GENERALIZED**
   - Mapping type: **one-to-many**
   - Reason: informational and physical realization occupy distinct causal carriers.

3. **Contextual Reality**
   - Interpretation: **INFERRED**
   - Mapping type: **one-to-many**
   - Reason: local realization depends on context-bound resources such as matter, energy, location, compute, or private data.

---

## SRC-PASSAGE-005: Funding Changes Feasible Set, Not Truth Set

**Source location:** V3 §7, PDF p. 11, lines 275-299

**Source passage:**

> “Funding changes what can be attempted now. It does not change what answers are admissible.”

> “AdmissibleResults(i | S) = AdmissibleResults(i).”

### CRC mappings

1. **Axiom 24: Resource Authority Is Not Truth Authority**
   - Interpretation: **DIRECT / GENERALIZED**
   - Mapping type: **direct source -> CRC law**

2. **Authority primitive**
   - Interpretation: **GENERALIZED**
   - Mapping type: **one-to-many**
   - Reason: the passage distinguishes resource contribution from truth-governing authority.

3. **Fail-Closed Authority**
   - Interpretation: **INFERRED**
   - Mapping type: **one-to-many**
   - Reason: admissibility remains constrained independently of resources.

---

## SRC-PASSAGE-006: Causal Witness Certificate

**Source location:** V3 §8, PDF p. 12, lines 310-339

**Source passage:**

> “A Causal Witness Certificate is a public record ...”

> “The transition certificate ... certifies the result ... the witness certificate ... certifies the historical relation between the entity and that certified transition.”

### CRC mappings

1. **Axiom 22: Causal History Non-Erasure**
   - Interpretation: **GENERALIZED**
   - Mapping type: **one-to-many**

2. **Axiom 23: Witness Requires Causal Participation**
   - Interpretation: **DIRECT / GENERALIZED**
   - Mapping type: **one-to-many**

3. **Provenance primitive**
   - Interpretation: **GENERALIZED**
   - Mapping type: **one-to-many**
   - Reason: witness certificate is a structured provenance object.

4. **Calibration Provenance**
   - Interpretation: **INFERRED SUPPORT**
   - Mapping type: **one-to-many**
   - Reason: both rely on typed, auditable records linked to source and verification.

---

## SRC-PASSAGE-007: Incarnation Requirement

**Source location:** V3 §9.3, PDF p. 15, lines 447-454

**Source passage:**

> “A witness must have carried a real causal function.”

> “Λi(A) > 0 for a nontrivial witness claim.”

### CRC mappings

1. **Axiom 23: Witness Requires Causal Participation**
   - Interpretation: **DIRECT**
   - Mapping type: **direct source -> CRC law**

2. **Causal Transform Grounding**
   - Interpretation: **INFERRED**
   - Mapping type: **one-to-many**
   - Reason: both reject attribution without a real causal function.

---

## SRC-PASSAGE-008: Recognition Persists After Debt Closure

**Source location:** V3 §9.4, PDF p. 15, lines 455-466

**Source passage:**

> “Mrecognition,i → 0, Wi ≠ 0.”

> “Recognition survives as certified history; debt does not.”

### CRC mappings

1. **Axiom 22: Causal History Non-Erasure**
   - Interpretation: **GENERALIZED**
   - Mapping type: **direct support**

2. **Stage Extinction**
   - Interpretation: **INFERRED SUPPORT**
   - Mapping type: **one-to-many**
   - Reason: an active claim can extinguish while provenance remains.

---

## SRC-PASSAGE-009: Claim Extinction

**Source location:** V3 §10, PDF pp. 16-17

**Source passage:**

> “A financial claim must not outlive the causal residual that justified it.”

### CRC mappings

1. **Axiom 21: Stage Extinction**
   - Interpretation: **GENERALIZED**
   - Mapping type: **one-to-many source support**

2. **Axiom 20: Stage Conservation**
   - Interpretation: **INFERRED COMPLEMENT**
   - Mapping type: **paired-law support**
   - Reason: extinction after closure is the converse of preserving a still-needed carrier before closure.

---

## SRC-PASSAGE-010: Firm as Residual-Closure Machine

**Source location:** V3 §11, PDF p. 17

**Source passage:**

> “A firm is a temporary concentration ... justified when the concentration closes a target set of residuals faster or more reliably ...”

### CRC mappings

1. **Stage Conservation**
   - Interpretation: **GENERALIZED SUPPORT**

2. **Carrier relation**
   - Interpretation: **GENERALIZED SUPPORT**
   - Reason: a mechanism remains justified while it performs a live causal function.

### Unmapped remainder

The explicit concept of:

```text
organization as temporary residual-closure machine
```

has **not yet been promoted into a standalone CRC construct**.

Status: **UNMAPPED CANDIDATE**

---

## SRC-PASSAGE-011: Causal Leverage / Dependency Centrality

**Source location:** V3 §15, PDF pp. 20-21

**Source passage:**

> “Bi may include dependency centrality: a small technical bridge that unlocks thousands of downstream problems can outrank a very visible but isolated project.”

### CRC mappings

1. **Causal Leverage**
   - Interpretation: **GENERALIZED**
   - Mapping type: **one-to-many**

2. **Relationship / dependency graph**
   - Interpretation: **GENERALIZED SUPPORT**

3. **Cost-aware / leverage-aware planning candidate**
   - Interpretation: **INFERRED**
   - Status: **UNMAPPED TO CRC CORE**
   - Reason: could later inform causal planner selection.

---

## SRC-PASSAGE-012: Temporary Closure Frontier

**Source location:** V3 §16, PDF p. 21

**Source passage:**

> “A provisional economic floor is reached when every active residual is either closed ... or blocked ...”

### CRC mappings

1. **Causal Stage Classification**
   - Interpretation: **GENERALIZED**

2. **Resolution algebra**
   - Interpretation: **GENERALIZED SUPPORT**
   - Reason: distinguishes CLOSED from BLOCKED/UNRESOLVED frontier conditions.

### Unmapped remainder

The explicit dynamic:

```text
provisional closure -> innovation -> new frontier -> closure
```

is not yet a standalone CRC law.

Status: **UNMAPPED CANDIDATE**

---

## SRC-PASSAGE-013: Stage Conservation

**Source location:** V5 §19, PDF p. 44, lines 1476-1487

**Source passage:**

> “A mechanism cannot be removed before the residual it carries has been closed.”

> “Rj > 0 ∧ no certified substitute ⇒ mj remains functionally necessary.”

### CRC mappings

1. **Axiom 20: Stage Conservation**
   - Interpretation: **DIRECT / GENERALIZED**

2. **Carrier relation**
   - Interpretation: **DIRECT / GENERALIZED**

3. **Locality Conservation**
   - Interpretation: **INFERRED SUPPORT**
   - Reason: unresolved causal load must remain attached to a valid carrier rather than disappearing by boundary manipulation.

---

## SRC-PASSAGE-014: Stage Extinction

**Source location:** V5 §20, PDF p. 44, lines 1488-1500

**Source passage:**

> “A mechanism must not survive indefinitely after the residual that justified it is closed.”

> “Rj = 0 ∧ function(mj) = ∅ ⇒ mj should extinguish or transform.”

### CRC mappings

1. **Axiom 21: Stage Extinction**
   - Interpretation: **DIRECT / GENERALIZED**

2. **Resolution CLOSED**
   - Interpretation: **INFERRED SUPPORT**
   - Reason: closure changes whether a carrier remains valid.

---

## SRC-PASSAGE-015: Coherence Conservation / Protected Floors

**Source location:** V5 §21 and V6 §5, PDF pp. 44-45 and 50-51, lines 1697-1721

**Source passage:**

> “Coherence cannot be purchased at the price of coherence.”

> “the active target residual weakly contracts; no protected board crosses below its declared floor; no new externalized residual is created ...; any accepted loss remains recorded under non-erasure.”

### CRC mappings

1. **Axiom 19: Protected-Floor Admissibility**
   - Interpretation: **DIRECT / GENERALIZED**

2. **Transform admissibility**
   - Interpretation: **GENERALIZED SUPPORT**

3. **Preservation Must Be Declared**
   - Interpretation: **INFERRED SUPPORT**
   - Reason: accepted local change requires explicit preservation constraints.

4. **Locality Conservation**
   - Interpretation: **INFERRED SUPPORT**
   - Reason: externalized residual must remain represented rather than disappearing outside the active boundary.

---

## SRC-PASSAGE-016: Typed Economic Board

**Source location:** V6 §2, PDF pp. 49-50

### CRC mappings

1. **Typed Board construct**
   - Interpretation: **GENERALIZED**

2. **Context**
   - Interpretation: **GENERALIZED SUPPORT**

3. **Metric**
   - Interpretation: **GENERALIZED SUPPORT**

4. **Carrier**
   - Interpretation: **GENERALIZED SUPPORT**

5. **State**
   - Interpretation: **GENERALIZED SUPPORT**

### Mapping type

**one-to-many**

---

## SRC-PASSAGE-017: Typed Residual

**Source location:** V6 §3, PDF p. 50

### CRC mappings

1. **Axiom 16: Residual Primacy**
   - Interpretation: **DIRECT / GENERALIZED**

2. **Carrier**
   - Interpretation: **DIRECT SUPPORT**

3. **Metric**
   - Interpretation: **DIRECT SUPPORT**

---

## SRC-PASSAGE-018: Active Need

**Source location:** V6 §4, PDF p. 50, lines 1697-1705

**Source passage:**

> “Ni = 0 means that this specific floor is not currently breached. It does not mean that the entire system is globally solved.”

### CRC mappings

1. **Active Need construct**
   - Interpretation: **DIRECT / GENERALIZED**

2. **Resolution non-overclaim boundary**
   - Interpretation: **INFERRED**
   - Reason: local satisfaction does not imply global CLOSED.

3. **Contextual Reality**
   - Interpretation: **INFERRED SUPPORT**
   - Reason: resolution remains scoped to the active board/context.

---

## SRC-PASSAGE-019: Certified Bridge / No Arbitrary Aggregation

**Source location:** V6 §6, PDF p. 51, lines 1717-1725

**Source passage:**

> “Only after such a bridge is certified may an Ri term be transported ...”

> “no bridge ⇒ no arithmetic combination.”

### CRC mappings

1. **Axiom 18: Unbridged Is Not Commensurable**
   - Interpretation: **DIRECT**

2. **Axiom 7: Explicit Projection**
   - Interpretation: **DIRECT SUPPORT**

3. **Bridge derived construct**
   - Interpretation: **DIRECT SUPPORT**

4. **Metric**
   - Interpretation: **DIRECT SUPPORT**

### Mapping type

**one-to-many**

---

## SRC-PASSAGE-020: Intervention-Response Causal Leverage

**Source location:** V6 §7, PDF pp. 51-52

### CRC mappings

1. **Causal Leverage**
   - Interpretation: **DIRECT / GENERALIZED**

2. **Transform**
   - Interpretation: **DIRECT SUPPORT**

3. **Metric**
   - Interpretation: **DIRECT SUPPORT**

4. **Residual Primacy**
   - Interpretation: **DIRECT SUPPORT**

---

## SRC-PASSAGE-021: Reliability as Profile

**Source location:** V6 §8, PDF p. 52

### CRC mappings

1. **Reliability Profile**
   - Interpretation: **DIRECT / GENERALIZED**

2. **No sovereign scalar principle**
   - Interpretation: **DIRECT**
   - Status: **UNMAPPED AS STANDALONE AXIOM**

3. **Metric discipline**
   - Interpretation: **GENERALIZED SUPPORT**

---

## SRC-PASSAGE-022: Finite Strict-Descent Closure

**Source location:** V6 §10, PDF pp. 52-53

### CRC mappings

1. **Finite Strict-Descent Closure**
   - Interpretation: **DIRECT**

2. **Resolution CLOSED**
   - Interpretation: **FORMAL SUPPORT**

3. **Protected-Floor Admissibility**
   - Interpretation: **FORMAL DEPENDENCY**

4. **Certified Bridge**
   - Interpretation: **FORMAL DEPENDENCY**

---

## SRC-PASSAGE-023: Lyapunov-Type Residual Contraction

**Source location:** V6 §11, PDF p. 53

### CRC mappings

1. **Lyapunov-Type Residual Contraction**
   - Interpretation: **DIRECT**

2. **Residual Primacy**
   - Interpretation: **FORMAL SUPPORT**

3. **Temporal evolution**
   - Interpretation: **FORMAL SUPPORT**

---

## SRC-PASSAGE-024: Carrier Relation

**Source location:** V6 §12, PDF p. 53

**Source statement:**

```text
m_j |= R_j
```

when mechanism `m_j` performs a necessary function for representing, allocating, absorbing, or closing residual `R_j`.

### CRC mappings

1. **Stage Conservation**
   - Interpretation: **DIRECT**

2. **Stage Extinction**
   - Interpretation: **DIRECT**

3. **Carrier**
   - Interpretation: **GENERALIZED SUPPORT**

4. **Relationship**
   - Interpretation: **GENERALIZED SUPPORT**

### Unmapped candidate

A formal CRC-level **Carrier Relation operator** has not yet been separately defined.

Status: **UNMAPPED CANDIDATE**

---

## SRC-PASSAGE-025: Stage Assignment as Auditable Hypothesis

**Source location:** V6 §14, PDF p. 54, lines 1870-1877

**Source passage:**

> “The assignment must include: the evidence supporting the stage; the residual still carried ...; the exit condition ...; the falsifier ...”

### CRC mappings

1. **Causal Stage Classification**
   - Interpretation: **DIRECT / GENERALIZED**

2. **Provenance**
   - Interpretation: **DIRECT SUPPORT**

3. **Resolution**
   - Interpretation: **GENERALIZED SUPPORT**

4. **Context**
   - Interpretation: **GENERALIZED SUPPORT**

---

## SRC-PASSAGE-026: Calibration Ledger

**Source location:** V6 §15, PDF p. 54, lines 1878-1885

**Source passage:**

> “Every empirical parameter ... should carry a calibration record Ck = (variable, unit, source, method, interval, date, domain, version).”

> “A parameter without such a record is not zero; it is UNKNOWN.”

### CRC mappings

1. **Axiom 17: Unknown Is Not Zero**
   - Interpretation: **DIRECT**

2. **Axiom 26: Calibration Provenance**
   - Interpretation: **DIRECT**

3. **Provenance**
   - Interpretation: **DIRECT SUPPORT**

4. **Metric**
   - Interpretation: **DIRECT SUPPORT**

### Mapping type

**one-to-many**

---

## SRC-PASSAGE-027: Formal / Empirical Status Table

**Source location:** V6 §16, PDF p. 55, lines 1886-1897

**Source passage includes:**

```text
Typed residual: FORMAL-CLOSED
Need: FORMAL-CLOSED
Leverage: FORMAL-CLOSED, empirical value pending
Reliability: FORMAL-CLOSED
Protected floors: FORMAL-CLOSED
Cross-domain aggregation: BRIDGE-REQUIRED
Stage Conservation / Extinction: FORMAL-CLOSED
Finite strict-descent: CONDITIONAL-THEOREM
Lyapunov contraction: CONDITIONAL-THEOREM
```

### CRC mappings

1. **Formal / Empirical Boundary**
   - Interpretation: **DIRECT**

2. **Axiom 17: Unknown Is Not Zero**
   - Interpretation: **DIRECT SUPPORT**

3. **Axiom 18: Unbridged Is Not Commensurable**
   - Interpretation: **DIRECT SUPPORT**

4. **Axiom 20: Stage Conservation**
   - Interpretation: **STATUS SUPPORT**

5. **Axiom 21: Stage Extinction**
   - Interpretation: **STATUS SUPPORT**

6. **Finite Strict-Descent Closure**
   - Interpretation: **STATUS SUPPORT**

7. **Lyapunov-Type Residual Contraction**
   - Interpretation: **STATUS SUPPORT**

### Mapping type

**strong one-to-many**

---

## SRC-PASSAGE-028: Operational V6 Audit Cycle

**Source location:** V6 §17, PDF pp. 55-56

### CRC mappings

1. **Source-Derived Operational Cycle**
   - Interpretation: **DIRECT / GENERALIZED**

2. **Context**
   - Interpretation: **support**

3. **Residual Primacy**
   - Interpretation: **support**

4. **Metric**
   - Interpretation: **support**

5. **Protected-Floor Admissibility**
   - Interpretation: **support**

6. **Unbridged Is Not Commensurable**
   - Interpretation: **support**

7. **Calibration Provenance**
   - Interpretation: **support**

8. **Resolution**
   - Interpretation: **support**

### Mapping type

**one-to-many operational integration passage**

---

## SRC-PASSAGE-029: Falsification Program

**Source location:** V6 §18, PDF p. 56

### CRC mappings

1. **Causal Stage Classification**
   - Interpretation: **DIRECT SUPPORT**

2. **Certified Bridge validity**
   - Interpretation: **DIRECT SUPPORT**

3. **Protected-Floor Admissibility**
   - Interpretation: **DIRECT SUPPORT**

4. **Conditional closure laws**
   - Interpretation: **DIRECT SUPPORT**

### Unmapped remainder

The source explicitly lists falsifiers for:

- irreproducible typed residuals;
- bridge reconstruction failure;
- protected-floor violations;
- indistinguishable stage labels;
- unreliable witness-derived reliability;
- externalized closure;
- violated Lyapunov contraction;
- premature Stage Extinction.

CRC does **not yet have a dedicated Falsification Registry construct**.

Status: **UNMAPPED CANDIDATE**

---

# One-to-Many Mapping Summary

The following passages currently map to multiple CRC laws or constructs:

| Source passage | CRC targets |
|---|---|
| SRC-PASSAGE-004 | Axiom 25, Carrier, Context |
| SRC-PASSAGE-005 | Axiom 24, Authority, Fail-Closed Authority |
| SRC-PASSAGE-006 | Axiom 22, Axiom 23, Provenance, Calibration Provenance |
| SRC-PASSAGE-013 | Stage Conservation, Carrier Relation, Locality Conservation |
| SRC-PASSAGE-015 | Protected-Floor Admissibility, Transform admissibility, Preservation, Locality |
| SRC-PASSAGE-016 | Typed Board, Context, Metric, Carrier, State |
| SRC-PASSAGE-019 | Axiom 18, Explicit Projection, Bridge, Metric |
| SRC-PASSAGE-026 | Unknown Is Not Zero, Calibration Provenance, Provenance, Metric |
| SRC-PASSAGE-027 | Formal/Empirical Boundary plus six status-bearing CRC laws |
| SRC-PASSAGE-028 | Operational cycle plus seven supporting CRC concepts |

---

# Many-to-One Mapping Summary

The following CRC laws depend on multiple source passages:

| CRC law | Source passages |
|---|---|
| **Axiom 16: Residual Primacy** | 001, 017, 020, 023 |
| **Axiom 18: Unbridged Is Not Commensurable** | 019, 027, 028 |
| **Axiom 19: Protected-Floor Admissibility** | 015, 020, 022, 027, 028, 029 |
| **Axiom 20: Stage Conservation** | 009, 010, 013, 024, 027 |
| **Axiom 21: Stage Extinction** | 008, 009, 014, 024, 027, 029 |
| **Axiom 22: Causal History Non-Erasure** | 003, 006, 008, 013 |
| **Axiom 23: Witness Requires Causal Participation** | 006, 007 |
| **Axiom 24: Resource Authority Is Not Truth Authority** | 005 |
| **Axiom 25: Global Result / Local Realization** | 003, 004 |
| **Axiom 26: Calibration Provenance** | 006, 026, 027, 028 |
| **Causal Stage Classification** | 001, 002, 012, 018, 025, 027, 029 |
| **Finite Strict-Descent Closure** | 001, 015, 017, 019, 022, 027 |
| **Lyapunov-Type Residual Contraction** | 001, 023, 027, 029 |

---

# Unmapped Source Passages / Candidate CRC Extensions

These source-derived concepts are tracked but have not yet been promoted into explicit standalone CRC laws or constructs.

## U-001 Public Knowledge Monotonicity

```text
K_(t+1) >= K_t
```

Potential CRC direction:

```text
CertifiedKnowledgeMonotonicity
```

Status: **UNMAPPED**

---

## U-002 Temporary Residual-Closure Machine

Source concept:

```text
organization = temporary carrier justified by closure performance
```

Potential CRC direction:

```text
FunctionalCarrier
or
TemporaryClosureCarrier
```

Status: **UNMAPPED**

---

## U-003 Moving Closure Frontier

Source dynamic:

```text
provisional closure
-> innovation
-> new frontier
-> closure
```

Potential CRC direction:

```text
FrontierReopeningLaw
```

Status: **UNMAPPED**

---

## U-004 Dependency-Centrality Allocation

Source concept:

```text
small causal bridge may outrank visible isolated work
when it unlocks many downstream residuals
```

Potential CRC direction:

```text
DependencyLeverage
```

Status: **UNMAPPED**

---

## U-005 No Sovereign Scalar

Source concept:

```text
multidimensional reliability profile
!=
privileged universal scalar
```

Potential CRC direction:

```text
NoScalarCollapseLaw
```

Status: **UNMAPPED**

---

## U-006 Carrier Relation Operator

Source notation:

```text
m |= R
```

Potential CRC direction:

```text
Carries(m,R)
```

as a formal Relationship subtype.

Status: **UNMAPPED**

---

## U-007 Falsification Registry

Source V6 includes explicit falsifiers for bridges, residuals, stage labels, protected floors, witness reliability, closure boundaries, and contraction claims.

Potential CRC direction:

```text
Falsifier
EvidenceAgainst
ResolutionInvalidation
```

Status: **UNMAPPED**

---

# Reverse-Index Rule

Every future source merged into CRC should add entries in this file before or with the law merge.

Required fields:

```text
Source Passage ID
Source ID
Section / page / line range
Exact source proposition
CRC laws derived from it
Interpretation level
Mapping cardinality
Calibration status
Unmapped remainder
```

A source passage with no current CRC use remains explicitly listed as **UNMAPPED** rather than being silently discarded.

---

# Related Files

- `CORE_PRIMITIVES_AND_AXIOMS.md`
- `SOURCE_LEDGER.md`
- `PROVENANCE_MATRIX.md`
