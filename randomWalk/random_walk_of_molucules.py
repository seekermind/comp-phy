import random as rn
import numpy as np

x = 0
T = 298
r = 232*10**(-12)
P = 1.0125*10**5
v = np.sqrt(3*8.3*T/0.029)
l = (1.38*10**(-23)*T)/(4*np.pi*r**2*P)
step = v/(1000*l)

for i in range(int(step)):
    x += rn.choice([-1,1])

print(x*l)
