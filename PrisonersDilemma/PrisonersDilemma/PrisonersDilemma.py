import random
import numpy
from deap import creator, base, tools, algorithms
import Game, Calculations, Fitness

def evaluatePopulation():
    
    for ind in population:
        if ind.fitness:
            del ind.fitness

    tournamentScores = Game.playTournament(population, tournamentLength)
    #print(tournamentScores)

    maxPoints = 5 * (len(population) - 1) * tournamentLength
    Fitness.evaluatePopulation(population, tournamentScores, maxPoints)

    #for ind in population: print(ind.fitness)
    
    return

def nextGeneration():
    offspring = toolbox.select(population, populationSize)
    offspring = list(map(toolbox.clone, offspring))
    random.shuffle(offspring)

    # for ind in offspring: print(ind, "\n", ind.fitness)
    # print("\n")

    # crossover of the offspring
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < cxProb:
            toolbox.mate(child1, child2)

    # mutation of the offspring
    for mutant in offspring:
        if random.random() < mutProb:
            toolbox.mutate(mutant)

    population[:] = offspring
    evaluatePopulation()

    for ind in population: print(ind, "\n", ind.fitness)
    print("\n")

    return

indSize = 71   # size of single individual list
tournamentLength = 10
populationSize = 10
generations = 2
cxProb = 0.8
mutProb = 0.3

toolbox = base.Toolbox()

# create fitness maximizing the objective
creator.create("StrategyFitness", base.Fitness, weights = (1.0,))
# create individual containing of a list with created fitness
creator.create("Individual", numpy.ndarray, fitness = creator.StrategyFitness)

# register function generating random value for initialized individual
toolbox.register("boolAttribute", random.randint, 0, 1)
# register function creating new individual
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.boolAttribute, n = indSize)
# register function creating new population
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# register function selecting individual from population
toolbox.register("select", tools.selTournament, tournsize = 2)
# register function mating two individuals with one point crossover
toolbox.register("mate", tools.cxOnePoint)
# register function mutating individual with 5% probability of shuffling indexes
toolbox.register("mutate", tools.mutShuffleIndexes, indpb = 0.05)

population = toolbox.population(populationSize)
evaluatePopulation()

# ind in population: print(ind, "\n", ind.fitness)
# print("\n")

for i in range(generations):
   nextGeneration()
   evaluatePopulation()
    