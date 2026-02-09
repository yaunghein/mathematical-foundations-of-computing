import numpy as np
from matplotlib import pyplot as plt


def f(x):
    # return x ** 3
    return x * np.sin(3 * x)
    # return x**2 - 2


a = -3
b = 3
n = 100

x_points = np.linspace(a, b, n + 1)
y_points = f(x_points)
V = np.zeros((n+1, n+1))

for i in range(n+1):
    for j in range(n+1):
        V[i][j] = x_points[i]**j

c = np.linalg.solve(V, y_points)


def pn(x, coeffs):
    return sum(c * x**i for i, c in enumerate(coeffs))


x_fine = np.linspace(a, b, 200)
y_poly = pn(x_fine, c)
y_true = f(x_fine)

plt.figure(figsize=(10, 6))
plt.plot(x_fine, y_poly)
plt.plot(x_fine, y_true)
plt.scatter(x_points, y_points, color='red', label='Data Points $(x_k, y_k)$')
plt.show()
