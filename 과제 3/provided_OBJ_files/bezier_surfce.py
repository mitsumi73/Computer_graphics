import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ctrlpoints = np.array([
    [[0.0, 0.0, 0.0], [2.0, 0.0, 0.0], [4.0, 0.0, 0.0], [6.0, 0.0, 0.0]],
    [[0.0, 0.0, -2.0], [2.0, 0.0, -2.0], [4.0, 0.0, -2.0], [6.0, 0.0, -2.0]],
    [[0.0, 0.0, -4.0], [2.0, 0.0, -4.0], [4.0, 0.0, -4.0], [6.0, 0.0, -4.0]],
    [[0.0, 0.0, -6.0], [2.0, 0.0, -6.0], [4.0, 0.0, -6.0], [6.0, 0.0, -6.0]]
])

# Vẽ trục tọa độ
ax.quiver(0, 0, 0, 6.5, 0, 0, color='r')
ax.quiver(0, 0, 0, 0, 4, 0, color='g')
ax.quiver(0, 0, 0, 0, 0, -8, color='b')

# Vẽ mặt phẳng
X, Y = np.meshgrid(range(7), range(7))
Z = -6 * np.ones((7, 7))
ax.plot_wireframe(X, Y, Z, color='k')

# Vẽ các điểm điều khiển
ax.scatter(ctrlpoints[:, :, 0].flatten(),
           ctrlpoints[:, :, 1].flatten(),
           ctrlpoints[:, :, 2].flatten(), s=50, color='r')

# Vẽ đường nối điểm điều khiển
for i in range(4):
    ax.plot(ctrlpoints[i, :, 0],
            ctrlpoints[i, :, 1],
            ctrlpoints[i, :, 2], color='k')

for j in range(4):
    ax.plot(ctrlpoints[:, j, 0],
            ctrlpoints[:, j, 1],
            ctrlpoints[:, j, 2], color='k')

# Cài đặt góc nhìn
ax.view_init(elev=30, azim=-140)

# Hiển thị đồ thị
plt.show()