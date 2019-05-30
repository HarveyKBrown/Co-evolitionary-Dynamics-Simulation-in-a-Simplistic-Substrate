import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import random
from random import randint
import operator

generations = 600 #600
populationSize = 25 #25

class Substrate:
    x = []
    mutationRate = 0.005
    def __init__(self, initialx):
        self.x = []
        for i in range(0, 10):
            self.x.append(initialx)
    def copy(self, array):
            self.x = array[:]
    def mutate(self):
        n = Substrate(0)
        n.copy(self.x)
        for i in range(0, 10):
            for j in range(0, 10):
                if (np.random.rand() < self.mutationRate):
                    n.x[j] = (n.x[j] + 1) if (i >= n.x[j]) else (n.x[j] - 1)
        return n
    def print(self):
        print (self.x)
        print (self.y)
    def getTotal(self):
        return sum(x)
    def score1(self, enemyPopulation, S):
        # Player is scored against S number of individuals from enemy population
        enemySelection = random.sample(enemyPopulation, S)
        topIndex = 0
        wins = 0
        topDifference = 0
        for i in range(0, S):
            for j in range(0, 10):
                difference = abs(self.x[j] - enemySelection[i].x[j])
                if (difference > topDifference):
                    topDifference = difference
                    topIndex = j
            if (self.x[topIndex] > enemySelection[i].x[topIndex]):
                wins += 1
        return wins/S

subjFitness = [0, 0]
species = True
def fitnessProportionalSelection(population, enemies):
    S = 10
    global subjFitness
    global species
    species = not species
    populationScore = []
    population2 = []
    # Calculate scores
    for k in range(0, populationSize):
        populationScore.append(population[k].score1(enemies, S))
    populationScoreTotal = sum(populationScore)
    subjFitness[species] = populationScoreTotal/populationSize
    populationScoreAcc = cum_prob=np.cumsum(populationScore)
    # Select new generation
    if (populationScoreTotal == 0):
        for k in range(0, populationSize):
            rand = randint(0, populationSize - 1)
            population2.append(population[rand].mutate())
    else:
        for k in range(0, populationSize):
            rand = random.random() * populationScoreTotal
            for l in range(0, populationSize):
                if (populationScoreAcc[l] >= rand):
                    population2.append(population[l].mutate())
                    break
    return population2



"[[data1[x],[y]],[data2[x],[y]]]"
data = [[[],[]],[[],[]]]
data2 = [[[],[]],[[],[]]]
pop =   [[Substrate(0) for i in range(0, populationSize)],
        [Substrate(0) for i in range(0, populationSize)]]
for i in range(0, generations):
    # Mutate and select new populations
    for j in range(0, 2):
        children = []
        # Construct new generation using fitness proportional selection
        pop[j] = fitnessProportionalSelection(pop[j], pop[operator.mod(j+1, 2)])
    # Add data to graph
    for j in range(0, 2):
        for k in range(0, populationSize):
            data[j][0].append(i)
            data[j][1].append(sum(pop[j][k].x))
            #print(pop[j][k].x)
        data2[j][0].append(i)
        data2[j][1].append(subjFitness[j])


# set style of graph
fig = plt.figure()
gs = gridspec.GridSpec(3, 1, height_ratios=[12, 1, 1], wspace=1, hspace=.2)
ax0 = fig.add_subplot(gs[0])
ax0.axhline(y=50, color='black', linewidth=.5)
ax0.axis([1,generations, 0,100])
ax0.spines['right'].set_visible(False)
ax0.get_xaxis().set_visible(False)
ax0.set_ylabel("objective fitness")
ax0.set_yticks(np.arange(0, 101, 50))
ax1 = fig.add_subplot(gs[1])
ax1.axis([1,generations, 0,1])
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax2 = fig.add_subplot(gs[2])
ax2.axis([1,generations, 0,1])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.set_ylabel("subjv\nfit. for\neach\npopn.", rotation="horizontal", labelpad=20)
ax2.set_xlabel("Generation")
ax2.set_xticks(np.arange(0, generations+1, 200))
# give data to graphs
ax0.scatter(data[0][0], data[0][1], s=.5, c='#B00000', marker=".", alpha=1)
ax0.scatter(data[1][0], data[1][1], s=.5, c='#303030', marker=".", alpha=1)
ax1.scatter(data2[0][0], data2[0][1], s=.5, c='#B00000', marker=".", alpha=1)
ax2.scatter(data2[1][0], data2[1][1], s=.5, c='#303030', marker=".", alpha=1)
plt.show()