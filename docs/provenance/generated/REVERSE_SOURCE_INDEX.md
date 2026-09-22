# Set Calculus Reverse Source Index

> GENERATED FILE. Do not edit by hand.
> Source of truth: `docs/provenance/SOURCE_CATALOG.json`.
> Regenerate with: `python scripts/generate_provenance_views.py`.

## Calibration ledger and UNKNOWN boundary

- **Passage ID:** `gr-ai-gamma:artifact:causal-temporal-economics-v6-passage-calibration-ledger`
- **Source:** Causal Temporal Economics Version 6 (`gr-ai-gamma:artifact:causal-temporal-economics-v6`)
- **Location:** V6 §15, p. 54, lines 1878-1885
- **Calibration:** `EMPIRICAL_CALIBRATION_PENDING`
- **Source summary:** Empirical parameters require variable/unit/source/method/interval/date/domain/version provenance; missing calibration is UNKNOWN rather than zero.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| CRC Calibration Provenance | `CRC` | `GENERALIZED` | `PRIMARY` | `EMPIRICAL_CALIBRATION_PENDING` | `map:cte-calibration-to-crc-calibration-provenance` |

## Certified bridge and no arbitrary aggregation

- **Passage ID:** `gr-ai-gamma:artifact:causal-temporal-economics-v6-passage-certified-bridge`
- **Source:** Causal Temporal Economics Version 6 (`gr-ai-gamma:artifact:causal-temporal-economics-v6`)
- **Location:** V6 §6, p. 51, lines 1717-1725
- **Calibration:** `BRIDGE_REQUIRED`
- **Source summary:** Cross-carrier transport requires a certified bridge; no bridge implies no arithmetic combination.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| CRC Unbridged Is Not Commensurable | `CRC` | `GENERALIZED` | `PRIMARY` | `BRIDGE_REQUIRED` | `map:cte-bridge-to-crc-unbridged` |

## Residual primacy and closure

- **Passage ID:** `gr-ai-gamma:artifact:causal-temporal-economics-v6-passage-residual-primacy`
- **Source:** Causal Temporal Economics Version 6 (`gr-ai-gamma:artifact:causal-temporal-economics-v6`)
- **Location:** V3 §3, p. 8, lines 175-200
- **Calibration:** `FORMAL_CLOSED`
- **Source summary:** Residual is unresolved causal state; closure occurs at zero under declared scope and verification; productive action contracts residual.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| CRC Residual Primacy | `CRC` | `GENERALIZED` | `PRIMARY` | `FORMAL_CLOSED` | `map:cte-residual-to-crc-residual-primacy` |

## General Set Calculus primitive tuple

- **Passage ID:** `gr-ai-gamma:artifact:idgm-primitives-passage-sc-tuple`
- **Source:** IDGM Primitive Boundary (`gr-ai-gamma:artifact:idgm-primitives`)
- **Location:** General Set Calculus primitives
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** SC = <Set, Member, Relationship, State, Transform, Resolution, Provenance>

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Set Calculus Core | `SET_CALCULUS` | `DIRECT` | `PRIMARY` | `NOT_APPLICABLE` | `map:idgm-sc-tuple-to-set-calculus-core` |

## IDGM specialization primitive tuple

- **Passage ID:** `gr-ai-gamma:artifact:idgm-primitives-passage-specialization`
- **Source:** IDGM Primitive Boundary (`gr-ai-gamma:artifact:idgm-primitives`)
- **Location:** Added specialization primitives
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** IDGM = SC + <Intent, Authority, Evidence>

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Intent-Driven Generative Math Specialization | `IDGM` | `DIRECT` | `PRIMARY` | `NOT_APPLICABLE` | `map:idgm-specialization-passage-to-definition` |

## Intent-State semantic distinction

- **Passage ID:** `gr-ai-gamma:artifact:idgm-intent-passage-semantics`
- **Source:** Intent and Intent Delta (`gr-ai-gamma:artifact:idgm-intent`)
- **Location:** Intent semantics
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** Intent = what should become true; State = what is true; D(I,S) is the unresolved semantic delta.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Intent-State Distinction | `IDGM` | `DIRECT` | `PRIMARY` | `NOT_APPLICABLE` | `map:intent-semantics-to-intent-state-distinction` |

## Candidate Set Calculus primitive tuple

- **Passage ID:** `gr-ai-gamma:artifact:set-calculus-core-readme-passage-primitives`
- **Source:** Set Calculus Core README (`gr-ai-gamma:artifact:set-calculus-core-readme`)
- **Location:** Candidate primitives
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** Set, Member, Relationship, State, Transform, Resolution, Provenance.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Set Calculus Core | `SET_CALCULUS` | `DIRECT` | `PRIMARY` | `NOT_APPLICABLE` | `map:sc-core-readme-to-core` |

## Provenance survives transformation

