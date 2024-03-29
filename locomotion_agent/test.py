"""Code adapted from https://github.com/nikhilbarhate99/PPO-PyTorch"""

import os
import pathlib
from datetime import datetime

import torch
import numpy as np
import cv2

import gymnasium as gym
from PPO import PPO


#################################### Testing ###################################
def test():
    print("============================================================================================")

    ################## hyperparameters ##################

    # env_name = "CartPole-v1"
    # has_continuous_action_space = False
    # max_ep_len = 400
    # action_std = None

    # env_name = "LunarLander-v2"
    # has_continuous_action_space = False
    # max_ep_len = 300
    # action_std = None

    # env_name = "BipedalWalker-v3"
    # has_continuous_action_space = True
    # max_ep_len = 1500           # max timesteps in one episode
    # action_std = 0.1            # set same std for action distribution which was used while saving

    # environment hyperparameters
    env_name = "Humanoid-v4" #Humanoid-v4, BipedalWalker-v3, Ant-v4
    has_continuous_action_space = True
    max_ep_len = 1000           # max timesteps in one episode
    action_std = 0.1            # set same std for action distribution which was used while saving

    # renering hyperparameters
    render = True               # render environment on screen
    frame_delay = 0             # if required; add delay between frames
    if render:
        # save directory for video and logs
        save_dir = os.path.join(pathlib.Path().absolute(), "PPO_render", env_name)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # video sub-directory
        video_idx = len(os.listdir(save_dir))
        video_dir = os.path.join(save_dir, str(video_idx))
        if not os.path.exists(video_dir):
            os.makedirs(video_dir)

    total_test_episodes = 4    # total num of testing episodes

    K_epochs = 80               # update policy for K epochs
    eps_clip = 0.2              # clip parameter for PPO
    gamma = 0.99                # discount factor

    lr_actor = 0.0003           # learning rate for actor
    lr_critic = 0.001           # learning rate for critic
    #####################################################

    env = gym.make(env_name, render_mode="rgb_array")

    # state space dimension
    state_dim = env.observation_space.shape[0]

    # action space dimension
    if has_continuous_action_space:
        action_dim = env.action_space.shape[0]
    else:
        action_dim = env.action_space.n

    # initialize a PPO agent
    ppo_agent = PPO(state_dim, action_dim, lr_actor, lr_critic, gamma, K_epochs, eps_clip, has_continuous_action_space, action_std)

    # preTrained weights directory
    random_seed = 0             #### set this to load a particular checkpoint trained on random seed
    run_num_pretrained = 1      #### set this to load a particular checkpoint num

    directory = "PPO_preTrained" + '/' + env_name + '/'
    checkpoint_path = directory + f"PPO_{env_name}_{random_seed}_{run_num_pretrained}.pth"
    print("loading network from : " + checkpoint_path)

    ppo_agent.load(checkpoint_path)

    print("--------------------------------------------------------------------------------------------")
    test_running_reward = 0

    # loop through a number of episodes
    for ep in range(1, total_test_episodes + 1):
        ep_reward = 0
        state, _ = env.reset()
        height, width, _ = env.render().shape

        # write to video for rendering
        video_out = cv2.VideoWriter(
            os.path.join(video_dir, "ep_" + str(ep) + ".avi"), 
            cv2.VideoWriter_fourcc(*'MJPG'), 
            30,
            (width, height)
        )

        # go through all timesteps in this episode
        for t in range(1, max_ep_len+1):
            action = ppo_agent.select_action(state)
            state, reward, terminated, truncated, _ = env.step(action)
            ep_reward += reward

            if render:
                img = env.render()
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                video_out.write(img)

            if terminated or truncated:
                break
            # print(t)
        if render:
            video_out.release()

        # clear buffer
        ppo_agent.buffer.clear()

        test_running_reward +=  ep_reward
        print(f'Episode: {ep} \t\t Reward: {round(ep_reward, 2)}')
        ep_reward = 0

    env.close()

    print("============================================================================================")

    avg_test_reward = test_running_reward / total_test_episodes
    avg_test_reward = round(avg_test_reward, 2)
    print("average test reward : " + str(avg_test_reward))

    print("============================================================================================")


if __name__ == '__main__':
    test()
