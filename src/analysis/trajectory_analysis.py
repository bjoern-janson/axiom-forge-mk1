"""
trajectory_analysis.py

Axiom Forge Mk1

Trajectory Analysis

Transforms long-horizon experiment data into
measurable evolutionary signals.

Central hypothesis:

    D_c × C_e × A_c
              |
              v
            G_V
              |
              v
    long-horizon persistence


The important variable is not:

    current performance

but:

    change in future adaptive capacity
"""


from dataclasses import dataclass
from typing import Dict, List, Any
import statistics



@dataclass
class TrajectoryMetrics:
    """
    Summary statistics for an adaptive trajectory.
    """

    initial_viability: float

    final_viability: float

    viability_growth: float

    average_reward: float

    recovery_speed: float

    viability_volatility: float

    reca_mean: float



class TrajectoryAnalyzer:
    """
    Computes evolutionary trajectory metrics.
    """

    def analyze(
        self,
        horizon_result,
    ) -> TrajectoryMetrics:
        """
        Analyze a HorizonResult object.
        """

        steps = horizon_result.steps


        if not steps:
            return TrajectoryMetrics(
                initial_viability=0.0,
                final_viability=0.0,
                viability_growth=0.0,
                average_reward=0.0,
                recovery_speed=0.0,
                viability_volatility=0.0,
                reca_mean=0.0,
            )


        viability = [
            step.viability
            for step in steps
        ]


        rewards = [
            step.reward
            for step in steps
        ]


        reca_scores = [
            step.reca_score
            for step in steps
        ]


        initial = viability[0]

        final = viability[-1]


        return TrajectoryMetrics(

            initial_viability=
                initial,

            final_viability=
                final,

            viability_growth=
                final - initial,

            average_reward=
                statistics.mean(
                    rewards
                ),

            recovery_speed=
                self.recovery_velocity(
                    viability
                ),

            viability_volatility=
                self.volatility(
                    viability
                ),

            reca_mean=
                statistics.mean(
                    reca_scores
                ),
        )



    def recovery_velocity(
        self,
        viability: List[float],
    ) -> float:
        """
        Measures how quickly viability
        returns after disruption.

        Higher is better.

        Approximation:

            ΔV / Δt
        """

        if len(viability) < 2:
            return 0.0


        improvements = []


        for i in range(1, len(viability)):

            delta = (
                viability[i]
                -
                viability[i - 1]
            )

            if delta > 0:
                improvements.append(
                    delta
                )


        if not improvements:
            return 0.0


        return statistics.mean(
            improvements
        )



    def volatility(
        self,
        values: List[float],
    ) -> float:
        """
        Measures instability.

        Lower can indicate
        more consolidated adaptation.
        """

        if len(values) < 2:
            return 0.0


        return statistics.stdev(
            values
        )



    def compare_prediction_power(
        self,
        results: Dict[str, Any],
    ):
        """
        Compare whether RECA metrics predict
        future performance.

        Placeholder for statistical analysis.

        Future:

            regression:
            
            future_reward =
                β0
                +
                β1(current_reward)
                +
                β2(G_V)

        """

        dataset = {}


        for name, result in results.items():

            dataset[name] = (
                self.analyze(result)
            )


        return dataset



def estimate_viability_expansion(
    metrics: TrajectoryMetrics,
) -> float:
    """
    Estimate G_V.

    Simplified:

        G_V ≈ Δ viable capacity

    Future versions may include:

        reachable task manifold
        transfer performance
        counterfactual robustness
    """

    return (
        metrics.viability_growth
        *
        (
            1
            -
            metrics.viability_volatility
        )
    )



def rank_agents(
    metrics: Dict[str, TrajectoryMetrics],
):
    """
    Rank agents by estimated
    evolutionary capacity.
    """

    scores = {}


    for name, metric in metrics.items():

        scores[name] = (
            estimate_viability_expansion(
                metric
            )
        )


    return sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True,
    )
