# Set Calculus

Set Calculus is the implementation repository for a computational form of the foundational set work developed around structure, membership, transformation, and resolution.

The goal is not merely to describe sets, but to make set relationships executable so they can be used as a deterministic transformation layer inside larger systems.

## Purpose

This repository is intended to provide:

- a compact formal representation of set membership and transformation
- deterministic operations over sets and relationships
- explicit resolution states rather than implicit interpretation
- a reusable calculus that can be embedded in language, data, AI, and systems work
- machine-testable behavior for the underlying theory

## Design direction

The core implementation should keep the mathematical layer separate from presentation and model behavior.

```text
input structure
    -> normalize
    -> resolve set membership / relationship
    -> apply transform
    -> produce resolved state
    -> expose trace / provenance
```

The implementation should prefer deterministic operations wherever possible. Language models may explain or propose transformations, but the calculus itself should be inspectable and testable.

## Relationship to NLM

`set-calculus` is intended to become a lower-level reasoning/transform dependency for `nlm-ruby`.

The split is deliberate:

```text
nlm-ruby
   -> language / model-facing interpretation
   -> parser / routing
   -> set-calculus
   -> deterministic structural resolution
```

This keeps language generation separate from the formal transform engine.

## Initial milestones

1. Capture the canonical primitives and notation.
2. Define machine-readable set and relationship structures.
3. Implement deterministic membership and transform operations.
4. Add explicit result states such as resolved, unresolved, and logical failure.
5. Add trace output so every resolution can be inspected.
6. Build a conformance test suite from small canonical examples.
7. Expose a stable API for NLM and other systems to consume.

See `PLAN.md` for the working implementation plan.
