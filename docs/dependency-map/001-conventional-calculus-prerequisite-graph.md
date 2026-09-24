# Research 001: Conventional Calculus Prerequisite Dependency Graph

**Status:** Initial research document  
**Project:** Set Calculus  
**Scope:** Conventional undergraduate calculus from limits through ordinary differential equations  
**Purpose:** Separate mathematical prerequisite dependencies from inherited course packaging, then identify the minimal valid ordering of concepts.

---

## 1. Research question

Conventional university curricula commonly package calculus as:

```text
Calculus I
  -> Calculus II
  -> Calculus III / Multivariable Calculus
  -> Differential Equations
```

This document asks a different question:

> If the course labels are removed, what concepts actually depend on what other concepts?

The distinction matters because a catalog prerequisite is not necessarily a mathematical prerequisite. A course can require another course for administrative, pacing, or curricular reasons even when only part of the earlier course is mathematically necessary.

The Set Calculus research program therefore distinguishes:

- **institutional prerequisite** — what a university requires before enrollment;
- **conceptual prerequisite** — what a concept actually needs in order to be derived, understood, or used;
- **supporting prerequisite** — knowledge that is not logically necessary but materially improves comprehension or technique;
- **parallel dependency** — concepts that can be learned independently and later joined.

---

## 2. Institutional baseline

Current and representative university sequences show that the standard ordering is not universal.

### University of Illinois Chicago

UIC packages the sequence conventionally:

```text
MATH 180 Calculus I
  -> MATH 181 Calculus II
  -> MATH 210 Calculus III
  -> MATH 220 Introduction to Differential Equations
```

UIC Calculus I includes differentiation, extrema, related rates, antiderivatives, and the Riemann integral. Calculus II adds integration techniques, parametric and polar coordinates, sequences, series, and power series. Calculus III adds vectors, functions of several variables, partial differentiation, multiple integrals, vector fields, Green's theorem, and Stokes' theorem. Differential Equations then covers first- and second-order equations, Laplace transforms, series solutions, graphical and numerical methods, and partial differential equations.

### MIT

MIT's single-variable calculus curriculum contains differentiation, integration, integration techniques, improper integrals, sequences and series, and Taylor series. MIT also explicitly includes first-order differential equations by separation of variables in its single-variable calculus material.

MIT multivariable calculus requires single-variable calculus and then develops vectors and matrices, partial derivatives, multiple integrals, line integrals, Green's theorem, surface integrals, divergence, and Stokes' theorem.

MIT differential equations is organized around first-order equations, second-order linear equations, Fourier and Laplace methods, and first-order systems.

### UC Berkeley

Berkeley currently offers MATH 54, **Linear Algebra and Differential Equations**, after the second single-variable calculus course. Its prerequisite is Calculus II-level work, not multivariable calculus. The course combines matrix algebra, vector spaces, eigenvalues/eigenvectors, second-order differential equations, first-order systems, and Fourier series.

This is important evidence that the familiar

```text
Calc III -> Differential Equations
```

ordering is not mathematically mandatory.

---

## 3. Core dependency graph

The graph below separates the conceptual dependencies from course names.

