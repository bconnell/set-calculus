# Conventional Calculus Compatibility

This workspace records how conventional calculus concepts map into Set Calculus.

## Rule

Set Calculus should preserve valid conventional results. A new representation is not, by itself, evidence that the old mathematics was wrong.

When a problem is identified, classify it as one or more of:

- mathematical defect
- representational defect
- pedagogical defect
- historical artifact

## Compatibility record

Each mapped example should eventually record:

```text
conventional statement
-> conventional operation/result
-> Set Calculus representation
-> Set Calculus transform/resolution
-> mapped conventional result
-> equivalence / difference
-> provenance
```

The first examples should be deliberately small: derivative as change relation, integral as accumulation/recovery, and a simple first-order differential equation as a relationship between change and state.

## D1 derivative readiness

The required D1 example path now exists at [`examples/derivative/`](examples/derivative/).

Its conventional baseline is complete and executable:

```text
f(x)=x^2
-> f'(x)=2x
```

The Set Calculus half is intentionally marked blocked because the current repository does not yet define a canonical derivative representation or derivative transform/resolution rule.

That block is part of the evidence. It prevents a compatibility record from presenting invented notation or a placeholder transform as D1 validation.

See:

- [`examples/derivative/README.md`](examples/derivative/README.md)
- [`examples/derivative/record.json`](examples/derivative/record.json)
- [`COMPATIBILITY_RECORD.schema.json`](COMPATIBILITY_RECORD.schema.json)

This readiness artifact does not mark D1 PASS.
