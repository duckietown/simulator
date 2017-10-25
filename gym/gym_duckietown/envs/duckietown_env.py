import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pyglet
import math
import numpy as np
import zmq

# Rendering window size
WINDOW_SIZE = 512

class DuckietownEnv(gym.Env):
    """
    OpenAI gym environment wrapper for the Duckietown simulation.
    Connects to ROS/Gazebo through ZeroMQ
    """

    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 30
    }

    # Camera image size
    CAMERA_WIDTH = 100
    CAMERA_HEIGHT = 100

    # Camera image shape
    IMG_SHAPE = (CAMERA_WIDTH, CAMERA_HEIGHT, 3)

    def __init__(self):
        # For rendering
        self.window = None

        # Two-tuple of wheel torques, each in the range [-1, 1]
        self.action_space = spaces.Box(
            low=-1,
            high=1,
            shape=(2,)
        )

        # We observe an RGB image with pixels in [0, 255]
        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=DuckietownEnv.IMG_SHAPE
        )

        self.reward_range = (-1, 1000)

        # Environment configuration
        self.maxSteps = 1000

        # Initialize the state
        self.reset()
        self.seed()

    def _reset(self):
        # Step count since episode start
        self.stepCount = 0

        # FIXME
        # Return first observation
        return np.array([])

    def _seed(self, seed=None):
        """
        The seed function sets the random elements of the environment.
        """

        self.np_random, _ = seeding.np_random(seed)

        # TODO: can we ask the server to generate a new random map here?

        return [seed]

    def _step(self, action):
        assert isinstance(action, tuple) and len(action) == 2

        self.stepCount += 1

        reward = 0
        done = False

        # FIXME
        obs = np.array([])

        if self.stepCount >= self.maxSteps:
            done = True

        return obs, reward, done, {}

    def _render(self, mode='human', close=False):
        if close:
            if self.window:
                self.window.close()
            return

        if self.window is None:
            self.window = pyglet.window.Window(width=WINDOW_SIZE, height=WINDOW_SIZE)

        self.window.clear()
        self.window.switch_to()
        self.window.dispatch_events()

        # TODO: draw to a texture and display
        # Note: pyglet may have utils for this

        self.window.flip()
