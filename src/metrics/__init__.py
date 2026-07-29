"""
Axiom Forge Mk1 — Metrics Module

Contains quantitative measures for evaluating
Recursive Evolutionary Agency.

Core RECA variables:

    recursive_depth
        Measures depth of controllable causal recursion (D_c).

    consequence_coupling
        Measures how strongly environmental consequences
        influence adaptive selection (C_e).

    adaptive_consolidation
        Measures whether successful adaptations become
        persistent adaptive substrate (A_c).

    viability
        Measures expansion of future viable trajectories
        (G_V).

    composite_reca
        Combines the core dimensions into the RECA score.
"""

from .recursive_depth import RecursiveDepth
from .consequence_coupling import ConsequenceCoupling
from .adaptive_consolidation import AdaptiveConsolidation
from .viability import ViabilityMetric
from .composite_reca import CompositeRECA


__all__ = [
    "RecursiveDepth",
    "ConsequenceCoupling",
    "AdaptiveConsolidation",
    "ViabilityMetric",
    "CompositeRECA",
]
