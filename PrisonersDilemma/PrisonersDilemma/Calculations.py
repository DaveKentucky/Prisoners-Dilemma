import numpy

# convert binary value to decimal
def binToDec(binary):
    length = len(binary)
    decimal = 0
    for i in range(length):
        if binary[i] == 1:
            decimal += pow(2, (length - 1 - i))
    return decimal

# convert decimal value to 6-bit binary
def decToBin(decimal):
    binary = numpy.empty(6, int)
    if decimal - 32 >= 0:
        binary[0] = 1
        decimal -= 32
    else:
        binary[0] = 0
    if decimal - 16 >= 0:
        binary[1] = 1
        decimal -= 16
    else:
        binary[1] = 0
    if decimal - 8 >= 0:
        binary[2] = 1
        decimal -= 8
    else:
        binary[2] = 0
    if decimal - 4 >= 0:
        binary[3] = 1
        decimal -= 4
    else:
        binary[3] = 0
    if decimal - 2 >= 0:
        binary[4] = 1
        decimal -= 2
    else:
        binary[4] = 0
    if decimal - 1 >= 0:
        binary[5] = 1
        decimal -= 1
    else:
        binary[5] = 0
    return binary