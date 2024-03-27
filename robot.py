import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import constants as c
import numpy as np
import os

from sensor import SENSOR
from motor import MOTOR
from world import WORLD
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:            
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")        
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")

        os.remove("brain" + str(solutionID) + ".nndf")

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                self.jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                self.desiredAngle = (self.nn.Get_Value_Of(neuronName)) * c.motorJointRange
                self.motors[self.jointName].setValue(self.robotId, self.desiredAngle)

    def think(self):
        self.nn.Update()

    def get_fitness(self):
        self.stateOfLinkZero = p.getLinkState(self.robotId, 0)
        self.posOfLinkZero = self.stateOfLinkZero[0]
        self.xCoordinateOfLinkZero = self.posOfLinkZero[0]

        with open('tmp' + str(self.solutionID) + '.txt', 'w') as f:
            f.write(str(self.xCoordinateOfLinkZero))

        os.rename("tmp" + str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")

        f.close()
