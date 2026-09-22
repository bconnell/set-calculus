# Set Calculus Machine-Readable Provenance

This directory contains the repository-wide provenance model for Set Calculus and its specializations.

## Files

- `PROVENANCE_SCHEMA.json` - JSON Schema for the provenance graph.
- `SOURCE_CATALOG.json` - initial machine-readable source, passage, object, mapping, and audit records.

## Controlled interpretation enums

```text
interpretation_level:
  DIRECT
  GENERALIZED
  INFERRED
```

Interpretation describes **how the CRC/IDGM/Set Calculus object relates to the source statement**.

## Controlled mapping-role enums

```text
mapping_role:
  PRIMARY
  SUPPORT
  DEPENDENCY
  COMPLEMENT
  STATUS
```

Mapping role is orthogonal to interpretation. Do not encode `DIRECT SUPPORT` or similar hybrid labels.

## Controlled calibration-status enums

```text
NOT_APPLICABLE
FORMAL_CLOSED
FORMAL_DERIVED
EMPIRICAL_CALIBRATION_PENDING
BRIDGE_REQUIRED
CONDITIONAL_THEOREM
PROVENANCE_REQUIRED
DOMAIN_SCOPED
UNKNOWN
```

Calibration status is orthogonal to both interpretation and mapping role.

## Model

```text
Source
  -> Passage
      -> Mapping
          -> Calculus Object

Audit Finding
  -> Source / Passage / Mapping / Object
```

A source is an artifact or observation boundary.

A passage is the smallest practical source region supporting a provenance edge.

An object is a primitive, definition, axiom, law, theorem, construct, operator, pipeline, protocol, or resolution state.

A mapping is the explicit provenance edge between a source passage and a calculus object.

## Stable IDs

The model uses gr{Ai}Γ-compatible stable ASCII identifiers:

```text
gr-ai-gamma:artifact:<slug>
gr-ai-gamma:concept:<slug>
map:<slug>
audit:<slug>
```

Human-visible documentation should continue to render the canonical mark as `gr{Ai}Γ`.

## Repository-wide scope

The catalog is intended to cover:

```text
Set Calculus
  -> general primitives
  -> general axioms and laws
  -> dependency / transform model

Intent-Driven Generative Math
  -> specialization primitives
  -> IASTER
  -> Intent / Authority / Evidence
  -> planning, evidence, and resolution laws

Generative Governance Engine
  -> executable implementation of IDGM

Causal Reality Calculus
  -> Context / Carrier / Metric / Temporal / Authority
  -> causal laws
  -> source-derived CTE laws

future specializations
  -> same provenance model
```

## Provenance rule

A calculus object may be:

1. directly sourced;
2. generalized from a domain source;
3. inferred from multiple source constraints;
4. explicitly marked as calculus synthesis when no external source passage exists.

A missing source mapping must never be silently converted into a direct-source claim.

## Next extraction debt

The initial catalog deliberately records incomplete coverage.

Highest-priority remaining work:

1. register exact passage records from the Causal Cartesian Plane bundle for CRC Axioms 1-15;
2. extract every IDGM axiom and derived law into machine-readable object and passage records;
3. capture the canonical Set Calculus core documents under `docs/set-calculus-core/`;
4. map executable GGE model/engine behavior back to the formal IDGM laws;
5. generate the markdown source ledger, provenance matrix, reverse index, and coverage audit from the JSON graph rather than maintaining four independent truth stores.
