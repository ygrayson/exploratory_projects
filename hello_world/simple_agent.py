import time
import gym


class simple_agent():
    def __init__(self, env):
        self.env = env
        self.action_space = env.action_space

    def step(self, state, reward):
        return self.action_space.sample()

def main():
    """Simple agent"""
    # initialize environment
    env = gym.make("Hopper-v2")
    env.reset()

    # initialize agent in the environment
    agent = simple_agent(env)

    # start running agent
    done = False
    action = env.action_space.sample()
    for i in range(1000):
        env.render()
        # env.step() takes in an action
        state, reward, done, info = env.step(action)
        action = agent.step(state, reward)
        time.sleep(0.1)
    env.close()

    print("Done")


if __name__ == '__main__':
    main()