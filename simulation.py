import pybullet as p
import pybullet_data, time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")

for _ in range(1000):
    p.stepSimulation()
    time.sleep(.016)
    print(_)

p.disconnect()
