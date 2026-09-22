# Set Calculus Provenance Coverage Audit

> GENERATED FILE. Do not edit by hand.
> Source of truth: `docs/provenance/SOURCE_CATALOG.json`.
> Regenerate with: `python scripts/generate_provenance_views.py`.

## Computed coverage

- Sources: **12**
- Passages: **15**
- Calculus objects: **12**
- Mappings: **13**
- Passages with no mapping: **2**
- Objects with no mapping: **0**
- Duplicate exact mapping edges: **0**
- Overlapping captured line windows: **0**

## Source passages with no calculus mapping

- `gr-ai-gamma:artifact:set-calculus-readme-passage-core-pipeline`: Set Calculus core transformation pipeline
- `gr-ai-gamma:artifact:set-calculus-scope-v0-1-passage-core-scope`: v0.1 core implementation scope

## Calculus objects with no source mapping

None.

## Duplicate mappings

None.

## Overlapping passage windows

None detected from captured line ranges.

## Interpretation-level consistency

All mappings use controlled enum values validated before rendering:

```text
DIRECT
GENERALIZED
INFERRED
```

Mapping role is separately controlled as `PRIMARY | SUPPORT | DEPENDENCY | COMPLEMENT | STATUS`.

## Registered audit findings

| Finding | Class | Severity | Status | Summary | Recommended action |
|---|---|---|---|---|---|
| `audit:crc-axioms-1-15-primary-provenance-gap` | `UNSOURCED_OBJECT` | `HIGH` | `OPEN` | CRC Axioms 1-15 lack registered primary passage-level provenance. | Extract exact Causal Cartesian Plane passages and map Axioms 1-15; mark remaining axioms as inherited Set Calculus or CRC synthesis. |
| `audit:idgm-passage-extraction-incomplete` | `UNMAPPED_SOURCE` | `MEDIUM` | `OPEN` | IDGM axioms and laws are registered as a source artifact but passage-level source records remain incomplete. | Extract each IDGM axiom/law into passage and object records. |
| `audit:set-calculus-core-passage-extraction-partial` | `UNMAPPED_SOURCE` | `MEDIUM` | `OPEN` | Set Calculus source records now cover root scope/plan/provenance/core README, but the full canonical core specification remains incomplete. | Continue registering docs/set-calculus-core artifacts and map every formal primitive, resolution state, and law at passage level. |
