import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
