""" A rod with constant temperature and both end at 0 degree celcius help: https://ocw.mit.edu/courses/mathematics/18-303-linear-partial-differential-equations-fall-2006/lecture-notes/heateqni.pdf"""

import matplotlib.pyplot as plt 
import numpy as np
# from derivative import f1
# from cubicSplines import cubicInterpolationmatrix

def T(x, t, n, t0):
    result = 0
    for i in range(1, n+1):
        result += ((np.sin(((2*i)-1)*np.pi*x))/((2*i)-1))*(np.exp(-((2*i)-1)**2*np.pi**2*t))
    return result*((4*t0)/np.pi)

temp0 = 500     #initial temperature of the rod
""" l = 1           #length of the rod
kt = 80         #thermal conductivity
c = 450         #specific heat of the rod
p = 7300        #density of the rod

time0 = (l**2*c*p)/kt """

t = np.arange(0,1,0.01)

x = np.arange(0,1+0.01,0.01)
plt.plot(x, T(x, 0.01, 100, temp0))
# umax = [np.amax(T(x, 0, 100, temp0))]
# for i in t[1:]:
    # u = np.array(T(x, i, 30, temp0))
    # umax += [max(u)]
    # plt.plot(x,u)
# plt.plot([0.5 for i in range(len(umax))], umax, 'bo')
#plt.plot(t, umax, 'bo')
#S = cubicInterpolationmatrix(t, umax)
#plt.plot(t, [f1(i, 0.01, S, t, umax) for i in t], 'r--')
plt.show()
