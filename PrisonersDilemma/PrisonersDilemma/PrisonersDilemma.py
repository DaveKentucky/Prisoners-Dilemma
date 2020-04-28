import random
import numpy
from deap import creator, base, tools, algorithms
import Generator, Game, Calculations, Fitness

generator = Generator.Generator()
population = generator.generatePopulation(20)

tournamentLength = 10
tournamentScores = Game.playTournament(population, tournamentLength);

print(tournamentScores)

maxPoints = 5 * (len(population) - 1) * tournamentLength
Fitness.evaluatePopulation(population, tournamentScores, maxPoints)

for ind in population:
    print(ind.fitness)
