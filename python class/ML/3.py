import numpy as np
import matplotlib.pyplot as plt
soa = np.array([[0,0,1,0], [0,0,1,1], [0,0,0,1], [0,0,-1,1]])
X, Y, U, V = zip(*soa)
plt.figure()
ax = plt.gca()
ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
ax.set_xlim([-2,2])
ax.set_ylim([-1,2])
plt.text(1.0, 0.1, r'$\vec a$', fontsize=24, color='red', fontweight='bold')
plt.text(1.1, 1.1, r'$\vec b$', fontsize=24, color='blue', fontweight='bold')
plt.text(0.0, 1.1, r'$\vec c$', fontsize=24, color='green', fontweight='bold')
plt.text(-1.1, 1.1, r'$\vec d$', fontsize=24, color='yellow', fontweight='bold')
plt.draw()
plt.show()