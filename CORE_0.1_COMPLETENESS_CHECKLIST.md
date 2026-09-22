# Set Calculus Core 0.1 Completeness Checklist

**Status:** Active release gate  
**Branch:** `causal-reality-calculus`  
**Machine-readable companion:** `CORE_0.1_COMPLETENESS_CHECKLIST.yaml`  
**Release rule:** Core 0.1 is complete only when every REQUIRED gate below is checked and has linked pass evidence.

```text
SPECIFICATION PASS
∧ IMPLEMENTATION PASS
∧ CONFORMANCE PASS
∧ CONVENTIONAL-CALCULUS PASS
∧ PROVENANCE PASS
=
CORE 0.1 PASS
```

A percentage, milestone label, or informal judgment does not substitute for a failed required gate.

## Ownership

| Area | Owner | Responsibility |
|---|---|---|
| Core specification | Chad Coulter | Canonical definitions, architecture consistency, formal release decision |
| Provenance | Chad Coulter | Provenance preservation, historical trace, non-retraction requirements |
| Reference implementation | Chad Coulter, unless explicitly delegated | Executable reference semantics and deterministic resolver |
| Conformance suite | Chad Coulter, unless explicitly delegated | Canonical executable fixtures and release-test integrity |
| Conventional-calculus validation | Chad Coulter | Round-trip compatibility examples and dependency validation |
| Independent review | TBD | Optional pre-release adversarial review; does not replace required evidence |

If ownership changes, update this table without rewriting the mathematical requirement.

---

# A. Specification Gate

## A1. Canonical primitive vocabulary

- [ ] **A1 PASS — One canonical definition exists for every Core 0.1 primitive.**
  - **Owner:** Chad Coulter
  - **Required artifacts:**
    - `docs/set-calculus-core/README.md`
    - `docs/philosophy-of-set-calculus/CANONICAL_TERMINOLOGY_LEDGER.md`
  - **Required primitives:**
    ```text
    Set
    Member
    Relationship
    Identity
    State
    Transform
    Resolution
    Provenance
    ```
  - **PASS evidence:**
    - exactly one active canonical definition per primitive;
    - aliases explicitly identified;
    - `Identity != State` is explicit;
    - repository-wide terminology audit finds no incompatible active definitions.
  - **FAIL evidence:**
    - any primitive remains undefined;
    - two active canonical sections define the same primitive incompatibly;
    - Identity remains embedded in State as the canonical model.

## A2. Three-axis resolution state and four public states

- [ ] **A2 PASS — Resolution algebra is canonical and internally consistent.**
  - **Owner:** Chad Coulter
  - **Required artifacts:**
    - `docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md`
    - `docs/philosophy-of-set-calculus/CANONICAL_TERMINOLOGY_LEDGER.md`
  - **Required internal state:**
    ```text
    rho = <P,N,C>
    ```
  - **Required public states:**
    ```text
    VALID
    PARTIAL
    UNRESOLVED
    INVALID
    ```
  - **PASS evidence:**
    - P, N, and C have explicit construction semantics;
    - product partial order, join, meet, and incomparability are defined;
    - projection from `rho` to the four public states is deterministic under the active rule profile;
    - `PARTIAL != UNRESOLVED` everywhere;
    - obsolete three-state sections are removed, rewritten, or explicitly marked historical.
  - **FAIL evidence:**
    - any active canonical rule still assumes only VALID/UNRESOLVED/INVALID;
    - the same normalized evidence state can produce multiple public states without an explicit conflict-resolution rule.

## A3. Independent decisive closure

- [ ] **A3 PASS — Decisive Positive and Decisive Negative are independently defined.**
  - **Owner:** Chad Coulter
  - **Required artifact:** `docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md`
  - **Required laws:**
    ```text
    DecisivePositive != !DecisiveNegative
    DecisiveNegative != !DecisivePositive

    D+ -> positive closure
    D- -> negative closure
    ```
  - **PASS evidence:**
    - Constructive Positive Closure can derive VALID from sufficient positive witnesses;
    - no premise requires exhaustive elimination of negative alternatives;
    - overlapping `D+ ∧ D-` creates a decisive conflict object rather than silently preferring polarity.
  - **FAIL evidence:**
    - VALID requires proving that no decisive-negative alternative exists;
    - INVALID is defined merely as absence of positive proof;
    - one polarity wins by default.

