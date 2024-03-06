import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.x = np.linspace(0, 2 * np.pi, c.iters)
        self.motorVals = {}
        self.prepare_to_act()

    def prepare_to_act(self):   
        if self.jointName == 'Torso_BackLeg':
            self.amplitude = c.amplitude
            self.frequency = c.frequency
            self.phaseOffset = c.phaseOffset
        else:
            self.amplitude = c.amplitude
            self.frequency = c.frequency
            self.phaseOffset = c.phaseOffset/3
            self.frequency = c.frequency/3
            
        self.motorVals = self.amplitude * np.sin(self.frequency * self.x + self.phaseOffset)

    def setValue(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName,
                                                        controlMode = p.POSITION_CONTROL,
                                                        targetPosition = desiredAngle,
                                                        maxForce = c.force)

                
        
