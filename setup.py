from setuptools import setup, find_packages

setup(name='UniFlexGym',
    version='0.0.3',
    install_requires=['gym>=0.2.3'],
    packages=find_packages(),
    scripts=[],
    url='',
    license='MIT',
    author='Sascha Rösler',
    author_email='s.roesler@campus.tu-berlin.de',
    description='OpenAI Gym meets uniflex',
    long_description='OpenAI Gym meets uniflex',
    keywords='openAI gym, RL, uniflex',
)
