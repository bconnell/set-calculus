# Canonical Terminology Ledger

## Purpose

This ledger is the canonical naming reference for the current Set Calculus architecture.

It does not create a new architectural layer. It records the stable architecture and provides one canonical definition per term, together with its structural role, allowed aliases, and provenance.

If a terminology edit would add, remove, reorder, subordinate, or redefine structural branches, stop and clarify before changing the architecture.

## Stability Rule

~~~text
architecture = stable unless explicitly changed
~~~

Terminology may be refined within the existing structure.

## Canonical Terms

| Canonical term | Canonical definition | Structural role | Allowed aliases | Provenance |
|---|---|---|---|---|
| **Set Calculus** | A provenance-preserving transformation and resolution framework built around Set, Member, Relationship, State, Transform, Resolution, and Provenance. | Core formal system | SC | docs/set-calculus-core/README.md; SCOPE.md |
| **Foundational Structure** | A structure more abstract than any single mathematical, logical, or computational application, providing common substrate for the disciplines. | Foundational | foundation; foundational structures | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Monadic Relational Structure** | A single underlying relational object that may expose different domain functions without becoming multiple independent realities. Minimal working form: M = <E,R,S,T,P>. | Foundational | monadic structure; shared relational object | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Relational State** | The shared state of the monadic relational structure, including relations that may remain open across domain-local closures. | Foundational / cross-domain | shared relational state | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Domain Function** | A disciplinary projection or operation over the monadic relational structure that produces a domain-resolved view without becoming the whole object. | Cross-disciplinary interface | disciplinary function; domain-specific function | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Mathematics** | The domain function concerned with abstract mathematical structure, representation, measurement, transformation, bounds, invariants, and abstract mathematical application. | Discipline / domain function | mathematical domain | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Mathematical Structure** | An abstract formal mathematical object or relation defined for representation, calculation, transformation, or analysis. | Mathematics | mathematical form | Architecture discussion; FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Logic** | The domain function concerned with admissibility, contradiction, inference, reachability, unresolved states, filters, and closure. | Discipline / domain function | logical domain | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Logical Structure** | A reusable formal structure that determines or preserves how states resolve, remain open, classify, constrain, or relate under rules. | Logic | logic structure | Architecture discussion; FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Computer Science** | The domain function concerned with application: representing, executing, simulating, testing, managing, and using mathematical and logical structures. | Discipline / domain function | CS; computational domain | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Application** | A concrete problem area or use-domain in which foundational, mathematical, and logical structures are applied. | Computer Science / applied study | application domain | Architecture discussion; FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Local Closure** | A valid closure reached inside one domain function over its own representation and rules. | Cross-domain logical condition | domain closure; disciplinary closure | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Relational Closure** | Closure of the larger shared relational object after materially relevant cross-domain relations have also resolved. | Foundational / cross-domain closure condition | global relational closure | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Cross-Domain Relation** | A relation that remains materially present across two or more domain-resolved views of the same monadic relational structure. | Cross-disciplinary | cross-domain relationship | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Resolution Space** | The structured space of candidate states, witnesses, paths, constraints, and possible resolutions prior to forced closure. | Foundational / logical research object | pre-causal resolution space when causally neutral; solution space only when specifically referring to solutions | docs/philosophy-of-set-calculus/HISTORICAL_CHECKPOINT_PRE_CAUSAL_RESOLUTION_SPACE.md |
| **Theory** | A logical structure that preserves structured non-determinative, non-resolved possibility space without forcing closure. | Logical structure | theory space | HISTORICAL_CHECKPOINT_PRE_CAUSAL_RESOLUTION_SPACE.md; architecture discussion |
| **State** | A structure representing what presently holds at an active resolution boundary, including unresolved relations where applicable. | Logical structure; Set Calculus primitive | system state only when specialized | docs/set-calculus-core/README.md; docs/causal-reality-calculus/CORE_PRIMITIVES_AND_AXIOMS.md |
| **Data** | As a logical structure, the formal organization that determines what counts as a datum, how identity and relations persist, and what transformations are valid; as an application, concrete information being stored, moved, queried, transformed, compared, reconstructed, or analyzed. | Logical structure and application | datum structure only when explicitly singular | Architecture discussion |
| **Simulation** | A logical structure for evaluating possible transforms or trajectories without committing them to the represented real state. | Logical structure | simulated resolution when context requires | Architecture discussion |
| **Management** | A logical structure governing persistence, transition, control, reconciliation, and coordination of state. | Logical structure | state management only when narrowed to state | Architecture discussion |
| **Planning** | A logical structure over possible future transitions, paths, constraints, and candidate resolutions. | Logical structure | plan structure | Architecture discussion |
| **Alignment** | A logical structure that constrains admissible relationships among objectives, states, transforms, and outcomes. | Logical structure | alignment structure | Architecture discussion; Causal AI alignment work |
| **Paradox** | A structure that marks unresolved incompatibility within an active structure and, when that incompatibility cannot be resolved there, may expose insufficiency in the foundational structure itself. | Logical and foundational | Logical Paradox; Foundational Paradox as role-qualified forms | Architecture discussion; FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Discriminated Union** | A logical structure in which one discriminator selects a branch and the selected branch carries its own required structure. | Logical structure / filter form | tagged union permitted as implementation synonym; enum is not equivalent | docs/philosophy-of-set-calculus/NOVELTY_CLASSIFICATION.md |
| **Novelty Filter** | A logical filter implemented as a discriminated union that classifies a novelty claim relative to resolution-space validity, prior structure, interpretation, and provenance. | Logical filter | Novelty Discriminated Union | docs/philosophy-of-set-calculus/NOVELTY_CLASSIFICATION.md |
| **Novel** | A novelty classification in which the relevant resolution space is valid and the structure, behavior, application, or formal object is genuinely new. | Novelty branch | none | docs/philosophy-of-set-calculus/NOVELTY_CLASSIFICATION.md |
| **Pseudo-Novel** | A novelty classification in which the underlying object and resolution space are valid, while the materially new contribution is interpretation, formalization, or structural framing. | Novelty branch | PseudoNovel in machine identifiers | docs/philosophy-of-set-calculus/NOVELTY_CLASSIFICATION.md |
| **Faux-Novel** | A novelty classification in which apparent novelty is produced by an incorrect, incomplete, or invalid resolution space and collapses when that space is corrected. | Novelty branch | FauxNovel in machine identifiers | docs/philosophy-of-set-calculus/NOVELTY_CLASSIFICATION.md |
| **Transform** | A mapping from one state into another; preservation and change must be declared rather than assumed. | Set Calculus primitive / logical operation | transformation | docs/set-calculus-core/README.md; docs/causal-reality-calculus/CORE_PRIMITIVES_AND_AXIOMS.md |
| **Resolution** | The explicit outcome of evaluating a structure under the active rules and boundaries. | Set Calculus primitive | resolved outcome | docs/set-calculus-core/README.md; docs/causal-reality-calculus/CORE_PRIMITIVES_AND_AXIOMS.md |
| **Provenance** | The lineage establishing where an object, claim, state, transform, or resolution came from and how it was produced. | Set Calculus primitive / cross-cutting requirement | trace when specifically referring to execution trace | PROVENANCE.md; docs/causal-reality-calculus/CORE_PRIMITIVES_AND_AXIOMS.md |
| **Cause** | An application-level study of causal relationships and effects; cause itself is not a root primitive in CRC. | Computer Science application | none | docs/causal-reality-calculus/CORE_PRIMITIVES_AND_AXIOMS.md; architecture discussion |
| **Relation** | An application-level study of relationships among states, members, transforms, or systems. | Computer Science application | relationship study | Architecture discussion |
| **Causal Relations** | A Computer Science application domain concerned with applying mathematical and logical structures to interacting causes, states, carriers, trajectories, contexts, and effects. | Computer Science application | causal-relations study | Architecture discussion; CRC mapping discussion |
| **Game Theory** | An application domain concerned with strategic interaction among agents, choices, states, payoffs, constraints, and trajectories. | Computer Science application; may also have mathematical formalizations | none | Architecture discussion |
| **Triadic Resolution Path** | A generalized three-path resolution structure with lower-bound, middle/balancing, and upper-bound paths. | Structural abstraction used across disciplines | none | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Collatz** | Historical source/provenance anchor for an observed source dynamic from which the Triadic Resolution Path abstraction is being explored. | Historical source anchor | Collatz problem when referring to the historical problem itself | docs/philosophy-of-set-calculus/FOUR_BODY_KNOWLEDGE_ARCHITECTURE.md |
| **Trajectory** | An ordered alternating sequence of States and Transforms, written π = <s0,T1,s1,...,Tn,sn>. | Set Math formal structure | path only when order and transform semantics are preserved | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Trajectory Admissibility** | A three-valued relation that determines whether a trajectory is valid, invalid, or unresolved under active Context and Authority. | Logical / Set Math relation | admissibility relation | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Boundary Compatibility** | The three-valued compatibility predicate that determines whether two trajectory segments may be validly concatenated across state, context, authority, invariant, and provenance boundaries. | Logical / Set Math relation | boundary predicate | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Representation Structure** | A structure G=<V,R,Σ,Φ,I,P> that represents objects, relations, distinctions, transforms, invariants, and provenance needed for resolution. | Mathematical / Set Math structure | representation model | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Resolution Depth** | The greatest depth t for which a representation structure can jointly satisfy all materially required representability, distinguishability, transform, invariant, reachability, and provenance requirements. | Mathematical / logical measure | supported depth | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Depth-Indexed Requirement Set** | The requirement object R_t=<Rep_t,Dist_t,Trans_t,Inv_t,Reach_t,Prov_t> defining what must hold for resolution through depth t. | Set Math formal structure | R_t; depth requirements | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Requirement Entailment** | The relation R_t ⊨ R_u meaning every materially necessary requirement at depth u is preserved, strictly strengthened, or legitimately replaced at depth t. | Logical / Set Math relation | depth entailment | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Legitimate Replacement** | A depth transition in which a shallower requirement may disappear syntactically only when an admissible witness discharges it while preserving its material resolution meaning and required provenance. | Logical / Set Math relation | replacement witness | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Boundary Evidence Object** | The minimum typed evidence bundle required to establish state, context, authority, invariant, and provenance compatibility across a trajectory boundary. | Set Math proof object | boundary evidence; E_B | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Boundary Witness** | A typed provenance-bearing proof object that establishes one boundary compatibility claim for state, context, authority, invariant, or provenance. | Set Math proof object | typed boundary witness | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Witness Envelope** | A uniform outer schema carrying claim, subject, boundary reference, evidence, provenance, rule basis, dependencies, contradictions, status, resolution record, and typed payload for a boundary witness. | Logical / Set Math validation structure | common witness envelope | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Witness Validation** | The uniform three-valued validation procedure that checks schema, boundary applicability, claim completeness, provenance, dependencies, contradictions, and typed proof validity. | Logical / Set Math procedure | ValidateWitness | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |
| **Admissible Concatenation Closure** | The working theorem that two admissible trajectory segments with an admissible boundary concatenate to an admissible trajectory. | Set Math theorem | concatenation closure theorem | docs/set-calculus-core/TRAJECTORY_ADMISSIBILITY_AND_RESOLUTION_DEPTH.md |

## Alias Rules

An alias may improve readability but must not silently change structural role.

~~~text
alias
!-> new definition
~~~

Role-qualified names are permitted when one canonical term legitimately operates through more than one interface.

~~~text
Paradox
  -> Logical Paradox
  -> Foundational Paradox

Data
  -> Data as logical structure
  -> Data as application
~~~

These are role qualifications of one canonical term, not unrelated definitions.

## Cross-Interface Rule

A term may legitimately appear in more than one structural role.

~~~text
same canonical term
+ different interface role
!= duplicate concept
~~~

Classification should answer:

~~~text
What role is this term playing here?
~~~

rather than forcing every term into exactly one disciplinary box.

## Structural Change Guard

Before changing this ledger in a way that would alter the architecture:

~~~text
proposed terminology change
        ↓
would structural relationships change?
        ↓
YES -> clarify before editing
NO  -> terminology update may proceed
~~~

This guard exists to prevent terminology maintenance from accidentally rewriting the architecture.
