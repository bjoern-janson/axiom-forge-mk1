"""
Axiom Forge Mk1
RECA Agent Prototype

Recursive Evolutionary Agency Agent

Core hypothesis:

    D_c × C_e × A_c → G_V

Where:

    D_c = Recursive depth
          Can consequences modify adaptive machinery?

    C_e = Consequence coupling
          Do consequences determine which modifications persist?

    A_c = Adaptive consolidation
          Do successful modifications become part of future behavior?

    G_V = Viability expansion
          Does the agent improve its future adaptive capacity?

This is a minimal research prototype, not a production agent.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Any
import random
import copy


@dataclass
class Modification:
    """
    Represents a candidate adaptive change.

    A modification is not automatically retained.
    It must survive consequence-based selection.
    """

    parameter: str
    old_value: Any
    new_value: Any
    consequence_score: float = 0.0
    retained: bool = False


@dataclass
class AdaptiveMemory:
    """
    Consolidated adaptive structures.

    This represents inherited adaptive substrate.

    Future adaptation begins from here.
    """

    successful_patterns: Dict[str, Any] = field(default_factory=dict)

    def store(self, modification: Modification):
        if modification.retained:
            self.successful_patterns[
                modification.parameter
            ] = modification.new_value


class RECAAgent:
    """
    Recursive Evolutionary Agency Agent.

    Architecture:

        Environment
              |
              v
           Consequence
              |
              v
        Selection Mechanism
              |
              v
       Adaptive Modification
              |
              v
        Consolidated Substrate
              |
              v
       Improved Future Adaptation


    Unlike a learner:

        E → S

    and unlike a meta-learner:

        E → S → T

    RECA attempts:

        E → S → T → σ

    where σ represents selection over future transformations.
    """

    def __init__(
        self,
        initial_parameters: Dict[str, float]
    ):

        # Current adaptive machinery
        self.parameters = initial_parameters

        # Persistent evolutionary memory
        self.memory = AdaptiveMemory()

        # History for analysis
        self.history: List[Dict] = []

        # Metrics
        self.modifications_attempted = 0
        self.modifications_retained = 0


    # ---------------------------------------------------------
    # Action Generation
    # ---------------------------------------------------------

    def act(self, observation):
        """
        Generate action from current adaptive substrate.

        Mk1 uses a simple weighted policy.
        """

        score = sum(
            self.parameters.values()
        )

        return score


    # ---------------------------------------------------------
    # Consequence Processing
    # ---------------------------------------------------------

    def receive_consequence(
        self,
        consequence: float
    ):
        """
        Convert environmental consequences into
        adaptive pressure.

        This is C_e.

        Consequence must influence selection.
        """

        self.last_consequence = consequence


    # ---------------------------------------------------------
    # Mutation / Variation
    # ---------------------------------------------------------

    def generate_modifications(
        self
    ) -> List[Modification]:

        """
        Generate candidate changes.

        Variation without selection is not evolution.
        """

        modifications = []

        for key, value in self.parameters.items():

            direction = random.choice(
                [-1, 1]
            )

            mutation = value + (
                direction *
                random.uniform(
                    0.05,
                    0.2
                )
            )

            modifications.append(
                Modification(
                    parameter=key,
                    old_value=value,
                    new_value=mutation
                )
            )

        return modifications


    # ---------------------------------------------------------
    # Selection
    # ---------------------------------------------------------

    def evaluate_modification(
        self,
        modification: Modification
    ):
        """
        Test whether a modification improves
        consequence outcomes.

        This implements:

            C_e

        Reality filters changes.
        """

        original = self.parameters[
            modification.parameter
        ]

        # Temporary application

        self.parameters[
            modification.parameter
        ] = modification.new_value


        simulated_result = self.evaluate_future_viability()


        # Restore

        self.parameters[
            modification.parameter
        ] = original


        modification.consequence_score = (
            simulated_result
        )


        return modification


    def select(
        self,
        modifications: List[Modification]
    ):

        """
        Retain modifications that improve
        future viability.

        Selection over adaptive mechanisms.
        """

        for modification in modifications:

            self.modifications_attempted += 1

            if modification.consequence_score > 0:

                modification.retained = True

                self.parameters[
                    modification.parameter
                ] = modification.new_value


                self.memory.store(
                    modification
                )

                self.modifications_retained += 1



    # ---------------------------------------------------------
    # Consolidation
    # ---------------------------------------------------------

    def consolidate(self):
        """
        Adaptive consolidation.

        Successful changes become
        future starting conditions.

        This implements A_c.
        """

        for key, value in (
            self.memory.successful_patterns.items()
        ):

            self.parameters[key] = value



    # ---------------------------------------------------------
    # Viability Estimation
    # ---------------------------------------------------------

    def evaluate_future_viability(
        self
    ):
        """
        Placeholder viability estimator.

        Future versions replace this with:

            G_V = Δ|V*_τ|

        reachable viable future expansion.

        Mk1 proxy:

        coherent parameter improvement.
        """

        return (
            sum(
                self.parameters.values()
            )
            /
            len(self.parameters)
        )


    # ---------------------------------------------------------
    # Evolution Step
    # ---------------------------------------------------------

    def evolve(self):

        """
        Complete RECA cycle:

            consequence
                  |
              variation
                  |
              selection
                  |
             consolidation
                  |
          improved substrate

        """

        candidates = (
            self.generate_modifications()
        )

        evaluated = [
            self.evaluate_modification(m)
            for m in candidates
        ]

        self.select(
            evaluated
        )

        self.consolidate()


        self.history.append(
            {
                "parameters":
                    copy.deepcopy(
                        self.parameters
                    ),

                "retained":
                    self.modifications_retained,

                "attempted":
                    self.modifications_attempted
            }
        )


    # ---------------------------------------------------------
    # Metrics
    # ---------------------------------------------------------

    def get_metrics(self):

        return {

            "D_c":
                1.0,

            "C_e":
                (
                    self.modifications_retained /
                    max(
                        1,
                        self.modifications_attempted
                    )
                ),

            "A_c":
                len(
                    self.memory.successful_patterns
                ),

            "history":
                self.history
        }