## A4. Six typed boundary witnesses

- [ ] **A4 PASS — All six boundary witness types are canonical.**
  - **Owner:** Chad Coulter
  - **Required artifact:** `docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md`
  - **Required witness types:**
    ```text
    IDENTITY
    STATE
    CONTEXT
    AUTHORITY
    INVARIANT
    PROVENANCE
    ```
  - **PASS evidence:**
    - each witness has a typed payload;
    - cardinality, nullability, and relation-specific evidence are defined;
    - VALID/PARTIAL/UNRESOLVED/INVALID outcomes are defined;
    - aggregate boundary validation includes all six.
  - **FAIL evidence:**
    - any active section still says there are five witness types;
    - Identity is still represented as a State relation;
    - a required witness lacks validation semantics.

## A5. Transform semantics

- [ ] **A5 PASS — Transform is specified strongly enough for independent implementation.**
  - **Owner:** Chad Coulter
  - **Required artifacts:**
    - `docs/set-calculus-core/README.md`
    - canonical transform specification to be added under `docs/set-calculus-core/`
  - **Minimum required semantics:**
    ```text
    applicability
    input requirements
    output guarantees
    preserved properties
    changed properties
    provenance effect
    failure state
    composition
    identity transform
    reversible
    partially reversible
    irreversible
    closure-producing
    ```
  - **PASS evidence:**
    - two independent implementers can determine whether `T2 o T1` is legal from the specification alone;
    - transform-produced properties are never projected backward without an explicit rule.
  - **FAIL evidence:**
    - transform composition depends on undocumented convention;
    - reversibility or preservation behavior is implicit.

## A6. Trajectory and boundary semantics

- [ ] **A6 PASS — Trajectory semantics use the current six-witness/four-state model throughout.**
  - **Owner:** Chad Coulter
  - **Required artifact:** `docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md`
  - **PASS evidence:**
    - trajectory form `pi=<s0,T1,s1,...,Tn,sn>` is canonical;
    - concatenation requires boundary validation;
    - boundary validation uses Identity, State, Context, Authority, Invariant, and Provenance;
    - local admissibility does not imply concatenated admissibility;
    - partial trajectory resolution preserves known resolved structure.
  - **FAIL evidence:**
    - active trajectory algebra still uses the obsolete three-state table as canonical;
    - boundary compatibility omits Identity.

## A7. Tie-break sequent calculus

- [ ] **A7 PASS — Decisive conflicts have a complete formal tie-break calculus.**
  - **Owner:** Chad Coulter
  - **Required artifact:** `docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md`
  - **Required sequent form:**
    ```text
    Gamma ; Q |-Omega kappa
    ```
  - **PASS evidence:**
    - admissible-rule formation is defined;
    - scope, dependency, provenance, supersession, and specificity precedence are defined;
    - maximal-rule selection is defined;
    - global positive, global negative, partial, and unresolved conflict rules are defined;
    - losing rules/witnesses remain preserved in provenance.
  - **FAIL evidence:**
    - a tie-break may select a result without a sound rule;
    - unresolved maximal-rule disagreement is forced into VALID or INVALID.

## A8. Structural proof rules

- [ ] **A8 PASS — Structural proof-rule status is explicitly declared.**
  - **Owner:** Chad Coulter
  - **Required artifact:** canonical proof-calculus section/file under `docs/set-calculus-core/`
  - **Rules requiring status:**
    ```text
    weakening
    contraction
    exchange
    cut
    substitution
    ```
  - **For each rule, declare exactly one:**
    ```text
    ADMISSIBLE
    RESTRICTED
    NOT_ADMISSIBLE
    UNRESOLVED
    ```
  - **PASS evidence:**
    - every rule has an explicit status and, where restricted, explicit conditions;
    - unresolved metatheory is labeled rather than silently assumed.
  - **FAIL evidence:**
    - an implementation must guess whether a structural proof operation is legal.

