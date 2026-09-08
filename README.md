# Set Calculus

Set Calculus is the implementation and research repository for a computational form of the foundational set work developed around structure, membership, transformation, and resolution.

The project has two linked goals:

1. make set relationships executable as a deterministic transformation layer; and
2. reconstruct calculus from mathematical dependency, transformation, and resolution rather than inherited course boundaries.

The goal is not merely to describe sets. It is to make relationships between states explicit, executable, reversible where possible, and traceable.

## Core idea

```text
input structure
    -> normalize
    -> resolve set membership / relationship
    -> apply transform
    -> produce resolved state
    -> expose trace / provenance
```

A property produced by a transform is not assumed to be a property of the unresolved input.

```text
Potential != Resolved
Unresolved != Unknown
```

An unresolved state may preserve enough relational information to become resolvable when later constraints arrive.

## Mathematical direction

Set Calculus will model:

- sets and membership
- relationships between sets and members
- transformations between states
- explicit resolution states
- reversible and irreversible transforms
- closure and logical failure
- provenance and trace
- value and properties as state-dependent outcomes

The project should remain compatible with conventional calculus wherever conventional calculus is valid. The aim is not to discard derivatives, integrals, differential equations, limits, vector fields, or existing notation. It is to expose the deeper dependency structure that connects them.

## Curriculum reconstruction

A parallel research track will map the actual prerequisite graph behind:

- Calculus I
- Calculus II
- Calculus III / multivariable calculus
- Differential Equations

The course labels will be treated as historical containers, not as assumed mathematical dependencies.

We will ask:

> If calculus were reconstructed from its mathematical dependencies rather than its historical curriculum, what is the minimal valid ordering of concepts?

This work will feed a Set Calculus textbook and a compatibility layer for students and practitioners already trained in conventional calculus.

## Relationship to NLM

`set-calculus` is intended to become a lower-level reasoning and transform dependency for `nlm-ruby`.

```text
nlm-ruby
   -> interpretation / parser / routing
   -> normalized relational structure
   -> set-calculus
   -> deterministic structural resolution
   -> resolved structure + trace
```

This keeps language generation separate from the formal transform engine.

## Repository map

```text
README.md
PLAN.md
SCOPE.md
PROVENANCE.md
LICENSE
LICENSE_REQUIREMENTS.md
docs/
  dependency-map/
  conventional-calculus/
  set-calculus-core/
  textbook/
```

## Initial milestones

1. Capture canonical primitives and notation.
2. Define machine-readable set, relationship, transform, state, and provenance structures.
3. Implement deterministic membership and transform operations.
4. Add explicit result states such as resolved, unresolved, reversible resolution, closure, and logical failure.
5. Build conformance tests from small canonical examples.
6. Construct a dependency map of conventional calculus topics.
7. Derive a Set Calculus teaching order from that dependency map.
8. Build a compatibility mapping from conventional calculus into Set Calculus.
9. Draft the Set Calculus textbook as the canonical educational specification.
10. Finalize the immutable reciprocal-open license before public release.

See `PLAN.md` and `SCOPE.md` for the current working boundaries.
