"""
Axiom Forge Mk1 — Agents Module

Contains adaptive agent implementations used
for Recursive Evolutionary Agency experiments.

Available agents:

    RECAAgent
        Experimental agent implementing
        recursive adaptation mechanisms.

    BaselineAgent
        Control agent for comparison against
        static or non-recursive adaptation.
"""

from .reca_agent import RECAAgent
from .baseline_agent import BaselineAgent


__all__ = [
    "RECAAgent",
    "BaselineAgent",
]
