# Set Calculus

## Mission

Set Calculus is a living mathematical knowledge base, executable transformation system, model-training corpus, and educational foundation.

Its mission is to:

1. **Provide rigorous training and grounding material for models.**  
   The repository preserves mathematical primitives, relationships, transforms, derivations, provenance, unresolved states, competing formulations, and historical development so that models can learn from a traceable body of mathematical knowledge rather than from flattened conclusions alone.

2. **Provide durable, explorable mathematics for humans.**  
   The repository is intended to be read, challenged, extended, derived from, implemented, and reused. Mathematical claims should remain inspectable through their definitions, dependencies, transforms, evidence, and provenance.

3. **Provide a foundational structure for a student-centered academic process.**  
   Learning should follow the actual dependency structure of knowledge where practical, rather than treating inherited course boundaries or instructor authority as mathematical prerequisites. Students should be able to inspect why a statement is true, trace where it came from, challenge its derivation, and reconstruct the result independently.

4. **Preserve knowledge across transformation.**  
   Human-authored, AI-authored, human-directed AI, tool-generated, and automation-generated records are part of the developing corpus. New representations may extend, annotate, specialize, or challenge earlier material without silently erasing it.

### Curator's academic principle

It is the curator's belief that the authority of academia has, in many places, overtaken academia's desire to find truth in knowledge rather than a truth in authority.

Set Calculus therefore treats academic authority as a guide to inquiry, not a substitute for inquiry. Expertise may preserve context, identify prior work, teach methods, and challenge errors, but mathematical authority should ultimately be earned through evidence, derivation, reproducibility, provenance, and the ability to withstand examination.

The learner should be able to ask:

> What makes this true, where did it come from, what does it depend on, and can I reproduce the path myself?

The educational aim is not teacher idolization. It is a relationship in which teachers, students, researchers, and models can participate in the examination and development of knowledge while the knowledge itself remains inspectable and challengeable.

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
