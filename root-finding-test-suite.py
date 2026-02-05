import matplotlib.pyplot as plt


def f(x):
    # return x**2 - 4
    return (x-1)**3


def df(x):
    # return 2 * x
    return 2 * (x**2)


A, B = 0, 5
X0 = 4
ALPHA = -0.1
EPS = 1e-7
MAX_ITER = 40


def run_bisection(a, b, eps, max_iter):
    errors = []
    print("\nBisection Errors:")
    for i in range(max_iter):
        error = abs(b - a)
        errors.append(error)
        print(f"Iteration {i}: {error}")
        if error < eps:
            break
        mid = (a + b) / 2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return errors


def run_newton(x0, eps, max_iter):
    errors = []
    curr_x = x0
    print("\nNewton Errors:")
    for i in range(max_iter):
        f_val = f(curr_x)
        df_val = df(curr_x)
        if df_val == 0:
            break
        next_x = curr_x - f_val / df_val
        error = abs(next_x - curr_x)
        errors.append(error)
        print(f"Iteration {i}: {error}")
        if error < eps:
            break
        curr_x = next_x
    return errors


def run_relaxation(x0, alpha, eps, max_iter):
    errors = []
    curr_x = x0
    print("\nRelaxation Errors:")
    for i in range(max_iter):
        next_x = curr_x + alpha * f(curr_x)
        error = abs(next_x - curr_x)
        errors.append(error)
        print(f"Iteration {i}: {error}")
        if error < eps:
            break
        curr_x = next_x
    return errors


err_bisect = run_bisection(A, B, EPS, MAX_ITER)
err_newton = run_newton(X0, EPS, MAX_ITER)
err_relax = run_relaxation(X0, ALPHA, EPS, MAX_ITER)

plt.figure(figsize=(10, 6))
plt.plot(err_bisect, label='Bisection', color='blue', linestyle='--')
plt.plot(err_newton, label='Newton', color='black', linewidth=2)
plt.plot(err_relax, label='Relaxation', color='yellowgreen', linewidth=2)

plt.yscale('log')
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.title('Root Finding Convergence')
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.show()
