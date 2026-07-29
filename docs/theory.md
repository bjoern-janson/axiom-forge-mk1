# Axiom Forge Mk1 Theory

## Recursive Evolutionary Agency (RECA)

## Abstract

Axiom Forge studies a specific transition in adaptive systems:

The transition from systems that **adapt** to systems whose **capacity for adaptation itself can evolve**.

The central hypothesis is:

> Recursive Evolutionary Agency emerges when environmental consequences penetrate adaptive control, select among adaptive modifications, and consolidate successful changes into structures that expand future viable adaptive trajectories.

The framework does not attempt to define intelligence.

Instead, it studies the conditions under which adaptive processes remain capable of improving.

---

# 1. The Central Distinction

Adaptive systems exist along a hierarchy defined by the depth at which environmental consequences can influence internal processes.

The key question:

> Where does environmental feedback terminate?

---

# Level 0 — Optimization

## Feedback endpoint: output

\[
E \rightarrow A
\]

The environment evaluates actions, but the mechanism producing those actions remains fixed.

Examples:

- fixed optimization algorithms
- static search procedures
- traditional solvers

The system can find solutions but cannot change the process that generates solutions.

---

# Level 1 — Adaptation

## Feedback endpoint: state

\[
E \rightarrow S
\]

The environment modifies internal state.

\[
S_{t+1}=T(S_t,E_t)
\]

The system learns from experience.

However:

\[
T=\text{constant}
\]

The mechanism of adaptation itself does not change.

---

# Level 2 — Meta-Adaptation

## Feedback endpoint: transformation rule

\[
E \rightarrow S \rightarrow T
\]

The system can modify the process by which it changes.

\[
T_{t+1}=M(T_t,E_t)
\]

Examples:

- learned optimizers
- architecture adaptation
- meta-learning systems

The system can improve how it learns.

---

# Level 3 — Recursive Evolutionary Agency

## Feedback endpoint: selection dynamics

\[
\boxed{
E \rightarrow S \rightarrow T \rightarrow \sigma
}
\]

The system can modify the mechanisms determining which adaptive changes persist.

The critical transition:

\[
\boxed{
\text{selection itself becomes adaptive}
}
\]

The system does not merely change.

It changes the process by which changes survive.

---

# 2. The Minimal Causal Invariant

Recursive Evolutionary Agency requires three conditions.

\[
\boxed{
D_c \times C_e \times A_c \rightarrow G_{\mathcal V}
}
\]

---

# 2.1 Recursive Depth (\(D_c\))

## Definition

The depth to which environmental consequences can penetrate adaptive machinery.

A system with low \(D_c\):

\[
E \rightarrow A
\]

A system with high \(D_c\):

\[
E \rightarrow S \rightarrow T \rightarrow \sigma
\]

Without recursive depth, consequences cannot modify future adaptation mechanisms.

Failure mode:

\[
\text{frozen adaptation}
\]

---

# 2.2 Consequence Coupling (\(C_e\))

## Definition

The degree to which environmental consequences determine which adaptive changes persist.

Self-modification alone is insufficient.

A system may have:

\[
\Delta T \neq 0
\]

without:

\[
\Delta T_{\text{selected}}
\]

Evolution requires:

\[
\text{variation}
+
\text{consequence-dependent selection}
\]

Failure mode:

\[
\text{ungrounded drift}
\]

---

# 2.3 Adaptive Consolidation (\(A_c\))

## Definition

The ability to preserve successful adaptive changes as part of the future adaptive substrate.

Without consolidation:

\[
\text{adaptation}
\rightarrow
\text{temporary recovery}
\]

With consolidation:

\[
F_t\rightarrow F_{t+1}
\]

Future adaptation begins from a transformed foundation.

Failure mode:

\[
\text{ephemeral adaptation}
\]

---

# 3. The Viability Object

Current performance is not the primary object.

A system may improve current capability while reducing future adaptability.

Define:

\[
\mathcal V_\tau^*(X_t)
\]

as:

\[
\{\text{future states reachable while remaining adaptively viable}\}
\]

The RECA condition:

\[
\boxed{
\Delta\mathcal V_\tau^*>0
}
\]

means that adaptive experience expands future viable trajectories.

---

# 4. Capability vs Evolvability

Axiom Forge distinguishes:

## Capability

\[
R_t
\]

"What can the system do now?"

---

## Evolvability

\[
G_{\mathcal V}
\]

"Does the system become better at producing future capability?"

These quantities are not assumed to be identical.

A system may have:

\[
R_A>R_B
\]

but:

\[
G_{\mathcal V,B}>G_{\mathcal V,A}
\]

Under repeated environmental change:

\[
R_B(t)>R_A(t)
\]

may emerge.

---

# 5. Adaptive Inheritance

The core evolutionary property is:

\[
\boxed{
\text{successful adaptation becomes the substrate for future adaptation}
}
\]

This does not require biological inheritance.

It requires that previous adaptive success modifies the starting conditions of future adaptation.

The causal loop:

\[
\text{consequence}
\rightarrow
\text{selection}
\rightarrow
\text{consolidation}
\rightarrow
\text{future adaptive improvement}
\]

---

# 6. Failure Modes

Axiom Forge identifies four major failure regimes.

| Regime | Missing Property | Result |
|---|---|---|
| Frozen | \(D_c\) | Cannot modify adaptive machinery |
| Drifting | \(C_e\) | Changes without environmental grounding |
| Ephemeral | \(A_c\) | Discovers improvements but loses them |
| RECA | All present | Builds cumulative adaptive capacity |

---

# 7. Falsifiable Predictions

The framework makes one primary prediction:

\[
\boxed{
G_{\mathcal V}(t)
\rightarrow
R(t+n)
}
\]

Future viability expansion should predict long-horizon capability better than current capability alone.

This can be tested against:

- benchmark score
- reward
- compute
- parameter count
- architecture size

---

# 8. Falsification Criteria

Axiom Forge fails if:

1. \(G_{\mathcal V}\) provides no predictive value beyond current capability.
2. Systems with higher \(D_c,C_e,A_c\) do not show increased viability expansion.
3. Viability expansion does not improve persistence under distribution shift.
4. The proposed metrics cannot be operationalized independently of performance.

---

# 9. Summary

The central claim:

\[
\boxed{
\textbf{
Recursive Evolutionary Agency occurs when environmental consequences penetrate adaptive control, select among adaptive modifications, and consolidate successful changes into structures that expand future viable adaptive trajectories.
}
}
\]

Compressed:

\[
\boxed{
\textbf{
Evolution begins when successful adaptation becomes the substrate for future adaptation.}
}
\]

Axiom Forge exists to test whether this property can be measured.
