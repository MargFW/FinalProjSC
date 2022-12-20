# FinalProjSC

## Table of Contents
* Introduction
* Configuration/Installation
* Operating Instructions
* File Manifest
* Troubleshooting
* Credits and Acknowledgments

## Introduction
### General
This program visually actuates a robot through different heating and cooling cycles. User gets to choose amount of legs,
and window will show cycles, time, and distance traveled. Restuls can be used for SI.

### Inputs and Ouputs
The goal of this project is to show the actuation of a hydrogel robot through different heating and cooling cycles. Due to the chemcial nature of the hydrogels as well as their shapes/amounts when placed together, the. robots they compose can create drastically different movement arcs, and therefore differernt distances traveled. Input will be taken from the user to choose what kind of robot they would like to see actuated: 2 legs, three legs, or four. The "output" will be a window screen the user can interact with and see how the robot is actuated and how it's movement and displacement change as cycles are pushed.

## Configuration/Installation
User MUST have Arcade Library installed. If not, user can go to https://api.arcade.academy/en/latest/install/index.html#installation-instructions,
or use "pip install arcade" in terminal.

Once installed, user can download and run programs like standard. NOTICE: Images MUST be installed inside the same file where ROBORRUNNER is stored.

## Operating Instructions
Code may be run isntantaneously.

## File Manifest
The given files in this repository are:

README : This file, which describes the program, project, and its facets
ROBORUNNER: The robot visualization "game".
Images: The file containing frames for robot animation.

## Troubleshooting
Due to the demanding usage of the program, it is reccomennded to restart the kernel every fourth use. Refusing to restart the kernel can lead
to time delay in program actions, such as animation, causing timing to not line up with what is expected.

You can tell you need to restart the kernel if: animation of swelling/deswelling does not line up with heating/cooling cycles, heating/cooling cycles begin to overlap, etc.

Differences in processing may also vary by computer. Prrogram is currently written on a beat-up Mac.

## Credits and Acknowledgments
Creator (of code and figures):
* Margaret Wang   (MargFW)
Sources of Data:
* Aishwarya Pantula, Bibekananda Datta, Yupin Shi, Margaret Wang, Jiayu Liu, Siming Deng, Noah Cowan, Thao Nguyen, and David Gracias. "Untethered Unidirectionally Crawling Gels Driven by an Asymmetry in Contact Forces." (Science Robotics, 2022).![image. (https://user-images.githubusercontent.com/116837473/208569372-b685fe02-5cd6-4193-a696-7b09cb4b7d9b.png)

     
This project is inspired by EN.540.635 (Software Carpentry) with help of course intstructors Anastasia Georgiou and Colin Yancey.
