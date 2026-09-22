# Causal Reality Calculus Provenance Coverage Audit

This audit compares:

- `CORE_PRIMITIVES_AND_AXIOMS.md`
- `SOURCE_LEDGER.md`
- `PROVENANCE_MATRIX.md`
- `REVERSE_SOURCE_INDEX.md`

The purpose is to detect provenance gaps and taxonomy drift without silently rewriting the underlying records.

## Audit classes

```text
A. source passages with no CRC mapping
B. CRC laws with no source mapping
C. duplicate or overlapping mappings
D. interpretation-level inconsistencies
```

Audit status values:

- **PASS**: no issue detected.
- **PARTIAL**: mapped, but some source content remains unused.
- **GAP**: no registered mapping exists.
- **DUPLICATE**: same source/law edge is represented redundantly without adding provenance information.
- **OVERLAP**: source windows overlap and may cause double counting.
- **INCONSISTENT**: interpretation taxonomy differs between provenance artifacts.
- **REVIEW**: mapping exists but its classification should be normalized.

---

# Executive Summary

| Audit class | Result |
|---|---:|
| Registered source passages fully unmapped | **0** |
| Registered source passages with unmapped remainder | **7** |
| Numbered CRC axioms with no registered source mapping | **15** |
| Additional named CRC laws/structures with no registered source mapping | **5 primary groups** |
| Exact duplicate source-to-law edges detected | **0 confirmed** |
| Overlapping / potentially duplicate source windows | **2 material cases** |
| Interpretation-level inconsistencies | **systemic taxonomy drift detected** |

The current provenance system is strong for the Causal Temporal Economics merge, but incomplete for the CRC material that predates that merge.

---

# A. Source Passages With No CRC Mapping

## A.1 Fully unmapped registered passages

**Result: PASS**

Every registered `SRC-PASSAGE-001` through `SRC-PASSAGE-029` currently has at least one CRC mapping in `REVERSE_SOURCE_INDEX.md`.

```text
fully unmapped registered passages = 0
```

## A.2 Partially unmapped passages / retained source remainder

Seven source-derived concepts remain explicitly tracked as unmapped candidates.

| ID | Source concept | Current status | Candidate CRC destination |
|---|---|---|---|
| U-001 | Public Knowledge Monotonicity | **PARTIAL** | `CertifiedKnowledgeMonotonicity` |
| U-002 | Temporary Residual-Closure Machine | **PARTIAL** | `FunctionalCarrier` / `TemporaryClosureCarrier` |
| U-003 | Moving Closure Frontier | **PARTIAL** | `FrontierReopeningLaw` |
| U-004 | Dependency-Centrality Allocation | **PARTIAL** | `DependencyLeverage` |
| U-005 | No Sovereign Scalar | **PARTIAL** | `NoScalarCollapseLaw` |
| U-006 | Carrier Relation Operator | **PARTIAL** | `Carries(m,R)` Relationship subtype |
| U-007 | Falsification Registry | **PARTIAL** | `Falsifier`, `EvidenceAgainst`, `ResolutionInvalidation` |

These are not lost material. They are deliberately retained as unmapped source remainder.

---

# B. CRC Laws With No Registered Source Mapping

## B.1 Numbered axioms 1-15

The following CRC axioms exist in `CORE_PRIMITIVES_AND_AXIOMS.md` but currently have no entry in the forward provenance matrix and no registered source ID in the source ledger.

| CRC law | Mapping status | Current origin note |
|---|---|---|
| Axiom 1: Contextual Reality | **GAP** | Predates CTE merge; derived during initial CRC formalization |
| Axiom 2: Contextual Membership | **GAP** | Predates CTE merge; influenced by problem-local Plane behavior |
| Axiom 3: Composite Identity | **GAP** | Predates CTE merge; influenced by Causal Cartesian Plane identity rules |
| Axiom 4: Address-Measure Separation | **GAP** | Predates CTE merge; influenced by Plane rank/metric firewall |
| Axiom 5: Grounded Metric | **GAP** | Predates CTE merge; influenced by Plane metric-receipt discipline |
| Axiom 6: Causal Transform Grounding | **GAP** | Initial CRC synthesis |
| Axiom 7: Explicit Projection | **GAP** as primary provenance | CTE passage 019 now supplies secondary support, but original source is not registered |
| Axiom 8: Preservation Must Be Declared | **GAP** as primary provenance | Initial CRC synthesis from transform-preservation behavior |
| Axiom 9: Transform Non-Projection | **GAP** | Inherited/generalized from Set Calculus, but no CRC source mapping recorded |
| Axiom 10: Temporal Distinction | **GAP** as primary provenance | CTE passage 002 now supplies secondary support |
| Axiom 11: Precedence Is Not Reversibility | **GAP** | Initial CRC synthesis |
| Axiom 12: Symmetry Is Not Causal Inversion | **GAP** | Predates CTE merge; influenced by Plane mirror/inverse firewall |
| Axiom 13: Provenance Persistence | **GAP** as primary provenance | CTE passages 006/026 support it, but original provenance is not registered |
| Axiom 14: Explicit Unresolved State | **GAP** | Initial CRC synthesis |
| Axiom 15: Fail-Closed Authority | **GAP** as primary provenance | CTE passage 005 supports it indirectly; original provenance is not registered |