## A9. Resolution transition semantics

- [ ] **A9 PASS — Legal resolution-state transitions are formally specified.**
  - **Owner:** Chad Coulter
  - **Required artifact:** canonical resolution-transition section/file under `docs/set-calculus-core/`
  - **PASS evidence:**
    - legal transitions among UNRESOLVED, PARTIAL, VALID, and INVALID are stated;
    - reopening, reclassification, supersession, and new-material-evidence conditions are explicit;
    - conclusion change never deletes proof history.
  - **FAIL evidence:**
    - a final classification can change without a recorded material cause.

---

# B. Reference Implementation Gate

## B1. Executable core types

- [ ] **B1 PASS — Reference implementation can represent all canonical core objects.**
  - **Owner:** Chad Coulter unless delegated
  - **Required artifact path:** `src/` or an explicitly named reference-runtime directory
  - **Required types:**
    ```text
    Identity
    State
    Relationship
    Transform
    Witness
    BoundaryEvidence
    ResolutionEvidenceState<P,N,C>
    ResolutionStatus
    Trajectory
    Provenance
    ```
  - **PASS evidence:**
    - valid canonical fixtures construct successfully;
    - malformed required structures fail explicitly;
    - serialization/deserialization is deterministic where provided.
  - **FAIL evidence:**
    - a required formal object has no executable representation.

## B2. Deterministic resolver

- [ ] **B2 PASS — A deterministic end-to-end resolver exists.**
  - **Owner:** Chad Coulter unless delegated
  - **Required artifact path:** reference implementation under `src/` or named runtime directory
  - **Minimum interface semantics:**
    ```text
    normalize(...)
    validateWitness(...)
    validateBoundary(...)
    applyTransform(...)
    resolve(...)
    composeTrajectory(...)
    trace(...)
    ```
  - **PASS evidence:**
    - identical normalized input + identical rule set produces identical result and trace;
    - unresolved requirements are never silently guessed.
  - **FAIL evidence:**
    - formal resolution depends on nondeterministic language-model output;
    - missing evidence is silently converted into a resolved value.

## B3. Four-state executable behavior

- [ ] **B3 PASS — Implementation produces all four canonical public states.**
  - **Owner:** Chad Coulter unless delegated
  - **Required artifacts:** implementation + canonical fixtures
  - **PASS evidence:**
    - at least one fixture each returns VALID, PARTIAL, UNRESOLVED, INVALID;
    - PARTIAL retains resolved substructure that UNRESOLVED does not possess.
  - **FAIL evidence:**
    - PARTIAL is only a renamed UNRESOLVED.

## B4. Constructive positive closure execution

- [ ] **B4 PASS — Positive closure executes without negative exhaustion.**
  - **Owner:** Chad Coulter unless delegated
  - **Required artifact:** canonical fixture under `tests/conformance/`
  - **PASS evidence:**
    ```text
    sufficient positive witness
    + unresolved unrelated negative alternatives
    -> VALID
    ```
    and the trace contains no negative-exhaustion prerequisite.
  - **FAIL evidence:**
    - runtime waits for or synthesizes elimination of all negative alternatives before returning VALID.

## B5. Decisive conflict execution

- [ ] **B5 PASS — Runtime enters tie-break calculus when D+ and D- overlap.**
  - **Owner:** Chad Coulter unless delegated
  - **Required artifacts:** conflict fixtures under `tests/conformance/`
  - **PASS evidence:**
    - overlapping `D+ ∧ D-` creates a conflict;
    - fixtures demonstrate positive, negative, partial, and unresolved conflict outcomes under different admissible rule sets.
  - **FAIL evidence:**
    - runtime hardcodes positive-first or negative-first behavior.

## B6. Reconstructible trace

