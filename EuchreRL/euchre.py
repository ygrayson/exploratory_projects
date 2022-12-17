# Euchre RL Agent Environment
# Author: Qianbo Yin
# QUESTION: 1. HOW TO CREATE MULTI-AGENT INTERFACE
# 2. WHAT DOES ALL THE OTHER AGENTS DO

from rl_glue import RLGlue
from manager import Manager
from EuchreEnvironment import EuchreEnvironment
from QLearningAgent import TDAgent


def run_experiment(env, agent, env_info, agent_info):
    """Run the environment and agent while collecting cumulative reward."""
    # use RLGlue to run experiment
    rl_glue = RLGlue(env, agent)
    rl_glue.rl_init(agent_info, env_info)

def main():
    # define environment and agent
    env = EuchreEnvironment
    agent = TDAgent
    env_info = {'max_points': 10, 'agent_num': 1}
    agent_info = {'discount': 0.9, 'learning_rate': 0.1, 'epsilon': 0.05}

    run_experiment(env=env, agent=agent, env_info=env_info, agent_info=agent_info)
    



if __name__ == '__main__':
    main()
