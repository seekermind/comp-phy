""" This program figure out average distance D (or the average number of steps) to go to be out of the city(LxL square block) limit if you start from a random coordinate. A step is 1 meter long."""


import random
import numpy
import math

L = 100
walkchoice = [1,-1]

stepList = []
distanceList = []

for i in range(100):
    step = 0
    x0 = random.randint(0, L)
    y0 = random.randint(0,L)
    coordinate = [x0,y0]
    while(coordinate[0] > 0 and coordinate[0] < L and coordinate[1] > 0 and coordinate[1] < L):
        coordinate[random.randint(0,1)] += random.choice(walkchoice)
        step += 1
    stepList += [step]
    distanceList = [math.sqrt((coordinate[0] - x0)**2 + (coordinate[1] - y0)**2)]

stepList = numpy.array(stepList)
stepMean = numpy.mean(stepList)
distanceList = numpy.array(distanceList)
distanceMean = numpy.mean(distanceList)

print(stepMean, distanceMean)
