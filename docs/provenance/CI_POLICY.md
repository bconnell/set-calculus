# Provenance CI Policy

Provenance CI is advisory only.

Its purpose is to detect when generated provenance views differ from the machine-readable provenance graph and make that difference visible to maintainers.

## Policy

- CI may regenerate provenance views in its temporary workspace for comparison.
- CI may report or warn about drift.
- CI must not auto-commit, push, merge, or otherwise write provenance changes back to the repository.
- AI or automation may propose provenance updates, but does not hold authority to accept them.
- Changes to `SOURCE_CATALOG.json`, generated provenance views, mappings, interpretation levels, calibration status, or source records require human review and approval.
- A human maintainer decides whether drift represents:
  - an intended catalog change;
  - an outdated generated view;
  - an incorrect source mapping;
  - an unresolved provenance question;
  - or no action at all.
- Unresolved provenance should remain unresolved rather than being automatically normalized or filled in.

## Authority boundary

```text
automation
  -> detect
  -> compare
  -> report
  -> propose

human maintainer
  -> review
  -> approve / reject / defer
  -> commit
```

The provenance system is designed to preserve history and uncertainty, not to transfer editorial or mathematical authority to CI or AI tooling.

## Maintainer approval checklist

Before committing a provenance update:

- [ ] Review the proposed source, passage, object, mapping, or audit changes.
- [ ] Regenerate the provenance views with `python scripts/generate_provenance_views.py`.
- [ ] Inspect the resulting diff, including generated Markdown and any catalog/schema changes.
- [ ] Confirm that interpretation level, mapping role, calibration status, and source locations are correct.
- [ ] Resolve or explicitly leave unresolved any provenance uncertainty; do not fill gaps automatically.
- [ ] Record explicit human approval before commit.
- [ ] Commit only the changes that the maintainer has approved.

## Submitted and captured data preservation

AI and automation have a preservation duty over all submitted or captured material, regardless of whether it originated with a human, an AI system, a tool, or a human-directed AI workflow.

The default rule is:

```text
submitted or captured data
  -> preserve

human-authored data
AI-authored data
human-directed AI output
tool-generated records
automation-generated records
  -> all preserved under the same rule

AI / automation
  -> may add
  -> may annotate
  -> may classify
  -> may propose correction
  -> may propose redaction or reduction
  -> must not delete preserved data

human maintainer
  -> may authorize removal
```

Only a human maintainer may authorize permanent removal of preserved data from the provenance corpus. Origin does not change the preservation duty.

AI must not silently:

- delete;
- overwrite with a reduced version;
- redact in place;
- summarize away source detail;
- collapse contradictory submissions or generated records;
- replace original material with a normalized interpretation;
- remove provenance because a later representation appears cleaner or more complete.

Preservation applies to source records, passages, mappings, annotations, submitted files, human-authored corrections, AI-authored outputs, human-directed AI outputs, tool-generated records, automation-generated records, dissenting records, superseded material, and unresolved attribution.

A transformed or improved representation may coexist with the original, but it does not replace the original unless a human explicitly approves that replacement. AI provenance must remain distinguishable from human provenance, but both are retained.

## Segregation of redacted or reduced representations

If AI or automation produces, proposes, or encounters a representation that redacts, reduces, compresses, omits, masks, or otherwise contains less information than the preserved whole, the reduced representation must be segregated from the canonical preserved source.

Use:

```text
docs/provenance/segregated/
```

for provenance records describing such reductions.

The segregation record must identify:

```text
original source or record
reduced / redacted representation
type of reduction
reason for reduction
who or what proposed the reduction
whether the reduction was human-requested
date / version when known
information categories affected
whether the original remains preserved
human approval status
```

The segregation area is a record of transformation, not a deletion queue.

A segregated record must never be interpreted as authorization to remove the original.

## Reduction trace requirement

Any AI-produced redaction or reduction should be representable as:

```text
original whole
  -> reduction operation
  -> reduced representation
```

with the operation and reason recorded.

Examples of reduction types include:

```text
REDACTION
OMISSION
SUMMARY
COMPRESSION
NORMALIZATION
DEDUPLICATION_PROPOSAL
PRIVACY_MASKING
SENSITIVITY_MASKING
SCOPE_REDUCTION
OTHER
```

When the reason is unknown, record:

```text
reason = UNKNOWN
```

rather than inventing one.

## Human removal authority

Permanent removal is a distinct human-authorized operation.

```text
AI may recommend removal
AI may segregate a reduced representation
AI may flag sensitive or duplicative material

AI must not authorize permanent deletion of human-authored, AI-authored, tool-generated, or automation-generated preserved records

human approval
  -> required before removal
```

If a human approves removal, the provenance record should retain, when appropriate and safe:

- that a removal occurred;
- what record or source was affected;
- the human authorization boundary;
- the stated reason;
- the date or version of removal.

This does not require preserving content that a human has explicitly ordered to be deleted when retaining that content would defeat the deletion itself.

