import random
import numpy
from deap import creator, base, tools, algorithms
import Game, Fitness
from tkinter import *

def main():
    
    bgColor = "LightSkyBlue2"
    fontColor = "grey18"

    window = Tk()
    window.configure(background = bgColor)
    window.title("Prisonner's Dilemma")

    Label(window, text = "Prisonner's Dilemma Genetic Algorithm", font = "none, 24", bg = bgColor, fg = fontColor).grid(row = 0, column = 0, columnspan = 2, padx = 2, pady = 8)
    Label(window, text = "Population size:", font = "none, 18", bg = bgColor, fg = fontColor).grid(row = 1, column = 0, padx = 70, pady = 2, sticky = W)
    Label(window, text = "Generations:", font = "none, 18", bg = bgColor, fg = fontColor).grid(row = 2, column = 0, padx = 70, pady = 2, sticky = W)
    Label(window, text = "Crossover Probability:", font = "none, 18", bg = bgColor, fg = fontColor).grid(row = 3, column = 0, padx = 70, pady = 2, sticky = W)
    Label(window, text = "Mutation Probability:", font = "none, 18", bg = bgColor, fg = fontColor).grid(row = 4, column = 0, padx = 70, pady = 2, sticky = W)
    Label(window, text = "Tournament rounds:", font = "none, 18", bg = bgColor, fg = fontColor).grid(row = 5, column = 0, padx = 70, pady = 2, sticky = W)
    
    varPop = DoubleVar(value = 20)  # initial value of population
    varGen = DoubleVar(value = 100)  # initial value of generations
    varCX = DoubleVar(value = 0.75)  # initial value of crossover probability
    varMut = DoubleVar(value = 0.30)  # initial value of mutation probability
    varRounds = DoubleVar(value = 100) # initial value of rounds per tournament

    spinboxPop = Spinbox(window, from_ = 2, to = 50, width = 4, fg = fontColor, font = "none, 16", textvariable = varPop)
    spinboxPop.grid(row = 1, column = 1)
    spinboxGen = Spinbox(window, from_ = 0, to = 500, width = 4, fg = fontColor, font = "none, 16", textvariable = varGen)
    spinboxGen.grid(row = 2, column = 1)
    spinboxCX = Spinbox(window, from_ = 0.00, to = 1.00, increment = 0.05, width = 4, fg = fontColor, font = "none, 16", textvariable = varCX)
    spinboxCX.grid(row = 3, column = 1)
    spinboxMut = Spinbox(window, from_ = 0.00, to = 1.00, increment = 0.05, width = 4, fg = fontColor, font = "none, 16", textvariable = varMut)
    spinboxMut.grid(row = 4, column = 1)
    spinboxRounds = Spinbox(window, from_ = 0, to = 300, width = 4, fg = fontColor, font = "none, 16", textvariable = varRounds)
    spinboxRounds.grid(row = 5, column = 1)

    Label(window, text = "Predefined strategies:", font = "none, 18", bg = bgColor, fg = fontColor).grid(row = 6, column = 0, columnspan = 2, pady = 10)
    Label(window, text = "Always Cooperate", font = "none, 14", bg = bgColor, fg = fontColor).grid(row = 7, column = 0, padx = 70, sticky = W)
    Label(window, text = "Always Defect", font = "none, 14", bg = bgColor, fg = fontColor).grid(row = 8, column = 0, padx = 70, sticky = W)
    Label(window, text = "Gradual", font = "none, 14", bg = bgColor, fg = fontColor).grid(row = 9, column = 0, padx = 70, sticky = W)
    Label(window, text = "Grudger", font = "none, 14", bg = bgColor, fg = fontColor).grid(row = 10, column = 0, padx = 70, sticky = W)
    Label(window, text = "Pavlov", font = "none, 14", bg = bgColor, fg = fontColor).grid(row = 11, column = 0, padx = 70, sticky = W)
    Label(window, text = "Soft-Majo", font = "none, 14", bg = bgColor, fg = fontColor).grid(row = 12, column = 0, padx = 70, sticky = W)
    Label(window, text = "Tit For Tat", font = "none, 14", bg = bgColor, fg = fontColor).grid(row = 13, column = 0, padx = 70, sticky = W)
    Label(window, text = "Tit For 2 Tats", font = "none, 14", bg = bgColor, fg = fontColor).grid(row = 14, column = 0, padx = 70, sticky = W)

    alwaysCooperate = IntVar(value = 1)
    Checkbutton(window, variable = alwaysCooperate, bg = bgColor).grid(row = 7, column = 1, padx = 70, sticky = E)
    alwaysDefect = IntVar(value = 1)
    Checkbutton(window, variable = alwaysDefect, bg = bgColor).grid(row = 8, column = 1, padx = 70, sticky = E)
    gradual = IntVar(value = 1)
    Checkbutton(window, variable = gradual, bg = bgColor).grid(row = 9, column = 1, padx = 70, sticky = E)
    grudger = IntVar(value = 1)
    Checkbutton(window, variable = grudger, bg = bgColor).grid(row = 10, column = 1, padx = 70, sticky = E)
    pavlov = IntVar(value = 1)
    Checkbutton(window, variable = pavlov, bg = bgColor).grid(row = 11, column = 1, padx = 70, sticky = E)
    softMajo = IntVar(value = 1)
    Checkbutton(window, variable = softMajo, bg = bgColor).grid(row = 12, column = 1, padx = 70, sticky = E)
    titForTat = IntVar(value = 1)
    Checkbutton(window, variable = titForTat, bg = bgColor).grid(row = 13, column = 1, padx = 70, sticky = E)
    titFor2Tats = IntVar(value = 1)
    Checkbutton(window, variable = titFor2Tats, bg = bgColor).grid(row = 14, column = 1, padx = 70, sticky = E)


    def LaunchGA():

        popSize = int(spinboxPop.get())
        generations = int(spinboxGen.get())
        cxProb = float(spinboxCX.get())
        mutProb = float(spinboxMut.get())
        rounds = int(spinboxRounds.get())
        strategies = [alwaysCooperate.get(), alwaysDefect.get(), gradual.get(), grudger.get(), pavlov.get(), softMajo.get(), titForTat.get(), titFor2Tats.get()]
        
        scores = numpy.zeros(5)
        for i in range(5):
            scores[i] = StartGeneration(popSize, generations, cxProb, mutProb, rounds, strategies)
        
        avg = numpy.average(scores)
        file = open("results.txt", "w")
        for f in scores:
            file.write(str(f))
            file.write("\n")

        file.write("Average: " + str(avg))

        file.close()
        print("Successfully saved results of 5 generations to file\n")

        return

    Button(window, text = "Start", font = "none, 10", bg = fontColor, activebackground = "gray48", fg = "white", width = 20, command = LaunchGA).grid(row = 15, column = 0, columnspan = 2, pady = 10)

    window.mainloop()

    return

