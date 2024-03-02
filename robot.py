import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import constants as c
import numpy as np
from sensor import SENSOR
from motor import MOTOR
from world import WORLD

class ROBOT:            
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")        
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.prepare_to_sense()
        self.prepare_to_act()

    def prepare_to_sense(self):
        self.sensors = {}
        
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
        
    def sense(self, i):
        for t in self.sensors.values():
            t.getValue(i)

    def prepare_to_act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    def act(self, i):
        for motor in self.motors.values():
            motor.setValue(self.robotId, i)
    
