import matplotlib.pyplot as plt
import math as m

N = 50
Q = 99
def omega(N, q):
    list = []
    for i in range(q+1):
        list += [m.factorial(N+i-1)/(m.factorial(N-1)*m.factorial(i))]
    return list

mul = omega(N, Q)
q = list(range(Q+1))
s = [m.log(i) for i in mul]
def d(q, s):
    list = [0]
    for i in range(1, len(q)-2):
        list += [(q[i+1]-q[i-1])/(s[i+1]-s[i-1])]
    list += [(q[-1]-q[-2])/(s[-1]-s[-2])]
    return list

t = d(q, s)
c = d([i/N for i in q], t)

# print(s)
f, x = plt.subplots(2)
x[0].plot(q,s)
x[1].plot(t[1:-2], c[1:-2])
plt.show()