def StartGeneration(popSize, gen, cxProb, mutProb, tournamentRounds, strategies):
    
    indSize = 71   # size of single individual array

    # create fitness maximizing the objective
    creator.create("StrategyFitness", base.Fitness, weights = (1.0,))
    # create individual containing of a list with created fitness
    creator.create("Individual", numpy.ndarray, fitness = creator.StrategyFitness, scores = numpy.empty(0, int))
    
    # register function generating random value for initialized individual
    toolbox.register("boolAttribute", random.randint, 0, 1)
    # register function creating new individual
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.boolAttribute, n = indSize)
    # register function creating new population
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    # register function evaluating fitness
    toolbox.register("evaluate", Fitness.evaluate, size = popSize, rounds = tournamentRounds, strategyChosen = strategies)
    # register function selecting individual from population with Tournament Selection
    toolbox.register("selectTournament", tools.selTournament, tournsize = 2)
    # register function selecting individual from population with Roulette Selection
    toolbox.register("selectRoulette", RouletteSelection)
    # register function selecting individual from population with Rank Selection
    toolbox.register("selectRank", RankSelection)
    # register function mating two individuals with one point crossover
    toolbox.register("mateOnePoint", tools.cxOnePoint)
    # register function mating two individuals with one point crossover
    toolbox.register("mateTwoPoints", tools.cxTwoPoint)
    # register function mutating individual with 5% probability of shuffling indexes
    toolbox.register("mutateShuffleIndexes", tools.mutShuffleIndexes, indpb = 0.05)
    # register function mutating individual with 5% probability of flipping bit
    toolbox.register("mutateFlipBit", tools.mutFlipBit, indpb = 0.05)
    
    population = toolbox.population(popSize)
    toolbox.evaluate(population)
    best = tools.selBest(population, 1)
    print("\nGeneration 0. Highest score:", numpy.average(best[0].scores), "Best fitness:", best[0].fitness, "\n")
        
    for i in range(gen):
        population = nextGeneration(population, popSize, cxProb, mutProb)
        best = tools.selBest(population, 1)
        print("\nGeneration", str(i + 1) + ". Highest score:", numpy.average(best[0].scores), "Best fitness:", best[0].fitness, "\n")

    #decodeStrategy(best[0])

    return numpy.average(best[0].scores)

