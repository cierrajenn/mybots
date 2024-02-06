import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet_data, time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(100)

for _ in range(100):
    backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link('BackLeg')
    p.stepSimulation()
    time.sleep(.016)

p.disconnect()

print(backLegSensorValues)