- **Passage ID:** `gr-ai-gamma:artifact:set-calculus-core-readme-passage-provenance-survives`
- **Source:** Set Calculus Core README (`gr-ai-gamma:artifact:set-calculus-core-readme`)
- **Location:** Initial invariants / Provenance survives transformation
- **Calibration:** `PROVENANCE_REQUIRED`
- **Source summary:** A resolution retains enough trace to identify admitted inputs, relationships, and transforms.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Set Calculus Provenance Persistence | `SET_CALCULUS` | `DIRECT` | `PRIMARY` | `PROVENANCE_REQUIRED` | `map:sc-provenance-persistence` |

## Transform-produced property non-projection

- **Passage ID:** `gr-ai-gamma:artifact:set-calculus-core-readme-passage-transform-nonprojection`
- **Source:** Set Calculus Core README (`gr-ai-gamma:artifact:set-calculus-core-readme`)
- **Location:** Initial invariants / Transform-produced properties
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** property(T(x)) does not imply property(x) unless an explicit rule establishes backward implication.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Set Calculus Transform Non-Projection | `SET_CALCULUS` | `DIRECT` | `PRIMARY` | `NOT_APPLICABLE` | `map:sc-transform-nonprojection` |

## Unresolved is not unknown

- **Passage ID:** `gr-ai-gamma:artifact:set-calculus-core-readme-passage-unresolved-not-unknown`
- **Source:** Set Calculus Core README (`gr-ai-gamma:artifact:set-calculus-core-readme`)
- **Location:** Initial invariants / Unresolved is not unknown
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** Unresolved != Unknown; unresolved state may retain constraints, relationships, provenance, and resolution paths.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Set Calculus Unresolved Is Not Unknown | `SET_CALCULUS` | `DIRECT` | `PRIMARY` | `NOT_APPLICABLE` | `map:sc-unresolved-not-unknown` |

## Preserve provenance without manufacturing provenance

- **Passage ID:** `gr-ai-gamma:artifact:set-calculus-provenance-passage-principle`
- **Source:** Set Calculus Provenance (`gr-ai-gamma:artifact:set-calculus-provenance`)
- **Location:** Provenance principle
- **Calibration:** `PROVENANCE_REQUIRED`
- **Source summary:** Preserve provenance without manufacturing provenance; unresolved attribution remains uncertain rather than silently assigned.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Set Calculus Provenance Principle | `SET_CALCULUS` | `DIRECT` | `PRIMARY` | `PROVENANCE_REQUIRED` | `map:sc-provenance-principle` |

## Set Calculus core transformation pipeline

- **Passage ID:** `gr-ai-gamma:artifact:set-calculus-readme-passage-core-pipeline`
- **Source:** Set Calculus README (`gr-ai-gamma:artifact:set-calculus-readme`)
- **Location:** Core idea
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** input structure -> normalize -> resolve membership/relationship -> apply transform -> resolved state -> provenance

**CRC/Set Calculus mappings:** `UNMAPPED`

## Deterministic execution and trace

- **Passage ID:** `gr-ai-gamma:artifact:set-calculus-plan-passage-deterministic-execution`
- **Source:** Set Calculus Working Plan (`gr-ai-gamma:artifact:set-calculus-plan`)
- **Location:** 3. Deterministic execution
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** Same normalized inputs and rules should reproduce a transform; trace explains inputs, rule, intermediate change, and final state.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Set Calculus Deterministic Execution | `SET_CALCULUS` | `DIRECT` | `PRIMARY` | `NOT_APPLICABLE` | `map:sc-deterministic-execution` |

## Explicit resolution model

- **Passage ID:** `gr-ai-gamma:artifact:set-calculus-plan-passage-explicit-resolution`
- **Source:** Set Calculus Working Plan (`gr-ai-gamma:artifact:set-calculus-plan`)
- **Location:** 2. Resolution model
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** Operations terminate in explicit states rather than silently guessing; initial classes are resolved, unresolved, reversible resolution, closure, and logical failure.

| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |
|---|---|---|---|---|---|
| Set Calculus Explicit Resolution | `SET_CALCULUS` | `DIRECT` | `PRIMARY` | `NOT_APPLICABLE` | `map:sc-explicit-resolution` |

## v0.1 core implementation scope

- **Passage ID:** `gr-ai-gamma:artifact:set-calculus-scope-v0-1-passage-core-scope`
- **Source:** Set Calculus v0.1 Scope (`gr-ai-gamma:artifact:set-calculus-scope-v0-1`)
- **Location:** Core implementation scope
- **Calibration:** `NOT_APPLICABLE`
- **Source summary:** Set, Member, Relationship, Transform, State, Resolution, Provenance/Trace plus deterministic application, explicit unresolved states, reversibility where valid, closure, failure, and conformance fixtures.

**CRC/Set Calculus mappings:** `UNMAPPED`
