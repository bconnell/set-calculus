# D1 Derivative Compatibility Readiness

**Status:** blocked pending a canonical Set Calculus derivative mapping  
**Gate claim:** not asserted  
**Owner of D1 pass/fail:** Chad Coulter

## Required example

The Core 0.1 checklist requires the minimum conventional example:

```text
f(x)=x^2
-> f'(x)=2x
```

The conventional result is valid.

Using the ordinary limit definition,

```text
f'(x)
= lim_(h->0) [((x+h)^2 - x^2) / h]
= lim_(h->0) [2x + h]
= 2x
```

## Compatibility record

The required D1 record currently resolves as:

```text
conventional statement
  f(x)=x^2

-> conventional result
  f'(x)=2x

-> Set Calculus representation
  BLOCKED: no canonical derivative representation is defined in the current repository

-> Set Calculus transforms/resolution
  BLOCKED: no canonical derivative transform/resolution semantics are defined in the current repository

-> mapped conventional result
  UNDETERMINED

-> provenance
  CORE_0.1_COMPLETENESS_CHECKLIST.md
  docs/conventional-calculus/README.md
```

The machine-readable record is in `record.json`.

## Why this is blocked

The repository requires a derivative round trip, but the current Core material does not define a canonical derivative operator, a difference-quotient representation, or a Set Calculus transform that resolves a derivative.

Creating one only to make this example pass would confuse proposed mathematics with accepted project semantics.

This artifact therefore preserves the valid conventional baseline and makes the missing Set Calculus side explicit.

## What would unblock the candidate round trip

A future candidate can populate the currently null Set Calculus fields only after a reviewable derivative representation and transform/resolution rule exists.

At that point the compatibility validator can require:

```text
mapped conventional result == f'(x)=2x
```

and can reject any unexplained difference.

That executable equality would still be evidence for Chad to review; it would not cause this contributor artifact to mark D1 PASS on its own.

## Validation

From the repository root:

```bash
python scripts/audit_core_d1_derivative_readiness.py
python scripts/audit_core_d1_derivative_readiness.py --self-test
```