- [ ] **B6 PASS — Every resolution exposes reconstructible provenance.**
  - **Owner:** Chad Coulter
  - **Required artifact:** reference trace format + fixtures
  - **PASS evidence:** trace exposes:
    ```text
    inputs
    active rules
    witnesses
    transforms
    intermediate resolution states
    rho=<P,N,C>
    final projection
    conflicts
    tie-breaks
    supersessions/reclassifications
    provenance
    ```
  - **FAIL evidence:**
    - final result cannot be reconstructed from retained trace data.

---

# C. Conformance Test Gate

## C1. Canonical conformance suite

- [ ] **C1 PASS — Canonical executable conformance suite exists and passes 100%.**
  - **Owner:** Chad Coulter unless delegated
  - **Required artifact path:** `tests/conformance/`
  - **Required fixture families:**
    - primitive validity;
    - Identity vs State;
    - transform applicability;
    - all six boundary witnesses;
    - PARTIAL vs UNRESOLVED;
    - Decisive Positive;
    - Decisive Negative;
    - decisive conflict;
    - precedence rules;
    - provenance preservation;
    - legal reclassification.
  - **PASS evidence:**
    - every canonical fixture passes in CI;
    - zero flaky/probabilistic fixtures define formal semantics.
  - **FAIL evidence:**
    - any required canonical fixture fails or lacks an expected result.

## C2. Precedence conformance

- [ ] **C2 PASS — Tie-break precedence is demonstrated by executable examples.**
  - **Owner:** Chad Coulter unless delegated
  - **Required artifact path:** `tests/conformance/tie-break/`
  - **Required cases:**
    ```text
    out-of-scope rule loses regardless of specificity
    failed dependency defeats otherwise eligible rule
    invalid provenance cannot win through specificity
    valid supersession can govern over specificity
    incomparable maximal rules with conflicting conclusions -> UNRESOLVED
    incomparable maximal rules with same conclusion -> shared conclusion
    ```
  - **PASS evidence:** all cases produce the specified result with trace.
  - **FAIL evidence:** rule precedence depends on insertion order or polarity.

## C3. CI release gate

- [ ] **C3 PASS — Core 0.1 CI blocks release on conformance failure.**
  - **Owner:** Chad Coulter unless delegated
  - **Required artifact path:** `.github/workflows/`
  - **PASS evidence:**
    - canonical test suite runs automatically;
    - nonzero test failure blocks the Core 0.1 release path.
  - **FAIL evidence:**
    - release can be marked Core 0.1 with failing canonical tests.

---

# D. Conventional-Calculus Validation Gate

## D1. Derivative round trip

- [ ] **D1 PASS — A conventional derivative round-trips through Set Calculus unchanged.**
  - **Owner:** Chad Coulter
  - **Required artifact path:** `docs/conventional-calculus/examples/derivative/`
  - **Minimum example:** `f(x)=x^2 -> f'(x)=2x`
  - **Required record:**
    ```text
    conventional statement
    -> conventional result
    -> Set Calculus representation
    -> Set Calculus transforms/resolution
    -> mapped conventional result
    -> provenance
    ```
  - **PASS evidence:** mapped result equals the valid conventional result.
  - **FAIL evidence:** Set Calculus changes the valid mathematical result without an explicitly demonstrated reason.

## D2. Definite-integral round trip

- [ ] **D2 PASS — A conventional definite integral round-trips unchanged.**
  - **Owner:** Chad Coulter
  - **Required artifact path:** `docs/conventional-calculus/examples/integral/`
  - **Minimum example:** `integral_0^1 x dx = 1/2`
  - **PASS evidence:**
    - mapped result equals `1/2`;
    - accumulation/resolution steps are traceable;
    - provenance survives the round trip.
  - **FAIL evidence:** mapped result differs without a proven defect in the conventional statement.

## D3. First-order ODE round trip

