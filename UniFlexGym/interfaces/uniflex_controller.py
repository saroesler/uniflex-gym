from abc import ABC, abstractmethod

class UniFlexController(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def execute_action(self, action):
        pass
    
    @abstractmethod
    def render():
        pass
    
    @abstractmethod
    def get_observationSpace(self):
        pass
    
    @abstractmethod
    def get_actionSpace(self):
        pass
    
    @abstractmethod
    def get_observation(self):
        pass
    
    @abstractmethod
    def get_gameOver(self):
        pass
    
    @abstractmethod
    def get_reward(self):
        pass

