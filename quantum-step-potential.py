from astropy import units as u
from astropy import constants as c
from math import *

m = c.m_e
E = 10 * u.eV
V = 20 * u.eV
h = c.hbar

k1 = sqrt(2*m*E/h**2) 

print(k1)
