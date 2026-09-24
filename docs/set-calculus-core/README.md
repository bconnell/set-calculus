# Set Calculus Core

This directory will hold the canonical mathematical vocabulary and formal transform model.

## Core 0.1 canonical path

See [`CORE_0.1_PATH_INDEX.md`](CORE_0.1_PATH_INDEX.md) for the repository-wide Core 0.1 navigation index.

The path index records both present artifacts and release-checklist artifacts that are still missing. `CORE_0.1_COMPLETENESS_CHECKLIST.md` remains the canonical pass/fail authority; the index does not declare gate completion.

## Candidate primitives

```text
Set
Member
Relationship
State
Transform
Resolution
Provenance
```

These names remain candidates until formally defined.

## Initial invariants

### Transform-produced properties

A property produced by a transform cannot automatically be projected backward onto its unresolved input.

```text
property(T(x)) does not imply property(x)
```

unless an explicit rule establishes that implication.

### Unresolved is not unknown

An unresolved state may contain constraints, relationships, provenance, and possible resolution paths even when it does not contain a unique final value.

```text
Unresolved != Unknown
```

### Provenance survives transformation

A resolution should retain enough trace to determine what admitted inputs, relationships, and transforms produced it.

### Explicit failure

The system should represent failure to resolve rather than silently inventing a value.

Candidate terminal or reportable states include:

- unresolved
- resolved
- reversible resolution
- closure
- logical failure

The exact vocabulary remains subject to formalization.

## First formalization task

Define each primitive independently of programming-language implementation, then express a minimal canonical example in both mathematical notation and machine-readable form.

## Active formalizations

- `TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md` - trajectory admissibility, composition, boundary compatibility, representation structures, depth-indexed requirements, requirement entailment, and supported resolution depth.
