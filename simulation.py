import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for _ in range(1000):
    p.stepSimulation()
    time.sleep(.016)
    print(_)

p.disconnect()
