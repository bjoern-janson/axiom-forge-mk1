# Axiom Forge Mk1 Agent Architecture

## Computational Architecture for Recursive Evolutionary Agency

## Abstract

Axiom Forge agents are designed to test whether adaptive systems can transform environmental consequences into improvements of future adaptation.

The core architectural hypothesis is:

\[
\boxed{
D_c \times C_e \times A_c
\rightarrow
G_{\mathcal V}
}
\]

A RECA agent must therefore contain mechanisms for:

1. receiving consequences,
2. modifying adaptive machinery,
3. selecting among modifications,
4. consolidating successful changes,
5. expanding future viable reachability.

---

# 1. Architectural Principle

A standard learning agent has:

\[
E\rightarrow S
\]

The environment updates internal state.

A meta-learning agent has:

\[
E\rightarrow S\rightarrow T
\]

The environment changes the learning process.

A RECA agent requires:

\[
\boxed{
E\rightarrow S\rightarrow T\rightarrow\sigma
}
\]

The environment must influence the process that determines which future transformations survive.

---

# 2. Core Agent Components

The minimal RECA architecture contains five components:

\[
Agent=(S,T,\sigma,A_c,M)
\]

Where:

| Component | Function |
|---|---|
| \(S\) | Adaptive state |
| \(T\) | Transformation mechanism |
| \(\sigma\) | Selection mechanism |
| \(A_c\) | Consolidation mechanism |
| \(M\) | Memory / substrate |

---

# 3. Adaptive State

\[
S_t
\]

## Definition

The current internal configuration used to generate behavior.

Examples:

- learned representations,
- policies,
- world models,
- strategies,
- internal parameters.

---

## Update

Basic adaptation:

\[
S_{t+1}=T(S_t,E_t)
\]

The state changes through interaction.

---

## Limitation

State adaptation alone does not create RECA.

A system can modify:

\[
S
\]

while leaving:

\[
T,\sigma
\]

unchanged.

---

# 4. Transformation Mechanism

\[
T
\]

## Definition

The process that generates adaptive change.

Examples:

- learning algorithm,
- search strategy,
- exploration mechanism,
- representation update rule.

---

## Meta-adaptation

A RECA candidate must allow:

\[
T_{t+1}=M(T_t,E_t)
\]

The system can improve how it changes.

---

## Example modifications

A system may discover:

- better exploration strategies,
- improved abstraction methods,
- more efficient update rules,
- new internal representations.

---

# 5. Selection Mechanism

\[
\sigma
\]

## Definition

The process deciding which transformations persist.

This is the critical RECA component.

---

## Without selection

\[
T\rightarrow T'
\]

means:

"the system changed."

---

## With selection

\[
\{T_1,T_2,...,T_n\}
\rightarrow
\sigma(T_i)
\]

means:

"the system preserves changes because consequences favored them."

---

## Requirements

A selection mechanism must:

- generate variation,
- evaluate consequences,
- retain useful changes,
- remove harmful changes.

---

# 6. Adaptive Consolidation

\[
A_c
\]

## Definition

The mechanism that converts temporary improvement into persistent adaptive structure.

---

## Without consolidation

\[
Adaptation
\rightarrow
Temporary\ success
\rightarrow
Reset
\]

---

## With consolidation

\[
Adaptation
\rightarrow
Structural\ change
\rightarrow
Improved\ future\ adaptation
\]

---

## Possible implementations

- long-term memory updates,
- architecture modification,
- reusable abstractions,
- learned learning rules,
- compressed causal models.

---

# 7. Memory Substrate

\[
M
\]

## Definition

The persistent substrate where adaptive gains accumulate.

---

## Memory is not storage alone

A RECA memory must preserve:

\[
\text{useful adaptive structure}
\]

not merely past observations.

---

## Examples

Weak memory:

\[
history\rightarrow replay
\]

Strong memory:

\[
history\rightarrow improved\ future\ transformation
\]

---

# 8. Full Agent Loop

The complete cycle:

\[
\boxed{
E_t
\rightarrow
S_t
\rightarrow
A_t
\rightarrow
Outcome
\rightarrow
Selection
\rightarrow
Consolidation
\rightarrow
S_{t+1},T_{t+1},\sigma_{t+1}
}
\]

The defining feature:

The outcome modifies the generator of future outcomes.

---

# 9. Minimal RECA Agent Pseudocode

initialize state S
initialize transformation rule T
initialize selector sigma
initialize memory M

while alive:

observe environment E

action = generate(S, T)

consequence = environment(action)

candidate_changes = propose_changes(
    S,
    T,
    consequence
)

evaluated_changes = sigma(
    candidate_changes,
    consequence
)

S, T = consolidate(
    evaluated_changes,
    M
)

update(M)

---

# 10. Agent Classes for Benchmark Comparison

The benchmark should include controlled agent families.

---

## Class 0 — Fixed Optimizer

Architecture:

\[
A=f(E)
\]

Properties:

\[
D_c\approx0
\]

---

## Class 1 — Learning Agent

Architecture:

\[
E\rightarrow S
\]

Properties:

\[
D_c>0
\]

but:

\[
T=\text{fixed}
\]

---

## Class 2 — Meta-Learning Agent

Architecture:

\[
E\rightarrow S\rightarrow T
\]

Properties:

Can improve learning rules.

---

## Class 3 — Self-Modifying Agent

Architecture:

\[
T\rightarrow T'
\]

Properties:

High modification ability.

May still have:

\[
C_e\approx0
\]

---

## Class 4 — RECA Agent

Architecture:

\[
\boxed{
E\rightarrow S\rightarrow T\rightarrow\sigma
}
\]

Properties:

- consequence-driven modification,
- adaptive selection,
- consolidation,
- viability expansion.

---

# 11. Measuring Architecture Properties

## Recursive Depth

Measure:

What internal variables change after environmental perturbation?

---

## Consequence Coupling

Measure:

Do successful consequences alter persistence probability?

---

## Adaptive Consolidation

Measure:

Do improvements transfer to future environments?

---

# 12. Architecture Ablation Tests

Axiom Forge requires removing components.

---

## Remove \(D_c\)

Prediction:

\[
G_{\mathcal V}\approx0
\]

The system cannot revise itself.

---

## Remove \(C_e\)

Prediction:

\[
G_{\mathcal V}\approx0
\]

Changes become unguided.

---

## Remove \(A_c\)

Prediction:

Temporary adaptation without accumulation.

---

The goal is not to prove a specific architecture.

The goal is to identify necessary causal mechanisms.

---

# 13. Open Questions

## How is variation generated?

Possible mechanisms:

- search,
- mutation,
- exploration,
- hypothesis generation.

---

## How is causality inferred?

Possible mechanisms:

- prediction errors,
- world models,
- counterfactual reasoning,
- causal compression.

---

## How is consolidation controlled?

Possible mechanisms:

- stability criteria,
- repeated validation,
- transfer success.

---

# Final Architecture Principle

A RECA agent is not defined by having:

- more parameters,
- more compute,
- more memory,
- more optimization power.

It is defined by:

\[
\boxed{
\textbf{
a system where consequences can improve the process that generates future improvement.
}
}
\]

The minimal computational signature:

\[
\boxed{
E
\rightarrow
S
\rightarrow
T
\rightarrow
\sigma
\rightarrow
A_c
\rightarrow
G_{\mathcal V}
}
\]

Axiom Forge does not ask:

> How intelligent is the agent?

It asks:

> Can the agent become better at becoming better?
