# Axiom Forge Mk1 Metrics

## Measuring Recursive Evolutionary Agency

## Abstract

Axiom Forge evaluates whether adaptive systems can transform environmental consequences into improvements of future adaptive capacity.

The benchmark is based on four primary quantities:

\[
\boxed{
D_c \times C_e \times A_c \rightarrow G_{\mathcal V}
}
\]

Where:

| Symbol | Name | Function |
|---|---|---|
| \(D_c\) | Recursive Depth | How deeply consequences can modify adaptive machinery |
| \(C_e\) | Consequence Coupling | How strongly consequences select adaptive changes |
| \(A_c\) | Adaptive Consolidation | How strongly useful changes persist |
| \(G_{\mathcal V}\) | Viability Expansion | Whether future viable reachability increases |

These metrics are not intended to measure intelligence directly.

They measure whether adaptation itself remains capable of improving.

---

# 1. Recursive Depth

\[
D_c
\]

## Definition

Recursive Depth measures how far environmental consequences penetrate into the causal structure responsible for future adaptation.

The question:

> What internal variables can reality modify?

---

## Conceptual hierarchy

### Output-level feedback

\[
E\rightarrow A
\]

Depth:

\[
D_c\approx0
\]

Consequences affect success but not the mechanism.

---

### State-level feedback

\[
E\rightarrow S
\]

The system updates internal state.

---

### Rule-level feedback

\[
E\rightarrow S\rightarrow T
\]

The system changes how it learns.

---

### Selection-level feedback

\[
E\rightarrow S\rightarrow T\rightarrow\sigma
\]

The system changes the process selecting future adaptations.

---

## Candidate estimator

Define:

\[
D_c=
\sum_i w_i I(E:M_i)
\]

where:

- \(M_i\) = adaptive mechanism layer
- \(I(E:M_i)\) = causal influence of environmental consequences on that layer
- \(w_i\) = depth weighting

Higher values indicate deeper causal penetration.

---

## Experimental measurement

Possible methods:

- intervention experiments
- causal ablation
- mechanism tracing
- perturbation response analysis

Question:

If the environment changes, what internal structures change?

---

# 2. Consequence Coupling

\[
C_e
\]

## Definition

Consequence Coupling measures whether environmental consequences actually determine which adaptive modifications persist.

The key distinction:

\[
\text{change}
\neq
\text{selected change}
\]

---

## Conceptual requirement

A system must satisfy:

\[
\Delta F
\rightarrow
\Delta F_{\text{retained}}
\]

where retention depends on consequences.

---

## Candidate estimator

\[
C_e=
P(Retention|Positive\ Consequence)
-
P(Retention|Neutral\ Consequence)
\]

High:

Successful modifications are preferentially preserved.

Low:

Changes persist independently of outcomes.

---

## Experimental measurement

Procedure:

1. Generate adaptive modifications.
2. Apply environmental evaluation.
3. Measure which modifications remain.
4. Compare retention rates.

---

## Failure signature

Low \(C_e\):

\[
\Delta F\neq0
\]

but:

\[
\Delta F_{\text{selected}}\approx0
\]

The system changes without evolutionary direction.

---

# 3. Adaptive Consolidation

\[
A_c
\]

## Definition

Adaptive Consolidation measures whether useful adaptive changes become part of the future adaptive substrate.

The key question:

> Does today's adaptation improve tomorrow's adaptation?

---

## Conceptual model

Without consolidation:

\[
Adaptation_t
\rightarrow
Recovery_t
\rightarrow
Reset
\]

With consolidation:

\[
Adaptation_t
\rightarrow
Substrate_{t+1}
\rightarrow
Improved\ Adaptation_{t+1}
\]

---

## Candidate estimator

\[
A_c=
\frac{
Transfer_{future}
-
Baseline_{future}
}
{
Initial\ improvement
+\epsilon
}
\]

Measures how much previous adaptation transfers into future contexts.

---

## Experimental measurement

Tests:

- delayed evaluation
- new task families
- distribution shifts
- memory disruption
- transfer learning

---

