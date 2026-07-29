# Axiom Forge Mk1 Environment Design

## Designing Environments for Recursive Evolutionary Agency

## Abstract

Axiom Forge environments are designed to distinguish:

- systems that optimize,
- systems that adapt,
- systems that improve their own adaptation process.

The benchmark does not reward immediate performance alone.

It evaluates whether environmental interaction produces:

\[
\boxed{
D_c \times C_e \times A_c
\rightarrow
G_{\mathcal V}
}
\]

The environment must therefore create repeated situations where:

1. previous strategies become insufficient,
2. consequences reveal the failure,
3. useful structural changes can persist,
4. future adaptation becomes easier.

---

# 1. Design Principle

## The environment must be non-stationary but structured

A purely random environment is insufficient.

Randomness rewards robustness.

It does not necessarily reward learning.

A RECA environment requires:

\[
\boxed{
\text{change}
+
\text{discoverable structure}
}
\]

The system must be able to extract useful regularities from consequences.

---

# 2. Environment Layers

Each environment contains four components:

\[
E=
(I,O,C,P)
\]

Where:

| Component | Meaning |
|---|---|
| \(I\) | Information available |
| \(O\) | Available actions |
| \(C\) | Consequence function |
| \(P\) | Perturbation process |

---

## Information

What can the system observe?

Examples:

- direct feedback
- delayed feedback
- partial observations
- noisy signals

---

## Actions

What can the system modify?

Examples:

- behavior
- internal representations
- strategies
- learning rules

---

## Consequences

How does reality evaluate changes?

Examples:

- reward
- survival
- resource accumulation
- task completion

---

## Perturbations

How does the environment change?

Examples:

- distribution shift
- new objectives
- resource changes
- novel tasks

---

# 3. Environment Requirements

## Requirement 1 — Consequence Visibility

The system must receive enough information for adaptation.

If consequences are invisible:

\[
C_e\approx0
\]

The system cannot learn from reality.

---

## Requirement 2 — Mechanism Accessibility

Consequences must be able to influence adaptive machinery.

If feedback only changes outputs:

\[
D_c\approx0
\]

The system remains fixed.

---

## Requirement 3 — Persistence Opportunity

Useful adaptations must have somewhere to accumulate.

If every episode resets completely:

\[
A_c\approx0
\]

No evolutionary process can emerge.

---

## Requirement 4 — Future Evaluation

The environment must test whether previous adaptations improve future performance.

Otherwise:

\[
G_{\mathcal V}
\]

cannot be measured.

---

# 4. Core Environment Families

---

# 4.1 Distribution Shift Environments

## Purpose

Test representation flexibility.

---

## Structure

Initial environment:

\[
E_0
\]

Later environment:

\[
E_1
\neq
E_0
\]

but both share hidden structure.

---

## Example

A system learns:

\[
A\rightarrow B
\]

The surface form changes:

\[
A'\rightarrow B
\]

The system must discover the invariant.

---

## Measures

Tests:

- representation expansion
- transfer
- causal abstraction

---

# 4.2 Resource Constraint Environments

## Purpose

Test adaptive restructuring.

---

## Structure

Resources vary:

\[
R_t
\rightarrow
R_{t+1}
\]

Examples:

- lower compute
- reduced memory
- fewer observations
- limited actions

---

## Desired behavior

A non-RECA system:

\[
\text{tries harder}
\]

A RECA system:

\[
\text{changes strategy}
\]

---

## Measures

Tests:

- mechanism revision
- efficiency improvement
- constraint handling

---

# 4.3 Memory Degradation Environments

## Purpose

Test adaptive consolidation.

---

## Structure

The system experiences:

\[
M_t
\rightarrow
M_t-\Delta M
\]

The question:

Did adaptation become structural?

---

## Non-RECA signature

\[
\text{learning}
\rightarrow
\text{forgetting}
\rightarrow
\text{relearning}
\]

---

## RECA signature

\[
\text{learning}
\rightarrow
\text{compression}
\rightarrow
\text{transfer}
\]

---

# 4.4 Objective Drift Environments

## Purpose

Test consequence coupling.

---

## Structure

The evaluation function changes:

\[
C_t
\neq
C_{t+1}
\]

---

## Example

A system optimizes:

\[
X
\]

The environment changes so:

\[
Y
\]

becomes valuable.

---

## Measure

Can the system detect that its selection criteria need revision?

---

# 4.5 Novel Task Generation

## Purpose

Directly measure viability expansion.

---

## Structure

After adaptation:

Generate unseen tasks:

\[
T_{future}
\]

Measure:

\[
|\mathcal T_{reachable}|
\]

---

## Question

Did past adaptation increase future capability?

---

# 5. The Mk1 Environment

The first implementation should be intentionally simple.

Goal:

Not maximum realism.

Goal:

Separate adaptive regimes.

---

## Proposed Mk1 World

### Adaptive Grid World

A procedurally generated environment containing:

- changing rules,
- hidden causal structure,
- limited resources,
- persistent memory,
- novel future tasks.

---

## Agent Classes

Compare:

### Fixed agent

No internal modification.

---

### Learning agent

Updates policy.

---

### Meta-learning agent

Updates learning process.

---

### RECA agent

Can modify and preserve adaptive mechanisms.

---

# 6. Perturbation Schedule

A benchmark run:

\[
E_1,E_2,...,E_n
\]

contains phases:

---

## Phase A — Familiarization

Agent learns environment.

Measure:

\[
R_0
\]

---

## Phase B — Shock

Introduce:

\[
\Delta E
\]

Measure:

- recovery
- adaptation

---

## Phase C — Consolidation

Allow structural changes.

Measure:

\[
A_c
\]

---

## Phase D — Transfer

Introduce new environments.

Measure:

\[
G_{\mathcal V}
\]

---

# 7. Anti-Gaming Constraints

The environment must prevent shortcuts.

---

## No single optimal policy

Otherwise:

\[
\text{optimization}
\approx
\text{evolution}
\]

---

## No infinite exploration

Otherwise:

\[
|\mathcal V|
\]

is inflated artificially.

---

## Reward future adaptation

The system should benefit from:

- reusable knowledge
- better representations
- improved learning mechanisms

---

# 8. Environment Evaluation Metrics

Each environment should report:

| Metric | Question |
|-|-|
| Recovery | How quickly does the system adapt? |
| Transfer | Does learning generalize? |
| Consolidation | Are improvements retained? |
| Novel reachability | Are new futures accessible? |
| Viability growth | Did adaptive capacity expand? |

---

# 9. Success Criterion

A successful RECA environment should produce:

\[
\boxed{
G_{\mathcal V}>0
}
\]

for systems that possess:

\[
D_c,C_e,A_c>0
\]

while separating them from:

- fixed optimizers,
- reactive learners,
- unstable self-modifiers.

---

# 10. Final Design Principle

The benchmark environment should create a world where:

\[
\boxed{
\text{past adaptation changes the quality of future adaptation}
}
\]

The decisive signal:

\[
\boxed{
\text{failure today creates advantage tomorrow}
}
\]

Axiom Forge environments are therefore not tests of intelligence.

They are tests of whether adaptive systems can convert environmental consequences into an expanding capacity for future adaptation.
