import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='UniflexRRM-v0',
    entry_point='uniflex_rrm.envs:UniflexRRM',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)
