import random
import numpy
from deap import creator, base, tools, algorithms
import Generator, Game, Calculations

generator = Generator.Generator()
population = generator.generatePopulation(20)

Game.runGame(population[0], population[1], 10)