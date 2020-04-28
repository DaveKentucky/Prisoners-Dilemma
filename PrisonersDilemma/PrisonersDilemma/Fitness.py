import numpy


# evaluate fitness of each individual in population
def evaluatePopulation(population, scores, maxPoints):
    popSize = len(population)
    sum = numpy.zeros(popSize, int)    # temporary array for score sums
    
    # sum the scores of each individual
    for i in range(popSize):
        for j in range(popSize):
            sum[i] += scores[i, j]

    # evaluate fitness of each individual
    for i in range(popSize):
        evaluate(population[i], sum[i], maxPoints)

    return
            
# evaluate fitness of the individual based on tournament score
def evaluate(individual, score, max):
    individual.fitness = (score / max)
    return
