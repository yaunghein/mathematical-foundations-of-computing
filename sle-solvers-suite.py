import random
import math
import csv
import matplotlib.pyplot as plt


def gaussian_elimination(A_in, b_in):
    n = len(A_in)
    A = [row[:] for row in A_in]
    b = b_in[:]
    for i in range(n):
        max_el = abs(A[i][i])
        pivot_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                pivot_row = k
        A[i], A[pivot_row] = A[pivot_row], A[i]
        b[i], b[pivot_row] = b[pivot_row], b[i]
        for j in range(i + 1, n):
            if A[i][i] == 0:
                continue
            factor = -A[j][i] / A[i][i]
            for k in range(i, n):
                if i == k:
                    A[j][k] = 0
                else:
                    A[j][k] += factor * A[i][k]
            b[j] += factor * b[i]
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= A[k][i] * x[i]
    return x


def jacobi(A, b, eps=1e-10, max_iter=100):
    n = len(A)
    x_prev = [0.0] * n
    for k in range(max_iter):
        x_curr = [0.0] * n
        for i in range(n):
            sigma = sum(A[i][j] * x_prev[j] for j in range(n) if i != j)
            x_curr[i] = (b[i] - sigma) / A[i][i]
        dist = math.sqrt(sum((x_curr[i] - x_prev[i])**2 for i in range(n)))
        if dist < eps:
            return x_curr, k + 1
        x_prev = x_curr[:]
    return x_prev, max_iter


def gauss_seidel(A, b, eps=1e-10, max_iter=100):
    n = len(A)
    x = [0.0] * n
    for k in range(max_iter):
        x_old = x[:]
        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - sigma) / A[i][i]
        dist = math.sqrt(sum((x[i] - x_old[i])**2 for i in range(n)))
        if dist < eps:
            return x, k + 1
    return x, max_iter


def gen_matrix(n, type='random'):
    if type == 'hilbert':
        return [[1.0 / (i + j + 1) for j in range(n)] for i in range(n)]
    matrix = [[random.uniform(-5, 5) for _ in range(n)] for _ in range(n)]
    if type == 'ddm':
        for i in range(n):
            row_sum = sum(abs(matrix[i][j]) for j in range(n) if i != j)
            matrix[i][i] = row_sum + random.uniform(1, 5)
    return matrix


def calculate_errors(A, x, b, x_test):
    res_vec = []
    for i in range(len(A)):
        ax_val = sum(A[i][j] * x[j] for j in range(len(x)))
        res_vec.append(ax_val - b[i])
    residue = math.sqrt(sum(v**2 for v in res_vec))
    distance = math.sqrt(sum((x[i] - x_test[i])**2 for i in range(len(x))))
    return residue, distance


all_results = []
dimensions = range(3, 51)

for n in dimensions:
    x_test = [1.0] * n

    A_rnd = gen_matrix(n, 'random')
    b_rnd = [sum(A_rnd[i][j] * x_test[j] for j in range(n)) for i in range(n)]
    sol = gaussian_elimination(A_rnd, b_rnd)
    r, d = calculate_errors(A_rnd, sol, b_rnd, x_test)
    all_results.append(["Random", n, "Gauss", r, d, "-"])

    A_hil = gen_matrix(n, 'hilbert')
    b_hil = [sum(A_hil[i][j] * x_test[j] for j in range(n)) for i in range(n)]
    for name, algo in [("Gauss", gaussian_elimination), ("Seidel", gauss_seidel)]:
        res = algo(A_hil, b_hil)
        sol, iters = res if isinstance(res, tuple) else (res, "-")
        r, d = calculate_errors(A_hil, sol, b_hil, x_test)
        all_results.append(["Hilbert", n, name, r, d, iters])

    A_ddm = gen_matrix(n, 'ddm')
    b_ddm = [sum(A_ddm[i][j] * x_test[j] for j in range(n)) for i in range(n)]
    for name, algo in [("Gauss", gaussian_elimination), ("Jacobi", jacobi), ("Seidel", gauss_seidel)]:
        res = algo(A_ddm, b_ddm)
        sol, iters = res if isinstance(res, tuple) else (res, "-")
        r, d = calculate_errors(A_ddm, sol, b_ddm, x_test)
        all_results.append(["DDM", n, name, r, d, iters])


with open('experiment_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["MatrixType", "N", "Algorithm",
                    "Residue", "Distance", "Iters"])
    writer.writerows(all_results)


def plot_exp(exp_name, metric_idx, ylabel):
    plt.figure(figsize=(8, 4))
    data = [row for row in all_results if row[0] == exp_name]
    algos = list(set(row[2] for row in data))
    for a in algos:
        sub = [row for row in data if row[2] == a]
        plt.plot([r[1] for r in sub], [r[metric_idx] for r in sub], label=a)
    plt.yscale('log')
    plt.title(f"{exp_name} Matrix: {ylabel}")
    plt.xlabel("N Size")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


plot_exp("Random", 4, "Distance Error")
plot_exp("Hilbert", 4, "Distance Error")
plot_exp("DDM", 4, "Distance Error")
