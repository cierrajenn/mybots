import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet_data, time, math, random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

targetAngles = np.linspace(-math.pi/4, math.pi/4, 1000)
np.save('data/motorVals.npy', targetAngles)
exit()

for _ in range(1000):
    # save each touch sensor value for the back and front legs
    backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link('BackLeg')
    frontLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link('FrontLeg')

    # create motors for front and back legs
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = 'Torso_BackLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = targetAngles[_],
                                maxForce = 50)
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = 'Torso_FrontLeg',
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = targetAngles[_],
                                maxForce = 50)
    
    p.stepSimulation()
    time.sleep(.016)

# save back and front leg touch sensor values ot their respective files
np.save('data/backLegSensorVals.npy', backLegSensorValues)
np.save('data/frontLegSensorVals.npy', frontLegSensorValues)

p.disconnect()

