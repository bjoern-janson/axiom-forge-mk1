"""
baseline_agent.py

Axiom Forge Mk1

Baseline Adaptive Agent

Purpose:

Control condition for RECA experiments.

The baseline can learn from consequences,
but cannot modify the mechanisms responsible
for learning.

This represents:

Level 1-2 adaptation

rather than:

Level 3 Recursive Evolutionary Agency.


No:

    recursive depth
    adaptive consolidation
    selection over transformations

"""

from dataclasses import dataclass, field
from typing import Dict, Any, List
import random



@dataclass
class Experience:

    state: Any

    action: Any

    reward: float

    next_state: Any



class BaselineAgent:
    """
    Simple adaptive learner.

    Implements:

        E -> S

    and optionally:

        E -> policy

    But does not modify:

        T
        sigma

    """

    def __init__(
        self,
        actions: List[Any],
        learning_rate: float = 0.1,
        exploration_rate: float = 0.1,
    ):

        self.actions = actions

        self.learning_rate = (
            learning_rate
        )

        self.exploration_rate = (
            exploration_rate
        )


        self.q_table: Dict = {}

        self.memory = []



    def act(
        self,
        state,
    ):
        """
        Select action.

        Uses epsilon-greedy policy.
        """

        if random.random() < (
            self.exploration_rate
        ):
            return random.choice(
                self.actions
            )


        values = (
            self.q_table
            .get(
                state,
                {}
            )
        )


        if not values:
            return random.choice(
                self.actions
            )


        return max(
            values,
            key=values.get
        )



    def update(
        self,
        experience: Experience,
    ):
        """
        Standard reinforcement update.

        The policy changes.

        The learning mechanism does not.
        """

        state = experience.state

        action = experience.action

        reward = experience.reward


        if state not in self.q_table:

            self.q_table[state] = {}


        old_value = (
            self.q_table[state]
            .get(action, 0.0)
        )


        updated = (
            old_value
            +
            self.learning_rate
            *
            (
                reward
                -
                old_value
            )
        )


        self.q_table[state][action] = (
            updated
        )


        self.memory.append(
            experience
        )



    def observe(
        self,
        transition,
    ):
        """
        Receive environment consequence.
        """

        experience = Experience(
            state=transition.state,

            action=transition.action,

            reward=transition.reward,

            next_state=transition.next_state,
        )


        self.update(
            experience
        )



    def reset(self):
        """
        Reset internal state.

        Important:

        No accumulated adaptive
        structure survives unless
        explicitly preserved.

        """

        self.q_table = {}

        self.memory = []



    def reca_score(self):
        """
        Baseline should score low.

        It has:

            Dc > 0
            Ce > 0

        but:

            Ac ≈ 0

        because learning does not
        modify the learning process.
        """

        return 0.0



    def get_state(self):
        """
        Diagnostics.
        """

        return {

            "q_table_size":
                len(self.q_table),

            "memory_size":
                len(self.memory),

            "learning_rate":
                self.learning_rate,

            "exploration_rate":
                self.exploration_rate,
        }
