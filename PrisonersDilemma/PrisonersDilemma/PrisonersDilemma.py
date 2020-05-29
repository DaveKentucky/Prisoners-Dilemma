import random
import numpy
from deap import creator, base, tools, algorithms
import Game, Calculations, Fitness, Strategies
from tkinter import *

def main():
    
    bgColor = "LightSkyBlue2"
    fontColor = "grey18"

    window = Tk()
    window.configure(background = bgColor)
    window.title("Prisonner's Dilemma")

    Label(window, text = "Prisonner's Dilemma Genetic Algorithm", bg = bgColor, fg = fontColor, font = "none, 24").grid(row = 0, column = 0)
    Label(window, text = "Generations:", bg = bgColor, fg = fontColor, font = "none, 18").grid(row = 1, column = 0)
    Label(window, text = "Population size:", bg = bgColor, fg = fontColor, font = "none, 18").grid(row = 2, column = 0)
    Label(window, text = "Crossover Probability:", bg = bgColor, fg = fontColor, font = "none, 18").grid(row = 3, column = 0)
    Label(window, text = "Mutation Probability:", bg = bgColor, fg = fontColor, font = "none, 18").grid(row = 4, column = 0)

    window.mainloop()

    return

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
        #if random.random() < cxProb:
            toolbox.mate(child1, child2)

    # mutation of the offspring
    for mutant in offspring:
        if random.random() < mutProb:
            toolbox.mutate(mutant)

    population[:] = offspring
    evaluatePopulation()

    # for ind in population: print(ind, "\n", ind.fitness)
    # print("\n")

    return

# print given strategy decoded into 'C' for cooperate and 'D' for defect
def decodeStrategy(individual):

    strategy = numpy.array(individual[7:])
    length = numpy.size(strategy)
    if length == 64:
        for i in range(length):
            bin = numpy.binary_repr(i, 6)
            bin = bin + ": " + numpy.binary_repr(strategy[i])
            bin = bin.replace("0", "C")
            bin = bin.replace("1", "D")
            move = bin[:2] + " " + bin[2:4] + " " + bin[4:]
            print(move)

    return

indSize = 71   # size of single individual list
tournamentLength = 100
populationSize = 20
generations = 0
cxProb = 0.8
mutProb = 0.1

toolbox = base.Toolbox()

# create fitness maximizing the objective
creator.create("StrategyFitness", base.Fitness, weights = (1.0,))
# create individual containing of a list with created fitness
creator.create("Individual", numpy.ndarray, fitness = creator.StrategyFitness, scores = numpy.zeros(0, int))

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

main()

for ind in population:
    Strategies.TitForTat(ind, tournamentLength)
    Strategies.AlwaysCooperate(ind, tournamentLength)
    Strategies.AlwaysDefect(ind, tournamentLength)
    Strategies.Grudger(ind, tournamentLength)
    Strategies.Gradual(ind, tournamentLength)
    print(ind.scores)

for i in range(generations):
    nextGeneration()
    evaluatePopulation()
    best = tools.selBest(population, 1)
    print("\nGeneration", i + 1, ". Best fitness:", best[0].fitness)
    #if i > generations - 5:
        #decodeStrategy(best[0])

