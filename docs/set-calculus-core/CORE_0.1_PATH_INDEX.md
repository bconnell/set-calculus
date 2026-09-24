# Core 0.1 Canonical Path Index

## Purpose

This file is the repository navigation index for Core 0.1.

It records where a reviewer or independent implementer should look for the current Core specification, release gate, conformance work, conventional-calculus compatibility work, dependency material, and provenance model.

This index does not mark any release gate as passed. `CORE_0.1_COMPLETENESS_CHECKLIST.md` remains the canonical pass/fail authority.

## Status vocabulary

- `PRESENT` — the referenced repository path exists at this revision.
- `MISSING_REQUIRED` — the Core 0.1 checklist requires the artifact, but the referenced path does not yet exist.

A missing required artifact remains missing. The index must not substitute a nearby document or infer completion.

## Canonical path table

| Category | Status | Repository path | Release-gate relation |
|---|---|---|---|
| Core release gate | PRESENT | `CORE_0.1_COMPLETENESS_CHECKLIST.md` | Governing Core 0.1 pass/fail checklist |
| Machine-readable release gate | PRESENT | `CORE_0.1_COMPLETENESS_CHECKLIST.yaml` | Machine-readable companion to the release gate |
| Release-gate schema | PRESENT | `CORE_0.1_COMPLETENESS_CHECKLIST.schema.json` | Validation schema for the machine-readable checklist |
| Core terminology | PRESENT | `docs/philosophy-of-set-calculus/CANONICAL_TERMINOLOGY_LEDGER.md` | A1 terminology reference |
| Active Core formalization | PRESENT | `docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md` | Active Core formal development referenced by A2-A9 |
| Core entry point | PRESENT | `docs/set-calculus-core/README.md` | Core directory entry point required by G2 |
| Provenance policy | PRESENT | `PROVENANCE.md` | F1 repository provenance policy |
| Machine-readable provenance guide | PRESENT | `docs/provenance/README.md` | Entry point for machine-readable provenance |
| Machine-readable provenance catalog | PRESENT | `docs/provenance/SOURCE_CATALOG.json` | F2 source/passage/object/mapping catalog |
| Provenance schema | PRESENT | `docs/provenance/PROVENANCE_SCHEMA.json` | F2 schema for provenance records |
| Conventional dependency graph | PRESENT | `docs/dependency-map/001-conventional-calculus-prerequisite-graph.md` | E1-E3 dependency work |
| Conventional compatibility workspace | PRESENT | `docs/conventional-calculus/README.md` | D1-D4 compatibility workspace and record shape |
| GGE executable specialization | PRESENT | `generative-governance-engine/README.md` | Executable IDGM/GGE work; not a substitute for Core B/C evidence |
| Canonical conformance fixtures | MISSING_REQUIRED | `tests/conformance/` | C1 required artifact path |
| Derivative round trip | MISSING_REQUIRED | `docs/conventional-calculus/examples/derivative/` | D1 required artifact path |
| Definite-integral round trip | MISSING_REQUIRED | `docs/conventional-calculus/examples/integral/` | D2 required artifact path |
| First-order ODE round trip | MISSING_REQUIRED | `docs/conventional-calculus/examples/ode-first-order/` | D3 required artifact path |
| Compatibility report | MISSING_REQUIRED | `docs/conventional-calculus/COMPATIBILITY_REPORT.md` | D4 required artifact |
| End-to-end provenance round trip | MISSING_REQUIRED | `docs/conventional-calculus/examples/provenance-round-trip/` | Candidate location for F3 evidence; maintainer approval required before treating this path as canonical |

## Reading order

For Core 0.1 review:

1. Read `CORE_0.1_COMPLETENESS_CHECKLIST.md` for required gates, ownership, evidence, and current blockers.
2. Read `docs/philosophy-of-set-calculus/CANONICAL_TERMINOLOGY_LEDGER.md` for canonical naming.
3. Read `docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md` for the active Core formalization currently referenced by the checklist.
4. Read `PROVENANCE.md` and `docs/provenance/README.md` before making provenance claims or edits.
5. Use `docs/conventional-calculus/README.md` and the dependency graph for the compatibility/curriculum track.
6. Treat every `MISSING_REQUIRED` row as open release work, not as an implied or partially satisfied artifact.

## Integrity rule

The path-index verifier checks that:

- every `PRESENT` path exists;
- every `MISSING_REQUIRED` path is still absent, forcing the index to be updated when the artifact appears;
- required G2 navigation categories remain represented;
- `README.md`, `SCOPE.md`, and `docs/set-calculus-core/README.md` link back to this index.

Run:

```bash
python scripts/audit_core_g2_path_index.py
```

The verifier establishes path-index consistency only. It does not establish G2 PASS or any child release gate.
