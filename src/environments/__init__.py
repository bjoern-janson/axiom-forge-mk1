"""
Axiom Forge Mk1 — Environments Module

Contains benchmark environments used to evaluate
adaptive systems under changing conditions.

Available environments:

    BaseEnvironment
        Abstract environment interface defining
        interaction, evaluation, and perturbation
        contracts.

    GridWorld
        Initial controlled environment for testing
        adaptation, recovery, and viability
        expansion.
"""

from .base_environment import BaseEnvironment
from .grid_world import GridWorld


__all__ = [
    "BaseEnvironment",
    "GridWorld",
]
