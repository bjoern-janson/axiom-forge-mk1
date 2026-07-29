"""
long_horizon_test.py

Axiom Forge Mk1

Long Horizon RECA Evaluation

Tests whether adaptive systems accumulate
future adaptive capacity over repeated
environmental perturbations.

Central hypothesis:

    D_c × C_e × A_c
              |
              v
            G_V
              |
              v
    long-horizon persistence


The experiment compares:

    - RECA agent
    - baseline adaptive agent


The critical measurement:

    Current performance
        vs
    Future adaptive trajectory
"""


from dataclasses import dataclass, field
from typing import Any, Dict, List

from src.experiments.perturbation import (
    PerturbationSchedule,
    default_reca_schedule,
)



@dataclass
class HorizonStep:
    """
    Records one environmental phase.
    """

    timestep: int

    reward: float

    viability: float

    reca_score: float

    perturbation: str



@dataclass
class HorizonResult:
    """
    Complete long horizon trajectory.
    """

    agent_name: str

    steps: List[HorizonStep] = field(
        default_factory=list
    )

    final_viability: float = 0.0

    viability_growth: float = 0.0



class LongHorizonTester:
    """
    Executes repeated perturbation experiments.
    """

    def __init__(
        self,
        environment,
        perturbation_schedule:
            PerturbationSchedule | None = None,
    ):

        self.environment = environment

        self.schedule = (
            perturbation_schedule
            or default_reca_schedule()
        )



    def evaluate(
        self,
        agent,
        episodes: int = 5,
    ) -> HorizonResult:
        """
        Run a long-horizon evaluation.
        """

        result = HorizonResult(
            agent_name=
                agent.__class__.__name__
        )


        initial_viability = (
            self.environment
            .evaluate_viability(
                self.environment.state
            )
        )


        timestep = 0


        for perturbation in (
            self.schedule.perturbations
        ):

            self.environment.apply_perturbation(
                {
                    "type":
                        perturbation.perturbation_type.value,

                    "severity":
                        perturbation.severity,

                    **perturbation.parameters,
                }
            )


            for _ in range(episodes):

                state = (
                    self.environment.reset()
                )


                done = False


                while not done:

                    action = (
                        agent.act(state)
                    )


                    transition = (
                        self.environment
                        .step(action)
                    )


                    state = (
                        transition.next_state
                    )


                    done = (
                        transition.done
                    )


                    viability = (
                        self.environment
                        .evaluate_viability(
                            state
                        )
                    )


                    reca_score = (
                        self.measure_reca(
                            agent
                        )
                    )


                    result.steps.append(
                        HorizonStep(
                            timestep=timestep,

                            reward=
                                transition.reward,

                            viability=
                                viability,

                            reca_score=
                                reca_score,

                            perturbation=
                                perturbation
                                .perturbation_type
                                .value,
                        )
                    )


                    timestep += 1


        result.final_viability = (
            result.steps[-1].viability
            if result.steps
            else 0.0
        )


        result.viability_growth = (
            result.final_viability
            -
            initial_viability
        )


        return result



    def measure_reca(
        self,
        agent,
    ) -> float:
        """
        Placeholder hook.

        Connects:

            recursive_depth.py
            consequence_coupling.py
            adaptive_consolidation.py

        """

        if hasattr(
            agent,
            "reca_score"
        ):
            return agent.reca_score()


        return 0.0



def compare_agents(
    tester: LongHorizonTester,
    agents: List[Any],
) -> Dict[str, HorizonResult]:
    """
    Compare multiple adaptive systems.
    """

    results = {}


    for agent in agents:

        results[
            agent.__class__.__name__
        ] = tester.evaluate(agent)


    return results



def summarize(
    results: Dict[str, HorizonResult],
) -> None:
    """
    Print benchmark summary.
    """

    print(
        "\n=== Long Horizon RECA Test ===\n"
    )


    for name, result in results.items():

        print(
            f"{name}"
        )

        print(
            f"Final viability: "
            f"{result.final_viability:.3f}"
        )

        print(
            f"Viability growth: "
            f"{result.viability_growth:.3f}"
        )

        print(
            f"Steps: "
            f"{len(result.steps)}"
        )

        print()
