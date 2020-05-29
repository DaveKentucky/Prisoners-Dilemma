import numpy
import Game

# plays single game against the TitForTat strategy
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

        # copy individual's previous move
        myMove = indMove

        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves = previousMoves[2:]

    individual.scores = numpy.append(individual.scores, indScore)
   
    return

# plays single game against the TitFor2Tats strategy
def TitFor2Tats(individual, rounds):
    
    myScore = 0
    indScore = 0
    myMove = 0
    indMove = 0
    defectsCount = 0
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

        # increment counter of individual's defections committed in a row
        if indMove == 1:
            defectsCount += 1
        else:
            defectsCount = 0
        # set myMove to defection if individual defected 2 times in a row, otherwise copy individual's move
        if defectsCount == 2:
            myMove = 1
        else:
            myMove = indMove

        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves = previousMoves[2:]

    individual.scores = numpy.append(individual.scores, indScore)
   
    return


# plays single game against the AlwaysCooperate strategy
def AlwaysCooperate(individual, rounds):
    
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

        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves = previousMoves[2:]

    individual.scores = numpy.append(individual.scores, indScore)

    return

# plays single game against the AlwaysDefect strategy
def AlwaysDefect(individual, rounds):
    
    myScore = 0
    indScore = 0
    myMove = 1
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

        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves = previousMoves[2:]

    individual.scores = numpy.append(individual.scores, indScore)

    return

# plays single game against the Grudger strategy
def Grudger(individual, rounds):
    
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

        # if individual defected, set myMove to defect
        if myMove == 0:
            if indMove == 1:
                myMove = 1

        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves = previousMoves[2:]

    individual.scores = numpy.append(individual.scores, indScore)

    return

# plays single game against the Gradual strategy
def Gradual(individual, rounds):
    
    myScore = 0
    indScore = 0
    myMove = 0
    indMove = 0
    defectsCount = 0
    defectsLeft = 0
    cooperationsLeft = 0
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
        
        # if individual defected increment counter
        if indMove == 1:
            defectsCount += 1
        if myMove == 1:
            defectsLeft -= 1
            # if it was the last defect change to cooperate for 2 turns
            if defectsLeft == 0:
                myMove = 0
                cooperationsLeft = 2
        else:
            cooperationsLeft -= 1
            # if at least 2 cooperations have been performed check if individual defected
            if cooperationsLeft <= 0:
                if indMove == 1:
                    myMove = 1
                    defectsLeft = defectsCount

        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves = previousMoves[2:]

    individual.scores = numpy.append(individual.scores, indScore)
   
    return

# plays single game against the Soft-Majo strategy
def SoftMajo(individual, rounds):
    
    myScore = 0
    indScore = 0
    myMove = 0
    indMove = 0
    defectsCount = 0
    cooperaionsCount = 0
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
        
        # increment counters of individual's specific moves
        if indMove == 0:
            cooperaionsCount += 1
        else:
            defectsCount += 1
        # set myMove based on moves performed by individual
        if cooperaionsCount >= defectsCount:
            myMove = 0
        else:
            myMove = 1

        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves = previousMoves[2:]

    individual.scores = numpy.append(individual.scores, indScore)
   
    return

# plays single game against the Pavlov strategy
def Pavlov(individual, rounds):
    
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
        
        # set myMove to cooperate if both players agreed this turn, otherwise set myMove to defect
        if myMove == indMove:
            myMove = 0
        else:
            myMove = 1

        # remove the oldest moves performed from history
        if i >= 3:
            previousMoves = previousMoves[2:]

    individual.scores = numpy.append(individual.scores, indScore)
   
    return