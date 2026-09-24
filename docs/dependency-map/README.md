# Calculus Dependency Map

This workspace reconstructs calculus by actual conceptual dependency rather than inherited course numbering.

## Method

For representative university Calculus I, Calculus II, Calculus III / Multivariable Calculus, and Differential Equations curricula:

1. record each mathematical topic;
2. identify the concepts actually required to understand or execute it;
3. distinguish hard prerequisites from pedagogical conventions;
4. construct prerequisite edges;
5. remove course labels from the graph;
6. examine valid topological orderings;
7. compare those orderings with conventional curricula.

## Edge meaning

```text
A -> B
```

means B genuinely depends on A. It should not mean merely that A is traditionally taught first.

## Initial concept families

The first mapping pass should include:

- functions and relations
- limits and continuity
- rates of change
- derivatives
- accumulation
- definite and indefinite integration
- Fundamental Theorem of Calculus
- sequences and series
- parametric representation
- polar representation
- vectors and vector-valued functions
- partial derivatives
- multiple integration
- vector fields
- ordinary differential equations
- systems of differential equations
- qualitative / phase behavior

This list is a starting inventory, not an asserted ordering.

## Evidence discipline

For each proposed dependency, record why it is required. Course placement alone is not evidence of mathematical necessity.

## Core 0.1 machine-readable companion

The current Core 0.1 teaching-order evidence is represented in one machine-readable companion:

- [`CORE_0.1_DEPENDENCY_INVENTORY.json`](CORE_0.1_DEPENDENCY_INVENTORY.json) — classified concept-level nodes and edges;
- [`CORE_0.1_DEPENDENCY_INVENTORY.schema.json`](CORE_0.1_DEPENDENCY_INVENTORY.schema.json) — structural schema;
- [`generated/CORE_0.1_DERIVED_TEACHING_ORDER.md`](generated/CORE_0.1_DERIVED_TEACHING_ORDER.md) — generated topological projection.

The JSON companion is the source for the generated teaching layers. The narrative research document remains the source context for the classifications and rationales. Generated Markdown must not be edited independently.

The companion is provisional contributor evidence. It does not set E1, E2, or E3 to PASS.
