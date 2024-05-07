import gymnasium as gym
import numpy as np
from gymnasium.envs.classic_control import PendulumEnv

class CustomPendulumEnv(PendulumEnv):
    def __init__(self, render=None):
        super(CustomPendulumEnv, self).__init__(render)
        self.cs = 100 # cost scaling

    def step(self, u):
        th, thdot = self.state  # th := theta

        g = self.g
        m = self.m
        l = self.l
        dt = self.dt

        u = np.clip(u, -self.max_torque, self.max_torque)[0]
        self.last_u = u  # for rendering
        costs = (self.cs * angle_normalize(th)) ** 2 + \
                0.1 * (self.cs * thdot)**2 + \
                0.001 * (self.cs * u)**2

        newthdot = thdot + (3 * g / (2 * l) * np.sin(th) + 3.0 / (m * l**2) * u) * dt
        newthdot = np.clip(newthdot, -self.max_speed, self.max_speed)
        newth = th + newthdot * dt

        self.state = np.array([newth, newthdot])

        if self.render_mode == "human":
            self.render()
        # truncation=False as the time limit is handled by the `TimeLimit` wrapper added during `make`
        return self._get_obs(), -costs, False, False, {}
    
def angle_normalize(x):
    return ((x + np.pi) % (2 * np.pi)) - np.pi