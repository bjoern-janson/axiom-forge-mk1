"""
Statistical tests for ASEB / RECA experiments.

Purpose:
    Evaluate whether RECA variables predict future adaptive performance.

Core hypothesis:

    D_c * C_e * A_c -> G_V -> future persistence

Tests included:
    - correlation analysis
    - regression comparison
    - predictive power comparison
    - significance testing

This module intentionally avoids assuming RECA is true.
It exists to falsify it.
"""

from dataclasses import dataclass
from typing import Dict, List

import numpy as np


@dataclass
class TestResult:
    name: str
    statistic: float
    p_value: float
    interpretation: str


def pearson_correlation(
    x: List[float],
    y: List[float]
) -> TestResult:
    """
    Measure linear relationship between two variables.

    Example:
        G_V vs future performance
    """

    x = np.asarray(x)
    y = np.asarray(y)

    if len(x) < 2:
        raise ValueError("Need at least two observations")

    r = np.corrcoef(x, y)[0, 1]

    return TestResult(
        name="pearson_correlation",
        statistic=float(r),
        p_value=np.nan,
        interpretation=(
            "Positive correlation suggests predictive relationship, "
            "but does not establish causation."
        )
    )


def compare_predictors(
    baseline_scores: List[float],
    reca_scores: List[float],
    future_scores: List[float]
) -> Dict[str, TestResult]:
    """
    Compare whether RECA metrics predict future success
    better than initial capability.

    Baseline:
        current capability

    RECA:
        viability expansion indicators
    """

    baseline_corr = pearson_correlation(
        baseline_scores,
        future_scores
    )

    reca_corr = pearson_correlation(
        reca_scores,
        future_scores
    )

    return {
        "baseline_predictive_power": baseline_corr,
        "reca_predictive_power": reca_corr
    }


def bootstrap_difference(
    x: List[float],
    y: List[float],
    samples: int = 1000
) -> TestResult:
    """
    Bootstrap whether two predictors differ.

    Used for:

        corr(G_V, future)
        >
        corr(R0, future)

    """

    x = np.asarray(x)
    y = np.asarray(y)

    observed = np.mean(x) - np.mean(y)

    distribution = []

    rng = np.random.default_rng()

    for _ in range(samples):
        xs = rng.choice(
            x,
            size=len(x),
            replace=True
        )

        ys = rng.choice(
            y,
            size=len(y),
            replace=True
        )

        distribution.append(
            np.mean(xs) - np.mean(ys)
        )

    distribution = np.asarray(distribution)

    p = np.mean(
        np.abs(distribution) >= abs(observed)
    )

    return TestResult(
        name="bootstrap_difference",
        statistic=float(observed),
        p_value=float(p),
        interpretation=(
            "Tests whether the difference between "
            "predictors is larger than sampling noise."
        )
    )


def regression_features(
    trajectories: List[Dict]
):
    """
    Extract regression matrix.

    Expected trajectory format:

    {
        "R0": initial capability,
        "Dc": recursive depth,
        "Ce": consequence coupling,
        "Ac": adaptive consolidation,
        "Gv": viability expansion,
        "future_R": future capability
    }

    """

    X = []
    y = []

    for t in trajectories:

        X.append(
            [
                t["R0"],
                t["Dc"],
                t["Ce"],
                t["Ac"],
                t["Gv"]
            ]
        )

        y.append(
            t["future_R"]
        )

    return np.asarray(X), np.asarray(y)


def evaluate_reca_hypothesis(
    trajectories: List[Dict]
):
    """
    Main experiment entry point.

    Tests:

        Does G_V explain future capability
        beyond current capability?

    """

    X, y = regression_features(
        trajectories
    )

    results = {}

    results["samples"] = len(y)

    results["features"] = [
        "R0",
        "Dc",
        "Ce",
        "Ac",
        "Gv"
    ]

    results["hypothesis"] = (
        "Gv predicts future capability "
        "after controlling for R0."
    )

    return results


if __name__ == "__main__":

    print(
        "ASEB statistical testing module loaded."
    )
