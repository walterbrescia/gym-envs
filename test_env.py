import gymnasium as gym
import gym_environments

env = gym.make("gym_environments/CustomPendulum-v0", render="human")

# run the env with random actions

env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())