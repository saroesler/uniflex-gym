# UniFlex-Gym

The [UniFlex environment](https://github.com/LARG/HFO) is an interface between UniFlex and openAI gym. It combines Software Defined Networking for WiFi with reinforcement learning. The environment creates a new interface to UniFlex controller. It is in the middle between the controller and the machine learning agent. The environent instantiates and starts the UniFlex controller. Therefore, it extends the openAI gym description by a `start_controller` method. The environent cares about steping. Therefore, the `step` method is a blocking call. Internaly it calls sleep. The sleep time in configurable.

A UniFlex controler has to implement the `UniFlexController` interface. 

## Installation

Please install UniFlex and openAI gym first:

```bash
cd uniflex-environent
pip install -e .
```

## Background
This work is part of the Bachelor Thesis
`Steuerung von Software Defined WLAN durch Machine Learning-Agenten am Beispiel der Kanalvergabe` at Technische Universität Berlin, Telecommunicatoin Network Group in 2019
