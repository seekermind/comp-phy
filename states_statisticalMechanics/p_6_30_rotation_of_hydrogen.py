import numpy as np
import astropy.constants as c
import astropy.units as u


def b_factor(E, T):
    return np.exp(-E/(c.k_B.to(u.eV/u.K).value * T))

T = 50
e = 0.0076
E_s = [i*(i+1)*e for i in range(0,100,2)]
Z = 0
for i in E_s:
    Z += b_factor(i,T)

E_average = 0
for i in E_s:
    E_average += i*b_factor(i,T)