def nextGeneration(pop, popSize, cxProb, mutProb):
    offspring = toolbox.selectRank(pop, popSize)
    offspring = list(map(toolbox.clone, offspring))
    random.shuffle(offspring)

    # crossover of the offspring
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < cxProb:
            toolbox.mateOnePoint(child1, child2)
            del child1.fitness
            del child2.fitness

    # mutation of the offspring
    for mutant in offspring:
        if random.random() < mutProb:
            toolbox.mutateShuffleIndexes(mutant)

    pop[:] = offspring
    toolbox.evaluate(pop)

    return pop

# print given strategy decoded into 'C' for cooperate and 'D' for defect
def decodeStrategy(individual):

    beg = individual[:7]
    strBeg = "First: " + str(beg[0]) + "\n Opponent C: " + str(beg[1]) + "\n Opponent D: " + str(beg[2]) + "\n Opponent CC: " + str(beg[3]) + "\n Opponent CD: " + str(beg[4]) + "\n Opponent DC: " + str(beg[5]) + "\n Opponent DD: " + str(beg[6])
    strBeg = strBeg.replace("0", "C")
    strBeg = strBeg.replace("1", "D")    
    print(strBeg)

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

# select k individuals from population with Roulette Selection
def RouletteSelection(population, k):
    
    offspring = list()
    popProb = numpy.zeros(len(population))
    sumFitness = 0
    sumProb = 0

    # sum fitness values of all individuals in population
    for ind in population:
        sumFitness += ind.fitness

    # count the probabilities for selection of each individual in population
    for i in range(len(population)):
        tmp = population[i].fitness / sumFitness
        popProb[i] = sumProb + tmp   
        sumProb += tmp
    
    # select k individuals from population
    for i in range(k):
        rand = random.random()
        for j in range(len(population)):
            if rand <= popProb[j]:
                offspring.append(population[j])
                break

    return offspring

# select k individual from population with Rank Selection
def RankSelection(population, k):
    
    offspring = list()
    popProb = numpy.zeros(len(population))
    popFitness = numpy.zeros(len(population))
    sumProb = 0

    # copy the fitness values of all individuals in population
    for i in range(len(population)):
        popFitness[i] = population[i].fitness

    # sort the array with fitness values
    popFitness = numpy.sort(popFitness)

    lowestProb = 1.0 / len(population)

    # count the probabilities for selection of each individual in population
    for i in range(len(population)):
         for j in range(len(population)):
             if population[i].fitness == popFitness[j]:
                 popProb[i] =  sumProb + j + 1
                 sumProb += (j + 1)
                 break

    # select k individuals from population
    for i in range(k):
        rand = random.randint(0, sumProb)
        for j in range(len(population)):
            if rand <= popProb[j]:
                offspring.append(population[j])
                break

    return offspring

cxProb = 0.8
mutProb = 0.1

toolbox = base.Toolbox()
main()