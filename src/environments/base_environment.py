"""
base_environment.py

Axiom Forge Mk1

Base Environment Interface

Defines the contract between:

    agent
       |
       v
    environment
       |
       v
    consequences

In ASEB / RECA:

The environment is not merely a place where
performance is measured.

It is the causal source that determines:

    - which adaptations survive
    - which strategies fail
    - whether viability expands

Core loop:

    X_t
      |
      v
    action
      |
      v
    consequence
      |
      v
    adaptive update
      |
      v
    X_(t+1)
"""


from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Tuple



@dataclass
class EnvironmentStep:
    """
    Result of one interaction step.

    Contains the information required for
    consequence coupling measurement.
    """

    next_state: Any

    reward: float

    done: bool

    consequence: Dict[str, Any]



@dataclass
class EnvironmentConfig:
    """
    Shared environment configuration.
    """

    max_steps: int = 100

    perturbation_enabled: bool = True

    seed: int | None = None



class BaseEnvironment(ABC):
    """
    Abstract RECA benchmark environment.

    Every environment must provide:

        reset()
        step()
        evaluate_viability()

    """

    def __init__(
        self,
        config: EnvironmentConfig | None = None,
    ):
        self.config = (
            config
            or EnvironmentConfig()
        )

        self.state = None
        self.step_count = 0



    @abstractmethod
    def reset(self) -> Any:
        """
        Start a new episode.

        Returns:

            initial environment state
        """

        pass



    @abstractmethod
    def step(
        self,
        action: Any,
    ) -> EnvironmentStep:
        """
        Apply an action.

        Must return:

            next state
            consequence
            reward
            termination signal

        """

        pass



    @abstractmethod
    def evaluate_viability(
        self,
        state: Any,
    ) -> float:
        """
        Estimate whether a state remains viable.

        Expected range:

            0.0 = non-viable
            1.0 = highly viable

        Used by:

            G_V

        """

        pass



    def apply_perturbation(
        self,
        perturbation: Dict[str, Any],
    ) -> None:
        """
        Modify environmental conditions.

        Examples:

            distribution shift
            resource reduction
            objective change
            memory degradation

        """

        raise NotImplementedError(
            "Environment does not support perturbations."
        )



    def current_state(self) -> Any:
        """
        Return current state.
        """

        return self.state



    def time_step(self) -> int:
        """
        Return current timestep.
        """

        return self.step_count



    def is_finished(self) -> bool:
        """
        Default episode termination.
        """

        return (
            self.step_count
            >=
            self.config.max_steps
        )
