import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
z = []

for theta in range(360):
    for phi in range(180):
        x.append(np.sin(theta)*np.cos(phi))
        y.append(np.sin(theta)*np.sin(phi))
        z.append(np.cos(theta))

ax = plt.axes(projection ='3d')
ax.plot3D(x, y, z, 'green')
plt.show()
