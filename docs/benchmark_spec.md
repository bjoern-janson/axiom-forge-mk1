# Axiom Forge Mk1 Benchmark Specification

## Recursive Evolutionary Agency Benchmark (RECA-Bench)

## Abstract

Axiom Forge defines a benchmark for measuring whether adaptive systems can improve their own capacity for future adaptation.

Traditional benchmarks evaluate:

\[
R_t
\]

current performance.

RECA-Bench evaluates:

\[
G_{\mathcal V}
\]

future viability expansion.

The central question:

> When exposed to environmental consequences, does a system merely recover, or does it become structurally better at adapting to future change?

---

# 1. Benchmark Objective

The benchmark tests the hypothesis:

\[
\boxed{
D_c \times C_e \times A_c
\rightarrow
G_{\mathcal V}
\rightarrow
P(\text{long-horizon persistence})
}
\]

Where:

| Variable | Meaning |
|---|---|
| \(D_c\) | Recursive depth |
| \(C_e\) | Consequence coupling |
| \(A_c\) | Adaptive consolidation |
| \(G_{\mathcal V}\) | Viability expansion |

The benchmark is successful if:

\[
G_{\mathcal V}
\]

predicts future adaptive performance better than static capability measures.

---

# 2. Evaluation Philosophy

The benchmark does not ask:

> Which system performs best immediately?

It asks:

> Which system improves its ability to remain adaptive after experiencing change?

A system is evaluated by trajectory:

\[
X_0
\rightarrow
X_1
\rightarrow
X_2
\rightarrow
...
\rightarrow
X_n
\]

rather than final score alone.

---

# 3. Experimental Structure

Each experiment contains four phases:

1. Baseline measurement
2. Environmental perturbation
3. Adaptive response
4. Future viability evaluation

---

# Phase 1 — Baseline Capability

Measure initial capability:

\[
R_0
\]

Metrics:

- task performance
- resource efficiency
- sample efficiency
- generalization ability

Systems should be matched where possible:

\[
R_A(0)\approx R_B(0)
\]

to isolate evolvability differences.

---

# Phase 2 — Environmental Perturbation

Systems encounter changing environments:

\[
E_1,E_2,...,E_n
\]

Perturbations should create situations where existing strategies become insufficient.

---

# 4. Perturbation Families

## 4.1 Distribution Shift

Tests:

\[
\text{representation flexibility}
\]

Examples:

- changed input distributions
- altered task statistics
- new environmental regimes

Question:

Can the system revise assumptions?

---

## 4.2 Resource Constraints

Tests:

\[
\text{adaptive efficiency}
\]

Examples:

- reduced compute
- reduced memory
- limited observations
- delayed feedback

Question:

Can the system restructure under constraint?

---

## 4.3 Memory Degradation

Tests:

\[
A_c
\]

Examples:

- removal of learned information
- corrupted memory
- partial forgetting

Question:

Were improvements structurally integrated?

---

## 4.4 Objective Corruption

Tests:

\[
C_e
\]

Examples:

- misleading rewards
- changing goals
- conflicting objectives

Question:

Does the system distinguish useful adaptation from local optimization?

---

## 4.5 Novel Task Families

Tests:

\[
G_{\mathcal V}
\]

Examples:

- unseen task categories
- new causal structures
- unfamiliar environments

Question:

Did previous adaptation expand future capability?

---

# 5. System Classes

RECA-Bench compares systems across adaptive depth.

---

## Class 0 — Fixed Optimizers

Properties:

\[
D_c\approx0
\]

Characteristics:

- fixed algorithm
- fixed representation
- no internal adaptation

Expected:

\[
G_{\mathcal V}\approx0
\]

---

## Class 1 — Adaptive Systems

Properties:

\[
D_c>0
\]

Characteristics:

- state updates
- learning
- memory

Expected:

Improved recovery but limited mechanism evolution.

---

## Class 2 — Meta-Adaptive Systems

Properties:

