# Generative Governance Engine

A zero-dependency executable reference implementation of Intent-Driven Generative Math (IDGM).

The governing formal specification lives in:

- `docs/intent-driven-generative-math/PRIMITIVES.md`
- `docs/intent-driven-generative-math/INTENT.md`
- `docs/intent-driven-generative-math/EXECUTION_KERNEL.md`
- `docs/intent-driven-generative-math/RESOLUTION_ALGEBRA.md`
- `docs/intent-driven-generative-math/AXIOMS_AND_LAWS.md`

The code is subordinate to those specifications. If implementation and formal specification disagree, the disagreement is a defect to resolve explicitly.

## What v0.1 executes

The engine implements the IASTER loop:

```text
Intent
  -> Authority
  -> State
  -> Transform
  -> Evidence
  -> Resolution
```

It provides:

- first-class Intent, Authority, State, Transform, Evidence, and Resolution objects
- semantic Intent-State delta
- deterministic authorization and precondition checks
- invariant-preserving Transform admission
- deterministic next-Transform planning
- Transform execution with state versioning
- current-state Evidence generation
- canonical Resolution classification:
  - COMPLETED
  - INCOMPLETE
  - BLOCKED
  - UNRESOLVED
  - SUPERSEDED
  - FAILED
- an end-to-end governance loop
- conformance tests for the six Resolution states and invariant protection

## Run

From this directory:

```cmd
python -m unittest discover -s tests -v
python -m generative_governance_engine.example
```

For editable installation:

```cmd
python -m pip install -e .
gge-example
```

## Design boundary

This is a reference kernel, not yet a policy language, theorem prover, LLM agent, workflow server, or production authorization service.

The first goal is to make the formal calculus executable without hiding ambiguity behind probabilistic behavior.
