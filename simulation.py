import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet_data, time, math, random
import matplotlib.pyplot as plt

blAmplitude = np.pi/9
blFrequency = 0.08
blPhaseOffset = -np.pi/2

flAmplitude = np.pi/15
flFrequency = 0.08
flPhaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

targetAngles = np.linspace(0, 2, 1000)
np.save('data/motorVals.npy', targetAngles)
scaled_targetAngles = np.interp(targetAngles, (targetAngles.min(), targetAngles.max()), (-np.pi/4, np.pi/4))
np.save('data/scaledMotorVals.npy', scaled_targetAngles)
##print(targetAngles)

blVec = np.zeros(1000)
for i in range(1000):
    blVec[i] = blAmplitude * np.sin(blFrequency * i + blPhaseOffset)

flVec = np.zeros(1000)
for i in range(1000):
    flVec[i] = flAmplitude * np.sin(flFrequency * i + flPhaseOffset)

for _ in range(1000):
    # save each touch sensor value for the back and front legs
    backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link('BackLeg')
    frontLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link('FrontLeg')

    # create motors for front and back legs
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = 'Torso_BackLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = blVec[_],
                                maxForce = 50)
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = 'Torso_FrontLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = flVec[_],
                                maxForce = 50)
    
    p.stepSimulation()
    time.sleep(.00042)

# save back and front leg touch sensor values ot their respective files
np.save('data/backLegSensorVals.npy', backLegSensorValues)
np.save('data/frontLegSensorVals.npy', frontLegSensorValues)

p.disconnect()

