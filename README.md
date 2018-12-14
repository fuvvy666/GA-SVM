# GA-SVM
data in English Premier League
Goal: find best gamma and C in SVM for EPL data to improve the accuracy of prediction.

GA-main.py:
main code, initial the value. Set the structure of chromosome. Initial the range of gamma and C.
Setting the training set and testing set.

Fitness.py:
calculate the fitness(accuracy of svm)

Genetic.py
def findBest()
def findWorse()
def initialize()
def calAveFitness()
def mutChrom()
def inRange()
def acrChrom()
def compareChrom()

SVM.PY
calculate the accuracy of SVM

data.py
convert .csv to list


