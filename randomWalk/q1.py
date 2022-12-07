import random as rn
import math as mt
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

K = 1000

list = ['s','n','e','w']

step = np.arange(1000,100000,1000)
distance = []

for i in step:
    x = 0
    y = 0
    for j in range(i):
        a = rn.choice(list)
        if (a == 's'):
            x -= 1
        elif (a == 'n'):
            x += 1
        elif (a == 'e'):
            y -= 1
        else:
            y += 1

    distance += [mt.sqrt(x**2 + y **2)]

distance = np.array(distance)
slop,intercept,rvalue,nvalue,stdErr = stats.linregress(step, distance)
plt.plot(step,distance,'ro',step, slop*step + intercept, 'g-')
plt.show()
#distance = np.array(distance)
#print(np.mean(distance))
