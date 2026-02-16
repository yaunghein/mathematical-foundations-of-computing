import numpy as np
import matplotlib.pyplot as plt

locators = np.loadtxt('locators.csv', delimiter=',')
distances = np.loadtxt('approx_dists.csv', delimiter=',')

x1, y1 = locators[0]
d1 = distances[0]

xi = locators[1:]
di = distances[1:]

A = np.column_stack([
    2 * (xi[:, 0] - x1),
    2 * (xi[:, 1] - y1)
])

b = (xi[:, 0]**2 - x1**2 + xi[:, 1]**2 - y1**2 + d1**2 - di**2)

ATA = A.T @ A
ATb = A.T @ b

ship_coords = np.linalg.solve(ATA, ATb)

print(f"Battleship located at: {ship_coords}")

plt.figure(figsize=(8, 8))
plt.scatter(locators[:, 0], locators[:, 1], color='red')
plt.scatter(ship_coords[0], ship_coords[1], color='blue')
plt.show()
