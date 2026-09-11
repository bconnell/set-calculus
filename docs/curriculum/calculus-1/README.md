# Set Calculus I — Relational Hex

This directory is the course implementation for **Set Calculus I: Relational Hex**.

The existing `docs/curriculum/level-1/` material remains architecture and design provenance. This directory contains the teachable course specification and individual lesson sources.

## Course Structure

- `lesson-plan.md` — canonical working sequence for Lessons 1–30.
- `LESSON_TEMPLATE.md` — standard machine-readable front matter and lesson-body structure.
- `01-*.md` through `30-*.md` — individual lesson sources.

## Pedagogical Architecture

Identity Resolver and Monad Resolver operations are embedded throughout Lessons 1–27 before being formally named and generalized in Lessons 28 and 29. Lesson 30 performs a resolver retrospective across the course.

Every lesson distinguishes between:

- **Resolution** — what the student can now resolve.
- **Unresolved Potential** — valid reachable structure exposed but not collected by the current lesson.
- **Next Relationships** — curriculum paths deliberately selected for subsequent traversal.

The recurring lesson structure is:

```text
S_n → R_n + P_(n+1)
```

A lesson produces a useful resolution without claiming to exhaust the resulting possibility space.
