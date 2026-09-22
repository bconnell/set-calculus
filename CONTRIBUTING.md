# Contributing to Set Calculus

Set Calculus is a living mathematical knowledge base, executable transformation system, model-training corpus, and educational foundation. Contributions should strengthen the project without erasing provenance, hiding uncertainty, or creating competing sources of truth.

## Before you start

Read the repository guidance that governs the area you plan to change:

- `README.md` for project purpose and mathematical direction.
- `SCOPE.md` for Core 0.1 scope, compatibility expectations, and defect classification.
- `PLAN.md` for execution, testing, and near-term implementation direction.
- `PROVENANCE.md` for provenance principles.
- `CORE_0.1_COMPLETENESS_CHECKLIST.md` for current release gates and ownership boundaries.
- `LICENSE_REQUIREMENTS.md` before proposing licensing changes.

For provenance work, also read:

- `docs/provenance/README.md`
- `docs/provenance/CI_POLICY.md`

For the Generative Governance Engine, read the governing IDGM specifications under `docs/intent-driven-generative-math/` before changing executable behavior.

## Keep contributions focused

Prefer one semantic purpose per pull request.

Before proposing a correction to existing mathematical material, use the classification required by `SCOPE.md`:

1. mathematical defect;
2. representational defect;
3. pedagogical defect; or
4. historical artifact.

Reorganization alone is not evidence that conventional mathematics is wrong.

Avoid unrelated formatting, renaming, cleanup, or restructuring in a contribution whose purpose is different.

## State mathematical claims clearly

Make the role and evidence status of a mathematical statement clear. Depending on the contribution, this may mean identifying a statement as a definition, explicit assumption or axiom, derived result, conjecture, computational observation, interpretation, compatibility mapping, or unresolved question.

For derived claims, make the dependencies and assumptions traceable.

For computational work, report what was computed and under which assumptions. A passing computation is evidence for the observed case; it is not automatically a proof of an unrestricted theorem.

When compatibility with conventional mathematics is claimed, preserve the assumptions and show the mapping clearly enough that the result can be checked independently.

Record counterexamples, failed mappings, and unresolved cases when they materially inform the result.

## Executable changes

The project direction in `PLAN.md` is tests first and deterministic execution with enough trace to reconstruct why a result occurred.

Executable contributions should therefore:

- add or update tests for changed behavior;
- preserve deterministic behavior where determinism is claimed;
- preserve explicit resolution states instead of hiding uncertainty;
- preserve useful trace information;
- keep runtime and specification claims aligned.

For the Generative Governance Engine, the formal IDGM specifications govern the reference implementation. If code and specification disagree, identify the disagreement explicitly rather than silently choosing one as correct.

Passing tests establish only what those tests exercise. They do not replace mathematical review or maintainer authority.

## Provenance

Follow the repository principle:

> Preserve provenance without manufacturing provenance.

Keep originating material, later transformations, independent contributions, generated or derived material, validation, correction, and unresolved attribution distinguishable when those distinctions matter.

For the current provenance system:

- `docs/provenance/SOURCE_CATALOG.json` is the canonical source catalog;
- generated provenance Markdown views are derived artifacts;
- generated views should be regenerated from their canonical source rather than edited directly;
- unresolved attribution should remain unresolved until evidence supports a stronger claim;
- provenance CI is advisory;
- final provenance acceptance requires human review.

Do not remove preserved provenance merely because material has been transformed or reorganized.

## Ownership and authority

Before changing a Core 0.1 area with an explicit owner, review the current ownership table in `CORE_0.1_COMPLETENESS_CHECKLIST.md`.

A technically correct implementation, passing test suite, generated artifact, or proof attempt does not by itself transfer repository authority or release authority.

When a proposed change crosses an owned boundary, present it as a reviewable proposal and preserve the existing authority relationship until the responsible maintainer accepts it.

## Generated artifacts

Identify the source of truth before editing generated material.

If a file is produced from a canonical machine-readable source, change the canonical source and run the generator. Do not create a second competing authority by hand-editing the generated view.

Where generation is intended to be deterministic, a second generation pass should not create additional changes.

## Licensing

Do not casually modify the repository license.

`LICENSE_REQUIREMENTS.md` states that the existing `LICENSE` remains untouched while the intended final licensing model is still being formalized and reviewed. Licensing proposals should be handled separately from ordinary mathematical, documentation, or implementation changes.

## Pull request evidence

A focused pull request should make review easier by stating:

- purpose;
- scope;
- non-goals when useful;
- affected files or mathematical objects;
- relevant authority or provenance impact;
- validation commands and observed results;
- known limitations;
- unresolved questions that remain.

For executable work, include enough information for another contributor to reproduce the validation.

For mathematical work, include enough information to trace assumptions, dependencies, derivation, and the evidence class being claimed.

## AI-assisted and generated work

AI systems may assist with research, transformation, implementation, testing, or drafting, but generated output is not self-validating.

When AI materially transforms source material, preserve the originating source and relevant transformation lineage. Do not replace a known human or source provenance record with a model-generated attribution.

Review generated mathematical claims and executable changes against the same evidence standards as human-authored material.

## Review and unresolved work

Maintainers decide what becomes part of the shared upstream project.

A rejected or unresolved contribution may still contain useful evidence, counterexamples, failed derivations, or research history. Preserve useful findings rather than rewriting history to make an earlier attempt appear successful.

If a question cannot yet be resolved from valid evidence, leave it explicitly unresolved.
