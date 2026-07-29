"""
viability.py

ASEB / RECA Benchmark Metrics

Core idea:
    Evolvability is not current performance.
    Evolvability is expansion of future viable reachable states.

This module implements practical estimators for:

    V_tau(X)
        Approximation of viable reachable state space.

    G_V
        Viability expansion after adaptation.

Theoretical target:

    ΔV_tau > 0

meaning:

    adapted system has access to a larger set of future viable trajectories.

This is an approximation layer for experiments.
"""

from dataclasses import dataclass
from typing import Callable, Iterable, Sequence
import math


@dataclass
class ViabilityEstimate:
    """
    Snapshot of estimated future viability.
    """

    reachable_states: int
    viable_states: int
    viability_ratio: float


@dataclass
class ViabilityExpansion:
    """
    Change in viability after adaptation.
    """

    before: ViabilityEstimate
    after: ViabilityEstimate

    delta_viable_states: int
    delta_ratio: float
    expansion_score: float


def estimate_viability(
    trajectories: Iterable[Sequence],
    viability_fn: Callable[[Sequence], bool],
) -> ViabilityEstimate:
    """
    Estimate viable reachable space.

    Parameters
    ----------
    trajectories:
        Sampled future trajectories from a system.

    viability_fn:
        Function deciding whether a trajectory remains viable.

    Returns
    -------
    ViabilityEstimate

    Notes
    -----
    This approximates:

        V_tau(X)

    using sampled reachable futures.

    A trajectory is counted as viable if it remains
    within adaptive bounds.
    """

    trajectories = list(trajectories)

    if len(trajectories) == 0:
        return ViabilityEstimate(
            reachable_states=0,
            viable_states=0,
            viability_ratio=0.0,
        )

    viable = [
        trajectory
        for trajectory in trajectories
        if viability_fn(trajectory)
    ]

    return ViabilityEstimate(
        reachable_states=len(trajectories),
        viable_states=len(viable),
        viability_ratio=len(viable) / len(trajectories),
    )


def compute_viability_expansion(
    before: ViabilityEstimate,
    after: ViabilityEstimate,
) -> ViabilityExpansion:
    """
    Compute G_V.

    The simplest estimator:

        G_V = Δ viable reachable futures

    Positive values indicate expansion.
    """

    delta_states = (
        after.viable_states -
        before.viable_states
    )

    delta_ratio = (
        after.viability_ratio -
        before.viability_ratio
    )

    # Normalize by previous viable space
    # to measure relative expansion.
    if before.viable_states > 0:
        expansion_score = (
            delta_states /
            before.viable_states
        )
    else:
        expansion_score = float(delta_states)

    return ViabilityExpansion(
        before=before,
        after=after,
        delta_viable_states=delta_states,
        delta_ratio=delta_ratio,
        expansion_score=expansion_score,
    )


def viability_gradient(
    history: Sequence[ViabilityEstimate],
) -> float:
    """
    Estimate:

        dV/dt

    over an experiment.

    Positive values indicate increasing
    viable future reachability.
    """

    if len(history) < 2:
        return 0.0

    start = history[0].viable_states
    end = history[-1].viable_states

    return (end - start) / (len(history) - 1)


def persistence_score(
    viability_history: Sequence[ViabilityEstimate],
) -> float:
    """
    Measures whether viability is maintained.

    A system that repeatedly collapses after shocks
    should score lower.

    Future versions may incorporate:
        - recovery time
        - adaptive debt
        - perturbation severity
    """

    if not viability_history:
        return 0.0

    ratios = [
        estimate.viability_ratio
        for estimate in viability_history
    ]

    return sum(ratios) / len(ratios)


def compare_systems(
    system_a_history: Sequence[ViabilityEstimate],
    system_b_history: Sequence[ViabilityEstimate],
) -> dict:
    """
    Compare two adaptive systems.

    Intended use:

        RECA agent vs baseline

    """

    return {
        "system_a": {
            "viability_gradient":
                viability_gradient(system_a_history),
            "persistence":
                persistence_score(system_a_history),
        },
        "system_b": {
            "viability_gradient":
                viability_gradient(system_b_history),
            "persistence":
                persistence_score(system_b_history),
        },
    }
