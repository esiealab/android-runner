[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=S2-group_android-runner&metric=alert_status)](https://sonarcloud.io/dashboard?id=S2-group_android-runner)
[![Build Status](https://travis-ci.org/S2-group/android-runner.svg?branch=master)](https://travis-ci.org/S2-group/android-runner)
[![Coverage Status](https://coveralls.io/repos/github/S2-group/android-runner/badge.svg?branch=master)](https://coveralls.io/github/S2-group/android-runner?branch=master&service=github)
# Android Runner
Android Runner (AR) is a tool for automatically executing measurement-based experiments on native and web apps running on Android devices.

The following scientific publication gives an overview about the main components, plugins, and configurations of Android Runner (as of 2020): [A-Mobile 2020 publication](https://github.com/S2-group/android-runner/blob/master/documentation/A_Mobile_2020.pdf)  

A complete tutorial on how to use Android Runner is available in the following YouTube playlist: [Android Runner Tutorials](https://www.youtube.com/watch?v=-ZXT176ljjI&list=PLLbZZOioDh3P50WcYbuBMZEJokJH3ZONr).

As visualized below, Android Runner consists of the following components:
- **Experiment orchestrator**: Is in charge of executing the whole experiment according to the experiment configuration provided by the user.
- **Devices manager**: Is responsible for providing a layer of abstraction on the low-level operations involving the Android devices.
- **Progress manager**: Keeps track of the execution of each run of the experiment.
- **Plugin handler**: Provides a set of facilities for managing the profilers and an extension point that third-party developers can use for integrating their own measurement tools into Android Runner.

<p align="center">
<img src="./documentation/overview.jpg" alt="Overview of Android Runner" width="500"/>
</p>

## Table of Contents
- [How to Cite Android Runner](#how-to-cite-android-runner)
- [Setup](#setup)
- [Quick Start](#quick-start)
- [Structure](#structure)
  - [devices.json](#devicesjson)
  - [Experiment Configuration](#experiment-configuration)
- [Plugin Profilers](#plugin-profilers)
- [Experiment Continuation](#experiment-continuation)
- [Compatible Devices](#compatible-devices)

## How to Cite Android Runner

If Android Runner is helping your research, consider to cite it as follows, thanks!

``` 
@inproceedings{A_Mobile_2020,
  title={{A Framework for the Automatic Execution of Measurement-based Experiments on Android Devices}},
  author={Ivano Malavolta and Eoin Martino Grua and Cheng-Yu Lam and Randy de Vries and Franky Tan and Eric Zielinski and Michael Peters and Luuk Kaandorp},
  booktitle={35th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW '20)},
  year={2020},
  url= {https://github.com/S2-group/android-runner/blob/master/documentation/A_Mobile_2020.pdf},
  organization={ACM}
}
```

## Setup
Instructions can be found [here](https://github.com/S2-group/android-runner/wiki/Setup). Instructions for specific plugins are included in the plugins' READMEs.

## Quick Start
To run an experiment, run:
```bash
python3 android-runner path_to_your_config.json
```
Example configuration files can be found in the subdirectories of the `examples` directory.

**More information about the specifics of Android Runner and use cases can be found in the [Wiki tab](https://github.com/S2-group/android-runner/wiki).**
