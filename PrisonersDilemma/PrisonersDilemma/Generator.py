import random
import numpy
from deap import creator, base, tools, algorithms

class Generator:
    def __init__(self):
        self.toolbox = base.Toolbox()
        # create fitness maximizing the objective
        creator.create("StrategyFitness", base.Fitness, weights = (1.0,))
        # create individual containing of a list with created fitness
        creator.create("Individual", numpy.ndarray, fitness = creator.StrategyFitness)

        strategySize = 71   # size of single individual list

        # register alias generating random value for initialized individual
        self.toolbox.register("boolAttribute", random.randint, 0, 1)
        # register alias creating new individual
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.boolAttribute, n = strategySize)
        # register alias creating new population
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
    
        return

    def generatePopulation(self, n):
        newPopulation = self.toolbox.population(n)
        for i in newPopulation:
            print(i)
    
        return newPopulation
