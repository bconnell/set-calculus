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

## Core 0.1 E1 coverage evidence

The repository's stated first mapping pass is tracked in [`CORE_0.1_E1_COVERAGE.json`](CORE_0.1_E1_COVERAGE.json), with a generated review view at [`generated/CORE_0.1_E1_COVERAGE.md`](generated/CORE_0.1_E1_COVERAGE.md).

That mapping is deliberately narrower than E1 itself: it verifies representation of the README's starting concept-family list, but it does not assert that the list is exhaustive enough for E1 PASS.

## Core 0.1 machine-readable companion

The current Core 0.1 dependency and teaching-order evidence is represented by:

- [`CORE_0.1_DEPENDENCY_INVENTORY.json`](CORE_0.1_DEPENDENCY_INVENTORY.json) — classified concept-level nodes and edges;
- [`CORE_0.1_DEPENDENCY_INVENTORY.schema.json`](CORE_0.1_DEPENDENCY_INVENTORY.schema.json) — structural schema;
- [`generated/CORE_0.1_DERIVED_TEACHING_ORDER.md`](generated/CORE_0.1_DERIVED_TEACHING_ORDER.md) — generated topological projection;
- [`CORE_0.1_E3_TEACHING_HYPOTHESIS.json`](CORE_0.1_E3_TEACHING_HYPOTHESIS.json) — staged teaching hypothesis derived from the graph;
- [`CORE_0.1_E3_TEACHING_HYPOTHESIS.schema.json`](CORE_0.1_E3_TEACHING_HYPOTHESIS.schema.json) — structural schema for the E3 hypothesis;
- [`generated/CORE_0.1_E3_TEACHING_HYPOTHESIS.md`](generated/CORE_0.1_E3_TEACHING_HYPOTHESIS.md) — generated human-review view of the staged hypothesis.

The dependency inventory is the source for the generated topological layers. The E3 hypothesis must match those layers exactly: stage precedence is dependency-derived, while order among concepts inside one stage remains explicitly non-forced.

The narrative research document remains the source context for classifications and rationales. Generated Markdown must not be edited independently.

These artifacts are provisional contributor evidence. They do not set E1, E2, or E3 to PASS.
