from gymnasium.envs.registration import register


"""
register example, adjust accordingly

register(
     id="gym_environments/GridWorld-v0",
     entry_point="gym_environments.envs:GridWorldEnv",
     max_episode_steps=300,
)
"""


register(
     id="gym_environments/CustomPendulum-v0",
     entry_point="gym_environments.envs:CustomPendulumEnv",
     max_episode_steps=1000,
)