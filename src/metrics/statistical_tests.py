"""
statistical_tests.py

Axiom Forge Mk1

Statistical evaluation of the RECA hypothesis.

Core hypothesis:

    D_c × C_e × A_c
              |
              v
            G_V
              |
              v
    long-horizon persistence


This module tests whether RECA variables
predict future performance better than
static capability measures.

Primary questions:

1. Does viability expansion predict future success?
2. Does G_V add information beyond initial reward?
3. Are RECA variables correlated with persistence?
"""

from dataclasses import dataclass
from typing import Dict, List, Any

import math
import statistics



@dataclass
class PredictionResult:
    """
    Result of predictive comparison.
    """

    predictor: str

    correlation: float

    sample_size: int

    interpretation: str



class StatisticalTester:
    """
    Statistical analysis engine.

    Designed for comparing:

        baseline agents

    against:

        RECA agents
    """



    def pearson_correlation(
        self,
        x: List[float],
        y: List[float],
    ) -> float:
        """
        Compute Pearson correlation.

        Used for testing:

            metric(t)
                ->
            future performance
        """

        if len(x) != len(y):
            raise ValueError(
                "Inputs must have equal length"
            )


        if len(x) < 2:
            return 0.0


        mean_x = statistics.mean(x)
        mean_y = statistics.mean(y)


        numerator = sum(
            (
                xi - mean_x
            )
            *
            (
                yi - mean_y
            )
            for xi, yi in zip(x, y)
        )


        denominator_x = math.sqrt(
            sum(
                (
                    xi - mean_x
                ) ** 2
                for xi in x
            )
        )


        denominator_y = math.sqrt(
            sum(
                (
                    yi - mean_y
                ) ** 2
                for yi in y
            )
        )


        if denominator_x == 0 or denominator_y == 0:
            return 0.0


        return (
            numerator
            /
            (
                denominator_x
                *
                denominator_y
            )
        )



    def evaluate_predictor(
        self,
        predictor_values: List[float],
        future_scores: List[float],
        name: str,
    ) -> PredictionResult:
        """
        Test whether a variable predicts
        future capability.
        """

        correlation = (
            self.pearson_correlation(
                predictor_values,
                future_scores,
            )
        )


        if correlation > 0.7:
            interpretation = (
                "Strong predictive relationship"
            )

        elif correlation > 0.4:
            interpretation = (
                "Moderate predictive relationship"
            )

        elif correlation > 0.1:
            interpretation = (
                "Weak predictive relationship"
            )

        else:
            interpretation = (
                "No meaningful relationship"
            )


        return PredictionResult(
            predictor=name,
            correlation=correlation,
            sample_size=len(
                predictor_values
            ),
            interpretation=interpretation,
        )



    def compare_reca_variables(
        self,
        trajectories: List[Dict[str, Any]],
    ):
        """
        Compare predictive power of:

        - initial capability
        - reward
        - viability expansion
        - RECA score

        """

        results = []


        initial_capability = [
            t["initial_reward"]
            for t in trajectories
        ]


        viability_growth = [
            t["G_V"]
            for t in trajectories
        ]


        reca_scores = [
            t["reca_score"]
            for t in trajectories
        ]


        future_performance = [
            t["future_reward"]
            for t in trajectories
        ]



        results.append(
            self.evaluate_predictor(
                initial_capability,
                future_performance,
                "initial_capability",
            )
        )


        results.append(
            self.evaluate_predictor(
                viability_growth,
                future_performance,
                "G_V",
            )
        )


        results.append(
            self.evaluate_predictor(
                reca_scores,
                future_performance,
                "RECA_score",
            )
        )


        return results



    def rank_predictors(
        self,
        results: List[PredictionResult],
    ):
        """
        Rank variables by predictive strength.
        """

        return sorted(
            results,
            key=lambda x: x.correlation,
            reverse=True,
        )



def format_results(
    results: List[PredictionResult],
):
    """
    Human-readable experiment output.
    """

    lines = []

    lines.append(
        "=== ASEB Predictive Analysis ==="
    )


    for result in results:

        lines.append(
            f"""
{result.predictor}
----------------
Correlation:
{result.correlation:.3f}

Samples:
{result.sample_size}

Interpretation:
{result.interpretation}
"""
        )


    return "\n".join(lines)
