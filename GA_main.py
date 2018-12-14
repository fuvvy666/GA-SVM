import Genetic
import Fitness
import data
import matplotlib.pyplot as plt

class Chrom:
    chrom = []
    fitness = 0
    def showChrom(self):
        print(self.chrom)
    def showFitness(self):
        print(self.fitness)

# basic argument

N = 100
mut = 0.4
acr = 0.4

pop = {} # dictionary
for i in range(N):
    pop[i] = Chrom()

chromNodes = 2
iterNum = 5000
chromRange = [[1,2],[1,1000]]
aveFitnessList = []
bestFitnessList = []

matches = data.vector('matches_2.csv')   # get the game result
result_train = data.get_result(matches)
training = data.vector('matches_train_2.csv')

# training data and testing data
matches_test = data.vector('test111.csv')
result_test = data.get_result(matches_test)
testing = data.vector('test222.csv')

ran = 20
best_gamma = [0]*ran
best_c = [0]*ran
best_fitness = [0]*ran

for loop in range(ran):
    pop = Genetic.initialize(pop, chromNodes, chromRange)
    pop = Fitness.calFitness(training, result_train, testing, result_test, pop)
    bestChrom = Genetic.findBest(pop)
    bestFitnessList.append(bestChrom[1]) # now best fitness
    aveFitnessList.append(Genetic.calAveFitness(pop,N)) # ave fitness



    for t in range(iterNum):
        pop = Genetic.mutChrom(pop, mut, chromNodes, bestChrom, chromRange)
        pop = Genetic.acrChrom(pop, acr, chromNodes)
        nowBestChrom = Genetic.findBest(pop)
        bestChrom = Genetic.compareChrom(nowBestChrom, bestChrom)
        worseChrom = Genetic.findWorse(pop)
        pop[worseChrom[0]].chrom = pop[bestChrom[0]].chrom
        pop[worseChrom[0]].fitness = pop[bestChrom[0]].fitness
        bestFitnessList.append(bestChrom[1])
        aveFitnessList.append(Genetic.calAveFitness(pop,N))


    #plt.figure(1)
    #x = list(range(iterNum+1))
    #plt.plot(x, aveFitnessList)
    #plt.plot(x, bestFitnessList)
    #plt.show()


    length = len(pop)
    for i in range(length):
        if pop[i].fitness > best_fitness[loop]:
            best_fitness[loop] = pop[i].fitness
            best_gamma[loop] = pop[i].chrom[0]
            best_c[loop] = pop[i].chrom[1]


print(best_gamma)
print(best_c)
print(best_fitness)


