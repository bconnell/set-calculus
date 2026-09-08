# Set Calculus Working Plan

This file captures the current implementation direction. It is intentionally a working plan, not a frozen specification.

## 1. Core primitives

Define the smallest set of first-class objects needed for computation:

- set
- member
- relationship
- transform
- state
- trace/provenance

The implementation should avoid baking presentation or natural-language assumptions into these primitives.

## 2. Resolution model

Each operation should terminate in an explicit state rather than silently guessing.

Initial result classes:

- resolved
- unresolved
- reversible resolution
- closure
- logical failure

The exact canonical state vocabulary should follow the formal set-calculus specification as it is captured.

## 3. Deterministic execution

A transform should be reproducible from the same normalized inputs and rules.

Each execution should expose enough trace data to answer:

- what inputs were used
- what rule/relationship was applied
- what intermediate state changed
- why the final state was returned

## 4. API boundary

The library should expose a small, stable interface suitable for other runtimes.

Candidate shape:

```text
normalize(input)
resolve(structure, rules)
transform(state, operation)
trace(result)
```

This API is provisional and should be replaced by the formal vocabulary once the primitives are fully captured.

## 5. Tests first

Build conformance examples before broad implementation.

Each test should define:

```text
given structure
+ operation
+ rule set
=> expected resolution state
+ expected trace
```

Start with very small examples and use them as executable definitions of behavior.

## 6. NLM integration

NLM should call Set Calculus as a deterministic resolver, not duplicate the transform logic.

```text
natural language
    -> parser / interpretation
    -> normalized structure
    -> set-calculus
    -> resolved structure + trace
    -> language rendering
```

This creates a hard boundary between model interpretation and formal resolution.

## 7. Near-term repository work

- capture canonical notation and terminology
- write the first primitive data structures
- create conformance fixtures
- implement one end-to-end transform path
- expose trace output
- create a minimal integration example for `nlm-ruby`

## Non-goals for the first pass

- building a full theorem prover
- encoding every downstream application
- coupling the calculus to one language model
- hiding unresolved states behind probabilistic output
