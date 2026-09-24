# Core 0.1 G1 Legacy Consistency Audit

**Audit base:** \`e2f343104d7b720693f12a483b9243deca6bbacb\`  
**Scope:** repository consistency evidence for \`CORE_0.1_COMPLETENESS_CHECKLIST.md\` gate G1  
**Status:** findings present; this document does not mark G1 as passed

## Purpose

G1 requires a repository-wide audit for active contradictions between legacy and current Set Calculus formalization. The required minimum search categories are:

- three-state admissibility as canonical;
- five-witness boundary model;
- \`IDENTITY\` inside a State relation;
- negative-exhaustion requirement;
- obsolete boundary aggregation;
- three-valued witness-validation return type.

This audit preserves the repository's authority boundary. It identifies evidence for maintainer review but does not decide canonical mathematics, rewrite provenance, or change the G1 checkbox.

## Current canonical correction anchors

The active trajectory formalization contains later corrective checkpoints that establish the current working direction:

- Section 24 separates Identity compatibility from State compatibility.
- Section 24 expands the boundary witness discriminator to six types: Identity, State, Context, Authority, Invariant, and Provenance.
- Section 25 makes PARTIAL a first-class resolution state and defines four-state validation/admissibility/entailment patterns.
- Section 26 labels the current boundary model as the "Six-Witness Four-State Boundary Model."
- Section 27 states that constructive positive closure does not require negative exhaustion and says the checkpoint supersedes the earlier assumption that positive closure requires it.

These later anchors are the basis for identifying earlier incompatible forms as legacy candidates. This is a consistency observation, not a claim that the audit has authority to promote or demote canonical rules.

## Confirmed review-required findings

All confirmed findings below occur in:

\`docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md\`

### 1. Earlier three-state admissibility remains active-looking

The early trajectory and boundary definitions use only:

\`ADMISSIBLE / INADMISSIBLE / UNRESOLVED\`

The early admissibility-composition table is likewise three-state.

Later Section 25 introduces four-valued admissibility with \`PARTIAL\`, and Section 26 identifies four-state resolution as the current model.

**Classification:** active contradiction candidate until the earlier form is explicitly harmonized or marked historical/superseded.

### 2. Three-valued entailment remains active-looking

Section 14.5 is titled "Three-valued entailment" and defines:

\`ENTAILS / DOES_NOT_ENTAIL / UNRESOLVED\`

Section 25 later defines the domain-specific entailment states as:

\`ENTAILS / PARTIALLY_ENTAILS / UNRESOLVED / DOES_NOT_ENTAIL\`

**Classification:** active contradiction candidate until Section 14.5 is marked historical/superseded or rewritten under maintainer review.

### 3. Five-witness common envelope remains active-looking

Section 21 states:

> All five witness types share a common outer form

and its discriminator contains State, Context, Authority, Invariant, and Provenance, but no Identity.

Section 24 later separates Identity from State and expands the discriminator to six witness types.

**Classification:** direct G1 five-witness finding.

### 4. Common witness status remains three-state

Section 21 gives the witness status set as:

\`VALID / INVALID / UNRESOLVED\`

Section 25 later defines witness validation as:

\`VALID / PARTIAL / UNRESOLVED / INVALID\`

**Classification:** active contradiction candidate.

### 5. Uniform witness validation returns only three states

Section 22 defines \`ValidateWitness(W)\` with only:

\`VALID / INVALID / UNRESOLVED\`

and later says the typed validator returns those same three values.

Section 25 makes \`PARTIAL\` first-class.

**Classification:** direct G1 three-valued witness-validation finding.

### 6. Identity is still handled inside the earlier State witness path

The earlier typed-payload dispatch says:

\`STATE -> identity / compatibility / authorized projection\`

Section 24 later states:

\`IdentityCompat != StateCompat\`

and gives Identity its own witness payload.

**Classification:** direct G1 Identity-inside-State finding.

### 7. Earlier aggregate boundary evidence contains five witnesses

Section 22.2 constructs \`E_B\` from:

- State
- Context
- Authority
- Invariant
- Provenance

and validates those five components.

Section 24 later expands the boundary evidence object to include Identity as a separate sixth component.

**Classification:** direct G1 obsolete-boundary-aggregation finding.

### 8. Earlier aggregate text still says "all five VALID"

The earlier aggregation rule uses "all five VALID" as the positive boundary condition.

The later six-witness checkpoint supersedes that dimensionality.

**Classification:** direct G1 five-witness/aggregation finding.

## Negative-exhaustion search

The targeted search found the later canonical text rejecting negative exhaustion and explicitly describing that assumption as superseded. No separate unmarked rule requiring negative exhaustion was confirmed in this audit pass.

This is not a proof that no such wording exists anywhere. The repository-wide script remains responsible for continuing to search for positive requirement forms.

## Conservative cleanup path

The least destructive correction is:

1. preserve the earlier derivation;
2. mark incompatible earlier blocks as historical/superseded;
3. point readers directly to Sections 24-27 for the current working model;
4. avoid silently deleting earlier development history;
5. rerun the repository-wide audit;
6. leave the formal G1 PASS decision to the named maintainer.

This approach follows the repository's non-erasure and human-authority rules while removing ambiguity for an independent implementer.

## Reproducible audit tool

Run:

\`\`\`bash
python scripts/audit_core_g1_consistency.py
\`\`\`

Structured output:

\`\`\`bash
python scripts/audit_core_g1_consistency.py --json
\`\`\`

Strict mode returns a nonzero exit code when unmarked review-required candidates remain:

\`\`\`bash
python scripts/audit_core_g1_consistency.py --strict
\`\`\`

The script intentionally classifies findings conservatively:

- \`REVIEW_REQUIRED\` — matched text is not locally marked as historical/superseded;
- \`MARKED_HISTORICAL\` — nearby text explicitly marks the material historical, legacy, obsolete, or superseded;
- \`CONTROL_REFERENCE\` — the match occurs in the checklist, this audit, or the audit script itself.

A clean strict run is evidence for review. It is not, by itself, authority to check G1 PASS.
