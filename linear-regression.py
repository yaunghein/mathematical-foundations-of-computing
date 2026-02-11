import numpy as np
import matplotlib.pyplot as plt


def test_func(x):
    return 2 * x + 1


n = 50
x = np.random.uniform(0, 10, n)
noise = np.random.uniform(-2.5, 2.5, n)
# y = test_func(x)
y = test_func(x) + noise


A = np.array([
    [np.sum(x**2), np.sum(x)],
    [np.sum(x),    n]
])
B = np.array([np.sum(x * y), np.sum(y)])

m, b = np.linalg.solve(A, B)


plt.scatter(x, y)
plt.plot(x, test_func(x), 'g')
plt.plot(x, m * x + b, 'r')
plt.show()
