import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import comb
# Make sure scipy is installed, or use the custom comb function provided earlier

# Define the control points grid
P = np.array([[[0, 0, 0], [0, 1, 1], [0, 2, 0], [0, 3, 1]],
              [[1, 0, 1], [1, 1, 2], [1, 2, 2], [1, 3, 0]],
              [[2, 0, 0], [2, 1, 1], [2, 2, 1], [2, 3, 0]],
              [[3, 0, 1], [3, 1, 0], [3, 2, 0], [3, 3, 1]]])

# Bezier surface functions
def bernstein_poly(i, n, t):
    return comb(n, i) * (t ** (n - i)) * (1 - t) ** i

def bezier_surface(P, resolution=100):
    u = np.linspace(0, 1, resolution)
    v = np.linspace(0, 1, resolution)
    surface = np.zeros((resolution, resolution, 3))
    n = len(P) - 1
    m = len(P[0]) - 1

    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(resolution):
                for l in range(resolution):
                    b_ijk = bernstein_poly(i, n, u[k]) * bernstein_poly(j, m, v[l])
                    surface[k, l] += b_ijk * P[i][j]

    return surface

# Generate the Bezier surface
bezier_surf = bezier_surface(P)

# Plot the Bezier surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = bezier_surf[:, :, 0]
Y = bezier_surf[:, :, 1]
Z = bezier_surf[:, :, 2]
ax.plot_surface(X, Y, Z, color='b', alpha=0.6)  # Semi-transparent surface

# Plot the control points
for row in P:
    for point in row:
        ax.scatter(*point, color='r')

# Draw lines connecting control points in the u-direction and v-direction
for i in range(P.shape[0]):
    ax.plot(*zip(*P[i, :, :]), color='k')

for i in range(P.shape[1]):
    ax.plot(*zip(*P[:, i, :]), color='k')

# Set the labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Bezier Surface')

plt.show()
