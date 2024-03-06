import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.robot = ROBOT()
        self.world = WORLD()
        self.robot.prepare_to_sense()
        self.robot.prepare_to_act()
        
        p.setGravity(0, 0, -9.8)

    def run(self):
       for i in range(c.iters):
            self.robot.sense(i)
            self.robot.think()
            self.robot.act(i)
            time.sleep(.00042)
                

    def __del__(self):
        p.disconnect()
