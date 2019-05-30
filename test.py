import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import random
from random import randint
import operator

generations = 10 #600
populationSize = 1 #25

class Substrate:
    x = []
    mutationRate = 0.005
    def __init__(self, initialx):
        self.x = []
        for i in range(0, 10):
            self.x.append(initialx)
        #print("this one")
        #print(self.x)
    def copy(self, array):
            self.x = array[:]
            #print(array[:])
    def mutate(self):
        n = Substrate(0)
        print(self.x)
        n.copy(self.x)
        for i in range(0, 10):
            for j in range(0, 10):
                if (np.random.rand() < self.mutationRate):
                    n.x[j] = (n.x[j] + 1) if (i >= n.x[j]) else (n.x[j] - 1)
                #if (n.x[j] == -1):
                #    print(self.x[j])
        #print(n.x)
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
    
s = Substrate(10)
s = s.mutate()
print(s.x)

