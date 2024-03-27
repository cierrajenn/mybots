import numpy as np
import pyrosim.pyrosim as pyrosim
import os, random, time

class SOLUTION():
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name = "World", pos = [5, 5, 0.5], size = [1, 1, 1])
        pyrosim.End()
    

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name = "Torso", pos = [1.5, 0, 1.5], size = [1, 1, 1])

        pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg",
                           type = "revolute", position = [1, 0, 1])

        pyrosim.Send_Cube(name = "BackLeg", pos = [-0.5, 0, -0.5], size = [1, 1, 1])
        
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg",
                           type = "revolute", position = [2, 0, 1])
        
        pyrosim.Send_Cube(name = "FrontLeg", pos = [0.5, 0, -0.5], size = [1, 1, 1])
        

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron(name = 3, jointName = 'Torso_BackLeg')
        pyrosim.Send_Motor_Neuron(name = 4, jointName = 'Torso_FrontLeg')

        pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 3, weight = -1.0)
        #pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 3, weight = 1.5)
        pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 3, weight = -1.0)

        pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 4, weight = -1.0)
        #pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 4, weight = 0.75)
        pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 4, weight = -1.0)
        
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)

        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

    def start_simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

    def wait_for_simulation_to_end(self):
        self.fitnessFileName = 'fitness' + str(self.myID) + '.txt'

        while not os.path.exists(self.fitnessFileName):
            time.sleep(0.01)

        with open(self.fitnessFileName, 'r') as f:
            for line in f:
                self.fitness = float(line)

        f.close()

        os.remove(self.fitnessFileName)

    def set_ID(self):
        pass