```text
Functions / algebra / trigonometry
            |
            v
          Limits
            |
            +----------------------+
            |                      |
            v                      v
       Continuity            Sequences / convergence
            |                      |
            v                      v
   Derivative definition       Infinite series
            |                      |
            v                      v
  Differentiation rules        Power series
            |                      |
      +-----+------+               v
      |            |          Taylor series
      v            v                |
 Applications   Local linearity     |
 rates/extrema      |               |
      |             |               |
      +------+------+               |
             |                      |
             v                      |
        Antiderivatives             |
             |                      |
             v                      |
        Definite integral           |
             |                      |
             v                      |
 Fundamental Theorem of Calculus    |
             |                      |
      +------+------+               |
      |             |               |
      v             v               |
 Integration   Integral applications|
 techniques        |                |
      |             |                |
      +------+------+
             |
             v
   First-order differential equations
   (separable / elementary linear)
             |
      +------+--------------------+
      |                           |
      v                           v
Second-order ODEs           Numerical / slope-field methods
      |
      +------------+
                   |
                   v
             Linear systems <--------- Linear algebra
                   |
          +--------+---------+
          |                  |
          v                  v
     Eigen methods       Phase portraits
          |
          v
   Systems of ODEs

Power series ---------------------> Series solutions of ODEs
Integration techniques -----------> Laplace transforms / convolution
Trigonometric series -------------> Fourier methods

Single-variable derivatives
            |
            v
  Functions of several variables <---- vectors / coordinates
            |
            v
     Partial derivatives
            |
      +-----+------+
      |            |
      v            v
   Gradient     Multivariable chain rule
      |            |
      +------+-----+
             |
             v
      Optimization / Lagrange multipliers

Single-variable integration
            |
            v
      Multiple integrals
            |
            v
   Change of variables / Jacobians

Vectors + derivatives
            |
            v
       Vector fields
            |
      +-----+------+
      |            |
      v            v
 Line integrals  Surface integrals
      |            |
      +------+-----+
             |
             v
 Green / Stokes / Divergence theorems
```

---

## 4. Dependency interpretation

### 4.1 Limits are the first common root

The derivative is defined through a limit, and the Riemann integral is constructed through a limiting process. Conventional calculus therefore has a genuine foundational dependency:

```text
Limits
  -> derivative
  -> integral
```

Continuity is closely connected to limits and supports many of the standard theorems that follow.

### 4.2 Differentiation and integration form a joined trunk

Differentiation does not require the full apparatus of integration techniques, infinite series, polar coordinates, or multivariable calculus.

Likewise, once antiderivatives, definite integrals, and the Fundamental Theorem are available, many first-order differential equations become accessible immediately.

That produces the first important reordering result:

```text
Basic differentiation
  -> basic integration
  -> first-order differential equations
```

is a valid dependency path.

There is no intrinsic need to wait until after multivariable calculus.

### 4.3 Differential equations are not one dependency block

"Differential Equations" is itself a bundle of topics with different prerequisite depths.

#### Early-accessible differential equations

These can be introduced soon after basic integration:

- separable first-order ODEs;
- exponential growth and decay;
- elementary linear first-order equations;
- slope fields and qualitative first-order behavior;
- initial-value problems.

MIT's inclusion of separable first-order differential equations inside single-variable calculus provides an existing curricular example of this ordering.

#### Mid-level differential equations

These typically require stronger single-variable technique:

- second-order linear equations;
- forcing and resonance;
- Laplace transform methods;
- convolution;
- numerical methods.

#### Later differential equations

These depend on material often taught elsewhere:

- systems of ODEs depend strongly on linear algebra;
- eigenvalue methods depend on matrices/eigenvectors;
- series solutions depend on power series;
- Fourier methods depend on trigonometric series and integration;
- PDE introductions often benefit from multivariable derivatives and vector-calculus context.

Thus the conventional course called Differential Equations should be represented as a **fan-in structure**, not a single node after Calc III.

---

## 5. Calculus II is also not a single dependency block

Conventional Calc II usually combines several largely independent strands:

```text
Integration techniques
Sequences / series
Power series
Parametric curves
Polar coordinates
Applications of integration
```

These do not all depend on one another.

For example:

- integration by parts does not require infinite series;
- infinite series do not require polar coordinates;
- parametric curves do not require power series;
- first-order differential equations can begin before most series theory;
- power series are specifically important later for approximation and series solutions of ODEs.

This means Calc II is better understood as a **collection of branches sharing the Calc I trunk** than as a single prerequisite object.

---

## 6. Calculus III is also a bundle

Conventional multivariable calculus contains at least four distinguishable strands:

### A. Geometric / vector foundation

```text
vectors
coordinates
matrices
parametric curves
```

