"""
Axiom Forge Mk1

Experiment:
RECA Agent vs Baseline Agents

Core hypothesis:

    D_c * C_e * A_c
              |
              v
          G_V
              |
              v
    long horizon persistence


The experiment asks:

Does adaptive architecture predict
future performance better than
initial capability?
"""


from src.environments.grid_world import GridWorld
from src.agents.reca_agent import RECAAgent


class BaselineAgent:
    """
    Fixed adaptation baseline.

    Learns action values but does not
    modify the mechanism producing learning.

    Approximation:

        E -> S

    not:

        E -> S -> T -> selection
    """


    def __init__(self):

        self.q_values = {}

        self.learning_rate = 0.1

        self.actions = [
            "up",
            "down",
            "left",
            "right",
            "stay"
        ]



    def act(self, observation):

        state = (
            observation["position"]
        )

        if state not in self.q_values:

            self.q_values[state] = {
                a: 0
                for a in self.actions
            }


        return max(
            self.q_values[state],
            key=self.q_values[state].get
        )



    def update(
        self,
        observation,
        action,
        reward
    ):

        state = (
            observation["position"]
        )


        self.q_values[state][action] += (
            self.learning_rate *
            (
                reward -
                self.q_values[state][action]
            )
        )



class ExperimentResult:

    def __init__(self):

        self.rewards = []

        self.viability = []

        self.steps_survived = 0



    def record(
        self,
        reward,
        viability
    ):

        self.rewards.append(
            reward
        )

        self.viability.append(
            viability
        )



def run_episode(
    agent,
    environment,
    steps=500
):

    result = ExperimentResult()


    observation = (
        environment.reset()
    )


    for _ in range(steps):

        action = (
            agent.act(
                observation
            )
        )


        reward = (
            environment.step(
                action
            )
        )


        if hasattr(
            agent,
            "update"
        ):

            agent.update(
                observation,
                action,
                reward
            )


        result.record(
            reward,
            environment.viability_state()
        )


        observation = (
            environment.observe()
        )


        result.steps_survived += 1



    return result



def calculate_viability_gain(
    result
):

    """
    Proxy for:

        G_V

    Future versions replace this with:

        ΔV*_tau

    """

    if len(result.viability) < 2:

        return 0


    initial = (
        result.viability[0]
    )

    final = (
        result.viability[-1]
    )


    return final - initial



def summarize(
    name,
    result
):

    total_reward = sum(
        result.rewards
    )


    viability_gain = (
        calculate_viability_gain(
            result
        )
    )


    print("=" * 50)

    print(name)

    print(
        "Total reward:",
        round(total_reward, 2)
    )

    print(
        "Final viability:",
        result.viability[-1]
    )

    print(
        "Viability gain:",
        viability_gain
    )

    print(
        "Steps survived:",
        result.steps_survived
    )



def compare_agents(
    episodes=10
):

    """
    Main experiment.

    Future extension:

        Run statistical analysis:

            G_V -> future reward

        controlling for:

            compute
            parameters
            initial score
    """


    reca_results = []

    baseline_results = []



    for episode in range(episodes):

        print(
            f"Running episode {episode+1}/{episodes}"
        )


        reca_env = GridWorld()

        baseline_env = GridWorld()



        reca = RECAAgent()

        baseline = BaselineAgent()



        reca_result = run_episode(
            reca,
            reca_env
        )


        baseline_result = run_episode(
            baseline,
            baseline_env
        )


        reca_results.append(
            reca_result
        )

        baseline_results.append(
            baseline_result
        )



    print("\nFINAL RESULTS\n")


    reca_average = (
        sum(
            sum(r.rewards)
            for r in reca_results
        )
        /
        episodes
    )


    baseline_average = (
        sum(
            sum(r.rewards)
            for r in baseline_results
        )
        /
        episodes
    )


    print(
        "RECA average reward:",
        round(
            reca_average,
            2
        )
    )


    print(
        "Baseline average reward:",
        round(
            baseline_average,
            2
        )
    )


    reca_viability = (
        sum(
            calculate_viability_gain(r)
            for r in reca_results
        )
        /
        episodes
    )


    baseline_viability = (
        sum(
            calculate_viability_gain(r)
            for r in baseline_results
        )
        /
        episodes
    )


    print(
        "RECA average G_V:",
        round(
            reca_viability,
            2
        )
    )


    print(
        "Baseline average G_V:",
        round(
            baseline_viability,
            2
        )
    )



if __name__ == "__main__":

    compare_agents()