- [ ] **D3 PASS — A first-order ODE demonstrates unresolved structure and later resolution.**
  - **Owner:** Chad Coulter
  - **Required artifact path:** `docs/conventional-calculus/examples/ode-first-order/`
  - **Minimum example:** `dy/dt = ky` with an initial condition
  - **PASS evidence:**
    - differential relationship is represented before the state is fully resolved;
    - added condition(s) produce the conventional solution;
    - mapped conventional result agrees;
    - provenance remains reconstructible.
  - **FAIL evidence:** the unresolved differential relationship is treated as unknown/structureless or the valid conventional result changes without justification.

## D4. Compatibility law

- [ ] **D4 PASS — All canonical conventional examples satisfy backward compatibility.**
  - **Owner:** Chad Coulter
  - **Required artifact:** `docs/conventional-calculus/COMPATIBILITY_REPORT.md`
  - **PASS evidence:**
    ```text
    ordinary calculus valid
    -> Set Calculus preserves valid result
    ```
    for every Core 0.1 validation example.
  - **FAIL evidence:**
    - any discrepancy remains unexplained or unclassified.

---

# E. Dependency / Curriculum Gate

## E1. Dependency graph coverage

- [ ] **E1 PASS — Core calculus dependency graph covers the major conventional concept families.**
  - **Owner:** Chad Coulter
  - **Required artifact:** `docs/dependency-map/001-conventional-calculus-prerequisite-graph.md`
  - **PASS evidence:** major Calc I, Calc II, Calc III/multivariable, and ODE concept families are represented.
  - **FAIL evidence:** a major concept family required by the Core 0.1 compatibility examples is absent.

## E2. Dependency-edge classification

- [ ] **E2 PASS — Material dependency edges have explicit classes.**
  - **Owner:** Chad Coulter
  - **Required artifact:** dependency graph or machine-readable companion file
  - **Required classes:**
    ```text
    HARD
    STRONG
    SUPPORTING
    HISTORICAL/CURRICULAR
    ```
  - **PASS evidence:** every edge used to justify the proposed Core 0.1 teaching order has a class and rationale.
  - **FAIL evidence:** a course-order assumption is used as mathematical dependency evidence without classification.

## E3. Dependency-derived teaching sequence

- [ ] **E3 PASS — A teaching-order hypothesis is explicitly derived from the dependency graph.**
  - **Owner:** Chad Coulter
  - **Required artifacts:**
    - `docs/dependency-map/001-conventional-calculus-prerequisite-graph.md`
    - `docs/textbook/README.md` or successor curriculum document
  - **PASS evidence:** proposed ordering cites graph dependencies and labels hypotheses as hypotheses where not mathematically forced.
  - **FAIL evidence:** inherited Calc I/II/III packaging is treated as dependency proof.

---

# F. Provenance Gate

## F1. Provenance preservation

- [ ] **F1 PASS — Resolution never silently deletes provenance.**
  - **Owner:** Chad Coulter
  - **Required artifacts:**
    - `PROVENANCE.md`
    - formal core specification
    - executable trace fixtures
  - **PASS evidence:**
    - transform lineage retained;
    - losing conflict witnesses retained;
    - superseded rules retained;
    - reclassification records prior state and material cause.
  - **FAIL evidence:** a prior material witness, rule, state, or resolution disappears from the reconstructible record.

## F2. Source/interpretation separation

- [ ] **F2 PASS — Source provenance remains separate from interpretation.**
  - **Owner:** Chad Coulter
  - **Required artifacts:**
    - `docs/provenance/SOURCE_CATALOG.json`
    - `docs/provenance/PROVENANCE_SCHEMA.json`
    - generated provenance views
  - **PASS evidence:** DIRECT / GENERALIZED / INFERRED distinctions remain machine-readable and auditable.
  - **FAIL evidence:** inferred interpretation is stored as source provenance.

## F3. End-to-end provenance round trip

- [ ] **F3 PASS — At least one conventional-calculus example is reconstructible end to end.**
  - **Owner:** Chad Coulter
  - **Required artifact:** one D1-D3 example plus executable trace
  - **PASS evidence:** reviewer can reconstruct:
    ```text
    source
    -> normalized structure
    -> witnesses
    -> transforms
    -> rho
    -> public resolution
    -> conventional mapped result
    ```
  - **FAIL evidence:** any material link in the chain is missing or invented.

