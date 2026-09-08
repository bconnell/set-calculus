# Triadic Math–Logic–Computer Science Curriculum Architecture

**Status:** Working curriculum hypothesis  
**Project:** Set Calculus  
**Purpose:** Capture the emerging curriculum architecture for testing against the conventional prerequisite dependency graph.

## 1. Core hypothesis

The curriculum is not best understood as a single linear calculus sequence. It separates into three mutually reinforcing disciplines:

1. **Mathematics** — define and transform structure.
2. **Logic** — determine what can be resolved from that structure.
3. **Computer Science** — represent, execute, and simulate the structure and its resolutions.

The same underlying ideas are revisited at increasing levels of expressive power.

A useful summary is:

```text
Mathematics  -> Model
Logic        -> Resolve
CS           -> Execute
```

The three meet in executable simulation.

## 2. Three mathematical levels

### Calculus I — Relational Hex

Calc I establishes the relational abstraction and first-level transforms.

Core concerns include:

- relational structure
- sets, members, boundaries, and state
- first-order transforms
- reflection
- projection
- differentiation as change under transformation
- integration as accumulation/recovery across transformation

The Relational Hex is the organizing structure for this level.

### Calculus II — Lattice

Calc II introduces the lattice as the larger structured resolution space.

Core concerns include:

- lattice structure
- competing or compatible resolutions
- paradox resolution
- convergence and divergence
- recursion
- conditional transforms
- closure
- logical failure
- traversal through structured possibility/resolution spaces

A central research requirement is to define **paradox resolution** mathematically rather than use it only as a pedagogical label.

### Calculus III — State Management

Calc III is organized around state management rather than simply adding dimensions.

Core concerns include:

- state transition
- persistence
- dependency
- transform history
- invariants
- branching
- synchronization
- projection between states
- reversibility
- path dependence
- composition of complex transforms
- multidimensional state representations

Conventional multivariable calculus machinery can be interpreted as machinery operating over structured state.

## 3. Differential equations as the practical/application layer

Differential equations should not be one terminal course after the calculus sequence.

Each mathematical abstraction level should have a corresponding differential-equations/application layer:

```text
Calc I  -> Differential Equations I
Calc II -> Differential Equations II
Calc III -> Differential Equations III
```

This creates an alternating theory/application rhythm:

```text
Learn a representation
-> make it move
-> learn a richer representation
-> make that move
```

### Differential Equations I — Relational Dynamics

Applies the Relational Hex to changing relationships.

Questions include:

- How does one relational state change with another?
- How do first-order transforms evolve over time?
- What happens when two simple changing states constrain each other?

Candidate conventional material includes first-order ODEs, initial conditions, growth/decay, separable equations, simple feedback, and introductory coupled systems.

### Differential Equations II — Lattice Dynamics

Applies dynamics to lattice/resolution structures.

Questions include:

- How do transformations propagate through a lattice?
- When do interacting paths converge, diverge, oscillate, or conflict?
- How does a system behave when several resolutions remain possible?

This is the practical counterpart to Calc II's lattice and paradox-resolution machinery.

### Differential Equations III — State-System Dynamics

Applies dynamics to managed, persistent, multidimensional state.

Questions include:

- How do complex states evolve?
- How do state histories affect later transformations?
- How do multiple state domains interact?
- How do changes propagate across domain boundaries?

Candidate conventional material includes nonlinear systems, dynamical systems, stability, attractors, control systems, PDEs, diffusion, waves, and complex coupled-domain models.

## 4. The triadic curriculum

The larger architecture separates the work into Mathematics, Logic, and Computer Science curricula while keeping them synchronized around common structures.

| Level | Mathematics | Logic | Computer Science |
|---|---|---|---|
| I | Relational Hex and first transforms | Relational dynamics and elementary resolution | Basic executable simulation |
| II | Lattice | Paradox and lattice resolution | Network / multi-actor simulation |
| III | State management | Complex state resolution | Stateful systems simulation |

The disciplines ask different questions about the same underlying object.

### Mathematics

**What is the structure?**

It defines the representation, relationships, transformations, projections, lattices, and state spaces.

### Logic

