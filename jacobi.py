import random
import math


def generate_ddm(n, min_val=-10, max_val=10):
    matrix = []
    for i in range(n):
        row = [random.randint(min_val, max_val) for _ in range(n)]
        off_diag_sum = sum(abs(row[j]) for j in range(n) if i != j)
        row[i] = off_diag_sum + random.randint(1, 5)
        matrix.append(row)
    return matrix


def jacobi(A, b, eps=1e-6, max_iterations=100):
    n = len(A)
    x_prev = [0.0] * n

    for k in range(max_iterations):
        x_curr = [0.0] * n

        for i in range(n):
            sigma = sum(A[i][j] * x_prev[j] for j in range(n) if i != j)
            x_curr[i] = (b[i] - sigma) / A[i][i]

        distance = math.sqrt(sum((x_curr[i] - x_prev[i])**2 for i in range(n)))

        print(f"Iteration {k + 1}: Distance = {distance:.8f}: x = {x_curr}")

        if distance < eps:
            return x_curr

        x_prev = x_curr

    return x_prev


if __name__ == "__main__":
    n = 5
    A = generate_ddm(n)
    b = [random.randint(-10, 10) for _ in range(n)]

    print(f"A: {A}")
    print(f"b: {b}\n")

    # solution = jacobi([[2, 1], [1, -3]], [3, -2], eps=1e-10)
    solution = jacobi(A, b, eps=1e-10)
    print(f"Final Solution: {solution}")