### B. Multivariable differentiation

```text
functions of several variables
  -> partial derivatives
  -> gradient
  -> directional derivative
  -> multivariable chain rule
  -> constrained optimization
```

### C. Multivariable integration

```text
single-variable integration
  -> double integrals
  -> triple integrals
  -> coordinate transformations
```

### D. Vector calculus

```text
vector fields
  -> line integrals
  -> surface integrals
  -> Green / Stokes / Divergence theorems
```

These branches share some prerequisites, but they do not all need to occur before ordinary differential equations.

A student can study first- and second-order ODEs without knowing Stokes' theorem. A student can study linear systems of ODEs with linear algebra before learning triple integrals. Berkeley's MATH 54 is a live example of this split.

---

## 7. Minimal conceptual ordering

The dependency analysis suggests the following minimal spine:

```text
1. Functions
2. Limits
3. Continuity
4. Derivative
5. Differentiation rules
6. Local linearity / rates / extrema
7. Antiderivative
8. Definite integral
9. Fundamental Theorem of Calculus
10. Basic integration techniques
11. First-order differential equations
```

After that point, the curriculum branches rather than continuing as one line.

### Branch A: advanced single-variable / series

```text
improper integrals
sequences
series
power series
Taylor approximation
series solutions of ODEs
```

### Branch B: differential equations / dynamics

```text
first-order ODEs
second-order ODEs
qualitative methods
numerical methods
Laplace methods
```

with a join from linear algebra:

```text
linear algebra
  -> eigenvalues/eigenvectors
  -> systems of ODEs
```

### Branch C: multivariable differentiation

```text
vectors / coordinates
functions of several variables
partial derivatives
gradient
multivariable chain rule
optimization
```

### Branch D: multivariable integration and vector calculus

```text
multiple integrals
vector fields
line integrals
surface integrals
integral theorems
```

This graph is not a recommendation yet. It is the first dependency-derived representation.

---

## 8. First Set Calculus curriculum hypothesis

The graph supports the working hypothesis that a more dependency-faithful curriculum could introduce differential equations substantially earlier than the traditional Calc I -> Calc II -> Calc III -> Diff Eq sequence.

A candidate ordering for later testing is:

```text
Foundation
  Functions -> Limits -> Derivative -> Integral -> FTC

Transformation I
  Rates -> accumulation -> first-order ODEs

Technique / approximation
  Integration methods -> sequences -> series -> Taylor

Dynamics
  Second-order ODEs -> numerical methods -> Laplace

Relational extension
  Vectors -> multivariable functions -> partial derivatives

Higher-dimensional accumulation
  Multiple integrals -> vector fields -> line/surface integrals

Linear-system join
  Linear algebra -> eigen methods -> systems of ODEs

Global field relationships
  Green -> Stokes -> Divergence
```

This places differential equations near the point where the student first possesses the tools needed to recover a state from a relationship involving change.

That is structurally closer to:

```text
state
  -> change
  -> accumulation
  -> relationship between changes
  -> higher-dimensional relationships
```

than the conventional course sequence.

---

## 9. Set Calculus interpretation

The dependency graph exposes several principles relevant to Set Calculus.

### 9.1 Unresolved is not unknown

A first-order differential relationship can preserve meaningful structural information before a closed-form solution is known.

```text
dy/dt = ky
```

already constrains the possible state trajectories. The state is unresolved, not structureless.

### 9.2 A transformed property should not be assigned backward

If a quantity exists only after a transform, it should not automatically be treated as a property of the pre-transform state.

```text
P -> T(P) -> O
```

A property of `O` is not automatically a resolved property of `P`.

### 9.3 Course labels are containers, not dependencies

`Calc II`, `Calc III`, and `Differential Equations` are sets of concepts. Their ordering should not itself be treated as mathematical authority.

Set Calculus should resolve dependencies at the concept level first, then derive a teaching order.

---

