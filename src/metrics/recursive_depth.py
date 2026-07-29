"""
recursive_depth.py

Axiom Forge Mk1

ASEB / RECA Metric:

    D_c = Depth of controllable causal recursion


Measures:

    How deeply can environmental consequences
    penetrate into the mechanisms responsible
    for future adaptation?


Core hierarchy:

    Level 0:
        E → A
        Action/output optimization


    Level 1:
        E → S
        State adaptation


    Level 2:
        E → S → T
        Transformation-rule adaptation


    Level 3:
        E → S → T → σ
        Selection dynamics adaptation



Theory:

    D_c × C_e × A_c → G_V
"""


from dataclasses import dataclass
from typing import Dict, List, Sequence
from enum import IntEnum



class AdaptiveLayer(IntEnum):
    """
    Levels of causal recursion.
    """

    ACTION = 0

    STATE = 1

    TRANSFORMATION = 2

    SELECTION = 3



@dataclass
class ModificationChannel:
    """
    Represents a pathway through which
    environmental consequences can modify
    the system.

    Example:

        failure signal
              |
              v
        learning rule

    """

    target_layer: AdaptiveLayer

    consequence_driven: bool

    controllable: bool

    description: str = ""



@dataclass
class RecursiveDepthResult:
    """
    Output of D_c estimation.
    """

    depth_score: float

    maximum_layer: AdaptiveLayer

    active_layers: List[int]

    channel_count: int



def estimate_recursive_depth(
    channels: Sequence[ModificationChannel],
) -> RecursiveDepthResult:
    """
    Estimate D_c.

    The deepest consequence-controlled
    layer determines recursive depth.

    """

    if not channels:

        return RecursiveDepthResult(
            depth_score=0.0,
            maximum_layer=AdaptiveLayer.ACTION,
            active_layers=[],
            channel_count=0,
        )


    active_layers = []


    for channel in channels:

        if (
            channel.consequence_driven
            and
            channel.controllable
        ):
            active_layers.append(
                int(channel.target_layer)
            )


    if not active_layers:

        return RecursiveDepthResult(
            depth_score=0.0,
            maximum_layer=AdaptiveLayer.ACTION,
            active_layers=[],
            channel_count=len(channels),
        )


    max_layer = max(active_layers)


    # Normalize:

    # 0 → 0.0
    # 1 → 0.33
    # 2 → 0.66
    # 3 → 1.0

    depth_score = (
        max_layer /
        int(AdaptiveLayer.SELECTION)
    )


    return RecursiveDepthResult(
        depth_score=depth_score,
        maximum_layer=AdaptiveLayer(max_layer),
        active_layers=sorted(
            set(active_layers)
        ),
        channel_count=len(channels),
    )



def classify_system(
    result: RecursiveDepthResult,
) -> str:
    """
    Human-readable regime classification.
    """

    layer = result.maximum_layer


    if result.depth_score == 0:

        return "fixed optimizer"


    if layer == AdaptiveLayer.STATE:

        return "adaptive learner"


    if layer == AdaptiveLayer.TRANSFORMATION:

        return "meta-adaptive system"


    if layer == AdaptiveLayer.SELECTION:

        return "recursive evolutionary agency"


    return "unknown"



def recursive_profile(
    channels: Sequence[ModificationChannel],
) -> Dict:
    """
    Returns detailed recursion profile.
    """

    result = estimate_recursive_depth(
        channels
    )


    return {
        "D_c":
            result.depth_score,

        "maximum_layer":
            result.maximum_layer.name,

        "active_layers":
            result.active_layers,

        "classification":
            classify_system(result),

        "channels":
            result.channel_count,
    }



def intervention_depth_test(
    before: Sequence[ModificationChannel],
    after: Sequence[ModificationChannel],
) -> float:
    """
    Measures whether a system's causal
    control depth increases.

    Intended experiment:

        environmental pressure

              ↓

        recursive architecture expansion


    Positive value:

        deeper causal closure.
    """

    before_result = estimate_recursive_depth(
        before
    )

    after_result = estimate_recursive_depth(
        after
    )


    return (
        after_result.depth_score
        -
        before_result.depth_score
    )
