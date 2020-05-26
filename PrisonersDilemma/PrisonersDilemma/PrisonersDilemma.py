import random
import numpy
from deap import creator, base, tools, algorithms
import Generator, Game, Calculations, Fitness

def evaluateGeneration():
    
    tournamentScores = Game.playTournament(population, tournamentLength)
    #print(tournamentScores)

    maxPoints = 5 * (len(population) - 1) * tournamentLength
    Fitness.evaluatePopulation(population, tournamentScores, maxPoints)

    for ind in population: print(ind.fitness)
    
    return

def nextGeneration():
    toolbox = base.Toolbox()
    offspring = tools.selBest(population, offspringSize)
    offspring = list(map(toolbox.clone, offspring + offspring))
    
    for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
        tools.cxOnePoint(ind1, ind2)
        del ind1.fitness
        del ind2.fitness
    
    population[:] = offspring
    
    print("\n")
    #for ind in population: print(ind)
    
    return

tournamentLength = 10
populationSize = 8
offspringSize = int(populationSize / 2)
generations = 3

generator = Generator.Generator()
population = generator.generatePopulation(populationSize)
evaluateGeneration()

for i in range(generations):
   nextGeneration()
   evaluateGeneration()
    