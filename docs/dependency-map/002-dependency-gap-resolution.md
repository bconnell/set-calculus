# Research 002: Dependency-Gap Resolution Evidence

**Status:** Provisional contributor evidence  
**Parent evidence branch:** `dependency-e2-machine-readable-inventory`  
**Release authority:** This document does not mark E1, E2, or E3 PASS. `CORE_0.1_COMPLETENESS_CHECKLIST.md` assigns those decisions to Chad Coulter.

## 1. Purpose

The first machine-readable dependency inventory exposed three source gaps:

1. no classified incoming prerequisite for Trigonometric series;
2. no explicit cross-branch integration prerequisite for line and surface integrals;
3. uncertainty about how those missing dependencies should move the combined Green / Stokes / Divergence theorem layer.

This pass uses authoritative MIT mathematics material to resolve only the relationships directly supported by that evidence.

The classifications below remain `WORKING_INFERENCE` in the inventory. The source material supplies the mathematical relationship; mapping it into this repository's current concept nodes is still a contributor inference subject to maintainer review.

## 2. Fourier / trigonometric-series gap

### 2.1 Infinite series -> Trigonometric series

MIT Calculus with Theory notes introduce a trigonometric series using an explicit infinite summation of sine and cosine terms, then identify the coefficient-selected form as the Fourier series of a function.

That supports the concept-level dependency:

```text
Infinite series
  -> Trigonometric series
```

**Provisional class:** `HARD`

Reason: within the current node vocabulary, the object called a trigonometric series is itself an infinite series with trigonometric terms. This resolves the former `UNRESOLVED_SOURCE_GAP` root status of `trigonometric_series`.

Source:

- MIT OpenCourseWare, *Calculus with Theory*, course notes, Fourier-series section: https://ocw.mit.edu/courses/18-014-calculus-with-theory-fall-2010/d5305fffd94bc1db8da13d6c9e2cce82_MIT18_014F10_course_notes.pdf

### 2.2 Definite integral -> Fourier methods

The same MIT notes define Fourier coefficients using definite-integral formulas over the interval. MIT differential-equations Fourier material likewise centers coefficient computation and orthogonality relations.

That supports the additional dependency:

```text
Definite integral
  -> Fourier methods
```

**Provisional class:** `HARD`

Reason: the current Fourier-methods node includes constructing Fourier expansions, and the coefficient formulas require definite integration. This complements rather than replaces the existing:

```text
Trigonometric series
  -> Fourier methods
```

Sources:

- MIT OpenCourseWare, *Calculus with Theory*, course notes: https://ocw.mit.edu/courses/18-014-calculus-with-theory-fall-2010/d5305fffd94bc1db8da13d6c9e2cce82_MIT18_014F10_course_notes.pdf
- MIT OpenCourseWare, *Differential Equations*, Fourier Series: Basics: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/fourier-series-basics/

## 3. Cross-branch integration gap

### 3.1 Definite integral -> Line integrals

MIT's multivariable-calculus final review explains that after a curve is parameterized, the line-integral calculation is expressed in one parameter and becomes an ordinary single-variable integral.

That supports:

```text
Definite integral
  -> Line integrals
```

**Provisional class:** `HARD`

Reason: parameterization changes the geometric domain, but evaluation still uses the ordinary definite-integral machinery represented by the existing node.

Source:

- MIT OpenCourseWare, *Multivariable Calculus*, final-review transcript: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/sr7kCpzAuYw_transcript.pdf

### 3.2 Multiple integrals -> Surface integrals

MIT multivariable-calculus material derives the integral over a parameterized surface as a double integral over the parameter domain.

That supports:

```text
Multiple integrals
  -> Surface integrals
```

**Provisional class:** `HARD`

Reason: the surface-integral construction is evaluated through two-parameter/double-integration machinery.

Sources:

- MIT OpenCourseWare / MIT calculus text, surface-integral derivation: https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter24/section01.html
- MIT OpenCourseWare, *Multivariable Calculus*, surface-integral material: https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/resources/surface_integrls/

## 4. Effect on the integral-theorem layer

MIT's Stokes material explicitly relates a line integral around a boundary curve to a surface integral over a spanning surface. MIT course sequencing likewise places line/surface integration before the corresponding integral theorems.

The inventory already contained:

```text
Line integrals
  -> Green / Stokes / Divergence theorems

Surface integrals
  -> Green / Stokes / Divergence theorems
```

With Sections 3.1 and 3.2 resolved, the generated topological order now carries integration machinery into that theorem layer without adding a redundant direct edge.

Sources:

- MIT OpenCourseWare, *Multivariable Calculus*, Part C: Line Integrals and Stokes' Theorem: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/4.-triple-integrals-and-surface-integrals-in-3-space/part-c-line-integrals-and-stokes-theorem/
- MIT OpenCourseWare, *Multivariable Calculus*, lecture/readings sequence: https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/pages/readings/

The former question about whether the theorem layer should move is therefore resolved mechanically by the new incoming constraints.

## 5. Remaining structural question

One question remains deliberately unresolved:

> Should the combined Green / Stokes / Divergence theorem node be split into separate theorem nodes with distinct prerequisites?

The evidence establishes that the combined node belongs downstream of line/surface/multiple integration. It does not establish that a single combined node is the best long-term representation.

Green's theorem, Stokes' theorem, and the divergence theorem have related but non-identical domains and integral requirements. Splitting the node would alter graph architecture rather than merely fill a missing edge, so this contribution leaves that decision for maintainer review.

## 6. Evidence limits

This pass does not infer unreferenced prerequisites from general mathematical knowledge.

It does not treat course ordering alone as proof of a HARD dependency.

The HARD classifications above are tied to the operative mathematical form shown in the cited MIT material:

- trigonometric series are infinite series;
- Fourier coefficient construction uses definite integrals;
- line-integral evaluation reduces to a one-variable integral after parameterization;
- surface-integral evaluation reduces to a double integral over parameters.

No E1, E2, or E3 checklist state is changed.
