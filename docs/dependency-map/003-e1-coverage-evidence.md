# Research 003: E1 Initial-Family Coverage Evidence

**Status:** Provisional contributor evidence  
**Coverage source:** `docs/dependency-map/README.md` — "Initial concept families"  
**Release authority:** This document does not mark E1 PASS. `CORE_0.1_COMPLETENESS_CHECKLIST.md` assigns E1 ownership to Chad Coulter.

## 1. Purpose

The dependency-map README says the first mapping pass should include seventeen concept families. The machine-readable dependency inventory already represented fourteen of them directly or through clearly named concept nodes.

This pass resolves the three explicit omissions:

- parametric representation;
- polar representation;
- vectors and vector-valued functions, where vectors were present but vector-valued functions were not.

The coverage map is stored in `CORE_0.1_E1_COVERAGE.json`.

A complete mapping against the README's starting list is not equivalent to E1 PASS because the README itself says the list is only a starting inventory.

## 2. Parametric representation

### 2.1 Functions -> Parametric representation

MIT's single-variable calculus material describes a parametrized plane curve by a point `(x(t), y(t))`, and MIT multivariable material writes a space curve as `(x(t), y(t), z(t))`.

That supports:

```text
Functions / algebra / trigonometry
  -> Parametric representation / curves
```

**Provisional class:** `HARD`

The graph mapping is a contributor inference: the MIT source establishes that the coordinates of the parametrization are functions of a parameter; the repository chooses to represent the prerequisite with its existing functions node.

Sources:

- MIT OpenCourseWare, Single Variable Calculus, Session 80: Parametric Curves: https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-4-techniques-of-integration/part-c-parametric-equations-and-polar-coordinates/session-80-parametric-curves/
- MIT OpenCourseWare, Multivariable Calculus, Part C: Parametric Equations for Curves: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/1.-vectors-and-matrices/part-c-parametric-equations-for-curves/

### 2.2 Parametric representation -> Line integrals

MIT's line-integral material describes parametric representation as the standard general method for describing a path for evaluation and shows the calculation reducing to an ordinary one-variable integral after parameterization.

That supports:

```text
Parametric representation / curves
  -> Line integrals
```

**Provisional class:** `HARD`

Sources:

- MIT OpenCourseWare calculus text, "Making a Line Integral into an Ordinary Integral": https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter23/section01.html
- MIT OpenCourseWare, 18.02 Multivariable Calculus Lecture 19 transcript: https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/0f08f41ee83e277a7e168bb4279c006c_18_022007L19.pdf

## 3. Polar representation

### 3.1 Functions / trigonometry -> Polar representation

MIT defines polar coordinates by radius and angle and relates Cartesian and polar descriptions using trigonometric coordinate relations.

That supports:

```text
Functions / algebra / trigonometry
  -> Polar representation / coordinates
```

**Provisional class:** `HARD`

Sources:

- MIT OpenCourseWare calculus text, "Polar Coordinates": https://www.ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter03/section06.html
- MIT OpenCourseWare, Single Variable Calculus, Session 82: Polar Coordinates: https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-4-techniques-of-integration/part-c-parametric-equations-and-polar-coordinates/session-82-polar-coordinates/

### 3.2 Polar representation -> Multiple integrals

MIT has a dedicated double-integration treatment in polar coordinates. This demonstrates that polar representation is a substantial computational coordinate system for multiple integration, but rectangular-coordinate multiple integration does not require it.

That supports:

```text
Polar representation / coordinates
  -> Multiple integrals
```

**Provisional class:** `SUPPORTING`

Sources:

- MIT OpenCourseWare, Multivariable Calculus, Session 50: Double Integrals in Polar Coordinates: https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/3.-double-integrals-and-line-integrals-in-the-plane/part-a-double-integrals/session-50-double-integrals-in-polar-coordinates/
- MIT OpenCourseWare, 18.02 notes on changing variables in multiple integrals: https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/05f51f37ac3bb5801af56e6879728f68_multipl_integrls.pdf

## 4. Vector-valued functions

### 4.1 Functions + vectors -> Vector-valued functions

MIT's Calculus Revisited material introduces vector functions of a scalar variable after vector arithmetic, and the lecture explicitly treats scalar input with vector output while reviewing limits and differentiation of vector functions.

That supports two prerequisites in the current graph vocabulary:

```text
Functions / algebra / trigonometry
  -> Vector-valued functions

Vectors / coordinates
  -> Vector-valued functions
```

**Provisional class:** `HARD` for both.

Sources:

- MIT OpenCourseWare, Calculus Revisited: Multivariable Calculus, Lecture 1: Vector Functions of a Scalar Variable: https://ocw.mit.edu/courses/res-18-007-calculus-revisited-multivariable-calculus-fall-2011/resources/lecture-1-vector-functions-of-a-scalar-variable/
- MIT OpenCourseWare, Multivariable Calculus with Theory readings: https://ocw.mit.edu/courses/18-024-multivariable-calculus-with-theory-spring-2011/pages/readings/

### 4.2 Vector-valued functions and parametric curves

MIT's parametric-curve material writes a trajectory as coordinate functions and describes velocity and acceleration as vectors varying with the parameter. A vector-valued position function is therefore a useful unifying representation of parametric curves.

The inventory records:

```text
Vector-valued functions
  -> Parametric representation / curves
```

as `SUPPORTING`, not HARD. Parametric curves can be introduced directly through coordinate functions without first formalizing the broader vector-valued-function abstraction.

## 5. Coverage result

The machine-readable coverage map now has an explicit mapping for all seventeen concept families in the repository's stated first mapping pass.

That result means:

```text
initial-family coverage = 17 / 17
```

It does **not** mean:

```text
E1 PASS
```

The README says the family list is a starting inventory. Other named topics in the research document — for example improper integrals, directional derivatives, forcing/resonance, and PDE context — remain outside the narrow claim made by this audit.

## 6. Validation path

This branch validates both projections independently:

```bash
python scripts/audit_core_dependency_inventory.py --self-test
python scripts/generate_core_dependency_order.py --check
python scripts/audit_core_e1_coverage.py --self-test
python scripts/generate_core_e1_coverage.py --check
```

The dependency-order checks guard the graph structure and generated topological projection. The E1 checks separately guard exact coverage of the README's stated initial concept-family list and the generated coverage view.

## 7. Evidence limits

The external MIT material is used to justify the prerequisite mappings for the three newly represented concepts.

The definition of what counts as an E1 target in this batch comes from the repository's own README, not from the external sources.

No checklist state is changed.