These axioms are **not being declared unsupported**. They are **unregistered in the current source-provenance system**.

Recommended provenance action:

```text
Register Causal Cartesian Plane bundle as a CRC source
-> assign source ID
-> extract exact passages
-> map Axioms 1-15 where supported
-> classify any remaining axioms as CRC synthesis / inherited Set Calculus
```

## B.2 Additional CRC structures without registered primary source mapping

| CRC structure | Status |
|---|---|
| Locality Conservation | **GAP** as primary provenance |
| Causal Path Composition | **GAP** |
| Causal Resolution Algebra | **GAP** as primary provenance |
| Canonical CRC Identity | **GAP** |
| Canonical CRC Pipeline | **GAP** |

---

# C. Duplicate and Overlapping Mappings

## C.1 Exact duplicate source-to-law edges

**Result: PASS**

No confirmed exact duplicate edge was found where the same Source Passage ID maps to the same CRC law with the same interpretation and no additional provenance role.

Repeated CRC laws across different source passages are treated as intentional many-to-one support.

## C.2 Overlapping source windows

### OVERLAP-001: SRC-PASSAGE-015 and SRC-PASSAGE-018

`SRC-PASSAGE-015` includes V6 §5 with source window `lines 1697-1721`.

`SRC-PASSAGE-018` identifies Active Need using `lines 1697-1705`.

Therefore:

```text
SRC-PASSAGE-018 subset SRC-PASSAGE-015 source window
```

Status: **OVERLAP**

This is conceptually defensible because Active Need and Protected-Floor Admissibility are distinct source concepts, but line-window accounting can double-count the same passage.

Recommended normalization:

```text
SRC-PASSAGE-018 -> V6 §4 exact Active Need lines only
SRC-PASSAGE-015 -> V5 §21 + V6 §5 starting after Active Need definition
```

### OVERLAP-002: bundled source regions inside SRC-PASSAGE-015

`SRC-PASSAGE-015` combines V5 §21 Coherence Conservation and V6 §5 Protected Floors under one Passage ID.

Status: **REVIEW**

Recommended normalization:

```text
SRC-PASSAGE-015A = V5 §21 Coherence Conservation
SRC-PASSAGE-015B = V6 §5 Protected-Floor Partial Order
```

Then map both to Axiom 19 with separate interpretation roles.

## C.3 Forward/reverse matrix duplication

The existence of the same relationship in both `PROVENANCE_MATRIX.md` and `REVERSE_SOURCE_INDEX.md` is intentional and **not considered duplication**.

The forward matrix answers law -> source. The reverse index answers source -> law.

---

# D. Interpretation-Level Inconsistencies

## D.1 Canonical taxonomy

`PROVENANCE_MATRIX.md` defines exactly:

```text
DIRECT
GENERALIZED
INFERRED
```

These are the canonical interpretation levels.

## D.2 Hybrid labels in the forward matrix

Several rows use `DIRECT / GENERALIZED`.

Affected entries include:

- Axiom 19: Protected-Floor Admissibility
- Axiom 20: Stage Conservation
- Axiom 21: Stage Extinction
- Axiom 24: Resource Authority Is Not Truth Authority
- Active Need
- Causal Leverage
- Reliability Profile
- Causal Stage Classification

Status: **INCONSISTENT**

A single mapping edge should have one interpretation level.

Recommended correction:

- use **DIRECT** when CRC only normalizes notation;
- use **GENERALIZED** when CRC broadens the source domain;
- create two separate source edges if one passage supports both a direct domain law and a broader generalized CRC law.

## D.3 Noncanonical interpretation labels in reverse index

The reverse index uses labels not defined by the canonical taxonomy:

```text
DIRECT SUPPORT
GENERALIZED SUPPORT
INFERRED SUPPORT
INFERRED COMPLEMENT
FORMAL SUPPORT
FORMAL DEPENDENCY
STATUS SUPPORT
support
DIRECT / GENERALIZED
```

Status: **INCONSISTENT**

These phrases mix two dimensions:

1. interpretation level;
2. mapping role.

Recommended normalized schema:

```text
interpretation_level:
  DIRECT | GENERALIZED | INFERRED

mapping_role:
  PRIMARY | SUPPORT | DEPENDENCY | COMPLEMENT | STATUS
```

