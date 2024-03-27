from solution import SOLUTION

import constants as c
import copy

#import numpy as np

class HILL_CLIMBER():
    def __init__(self):
        self.parent = SOLUTION()

    def evolve(self):
        #self.parent.evaluate('DIRECT')

        for currentGeneration in range(c.numberOfGenerations):
            if currentGeneration == 0:
                self.parent.evaluate('GUI')
            else:
                self.parent.evaluate('DIRECT')
            self.evolve_for_one_generation()

    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.child.evaluate('DIRECT')
        self.print()
        self.select()

    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def print(self):
        print(self.parent.fitness, self.child.fitness)

    def show_best(self):
        self.parent.evaluate('GUI')
