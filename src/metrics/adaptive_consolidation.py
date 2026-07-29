"""
adaptive_consolidation.py

Axiom Forge Mk1

ASEB / RECA Metric:

    A_c = Adaptive Consolidation


Measures whether selected adaptive improvements
become persistent modifications to the future
adaptive substrate.


Core transition:

    successful adaptation

            ↓

    retained adaptive structure

            ↓

    improved future adaptation



Without consolidation:

    failure
      ↓
    correction
      ↓
    reset


With consolidation:

    failure
      ↓
    correction
      ↓
    structural improvement
      ↓
    easier future adaptation



Theory:

    D_c × C_e × A_c → G_V
"""


from dataclasses import dataclass
from typing import Dict, List, Sequence
import math



@dataclass
class AdaptationEvent:
    """
    Records an adaptive improvement.

    Represents:

        old mechanism
             |
             v
        modified mechanism
    """

    adaptation_id: str

    initial_performance: float

    post_change_performance: float

    future_performance: float

    reused: bool



@dataclass
class ConsolidationResult:
    """
    Adaptive consolidation measurement.
    """

    consolidation_score: float

    improvement_rate: float

    reuse_rate: float

    persistence_score: float

    sample_size: int



def improvement_rate(
    events: Sequence[AdaptationEvent]
) -> float:
    """
    Measures whether modifications
    initially improve performance.

    This is discovery.

    It is NOT consolidation.
    """

    if not events:
        return 0.0


    improvements = 0


    for event in events:

        if (
            event.post_change_performance
            >
            event.initial_performance
        ):
            improvements += 1


    return improvements / len(events)



def reuse_rate(
    events: Sequence[AdaptationEvent]
) -> float:
    """
    Measures whether successful changes
    are reused later.

    This captures inheritance of
    adaptive structure.
    """

    if not events:
        return 0.0


    reused = sum(
        1
        for event in events
        if event.reused
    )


    return reused / len(events)



def persistence_score(
    events: Sequence[AdaptationEvent]
) -> float:
    """
    Measures whether improvements survive.

    A modification that helps immediately
    but disappears later has low persistence.
    """

    if not events:
        return 0.0


    scores = []


    for event in events:

        initial = (
            event.initial_performance
        )

        future = (
            event.future_performance
        )


        gain = (
            future -
            initial
        )


        normalized = (
            gain /
            (
                abs(initial)
                +
                1e-8
            )
        )


        scores.append(
            max(
                0,
                min(
                    1,
                    normalized
                )
            )
        )


    return sum(scores) / len(scores)



def compute_adaptive_consolidation(
    events: Sequence[AdaptationEvent]
) -> ConsolidationResult:
    """
    Main A_c estimator.


    A_c requires:

        1. improvement occurred
        2. improvement was reused
        3. improvement persisted


    Geometric mean ensures that
    failure in one dimension matters.

    """

    if not events:

        return ConsolidationResult(
            consolidation_score=0.0,
            improvement_rate=0.0,
            reuse_rate=0.0,
            persistence_score=0.0,
            sample_size=0,
        )


    improvement = improvement_rate(
        events
    )

    reuse = reuse_rate(
        events
    )

    persistence = persistence_score(
        events
    )


    score = math.pow(
        improvement *
        reuse *
        persistence,
        1 / 3
    )


    return ConsolidationResult(
        consolidation_score=score,
        improvement_rate=improvement,
        reuse_rate=reuse,
        persistence_score=persistence,
        sample_size=len(events),
    )



def forgetting_test(
    events: Sequence[AdaptationEvent]
) -> float:
    """
    Estimates adaptive forgetting.

    High value:

        discovered adaptations
        disappear quickly.


    Low value:

        adaptive structure persists.
    """

    if not events:
        return 0.0


    forgotten = 0


    for event in events:

        if (
            event.post_change_performance
            >
            event.initial_performance
            and
            event.future_performance
            <=
            event.initial_performance
        ):
            forgotten += 1


    return forgotten / len(events)



def transfer_test(
    events: Sequence[AdaptationEvent]
) -> float:
    """
    Estimates whether adaptations
    generalize beyond the original
    environment.

    This approximates:

        specific fix
             ↓
        reusable structure
    """

    if not events:
        return 0.0


    transferred = 0


    for event in events:

        if (
            event.future_performance
            >
            event.initial_performance
        ):
            transferred += 1


    return transferred / len(events)
