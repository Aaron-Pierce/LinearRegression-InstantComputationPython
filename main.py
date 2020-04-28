from builtins import print
import numpy as np
import csv
import matplotlib.pyplot as plt
from sympy import *
from sympy.abc import i

weights = []
heights = []
with open("Fish.csv", newline="") as dataset:
    datareader = csv.reader(dataset, delimiter=' ', quotechar='|')
    firstline = True
    for row in datareader:
        if firstline:
            firstline = False
            continue
        split = row[0].split(",")
        species = split[0]
        if species != "Bream":
            continue
        weight = split[1]
        height = split[5]
        weights.append(float(weight))
        heights.append(float(height))

thetas = np.zeros((2, 1))

X = np.array(heights)
Y = np.array(weights)

print(X.shape)
print(Y)


def h(x):
    return thetas[0] + x*thetas[1]


def cost():
    return 0.5 * Sum(thetas[0] + thetas[1]*X[i], (i, 0, len(X) - 1))


def graph():
    plt.cla()
    plt.scatter(heights, weights)
    plt.plot((0, max(heights)), (thetas[0], h(max(heights))))


sumY = 0
sumX = 0
sumXY = 0
sumX2 = 0

for i in range(0, len(X)):
    sumY += Y[i]
    sumXY += X[i]*Y[i]
    sumX += X[i]
    sumX2 += (X[i] ** 2)

print(sumY, sumXY, sumX, "sums")

b = np.array([sumY, sumXY])

print("b", b)

aTwiddle = np.array([
    [len(X), sumX],
    [sumX, sumX2]
])

print("pinv")
print(np.linalg.inv(aTwiddle))

thetavec = np.linalg.pinv(aTwiddle).dot(b)

print("Atwiddle")
print(aTwiddle)
print(thetavec)

thetas[0] = thetavec[0]
thetas[1] = thetavec[1]

fig = plt.figure()
plt.xlabel("Bream height")
plt.ylabel("Bream weight")
graph()

plt.xlim([10, 20])
plt.ylim([0, 1250])
plt.show()
