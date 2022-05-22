from Library import *
import matplotlib.pyplot as plt
import numpy as np
import math


def func(x,y,z):
    return -n**2*math.pi**2*y

global n
n = 1
X1, Y1 = ShootingforODE(func, 0, 1, 0, 0, 0.01)
Y1 = Normalization(Y1)
n = 2
X2, Y2 = ShootingforODE(func, 0, 1, 0, 0, 0.01)
Y2 = Normalization(Y2)

plt.plot(X1,Y1,label = 'ground state ', c = 'darkcyan')
plt.plot(X2,Y2,label='1st excited state', c = 'lawngreen')

plt.xlabel('x')
plt.ylabel('psi')
plt.legend()
plt.show()
"""
The ground state and 1st excited state is plotted
"""