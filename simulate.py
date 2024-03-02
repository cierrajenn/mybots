import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet_data, time, math, random
import matplotlib.pyplot as plt

from simulation import SIMULATION

simulation = SIMULATION()
simulation.run()

##
### save back and front leg touch sensor values ot their respective files
##np.save('data/backLegSensorVals.npy', backLegSensorValues)
##np.save('data/frontLegSensorVals.npy', frontLegSensorValues)
##
##p.disconnect()
##
