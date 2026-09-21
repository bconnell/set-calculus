# IASTER Operational Kernel

IASTER is the execution kernel for Intent-Driven Generative Math.

```text
Intent
  -> Authority
  -> State
  -> Transform
  -> Evidence
  -> Resolution
```

## 1. Intent

Defines the desired outcome and active requirement boundary.

Question:

```text
What should become true?
```

## 2. Authority

Defines who or what may perform which Transform over which object, scope, and time boundary.

A useful shape is:

```text
Authority {
  actor
  object
  operation
  scope
  source
  lifetime
}
```

Authorization is operation-specific. Read authority does not imply delete authority. Local modification authority does not imply publication authority.

## 3. State

Current inspectable reality.

```text
State_t != State_(t+1)
```

unless established otherwise.

Current observed State outranks remembered State for execution.

## 4. Transform

```text
T : S_t -> S_(t+1)
```

A Transform is admissible when it is:

```text
authorized
in scope
constraint-safe
invariant-preserving
```

The preferred Transform is the smallest coherent operation that reduces the unresolved Intent-State delta or increases the reliable knowledge required to do so.

## 5. Evidence

Evidence is claim-relative proof.

```text
E |- q
```

means Evidence E is sufficient to establish proposition q.

Proof does not automatically generalize:

```text
BuildPass      !-> RuntimeCorrect
Screenshot     !-> SemanticCorrect
SingleSuccess  !-> LifecycleReliable
```

Evidence must preserve subject identity, provenance, freshness, and proof type.

## 6. Resolution

Resolution classifies the current generative condition:

```text
COMPLETED
INCOMPLETE
BLOCKED
UNRESOLVED
SUPERSEDED
FAILED
```

## Planning loop

```text
Intent + Authority + Current State
  -> unresolved semantic delta
  -> candidate Transforms
  -> admissibility filter
  -> selected Transform path
```

## Validation loop

```text
Transform
  -> New State
  -> Evidence
  -> Resolution
```

If the Resolution is nonterminal, the loop continues.

## Canonical execution rule

Given:

```text
<I, A, S, E>
```

select Transform T such that T is authorized, in scope, and invariant-preserving, and T either:

1. reduces the unresolved Intent-State delta;
2. increases reliable knowledge required to reduce it;
3. resolves authority;
4. repairs evidence; or
5. restores recoverability.

Then:

```text
S_(t+1) = T(S_t)
E_(t+1) = Observe(S_(t+1))
R_(t+1) = Resolve(I,A,S_(t+1),E_(t+1))
```