## D.4 Axiom 18 classification tension

The forward matrix classifies Axiom 18 as **DIRECT**, but its note says CRC broadens `residual carrier` to causal `Carrier`.

Status: **REVIEW**

Under the current definitions, broadening an economic/residual domain rule to all causal Carriers fits **GENERALIZED** more closely than **DIRECT**.

Recommended representation:

```text
Interpretation: GENERALIZED
Mapping role: PRIMARY
```

The nested source proposition `no certified bridge => no arithmetic combination` may remain DIRECT at the passage level.

## D.5 Axiom 23 classification

Axiom 23 is classified **DIRECT** in the forward matrix. Its CRC form `Witness(A,T) => CausalLoad(A,T) > 0` closely preserves the source incarnation requirement.

Status: **PASS**

Recommended reverse-index split:

```text
Passage 007 -> Axiom 23
Interpretation: DIRECT
Role: PRIMARY

Passage 006 -> Axiom 23
Interpretation: GENERALIZED
Role: SUPPORT
```

## D.6 Causal History Non-Erasure mapping breadth

The forward matrix maps Axiom 22 primarily from `Ractive -> 0, Whistory != 0` as **GENERALIZED**.

The reverse index additionally maps passages 003, 006, 008, and 013.

Status: **REVIEW**

Recommended roles:

```text
006 -> Axiom 22 : GENERALIZED / SUPPORT
008 -> Axiom 22 : GENERALIZED / PRIMARY
003 -> Axiom 22 : INFERRED / ANALOGICAL SUPPORT
013 -> remove from Axiom 22 unless an explicit derivation is documented
```

---

# E. Source-Location Quality Findings

These findings affect provenance precision.

## E.1 Calibration line range

`PROVENANCE_MATRIX.md` currently locates Axiom 26 at `V6 §15, PDF p. 54, lines 1870-1877`.

The calibration ledger begins after the Stage Assignment material, around `lines 1878+`.

Status: **LOCATION REVIEW**

The reverse index is more precise:

```text
SRC-PASSAGE-026
V6 §15
lines 1878-1885
```

Recommended correction: use the reverse-index window.

## E.2 Stage Classification line range

The Stage Classification passage and Calibration Ledger are adjacent. Future source IDs should preserve exact non-overlapping windows so a passage cannot accidentally inherit the calibration statement of its neighbor.

---

# F. Coverage Status by CRC Layer

| CRC layer | Provenance coverage |
|---|---|
| Set Calculus inherited primitives | **External/inherited, not audited here** |
| CRC primitives Context/Carrier/Metric/Temporal/Authority | **PARTIAL** secondary CTE support; primary origin not registered |
| Axioms 1-15 | **GAP** primary source mapping |
| Axioms 16-26 | **COVERED** by SRC-CTE-V6-20260909 |
| Typed Board / Active Need / Leverage / Reliability | **COVERED** |
| Conditional closure laws | **COVERED** |
| Causal Stage Classification | **COVERED**, interpretation normalization needed |
| Formal / Empirical Boundary | **COVERED** |
| Operational Cycle | **COVERED** |
| Unmapped source candidates U-001..U-007 | **TRACKED / NOT PROMOTED** |

---

# G. Audit Conclusions

```text
registered CTE source passages:
  no completely orphaned passage IDs
  seven retained unmapped candidate concepts

Axioms 16-26:
  source mapped

Axioms 1-15:
  primary provenance not yet registered

exact duplicate mapping edges:
  none confirmed

overlapping source windows:
  present

canonical interpretation taxonomy:
  DIRECT
  GENERALIZED
  INFERRED

current reverse-index vocabulary:
  contains noncanonical mixed labels
```

The largest provenance debt is therefore **not missing CTE coverage**. It is registering the source lineage for the first CRC layer, especially the Causal Cartesian Plane material that informed Axioms 1-15.

---

# H. Required Audit Rule for Future Merges

Every future source merge should pass these checks:

1. Every registered source passage is either mapped or explicitly marked UNMAPPED.
2. Every newly added CRC law has at least one source mapping or is explicitly labeled CRC SYNTHESIS.
3. A source-law edge has exactly one interpretation level: `DIRECT | GENERALIZED | INFERRED`.
4. Mapping role is stored separately: `PRIMARY | SUPPORT | DEPENDENCY | COMPLEMENT | STATUS`.
5. Duplicate exact edges are rejected.
6. Overlapping source windows are explicitly justified.
7. Calibration status is independent of interpretation level.
8. Source line/page ranges must not silently span unrelated neighboring propositions.

---

# Related Files

- `CORE_PRIMITIVES_AND_AXIOMS.md`
- `SOURCE_LEDGER.md`
- `PROVENANCE_MATRIX.md`
- `REVERSE_SOURCE_INDEX.md`