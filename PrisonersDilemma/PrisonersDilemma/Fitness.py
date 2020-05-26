import numpy


# evaluate fitness of each individual in population
def evaluatePopulation(population, scores, maxPoints):
    popSize = len(population)
    sum = numpy.zeros(popSize, int)    # temporary array for score sums
    
    fitnessRaw = numpy.zeros(popSize, float)
    fitnessMax = float(0)
    fitnessMin = float(0)
    fitnessAvg = float(0)
    maxReproduction = 2

    # sum the scores of each individual
    for i in range(popSize):
        for j in range(popSize):
            sum[i] += scores[i, j]

    # evaluate raw fitness of each individual
    for i in range(popSize):
        fitnessRaw[i] = evaluateRaw(sum[i], maxPoints) # count raw fitness

        if fitnessRaw[i] > fitnessMax:
            fitnessMax = fitnessRaw[i] # update highest raw fitness
        if fitnessRaw[i] < fitnessMin:
            fitnessMin = fitnessRaw[i]  # update lowest raw fitness

    fitnessAvg = numpy.average(fitnessRaw)  # count avarage raw fitness
    coefficients = countCoefficients(fitnessMax, fitnessMin, fitnessAvg, maxReproduction)   # count scaling function coefficients
   
    for i in range(popSize):
        evaluateScaled(population[i], fitnessRaw[i], coefficients)  # count scaled fitness

    return
            
# evaluate raw fitness of the individual based on tournament score
def evaluateRaw(score, max):

    fitness = (score / max)
    return fitness

# evaluate scaled fitness of the individual with Goldberg's linear scaling
def evaluateScaled(individual, fRaw, coef):

    fitness = coef[0] * fRaw + coef[1]
    if fitness > float(0):
        individual.fitness = fitness
    else:
        individual.fitness = float(0)

    return

# count a and b coefficients for Goldberg's linear scaling
def countCoefficients(fMax, fMin, fAvg, c):

    check = float(c * (fAvg - fMax) / (c - 1))
    if fMin > check:    # regular coefficients
        divider = float(fMax - fAvg)
        dividend1 = float((c - 1) * fAvg)
        dividend2 = float(fMax - (c * fAvg))
        a = dividend1 / divider
        b = fAvg * (dividend2 / divider)
    else:   # avoiding negative fitness
        divider = float(fAvg - fMin)
        dividend = float(fMin * fAvg)
        a = float(fAvg/ (fAvg - fMin))
        b = dividend / divider

    return (a, b)