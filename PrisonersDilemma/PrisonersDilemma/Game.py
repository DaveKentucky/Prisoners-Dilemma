import numpy

# get the next move based on 3 previous moves
def performMove(individual, previousMoves):

    if len(previousMoves) == 0:
        return individual[0]   # first encoded move
    if len(previousMoves) == 2:
        previousMovesValue = binToDec(previousMoves[1::2])
        return individual[previousMovesValue + 1]   # move based on first move
    if len(previousMoves) == 4:
        previousMovesValue = binToDec(previousMoves[1::2])
        return individual[previousMovesValue + 3]    # move based on 2 first moves
    if len(previousMoves) == 6:
        previousMovesValue = binToDec(previousMoves)
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

# convert binary value to decimal
def binToDec(binary):
    length = len(binary)
    decimal = 0
    for i in range(length):
        if binary[i] == 1:
            decimal += pow(2, (length - 1 - i))
    return decimal