import numpy as np
import scipy.constants as c
import matplotlib.pyplot as plt

temp = np.arange(0, 1000,1)
def speed(T, f, M):
    return [np.sqrt((((f+2)/f)*c.R*i)/(M/1000)) for i in T]

fig, ax = plt.subplots(1, 3)
ax[0].plot(temp, speed(temp, 5, 28.96), label='air')
ax[0].plot(temp, speed(temp, 5, 32), label='oxigen')
ax[0].plot(temp, speed(temp, 5, 28), label='nitrogen')
ax[0].plot(temp, speed(temp, 3, 4), label='helium')
ax[0].set_title("Speed of sound with temperature")
ax[0].legend(loc="upper left")
ax[0].margins(0.1)

ax[1].plot(temp, speed(temp, 1, 28.96), label='air')
ax[1].plot(temp, speed(temp, 1, 32), label='oxigen')
ax[1].plot(temp, speed(temp, 1, 28), label='nitrogen')
ax[1].plot(temp, speed(temp, 1, 4), label='helium')
ax[1].set_title("molecular speed with temperature")
ax[1].legend(loc="upper left")

ax[2].plot(speed(temp, 1, 28), speed(temp, 5, 28), label='nitrogen')
ax[2].plot(speed(temp, 1, 28.96), speed(temp, 5, 28.96), label='air')
ax[2].plot(speed(temp, 1, 4), speed(temp, 3, 4), label='helium')
ax[2].plot(speed(temp, 1, 32), speed(temp, 5, 32), label='oxigen')
ax[2].set_title("speed of sound vs molecular speed")
ax[2].legend(loc="upper left")


""" ax[0, 0].xlabel("temperater (K)")
ax[0, 0].ylabel("speed of sound (m/s)") """
plt.show()
