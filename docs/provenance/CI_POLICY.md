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

