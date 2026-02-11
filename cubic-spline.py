import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2])
y = np.array([1, 2, 0])
h = 1

m0 = 0
m2 = 0
m1 = (6 * ((y[2]-y[1])/h - (y[1]-y[0])/h)) / 4
m = [m0, m1, m2]


def S(x_val, i):
    t1 = (m[i] * (x[i+1] - x_val)**3) / (6 * h)
    t2 = (m[i+1] * (x_val - x[i])**3) / (6 * h)
    t3 = (y[i] - (m[i] * h**2) / 6) * ((x[i+1] - x_val) / h)
    t4 = (y[i+1] - (m[i+1] * h**2) / 6) * ((x_val - x[i]) / h)
    return t1 + t2 + t3 + t4


x_vals_seg0 = np.linspace(0, 1, 50)
x_vals_seg1 = np.linspace(1, 2, 50)

plt.plot(x_vals_seg0, S(x_vals_seg0, 0), 'b', label="S0(x)")
plt.plot(x_vals_seg1, S(x_vals_seg1, 1), 'g', label="S1(x)")
plt.scatter(x, y, color='red', zorder=5)
plt.legend()
plt.show()
