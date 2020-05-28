import numpy
import Game

# plays single game against and TitForTat strategy
def TitForTat(individual, rounds):
    
    myScore = 0
    indScore = 0
    myMove = 0
    indMove = 0
    previousMoves = numpy.empty(0, int)

    for i in range(rounds):
        # find next move of individual
        indMove = Game.performMove(individual, previousMoves)
        # get this round scores
        score = Game.countScore(myMove, indMove)
        # add performed moves to history
        previousMoves = numpy.append(previousMoves, [myMove, indMove])
        myScore += score[0]
        indScore += score[1]
        myMove = indMove
        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves = previousMoves[2:]

    return (myScore, indScore)
