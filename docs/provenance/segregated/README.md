# Segregated Provenance Records

This directory records provenance for representations that contain less information than the preserved human-submitted whole.

Examples include:

- redactions;
- omissions;
- summaries;
- compression;
- normalization;
- privacy or sensitivity masking;
- scope reduction;
- proposed deduplication.

The original human-submitted material remains canonical and preserved unless a human maintainer explicitly authorizes removal.

Each segregation record should identify:

```text
original source or record
reduced / redacted representation
reduction type
reason
proposer
human-requested: yes / no / unknown
date / version
information affected
original preserved: yes / no
human approval status
```

This directory records reduction transforms. It is not a deletion queue and does not authorize removal of source material.
