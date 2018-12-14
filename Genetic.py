import random

def findBest(pop): # find the best chrom
    best = ['1', 0.0000001]
    for i in pop:
        if best[1] < pop[i].fitness:
            best = [i, pop[i].fitness]
    return best

def findWorse(pop): # find the worst chrom
    worse = ['1', 999999]
    for i in pop:
        if worse[1] > pop[i].fitness:
            worse = [i, pop[i].fitness]
    return worse

def initialize(pop, chromNodes, chromRange):  # Initial
    for i in pop:
        chromList = []
        for j in range(chromNodes):
            chromList.append(random.uniform(chromRange[j][0], chromRange[j][1]+1))
        pop[i].chrom = chromList
    return pop

def calAveFitness(pop,N):
    sumFitness = 0
    for i in pop:
        sumFitness = sumFitness + pop[i].fitness
    aveFitness = sumFitness / N
    return aveFitness

def mutChrom(pop,mut,chromNodes,bestChrom,chromRange):
    for i in pop:
        if mut > random.random():

            mutNode = random.randrange(0,chromNodes)
            mutRange = random.random()*(1-pop[i].fitness/bestChrom[1])**2
            pop[i].chrom[mutNode] = pop[i].chrom[mutNode]*(1+mutRange)

            pop[i].chrom[mutNode] = inRange(pop[i].chrom[mutNode], chromRange[mutNode])
    return pop

def inRange(mutNode, chromRange):
    if chromRange[0] < mutNode < chromRange[1]:
        return mutNode
    else:
        return chromRange[0]

def acrChrom(pop, acr, chromNodes):
    for i in pop:
        for j in pop:
            if acr > random.random():
                acrNode = random.randrange(0, chromNodes)
                #exchange two nodes
                pop[i].chrom[acrNode], pop[j].chrom[acrNode] = pop[j].chrom[acrNode], pop[i].chrom[acrNode]
    return pop

def compareChrom(nowbestChorm, bestChrom):
    if bestChrom[1] > nowbestChorm[1]:
        return bestChrom
    else:
        return nowbestChorm


