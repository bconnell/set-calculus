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
- dependency-aware Transform selection
- blocked-state recovery through admissible prerequisite/precondition-enabling Transforms
- cost-aware path planning
- explicit transform base cost and risk penalty
- deterministic planner tie-breaking
- Transform execution with state versioning and completed-Transform history
- current-state Evidence generation
- canonical Resolution classification:
  - COMPLETED
  - INCOMPLETE
  - BLOCKED
  - UNRESOLVED
  - SUPERSEDED
  - FAILED
- an end-to-end governance loop
- conformance tests for Resolution, invariants, planner dependencies, recovery, cost, risk, and tie-breaking

## Planner semantics

Each Transform has:

```text
effective_cost = base_cost + risk_penalty
```

A path has:

```text
path_cost = sum(effective_cost(T_i))
```

`plan_path()` searches admissible dependency/recovery paths that reduce semantic Intent-State delta. A path may contain intermediate Transforms that do not directly satisfy Intent when those steps unlock a dependency or precondition required by a later advancing Transform.

Candidate success paths are ordered deterministically by:

1. lowest total effective path cost;
2. greatest semantic-delta reduction;
3. fewest Transforms;
4. lexicographically smallest Transform-ID path.

This means a longer low-cost safe path may outrank a shorter expensive or high-risk path.

Costs and risk penalties must be non-negative. The default Transform has:

```text
base_cost = 1.0
risk_penalty = 0.0
```

If no admissible path can reduce delta within the configured search depth, the current Resolution becomes `BLOCKED`.

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
