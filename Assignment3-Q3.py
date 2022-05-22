from Library import *
import numpy as np
import matplotlib.pyplot as plt


def LaplaceEqn (Phi):
    diff = 1
    while diff > 1e-6:
        Phi2 = Phi.copy()
        Phi[1:-1, 1:-1] = (Phi2[1:-1, :-2] + Phi2[1:-1, 2:] + Phi2[:-2, 1:-1] + Phi2[2:, 1:-1])/4
        diff = np.sqrt(np.sum(Phi- Phi2)**2)/np.sum(Phi2**2)
    return Phi

x = np.linspace(0,1,20)
y = np.linspace(0,1,20)

# potential
Pot = np.zeros((20, 20))

Pot[:, 0] = 1
Pot[:, 1] = 0
Pot[0, :] = 0
Pot[1, :] = 0

value = LaplaceEqn(Pot)
print("The Solution set is Printed: ",value)

from matplotlib import cm
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={"projection": "3d"})
X, Y = np.meshgrid(x, y)
surf = ax.plot_surface(X, Y, Pot, cmap=cm.hot)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('X- value')
ax.set_ylabel('Y-value')
ax.set_zlabel('Potential(V)')
plt.show()
"""
The Solution set is Printed and image is shown:
"""