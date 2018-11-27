import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='uniflex-v0',
    entry_point='UniFlexGym.envs.uniflex_env:UniflexEnv',
)