**What can be resolved from the structure?**

It studies potential versus resolved state, contradiction/paradox, constraints, closure, logical failure, and the provenance of resolution.

### Computer Science

**Can the structure and its transformations be executed?**

It implements representations, transformations, state preservation, dynamics, observation, and reproducible simulation.

Together:

```text
              Mathematics
                 MODEL
                   |
                   v
Logic ----->  SIMULATION  <----- Computer Science
RESOLVE                           EXECUTE
```

The curricula therefore act as mutual validation layers:

- If mathematics describes something logic cannot resolve, the resolution boundary becomes explicit.
- If logic claims a resolution that cannot be represented or executed, the computational model exposes the gap.
- If simulation produces behavior the mathematical representation cannot explain, the mathematical model requires refinement.

## 5. Simulation economics as the common laboratory

**Simulation economics** is the initial candidate shared application domain.

It provides systems with actors, resources, relationships, constraints, transactions, feedback, history, uncertainty, and delayed resolution. These properties make it useful for exercising all three curricula simultaneously.

### Level I — Transaction / relational simulation

A small economy can model relationships such as:

```text
Producer <-> Consumer
```

with production, demand, price, inventory, and exchange.

Differential Equations I makes those relationships dynamic.

### Level II — Market / network simulation

Multiple actors form a relational lattice. Students can examine propagation of supply shocks, substitution, feedback, competing outcomes, convergence, oscillation, and resolution across a network.

### Level III — Economic-system simulation

The simulation becomes a persistent state system:

```text
S(t) = {
  actors,
  resources,
  relationships,
  constraints,
  history
}
```

The system can branch, preserve history, project possible futures, compare paths, interact with external domains, and evaluate how changes propagate between state systems.

Economics is particularly useful for exercising a foundational Set Calculus distinction:

```text
Potential != Resolved
```

Examples:

- projected output is not realized output;
- demand is not a completed sale;
- allocated budget is not realized value;
- potential production is not production.

A property produced by a transform should not automatically be propagated backward onto its unresolved input.

## 6. Curriculum shape

The current hypothesis can therefore be viewed in two complementary ways.

### Theory/application sequence

```text
Calc I: Relational Hex
    -> DE I: Relational Dynamics

Calc II: Lattice
    -> DE II: Lattice Dynamics

Calc III: State Management
    -> DE III: State-System Dynamics
```

### Cross-disciplinary triad

```text
                 LEVEL I
        Math <-> Logic <-> CS
                 |
                 v
                 LEVEL II
        Math <-> Logic <-> CS
                 |
                 v
                 LEVEL III
        Math <-> Logic <-> CS
```

Simulation provides the executable laboratory at every level.

## 7. Working validation principle

The architecture suggests a three-way test for concepts introduced by Set Calculus:

```text
Define it mathematically
-> resolve it logically
-> execute it computationally
```

Failure at any step is useful information rather than something to hide. It identifies a representational, logical, or computational boundary that needs to be understood.

## 8. Research status

This document records a **candidate architecture**, not an established replacement for conventional mathematics, logic, or computer-science curricula.

The next research pass should test the architecture against the conventional prerequisite DAG rather than assuming the mapping is valid.

Questions to test include:

1. Which conventional Calc I/II/III topics map naturally into Relational Hex, Lattice, and State Management?
2. Which conventional differential-equation topics belong at each of the three application levels?
3. Which prerequisite edges are mathematically necessary versus historically/curricularly imposed?
4. What exact mathematical definition should be used for paradox resolution?
5. What logic curriculum is required at each level?
6. What CS concepts and implementation skills are required to make each level executable?
7. Can one simulation-economics project evolve continuously through all three levels without requiring concepts that the student has not yet learned?
8. Where does linear algebra enter the dependency graph?
9. Where do probability, statistics, numerical methods, optimization, and discrete mathematics enter?
10. Does the resulting graph remain backward-compatible with conventional calculus wherever conventional calculus is valid?

The immediate research task is to map conventional topics onto this 3 x 3 architecture, label prerequisite edges as **HARD / STRONG / SUPPORTING / HISTORICAL**, and determine whether a valid topological ordering emerges.