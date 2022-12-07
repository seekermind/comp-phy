import matplotlib.pyplot as plt
import numpy as np

### nice one
a = 4
b = 3

# a = 1
# b = 1
A = 1
B = 1
t = np.arange(0,10000, 0.1)
x = A * np.sin(np.radians(a * t) + 0)
y = B * np.sin(np.radians(b * t))


plt.plot(x, y)
plt.show()