## Failure signature

Low \(A_c\):

The system repeatedly solves the same problem without accumulating capability.

---

# 4. Viability Expansion

\[
G_{\mathcal V}
\]

## Primary Metric

Viability Expansion is the central outcome variable.

Definition:

\[
G_{\mathcal V}
=
\Delta |\mathcal V_\tau^*|
\]

where:

\[
\mathcal V_\tau^*
\]

is the set of future states reachable while maintaining adaptive viability.

---

# 4.1 Viability Space

A system does not maximize all possible futures.

It maximizes:

\[
\boxed{
\text{reachable viable futures}
}
\]

Randomness may increase possibility:

\[
|\mathcal V|\uparrow
\]

while reducing usefulness.

The target:

\[
|\mathcal V_\tau^*|
\]

---

# 4.2 Candidate Estimators

Because direct measurement is difficult, Axiom Forge uses proxies.

---

## Future Task Reachability

Measure:

\[
|\mathcal T_{reachable}|
\]

After adaptation:

How many new task families can the system solve?

---

## Perturbation Survival

Sample future environments:

\[
E_1,E_2,...,E_n
\]

Measure:

\[
P(success|E_i)
\]

---

## Adaptation Efficiency

Measure:

\[
\frac{\Delta R}{\Delta time}
\]

after environmental changes.

---

## Representation Expansion

Measure whether the system develops reusable internal structures.

---

# 5. Composite RECA Score

The benchmark may define:

\[
RECA=
D_c^\alpha
C_e^\beta
A_c^\gamma
G_{\mathcal V}^\delta
\]

where:

\[
\alpha,\beta,\gamma,\delta
\]

are experimentally determined weights.

The initial assumption:

\[
\alpha=\beta=\gamma=1
\]

should not be considered fixed.

---

# 6. Temporal Metrics

Static values are insufficient.

Axiom Forge evaluates trajectories.

---

## Recovery Rate

\[
\rho
\]

How quickly does the system return to viability after disruption?

---

## Adaptive Improvement Rate

\[
\dot{A}
\]

Does adaptation itself improve over time?

---

## Viability Growth Rate

\[
\Gamma_{\mathcal V}
=
\frac{\Delta\mathcal V_\tau^*}{\Delta t}
\]

The primary evolutionary signature.

---

# 7. Metric Relationships

The proposed causal model:

\[
\boxed{
D_c
\times
C_e
\times
A_c
\rightarrow
G_{\mathcal V}
\rightarrow
R(t+n)
}
\]

The benchmark tests whether this relationship exists.

---

# 8. Measurement Challenges

## Challenge 1: Defining Viability

Future possibility cannot be measured exhaustively.

Solution:

Use sampled approximation:

\[
\hat{\mathcal V}_\tau^*
\]

---

## Challenge 2: Separating Capability From Evolvability

A powerful system may also be highly evolvable.

Solution:

Control initial capability:

\[
R_A(0)\approx R_B(0)
\]

---

## Challenge 3: Avoiding Circular Metrics

Metrics must not simply reward performance.

A system should not score high because it already performs well.

The metric should measure:

\[
\text{improvement of future adaptation}
\]

not:

\[
\text{current ability}
\]

---

# 9. Falsification

Axiom Forge fails if:

- \(G_{\mathcal V}\) cannot be measured independently.
- \(D_c,C_e,A_c\) do not predict \(G_{\mathcal V}\).
- \(G_{\mathcal V}\) does not predict future persistence.
- Existing metrics explain all variance.

---

# 10. Summary

The minimal measurable hypothesis:

\[
\boxed{
D_c\times C_e\times A_c
\rightarrow
G_{\mathcal V}
\rightarrow
\text{future adaptive persistence}
}
\]

The benchmark does not ask:

> How capable is the system?

It asks:

> Does experience make the system better at becoming capable?

The defining signature of Recursive Evolutionary Agency:

\[
\boxed{
\Delta\mathcal V_\tau^*>0
}
\]

under environmental pressure.

Axiom Forge exists to determine whether this quantity is real, measurable, and predictive.
