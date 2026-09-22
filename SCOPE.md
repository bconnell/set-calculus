# Set Calculus v0.1 Scope

## Objective

Establish the smallest rigorous foundation needed to develop Set Calculus as an executable transformation system, a provenance-preserving mathematical corpus for human and model use, and a student-centered reconstruction of calculus around dependency, state, relationship, and resolution.

## v0.1 research questions

1. What concepts are genuinely prerequisite to differentiation, integration, differential equations, and multivariable operations?
2. Which parts of the conventional Calc I -> Calc II -> Calc III -> Differential Equations sequence reflect mathematical dependency, and which reflect historical or pedagogical packaging?
3. Can ordinary calculus operations be represented as transformations over explicitly defined states and sets without changing valid conventional results?
4. What information can be retained in an unresolved state that conventional representations tend to collapse or postpone?
5. What is the minimal vocabulary required to distinguish input properties, transform properties, and resolved-output properties?

## Core implementation scope

v0.1 includes:

- Set
- Member
- Relationship
- Transform
- State
- Resolution
- Provenance / Trace
- deterministic transform application
- explicit unresolved states
- reversible validation where the transform permits it
- closure and logical-failure states
- conformance fixtures

## Curriculum research scope

Collect representative topic sequences from university courses covering Calculus I, II, III / multivariable calculus, and Differential Equations.

For each mathematical concept, record its actual prerequisites rather than assuming its course placement is necessary.

Construct a directed acyclic graph where practical:

```text
concept A -> concept B
```

means that understanding or executing B genuinely requires A.

Then topologically examine the graph without Calc I / II / III labels and compare the emergent order with conventional curricula.

## Compatibility requirement

Set Calculus should be backward-compatible with ordinary calculus wherever ordinary calculus is valid.

When identifying a problem, classify it before proposing a correction:

- mathematical defect
- representational defect
- pedagogical defect
- historical artifact

Reorganization alone is not evidence that conventional mathematics is incorrect.

## Out of scope for v0.1

- replacing all conventional mathematical notation
- claiming conventional calculus is invalid as a whole
- a complete theorem prover
- every downstream application of Set Calculus
- probabilistic inference hidden behind deterministic terminology
- coupling the formal system to a particular LLM

## v0.1 exit criteria

v0.1 is ready to advance when the repository contains:

1. a canonical primitive vocabulary;
2. an initial formal transform/resolution model;
3. executable or machine-testable canonical examples;
4. a first conventional-calculus dependency graph;
5. a proposed dependency-derived teaching sequence;
6. at least one conventional-calculus example represented in Set Calculus and mapped back without changing its valid result;
7. provenance retained through the example end to end.
