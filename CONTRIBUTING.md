# Contributing to Set Calculus

Set Calculus is a collaborative mathematical and executable knowledge project. Contributions should preserve the repository's existing authority, provenance, evidence, and compatibility boundaries.

This file is contribution guidance. It does not replace the canonical mathematical specifications, release checklist, provenance policy, or license requirements.

## 1. Start from current repository state

Before beginning a contribution:

1. compare against current upstream `main`;
2. read the governing files for the area being changed;
3. identify the canonical source of truth;
4. identify any named ownership or approval boundary;
5. confirm that the proposed work is not already present.

Current repository state outranks remembered or previously summarized state.

## 2. Recommended contribution flow

Unless a maintainer directs otherwise:

1. work in a fork;
2. create a branch for one bounded semantic purpose;
3. validate the exact branch candidate;
4. open an upstream pull request;
5. keep unrelated cleanup out of the contribution.

A passing fork branch is proposed work until upstream maintainers accept it.

## 3. Respect repository authority

The active Core release ownership and evidence requirements are defined in:

- `CORE_0.1_COMPLETENESS_CHECKLIST.md`

Contributors should not treat passing tests, successful experiments, or a completed derivation as permission to redefine an owned canonical artifact.

Changes to canonical Core definitions, release semantics, reference implementation behavior, conformance requirements, provenance policy, or licensing should follow the applicable maintainer review boundary.

## 4. Preserve the distinction between evidence types

Different evidence establishes different things.

Examples:

```text
passing executable test
  != proof of a general theorem

computational experiment
  != unrestricted mathematical proof

generated provenance view
  != independent provenance authority

documentation statement
  != executable behavior

successful implementation
  != upstream acceptance
```

A contribution should state what its evidence supports and what remains unresolved.

## 5. Classify mathematical changes

When practical, identify whether a mathematical contribution is primarily a:

- definition;
- axiom or explicit assumption;
- derived law;
- lemma or theorem;
- conjecture or hypothesis;
- compatibility mapping;
- computational observation;
- counterexample;
- unresolved research question.

Do not strengthen a claim's status without the evidence required for the stronger status.

## 6. Conventional mathematics compatibility

The project requires compatibility with conventional mathematics wherever conventional mathematics is valid.

When proposing a correction or incompatibility, first classify the issue using the repository's existing categories:

- mathematical defect;
- representational defect;
- pedagogical defect;
- historical artifact.

Reorganization alone is not evidence that conventional mathematics is incorrect.

## 7. Tests and executable evidence

Executable contributions should include focused validation appropriate to the change.

Prefer:

- small canonical fixtures;
- deterministic behavior;
- explicit expected resolution;
- expected trace or provenance where relevant;
- negative and boundary cases;
- regression tests for discovered defects.

Tests are executable evidence. They should not silently become the sole authority for formal mathematics.

## 8. Provenance rules

The repository provenance policy is governed by:

- `PROVENANCE.md`
- `docs/provenance/README.md`
- `docs/provenance/CI_POLICY.md`

Follow these rules:

- preserve provenance without manufacturing provenance;
- unresolved attribution remains unresolved;
- do not collapse human, AI, tool, automation, implementation, or historical provenance into one attribution;
- do not silently delete, overwrite, normalize away, or summarize away preserved provenance material;
- AI or automation may detect, compare, report, and propose provenance changes, but human review controls acceptance.

### Machine-readable provenance

`docs/provenance/SOURCE_CATALOG.json` is the source of truth for the generated provenance views.

Do not edit the generated views independently:

```text
docs/provenance/generated/SOURCE_LEDGER.md
docs/provenance/generated/PROVENANCE_MATRIX.md
docs/provenance/generated/REVERSE_SOURCE_INDEX.md
docs/provenance/generated/COVERAGE_AUDIT.md
```

After an approved source-catalog change, regenerate with:

```cmd
python scripts/generate_provenance_views.py
```

Then inspect the resulting diff.

## 9. Generated and derived artifacts

Before editing a generated or derived file, find its canonical input and generator.

Prefer:

```text
canonical source
  -> generator
  -> derived artifact
```

over independent edits to the derived artifact.

If the generation process is expected to be deterministic, repeated generation from unchanged canonical input should not create additional drift.

## 10. Preserve submitted and captured material

The provenance CI policy gives AI and automation a preservation duty over submitted or captured provenance material.

Do not permanently remove preserved provenance data without the applicable human maintainer authority.

A corrected, reduced, normalized, or transformed representation may coexist with the original. It does not silently replace the original.

## 11. Keep specializations separate from Core

Specializations should not silently redefine the general Set Calculus layer.

For example:

```text
Set Calculus
  -> general structure / relationship / state / transform / resolution / provenance

Intent-Driven Generative Math
  -> specialization
  -> adds Intent / Authority / Evidence
```

When a specialization needs different semantics, identify the specialization boundary explicitly.

## 12. Determinism and unresolved states

Do not hide unresolved states behind probabilistic output while describing the result as deterministic.

For deterministic components, the same normalized inputs and governing rules should reproduce the same result and enough trace to explain it.

`UNRESOLVED`, `BLOCKED`, `FAILED`, and other explicit resolution states should remain distinct rather than being collapsed for convenience.

## 13. Licensing boundary

The repository's current and intended licensing state is described in:

- `LICENSE`
- `LICENSE_REQUIREMENTS.md`

Do not alter licensing material as incidental cleanup.

The existing `LICENSE` remains in place while any replacement terms are designed and reviewed. The intended future instrument has legal requirements beyond ordinary open-source licensing and requires qualified legal review before release.

## 14. Pull request evidence

A substantive pull request should make it possible for a reviewer to answer:

```text
What changed?
Why did it change?
What is the governing source of truth?
What authority boundary is affected?
What evidence supports the change?
What was tested?
What remains unresolved?
Does provenance change?
Does conventional compatibility change?
Does the Core 0.1 release gate change?
```

## 15. Uncertainty is acceptable

If a contribution uncovers a real question but cannot yet prove the answer, preserve the question and evidence.

Do not manufacture closure to make a contribution appear complete.
