from matplotlib import pyplot as plt
import numpy as np

r = 0.2


def x(t):
    # return r * t * np.cos(t)
    return 16 * np.power(np.sin(t), 3)


def y(t):
    # return r * t * np.sin(t)
    return 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3 * t) - np.cos(4 * t)


t_fine = np.linspace(0, 2 * np.pi, 400)
x_fine = x(t_fine)
y_fine = y(t_fine)

plt.figure(figsize=(8, 8))
plt.plot(x_fine, y_fine, label="Paramtric plot", color="red", linewidth="4")
plt.show()
