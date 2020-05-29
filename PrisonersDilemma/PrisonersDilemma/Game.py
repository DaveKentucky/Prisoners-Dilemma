import numpy
import Calculations

# Play a tournament among all population
def playTournament(population, rounds):
    popSize = len(population)
    scores = numpy.zeros((popSize, popSize), int)
    for i1 in range(popSize):
        for i2 in range(popSize):
            if i2 > i1:
                newScore = runGame(population[i1], population[i2], rounds)
                scores[i1, i2] = newScore[0]
                scores[i2, i1] = newScore[1]
    return scores

# Run a game between 2 individuals
def runGame(ind1, ind2, rounds):
    # arrays for history of performed moves
    previousMoves1 = numpy.empty(0, int)
    previousMoves2 = numpy.empty(0, int)

    score1 = 0
    score2 = 0
    for i in range(rounds):
        # perform both individuals moves
        newMove1 = performMove(ind1, previousMoves1)
        newMove2 = performMove(ind2, previousMoves2)
        # add performed moves to history
        numpy.append(previousMoves1, [newMove1, newMove2])
        numpy.append(previousMoves2, [newMove2, newMove1])
        # count score of the performed moves
        score = countScore(newMove1, newMove2)
        score1 += score[0]
        score2 += score[1]
        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves1 = previousMoves1[2:]
            previousMoves2 = previousMoves2[2:]

    #print("Score:", score1, score2)
    return score1, score2

# get the next move based on 3 previous moves
def performMove(individual, previousMoves):

    if len(previousMoves) == 0:
        return individual[0]   # first encoded move
    if len(previousMoves) == 2:
        previousMovesValue = Calculations.binToDec(previousMoves[1:2:2])
        return individual[previousMovesValue + 1]   # move based on first move
    if len(previousMoves) == 4:
        previousMovesValue = Calculations.binToDec(previousMoves[1:4:2])
        return individual[previousMovesValue + 3]    # move based on 2 first moves
    if len(previousMoves) == 6:
        previousMovesValue = Calculations.binToDec(previousMoves)
        return individual[previousMovesValue + 7]   # move based on 3 previous moves
    return

# count score of the single move
def countScore(myMove, enemyMove):
    if myMove == 0:
        if enemyMove == 0:
            return (3, 3)
        if enemyMove == 1:
            return (0, 5)
    if myMove == 1:
        if enemyMove == 0:
            return (5, 0)
        if enemyMove == 1:
            return (1, 1)
    return