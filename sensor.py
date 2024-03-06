import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.iters)

    def getValue(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