## 10. Dependency classes for the next research pass

Every edge in the graph should next be classified as one of:

```text
HARD
  concept B cannot be derived or meaningfully defined without A

STRONG
  B can technically be introduced without A, but A provides the normal mathematical machinery

SUPPORTING
  A materially improves understanding or technique but is not required

HISTORICAL / CURRICULAR
  A precedes B in common curricula but no strong mathematical dependency has yet been demonstrated
```

Example provisional classifications normalized to the Core 0.1 E2 vocabulary:

| Dependency | Initial class | Rationale |
|---|---|---|
| limits -> derivative definition | HARD | The derivative definition in this research graph is explicitly defined through a limit. |
| definite integral -> Fundamental Theorem | HARD | The Fundamental Theorem entry in this graph links differentiation to the already-defined definite integral. |
| basic integration -> separable first-order ODEs | STRONG | This document identifies separable first-order ODEs as accessible after basic integration; integration supplies the normal solution machinery without making all later integration technique a prerequisite. |
| power series -> series solutions of ODEs | HARD | The document identifies power series as specifically required for the series-solution branch. |
| linear algebra -> eigenvalue solution of ODE systems | HARD | The systems branch explicitly depends on matrices, eigenvalues, and eigenvectors from linear algebra. |
| Calc III as a whole -> first-order ODEs | HISTORICAL/CURRICULAR | The document gives direct curricular evidence that first-order ODE work can occur without treating Calc III as a mathematical prerequisite block. |
| multivariable calculus -> PDE methods | STRONG | The document describes multivariable derivatives and vector-calculus context as materially useful for PDE introductions while keeping the dependency topic-dependent. |

Explicit non-dependency observation:

| Relationship tested | Result | Rationale |
|---|---|---|
| vector calculus -> ordinary first-order ODEs | NONE | The graph explicitly separates ordinary first-order ODEs from the later vector-calculus branch; this is not a dependency edge and therefore does not receive an E2 dependency class. |

These classifications remain provisional and should be validated concept by concept. Normalizing this example table does not establish E2 PASS or classify every material edge used by the teaching-order hypothesis.

---

## 11. Research conclusions

The first dependency pass produces four major findings:

1. **The conventional four-course chain is not the mathematical dependency graph.** It is a curricular packaging scheme.
2. **First-order differential equations can be introduced directly after the derivative/integral/FTC trunk.** Existing MIT material already demonstrates this.
3. **Differential equations fan in from several branches.** First-order ODEs need much less preparation than systems, series solutions, Fourier methods, or PDEs.
4. **Calc II and Calc III should be decomposed before Set Calculus derives a new teaching order.** Both courses contain concept families that are only partially dependent on one another.

The strongest immediate research direction is therefore not "move Differential Equations before Calc III" as a single course-level operation. It is:

> Decompose Differential Equations, Calc II, and Calc III into concept nodes, classify each dependency edge, and topologically sort the resulting graph.

That will produce the first defensible Set Calculus curriculum order.

---

## 12. Sources

### MIT OpenCourseWare

- Single Variable Calculus syllabus: https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/syllabus/
- Multivariable Calculus syllabus: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/syllabus/
- Multivariable Calculus topic structure: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/download/
- Differential Equations syllabus: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/
- Single Variable Calculus 2006 syllabus, including first-order separable differential equations: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/syllabus/

### University of Illinois Chicago

- Mathematics course descriptions: https://catalog.uic.edu/all-course-descriptions/math/
- MATH 220 Introduction to Differential Equations: https://catalog.uic.edu/all-course-descriptions/math/

### University of California, Berkeley

- MATH 54 Linear Algebra and Differential Equations: https://undergraduate.catalog.berkeley.edu/courses/1147051

---

## 13. Next document

**Research 002:** Concept-level dependency classification for Calc II, Calc III, and Differential Equations, with HARD / STRONG / SUPPORTING / HISTORICAL edge labels and a first topological sort.
