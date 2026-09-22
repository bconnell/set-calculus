# Segregated Provenance Records

This directory records provenance for representations that contain less information than the preserved whole.

Examples include:

- redactions;
- omissions;
- summaries;
- compression;
- normalization;
- privacy or sensitivity masking;
- scope reduction;
- proposed deduplication.

The original preserved material remains retained unless a human maintainer explicitly authorizes removal. This applies equally to human-authored material, AI-authored output, human-directed AI output, tool-generated records, and automation-generated records.

Each segregation record should identify:

```text
original source or record
reduced / redacted representation
reduction type
reason
proposer
human-requested or human-directed: yes / no / unknown
date / version
information affected
original preserved: yes / no
human approval status
```

This directory records reduction transforms. It is not a deletion queue and does not authorize removal of source material.
