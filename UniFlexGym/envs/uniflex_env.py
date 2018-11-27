import os, time
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding
import importlib


import logging
logger = logging.getLogger(__name__)


class UniflexEnv(gym.Env):
    def __init__(self):
        self.stepTime = 10
        self.controller = None
    
    def start_controller(self, **kwargs):
        controllerName = 'controller.Controller'
        
        if 'controller' in kwargs:
            controllerName = kwargs['controller']
        
        #currentDirectory = os.getcwd()
        controllerSplit = controllerName.split(".")
        modulePath = ".".join(controllerSplit[:-1])
        className = controllerSplit[-1]

        controllerModule = importlib.import_module(modulePath)
        controllerClass = getattr(controllerModule, className)
        self.controller = controllerClass(**kwargs)
        self.controller.reset()
        
        self.observation_space = self.controller.get_observationSpace()
        self.action_space = self.controller.get_actionSpace()
    
    def configure(self, **kwargs):
        if 'steptime' in kwargs:
            self.stepTime = kwargs['steptime']
    """
    ---------------------------------------------------------------------------------------
    Main API:

    Attributes:
        observation_space
        action_space

    Methods:
        - observation = reset()
        - observation, reward, done, info = step(action)
        - render() -> not used
        
        observation and state are similarities
    """
    def step(self, action):
        self.controller.execute_action(action)
        time.sleep(self.stepTime)
        reward = self.controller.get_reward()
        ob = self.controller.get_observation()
        over = self.controller.get_gameOver()
        return ob, reward, over, {}
    
    '''
        Reset creates a new setting. It
        - recalculates the observation space
        - reset the abbort flag (if necessary)
    '''
    def reset(self):
        self.controller.reset()
        self.observation_space = self.controller.get_observationSpace()
        time.sleep(self.stepTime)
        return self.controller.get_observation()

    '''
        render has to be part of the API
        we have no data to render
    '''
    def render(self, mode='human', close=False):
        return self.controller.render()
