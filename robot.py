import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import constants as c
import numpy as np
from sensor import SENSOR
from motor import MOTOR
from world import WORLD
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:            
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")        
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.nn = NEURAL_NETWORK("brain.nndf")

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
                self.desiredAngle = self.nn.Get_Value_Of(neuronName)
                
                #self.motors[bytes(self.jointName, 'ASCII')].setValue(self.robotId, self.desiredAngle)
                for motor in self.motors.values():
                    motor.setValue(self.robotId, self.desiredAngle)


    def think(self):
        self.nn.Update()
        self.nn.Print()
