import matplotlib.pyplot as plt 
import numpy as np
import math

nA = int(input("nA: "))
nB = int(input("nB: "))
q = int(input("q: "))

x = np.arange(q+1)
def ncr(n, r):
    result = 1
    for i in range(r):
        result *= n
        n -= 1
    return result//math.factorial(r)

omegaA = []
omegaB = []
for i in range(0,21):
    omegaA += [ncr(nA+i-1, i)]
    omegaB += [ncr(nB+q-i-1, q-i)]

omega = [float(i*j) for i,j in zip(omegaA, omegaB)]

print(omegaA, omegaB, omega)

# plt.plot(x,omega)
# plt.show()
