# Temporal Reconciliation

## Curation Principle

A reconciliation is valid within the conditions under which it was resolved.

As those conditions change, the reconciliation may need to be tested again.

```text
resolved math at t1
+
changed state / assumptions / evidence at t2
        ↓
re-evaluation
        ↓
still reconciles
or
requires revision
or
returns to unresolved
```

The fact that a derivation reconciled yesterday is evidence of its prior validity, not a guarantee that it still reconciles today.

Set Calculus curation should therefore preserve:

- the mathematical result;
- the assumptions under which it resolved;
- the state of relevant definitions and dependencies;
- the provenance of the derivation;
- the time or version of resolution where meaningful;
- and the ability to re-run or re-check the reasoning later.

A resolved state may remain resolved, become superseded, require recalculation, or return to an unresolved state when its supporting conditions change.

The curator should therefore recheck important mathematics when the state of the corpus, its assumptions, evidence, dependencies, or definitions materially changes.

> Mathematics should not merely be preserved as resolved. It should remain capable of being reconciled again.

## Distinction

```text
historically resolved
!=
currently reconciled
```

The historical result remains part of provenance even when the current corpus no longer supports the same reconciliation.

## Curation implication

Set Calculus curation should preserve enough of each resolved state to allow later reconciliation rather than treating resolution as permanent closure.

```text
preserved prior resolution
        +
current corpus state
        ↓
reconciliation check
        ↓
confirmed
revised
superseded
or unresolved
```

This principle treats mathematical resolution as traceable through time rather than detached from the conditions that produced it.