\[
D_c\uparrow
\]

Characteristics:

- learned update rules
- architecture adaptation
- optimizer modification

Expected:

Improved learning efficiency.

---

## Class 3 — Recursive Evolutionary Systems

Properties:

\[
D_c>0
\]

\[
C_e>0
\]

\[
A_c>0
\]

Characteristics:

- adaptive mechanism revision
- consequence-based selection
- persistent structural improvement

Expected:

\[
G_{\mathcal V}>0
\]

---

# 6. Core Metrics

## 6.1 Recursive Depth

\[
D_c
\]

Question:

How deeply can consequences modify the adaptive process?

Possible measurements:

- number of adaptive layers reachable by feedback
- modification distance from output to mechanism
- causal influence mapping

---

## 6.2 Consequence Coupling

\[
C_e
\]

Question:

Do environmental consequences determine which changes persist?

Possible measurements:

\[
C_e
=
P(\text{retention}|\text{improved consequence})
-
P(\text{retention}|\text{neutral consequence})
\]

---

## 6.3 Adaptive Consolidation

\[
A_c
\]

Question:

Do useful changes persist into future adaptation?

Possible measurements:

- transfer performance
- cross-task reuse
- resistance to catastrophic forgetting
- retained improvement after perturbation

---

## 6.4 Viability Expansion

\[
G_{\mathcal V}
\]

Primary benchmark quantity.

Approximation:

\[
G_{\mathcal V}
=
\Delta|\mathcal V_\tau^*|
\]

where:

\[
\mathcal V_\tau^*
\]

represents future reachable viable states.

Possible proxies:

- number of successfully solved future task families
- robustness across environmental changes
- reachable policy space
- representation expansion
- adaptation speed on novel tasks

---

# 7. Primary Experimental Prediction

The benchmark tests:

\[
\boxed{
G_{\mathcal V}(t)
\rightarrow
R(t+n)
}
\]

The prediction:

A system with higher viability expansion should outperform systems with higher initial capability after sufficient environmental change.

Expected divergence:

Initial:

\[
R_A>R_B
\]

but:

\[
G_{\mathcal V,B}>G_{\mathcal V,A}
\]

After repeated perturbations:

\[
R_B(t)>R_A(t)
\]

---

# 8. Control Conditions

Experiments should control for:

- compute budget
- parameter count
- training time
- environment exposure
- initial performance
- information availability

The goal is to isolate:

\[
\text{evolvability}
\]

from:

\[
\text{raw capability}
\]

---

# 9. Required Results

A successful result would show:

\[
\boxed{
G_{\mathcal V}
>
R_0
}
\]

as a predictor of future performance.

Meaning:

The ability to expand future adaptive capacity predicts future success better than current competence.

---

# 10. Failure Conditions

The benchmark falsifies RECA if:

1. \(G_{\mathcal V}\) is indistinguishable from current performance.
2. \(D_c,C_e,A_c\) do not predict viability expansion.
3. High viability expansion does not improve persistence.
4. Systems cannot be separated by the proposed metrics.

---

# 11. Minimal Implementation Roadmap

## Mk1.0 — Toy Environments

Goal:

Validate whether the metrics separate adaptive regimes.

Examples:

- grid worlds
- evolutionary games
- symbolic environments

---

## Mk1.1 — Multi-Agent Environments

Goal:

Test consequence coupling and selection dynamics.

Examples:

- competing agents
- changing incentives
- resource competition

---

## Mk1.2 — Open-Ended Environments

Goal:

Test long-horizon viability expansion.

Examples:

- generated task families
- dynamic worlds
- continual learning environments

---

# Final Benchmark Principle

Axiom Forge does not measure:

\[
\text{how intelligent a system is}
\]

It measures:

\[
\boxed{
\text{whether a system can improve the process by which it becomes intelligent}
}
\]

The central experimental question:

\[
\boxed{
\text{Does failure become a source of future adaptive advantage?}
}
\]
