import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet_data, time, math, random
import matplotlib.pyplot as plt

import os, sys

from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)
simulation.run()
simulation.get_fitness()


##
### save back and front leg touch sensor values ot their respective files
##np.save('data/backLegSensorVals.npy', backLegSensorValues)
##np.save('data/frontLegSensorVals.npy', frontLegSensorValues)
##
##p.disconnect()
##
