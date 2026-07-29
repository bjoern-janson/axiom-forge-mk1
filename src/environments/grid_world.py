"""
Axiom Forge Mk1
Grid World Environment

A minimal non-stationary environment
for testing Recursive Evolutionary Agency.

The environment provides:

    E → consequence

The agent must convert consequences into:

    improved future adaptation


This environment tests:

    D_c:
        Can the agent modify itself?

    C_e:
        Do environmental consequences select changes?

    A_c:
        Do successful adaptations persist?

    G_V:
        Does future viability expand?
"""


from dataclasses import dataclass
from typing import Tuple, Dict, List
import random


Position = Tuple[int, int]


@dataclass
class Cell:

    reward: float
    cost: float
    terrain: str



class GridWorld:
    """
    Non-stationary adaptive environment.

    Layout:

        +---+---+---+
        |   |   |   |
        |   | A | R |
        |   |   |   |
        +---+---+---+


    Agent attempts to maximize
    accumulated viability.

    Periodically the environment shifts,
    forcing adaptation.
    """


    def __init__(
        self,
        size: int = 10,
        perturbation_rate: float = 0.1
    ):

        self.size = size

        self.perturbation_rate = (
            perturbation_rate
        )

        self.step_count = 0

        self.agent_position = (
            size // 2,
            size // 2
        )

        self.goal_position = (
            size - 1,
            size - 1
        )


        self.grid = (
            self.generate_world()
        )


        self.total_reward = 0



    # ---------------------------------------------------------
    # World Generation
    # ---------------------------------------------------------

    def generate_world(
        self
    ) -> Dict[Position, Cell]:

        """
        Generate terrain distribution.

        Different environments create
        different adaptive pressures.
        """

        world = {}

        terrains = [
            "normal",
            "resource",
            "hazard"
        ]


        for x in range(self.size):

            for y in range(self.size):

                terrain = random.choice(
                    terrains
                )


                if terrain == "resource":

                    reward = random.uniform(
                        1,
                        3
                    )

                    cost = 0.2


                elif terrain == "hazard":

                    reward = -1

                    cost = random.uniform(
                        1,
                        3
                    )


                else:

                    reward = 0.1

                    cost = 0.5


                world[(x,y)] = Cell(
                    reward=reward,
                    cost=cost,
                    terrain=terrain
                )


        return world



    # ---------------------------------------------------------
    # Agent Interaction
    # ---------------------------------------------------------

    def observe(
        self
    ) -> Dict:

        """
        Return current environmental state.

        Future versions can hide information
        to test causal discovery.
        """

        cell = self.grid[
            self.agent_position
        ]


        return {

            "position":
                self.agent_position,

            "terrain":
                cell.terrain,

            "step":
                self.step_count

        }



    def step(
        self,
        action: str
    ) -> float:

        """
        Execute action.

        Actions:

            up
            down
            left
            right
            stay


        Returns:

            consequence signal

        """


        self.move(
            action
        )


        cell = self.grid[
            self.agent_position
        ]


        consequence = (
            cell.reward -
            cell.cost
        )


        self.total_reward += consequence


        self.step_count += 1


        self.apply_perturbations()


        return consequence



    # ---------------------------------------------------------
    # Dynamics
    # ---------------------------------------------------------

    def move(
        self,
        action: str
    ):

        x, y = self.agent_position


        if action == "up":

            y += 1


        elif action == "down":

            y -= 1


        elif action == "left":

            x -= 1


        elif action == "right":

            x += 1


        x = max(
            0,
            min(
                self.size-1,
                x
            )
        )

        y = max(
            0,
            min(
                self.size-1,
                y
            )
        )


        self.agent_position = (
            x,
            y
        )



    # ---------------------------------------------------------
    # Environmental Perturbations
    # ---------------------------------------------------------

    def apply_perturbations(
        self
    ):

        """
        Creates distribution shifts.

        This is the pressure that tests:

            "Can failure improve future adaptation?"
        """


        if random.random() < (
            self.perturbation_rate
        ):

            self.shift_environment()



    def shift_environment(
        self
    ):

        """
        Modify the selection landscape.

        Examples:

        - resources disappear
        - hazards appear
        - reward structures change

        """

        changes = random.sample(
            list(
                self.grid.keys()
            ),
            k=5
        )


        for position in changes:

            cell = self.grid[
                position
            ]


            if cell.terrain == "resource":

                cell.reward *= 0.5


            elif cell.terrain == "hazard":

                cell.cost *= 1.5


            else:

                if random.random() < 0.5:

                    cell.terrain = "resource"

                    cell.reward = random.uniform(
                        1,
                        3
                    )



    # ---------------------------------------------------------
    # Viability Evaluation
    # ---------------------------------------------------------

    def viability_state(
        self
    ):

        """
        Estimate environment accessibility.

        Future versions:

            V*_tau(X)

        reachable viable states.

        Mk1 proxy:
            remaining positive-value cells
        """


        viable_cells = 0


        for cell in self.grid.values():

            if (
                cell.reward -
                cell.cost
            ) > 0:

                viable_cells += 1


        return viable_cells



    # ---------------------------------------------------------
    # Reset
    # ---------------------------------------------------------

    def reset(
        self
    ):

        self.agent_position = (
            self.size // 2,
            self.size // 2
        )

        self.step_count = 0

        self.total_reward = 0

        self.grid = (
            self.generate_world()
        )


        return self.observe()
