"""
perturbation.py

Axiom Forge Mk1

Environmental Perturbation System

Perturbations are the causal pressure mechanism
for testing Recursive Evolutionary Agency.

The benchmark does not ask:

    "Can the agent solve the current task?"

It asks:

    "Can consequences from failure reshape
     future adaptive capacity?"

Perturbation classes:

    - distribution shift
    - resource limitation
    - objective corruption
    - memory degradation
    - novel task introduction


Core hypothesis:

    D_c × C_e × A_c → G_V


A successful RECA agent should not only recover.

It should become more capable after repeated
environmental pressure.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List



class PerturbationType(Enum):
    """
    Types of environmental pressure.
    """

    DISTRIBUTION_SHIFT = "distribution_shift"

    RESOURCE_LIMIT = "resource_limit"

    OBJECTIVE_CHANGE = "objective_change"

    MEMORY_DEGRADATION = "memory_degradation"

    NOVEL_TASK = "novel_task"



@dataclass
class Perturbation:
    """
    Single environmental intervention.
    """

    perturbation_type: PerturbationType

    severity: float

    parameters: Dict[str, Any] = field(
        default_factory=dict
    )

    description: str = ""



@dataclass
class PerturbationResult:
    """
    Records the effect of an intervention.
    """

    perturbation: Perturbation

    pre_viability: float

    post_viability: float

    recovery_steps: int

    structural_change_detected: bool



class PerturbationGenerator:
    """
    Creates controlled environmental changes.

    Designed for repeated non-stationary
    benchmark environments.
    """

    def __init__(
        self,
        seed: int | None = None,
    ):
        self.seed = seed


    def distribution_shift(
        self,
        severity: float = 0.5,
    ) -> Perturbation:
        """
        Changes task distribution.

        Tests:

            representation flexibility
            abstraction transfer
        """

        return Perturbation(
            perturbation_type=
                PerturbationType.DISTRIBUTION_SHIFT,

            severity=severity,

            parameters={
                "environment_change":
                    severity
            },

            description=
                "Changes environmental statistics."
        )


    def resource_limit(
        self,
        severity: float = 0.5,
    ) -> Perturbation:
        """
        Reduces available resources.

        Tests:

            adaptive efficiency
            constraint handling
        """

        return Perturbation(
            perturbation_type=
                PerturbationType.RESOURCE_LIMIT,

            severity=severity,

            parameters={
                "resource_multiplier":
                    1 - severity
            },

            description=
                "Reduces available resources."
        )


    def objective_change(
        self,
        severity: float = 0.5,
    ) -> Perturbation:
        """
        Changes the optimization target.

        Tests:

            consequence interpretation
            goal flexibility
        """

        return Perturbation(
            perturbation_type=
                PerturbationType.OBJECTIVE_CHANGE,

            severity=severity,

            parameters={
                "objective_shift":
                    severity
            },

            description=
                "Changes environmental goals."
        )


    def memory_degradation(
        self,
        severity: float = 0.5,
    ) -> Perturbation:
        """
        Removes retained information.

        Tests:

            adaptive consolidation
            structural memory
        """

        return Perturbation(
            perturbation_type=
                PerturbationType.MEMORY_DEGRADATION,

            severity=severity,

            parameters={
                "memory_retention":
                    1 - severity
            },

            description=
                "Reduces stored adaptive structure."
        )


    def novel_task(
        self,
        severity: float = 0.5,
    ) -> Perturbation:
        """
        Introduces unseen task families.

        Tests:

            viability expansion
            abstraction creation
        """

        return Perturbation(
            perturbation_type=
                PerturbationType.NOVEL_TASK,

            severity=severity,

            parameters={
                "novelty":
                    severity
            },

            description=
                "Introduces new task domain."
        )



@dataclass
class PerturbationSchedule:
    """
    Sequence of environmental shocks.
    """

    perturbations: List[Perturbation]



def default_reca_schedule(
    severity: float = 0.5,
) -> PerturbationSchedule:
    """
    Standard RECA benchmark sequence.

    Order matters.

    Early shocks test recovery.
    Later shocks test accumulated adaptation.
    """

    generator = PerturbationGenerator()


    return PerturbationSchedule(
        perturbations=[
            generator.distribution_shift(
                severity
            ),

            generator.resource_limit(
                severity
            ),

            generator.objective_change(
                severity
            ),

            generator.memory_degradation(
                severity
            ),

            generator.novel_task(
                severity
            ),
        ]
    )
