import numpy as np
import matplotlib.pyplot as plt

basic_functions = [
    lambda x: x,
    lambda x: x**2,
    lambda x: np.sin(x),
    lambda x: np.cos(x),
    lambda x: np.exp(x) / 100
]


def secret_func(x, c, phi):
    return (c[0]*phi[0](x) + c[1]*phi[1](x) + c[2]*phi[2](x) + c[3]*phi[3](x) + c[4]*phi[4](x))


data = np.loadtxt('func_guess_data.csv', delimiter=',', skiprows=1)
x_data = data[:, 0]
y_data = data[:, 1]

A = np.column_stack([phi(x_data) for phi in basic_functions])

ATA = A.T @ A
ATy = A.T @ y_data

c_exact = np.linalg.solve(ATA, ATy)

c_guess = np.round(c_exact)

print(f"c_exact: {c_exact}")
print(f"c_guess: {c_guess}")

x_range = np.linspace(1, 10, 100)
y_fit = secret_func(x_range, c_guess, basic_functions)

plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color='orange')
plt.plot(x_range, y_fit, color='navy')
plt.show()