---

# G. Repository Consistency Gate

## G1. Legacy-state cleanup

- [ ] **G1 PASS — No active canonical contradiction remains between legacy and current formalization.**
  - **Owner:** Chad Coulter
  - **Required artifacts:** repository-wide audit report and corrected files
  - **Audit must search for at least:**
    ```text
    three-state admissibility as canonical
    five-witness boundary model
    IDENTITY inside StateRelation
    negative-exhaustion requirement
    obsolete boundary aggregation
    three-valued witness-validation return type
    ```
  - **PASS evidence:** zero unresolved active contradictions; historical material is clearly marked historical.
  - **FAIL evidence:** an independent implementer can reasonably choose two incompatible active rules from the repository.

## G2. Canonical path index

- [ ] **G2 PASS — Core 0.1 canonical artifacts are indexed from the repository entry points.**
  - **Owner:** Chad Coulter
  - **Required artifacts:**
    - `README.md`
    - `SCOPE.md`
    - `docs/set-calculus-core/README.md`
  - **PASS evidence:** a new implementer can locate the canonical specification, checklist, conformance fixtures, compatibility examples, and provenance model without searching commit history.
  - **FAIL evidence:** current canonical material is discoverable only through historical anchors or prior conversation context.

---

# H. Core 0.1 Release Gate

Check these only after every required child gate above passes.

- [ ] **SPECIFICATION PASS**
  - Evidence: A1-A9 and G1-G2 all PASS.

- [ ] **IMPLEMENTATION PASS**
  - Evidence: B1-B6 all PASS.

- [ ] **CONFORMANCE PASS**
  - Evidence: C1-C3 all PASS with CI evidence.

- [ ] **CONVENTIONAL-CALCULUS PASS**
  - Evidence: D1-D4 and E1-E3 all PASS.

- [ ] **PROVENANCE PASS**
  - Evidence: F1-F3 all PASS.

- [ ] **CORE 0.1 PASS**
  - **Owner:** Chad Coulter
  - **PASS evidence:**
    ```text
    SPECIFICATION PASS
    ∧ IMPLEMENTATION PASS
    ∧ CONFORMANCE PASS
    ∧ CONVENTIONAL-CALCULUS PASS
    ∧ PROVENANCE PASS
    ```
  - **FAIL evidence:** any required parent gate remains unchecked.

---

# Current Repository Snapshot

This section records the current checkpoint and should be updated as gates close.

## Currently evidenced

- [x] Initial conventional-calculus prerequisite graph exists.
  - Evidence: `docs/dependency-map/001-conventional-calculus-prerequisite-graph.md`

- [x] Canonical terminology ledger exists.
  - Evidence: `docs/philosophy-of-set-calculus/CANONICAL_TERMINOLOGY_LEDGER.md`

- [x] Three-axis resolution, decisive closure, constructive positive closure, tie-break precedence, and sequent-calculus working formalizations are anchored.
  - Evidence: `docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md`

- [x] Provenance policy exists.
  - Evidence: `PROVENANCE.md`

## Known open release blockers

- [ ] Legacy three-state/five-witness material has been fully normalized.
- [ ] Transform semantics are complete enough for independent implementation.
- [ ] Structural proof rules are classified.
- [ ] Resolution-transition semantics are closed.
- [ ] Reference implementation exists.
- [ ] Canonical conformance suite exists and passes.
- [ ] Derivative round-trip exists.
- [ ] Definite-integral round-trip exists.
- [ ] First-order ODE round-trip exists.
- [ ] End-to-end executable provenance round-trip exists.

---

# Release Principle

```text
Core 0.1 is not complete because the theory is interesting.

Core 0.1 is complete when the specification is coherent,
the implementation is derivable from it,
the tests enforce it,
ordinary calculus survives the round trip,
and provenance reconstructs how the result was reached.
```
