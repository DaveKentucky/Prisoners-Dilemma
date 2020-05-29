import numpy
import Strategies

# evaluate all individuals in given population          
def evaluate(pop, size, rounds, strChosen):
    
    min = float(0) # lowest score of population
    max = float(0) # highest score of population
    scores = numpy.empty(0, float)

    for ind in pop:
        Strategies.TestStrategy(ind, rounds, strChosen)
        indScore = numpy.average(ind.scores)
        scores = numpy.append(scores, indScore)

        # update lowest and highest scores
        if indScore < min:
            min = indScore
        if indScore > max:
            max = indScore

    avg = numpy.average(scores)
    coefficients = countCoefficients(min, max, avg, 2)

    for i in range(size):
        evaluateScaled(pop[i], scores[i], coefficients)
        print(i + 1, "score:", round(scores[i], 2), "fitness:", pop[i].fitness)

    return

# scale fitness of the individual with Goldberg's linear scaling
def evaluateScaled(individual, fRaw, coef):

    fitness = coef[0] * fRaw + coef[1]
    if fitness > float(0):
        individual.fitness = round(fitness, 2)
    else:
        individual.fitness = float(0)

    return

# count a and b coefficients for Goldberg's linear scaling
def countCoefficients(fMin, fMax, fAvg, c):

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