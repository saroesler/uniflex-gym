import os, time
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding
import importlib
import logging
import yaml
import threading

from uniflex.core.agent import Agent


logger = logging.getLogger(__name__)

'''
TODO
except KeyboardInterrupt:
        logger.debug("Agent exits")
    finally:
        logger.debug("Exit")
        agent.stop()
'''

class UniflexEnv(gym.Env):
    def __init__(self):
        self.stepTime = 10
        self.controller = None
        self.uniflex_agent = Agent()
    
    def start_controller(self, **kwargs):
        '''
        This part of the code is taken from uniflex-agent
        Copyright (c) 2015, Technische Universität Berlin
        Authors: Piotr Gawlowicz, Mikolaj Chwalisz
        '''
        logger.debug(kwargs)
        if not 'config' in kwargs:
            logger.error("Please run OpenAI uniflex_env with a uniflex config file")
            raise AttributeError('No config file')
            return
        
        config_file_path = kwargs['config']
        
        configPath = os.path.dirname(os.path.abspath(config_file_path))
        
        config = None
        with open(config_file_path, 'r') as f:
            config = yaml.load(f)
        
        self.uniflex_agent.load_config(config, configPath)
        '''
        self.uniflex_agent.run() is blocking, 
        paste the remaining code here:
        '''
        self.uniflex_agent.moduleManager.start()
        
        
        '''
        start 
        '''
        controllerList = self._get_openAI_controller(config, self.uniflex_agent.moduleManager)
        if len(controllerList) < 1:
            logger.error("We cannot find a OpenAI controller. Please define it in the config file")
            raise AttributeError('No cntroller!')
            return
        self.controller = controllerList[0]
        threading.currentThread().module = self.controller
        self.controller.reset()
        self.observation_space = self.controller.get_observationSpace()
        self.action_space = self.controller.get_actionSpace()
        
        if 'steptime' in kwargs:
            self.stepTime = kwargs['steptime']
    
    def _get_openAI_controller(self, config, moduleManager):
        controlApps = config.get('control_applications', {})
        openAIModules = []
        
        for controlAppName, params in controlApps.items():
            pyModuleName = params.get('module', None)
            if not pyModuleName:
                myfile = params.get('file', None)
                pyModuleName = myfile.split('.')[0]
            pyClassName = params.get('class_name', None)
            openAiGymControler = params.get('openAIGymController', False)
            
            if(not openAiGymControler):
                continue
            
            for module in moduleManager.modules.values():
                if module.name == pyClassName:
                    openAIModules.append(module)
        return openAIModules
    '''
        def configure(self, **kwargs):
            if 'steptime' in kwargs:
                self.stepTime = kwargs['steptime']
    '''
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
        self.action_space = self.controller.get_actionSpace()
        time.sleep(self.stepTime)
        return self.controller.get_observation()

    '''
        render has to be part of the API
        we have no data to render
    '''
    def render(self, mode='human', close=False):
        return self.controller.render()
