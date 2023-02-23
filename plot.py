import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

# Define function
def fun(x0, x1, x2, x3, x4):
    return np.power(x0, 2) + np.power(x1, 2) + np.power(x2, 2) + np.power(x3, 2) + np.power(x4, 2)

# Create 5D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data
X0 = np.arange(-3, 3, 0.25)
X1 = np.arange(-3, 3, 0.25)
X2 = np.arange(-3, 3, 0.25)
X3 = np.arange(-3, 3, 0.25)
X4 = np.arange(-3, 3, 0.25)
X0, X1, X2, X3, X4 = np.meshgrid(X0, X1, X2, X3, X4)
Z = fun(X0, X1, X2, X3, X4)

# Plot surface and color
ax.scatter(X0, X1, X2, c=Z, cmap=plt.cm.winter)
ax.set_xlabel('X0', color='r')
ax.set_ylabel('X1', color='g')
ax.set_zlabel('X2')

plt.show()