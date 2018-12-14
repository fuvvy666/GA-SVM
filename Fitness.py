import SVM


def calFitness(train, train_result, test, test_result, pop):
    for i in pop:

        pop[i].fitness = funcFitness(train, train_result, test, test_result, pop[i].chrom)

    return pop

def funcFitness(train, train_result, test, test_result, chrom):
    fitness = SVM.class_svm(train, train_result, test, test_result, chrom[0],chrom[1])
    return fitness