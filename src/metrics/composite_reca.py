"""
Composite RECA Metric

Axiom Forge Mk1

Computes the composite Recursive Evolutionary Agency (RECA)
index from the three causal primitives:

    D_c = Recursive Depth
    C_e = Consequence Coupling
    A_c = Adaptive Consolidation

Core hypothesis:

    RECA = D_c * C_e * A_c

The composite score is not intended as an intelligence metric.
It estimates whether an adaptive system has the causal structure
required for evolvability.

Pipeline:

    environmental consequence
            |
            v
    recursive access (D_c)
            |
            v
    consequence filtering (C_e)
            |
            v
    adaptive consolidation (A_c)
            |
            v
    viability expansion (G_V)
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class RECAResult:
    """
    Result container for composite RECA evaluation.
    """

    recursive_depth: float
    consequence_coupling: float
    adaptive_consolidation: float
    reca_score: float

    def as_dict(self) -> Dict[str, float]:
        return {
            "D_c": self.recursive_depth,
            "C_e": self.consequence_coupling,
            "A_c": self.adaptive_consolidation,
            "RECA": self.reca_score,
        }


def compute_reca(
    recursive_depth: float,
    consequence_coupling: float,
    adaptive_consolidation: float,
) -> float:
    """
    Compute composite Recursive Evolutionary Agency.

    Formula:

        RECA = D_c * C_e * A_c

    All inputs should be normalized:

        0 <= value <= 1

    A multiplicative formulation is used because each component
    represents a necessary causal bottleneck.
    """

    validate_metric(recursive_depth)
    validate_metric(consequence_coupling)
    validate_metric(adaptive_consolidation)

    return (
        recursive_depth
        * consequence_coupling
        * adaptive_consolidation
    )


def evaluate_reca(
    recursive_depth: float,
    consequence_coupling: float,
    adaptive_consolidation: float,
) -> RECAResult:
    """
    Full RECA evaluation returning component values
    and composite score.
    """

    score = compute_reca(
        recursive_depth,
        consequence_coupling,
        adaptive_consolidation,
    )

    return RECAResult(
        recursive_depth=recursive_depth,
        consequence_coupling=consequence_coupling,
        adaptive_consolidation=adaptive_consolidation,
        reca_score=score,
    )


def viability_prediction_proxy(
    reca_score: float,
    viability_growth: float,
) -> Dict[str, float]:
    """
    Stores the predicted relationship:

        RECA -> G_V

    This does not claim causality.
    It provides data for benchmark analysis.
    """

    validate_metric(reca_score)
    validate_metric(viability_growth)

    return {
        "RECA": reca_score,
        "G_V": viability_growth,
    }


def validate_metric(value: float) -> None:
    """
    Ensure normalized metric values.
    """

    if not 0 <= value <= 1:
        raise ValueError(
            "RECA components must be normalized between 0 and 1."
        )
