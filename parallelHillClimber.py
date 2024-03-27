from solution import SOLUTION

import constants as c
import copy, os

class PARALLEL_HILL_CLIMBER():
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        
        self.nextAvailableID = 0
        
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def evolve(self):
        self.evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.evolve_for_one_generation()

        self.show_best()
            

    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.evaluate(self.children)
        self.print()
        self.select()

    def spawn(self):
        self.children = {}

        for i in range(len(self.parents)): 
            self.children[i] = copy.deepcopy(self.parents[i])
            self.nextAvailableID += 1

    def mutate(self):
        for item in self.children:
            self.children[item].mutate()

    def evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].start_simulation('DIRECT')

        for j in range(c.populationSize):
            solutions[j].wait_for_simulation_to_end()

    def select(self):
        for key in self.parents.keys():
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def print(self):
        print()
        print()
        for key in self.parents.keys():
            print(self.parents[key].fitness, self.children[key].fitness)
        print()

    def show_best(self):
        lowestFit = self.parents[0]

        for key in self.parents.keys():
            if self.parents[key].fitness < lowestFit.fitness:
                lowestFit = self.parents[key]
        lowestFit.start_simulation('GUI')
