def generate_hilbert(n):
    matrix = []
    for i in range(n):
        row = [1.0 / (i + j + 1) for j in range(n)]
        matrix.append(row)
    return matrix


def gaussian_elimination(A, b):
    n = len(A)
    # Forward elimination
    for i in range(n - 1):
        if A[i][i] == 0:
            continue  # Basic check to avoid division by zero
        for j in range(i + 1, n):
            k_temp = - A[j][i] / A[i][i]
            for k in range(i, n):  # Only need to update from current column i onwards
                A[j][k] += k_temp * A[i][k]
            b[j] += k_temp * b[i]

    # Backward substitution
    x_sol = [0.0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        res = b[i]
        for j in range(i + 1, n):
            res -= A[i][j] * x_sol[j]
        x_sol[i] = res / A[i][i]
    return x_sol


def run_experiment(dimensions):
    for n in dimensions:
        print(f"\n--- Testing Dimension n = {n} ---")

        A = generate_hilbert(n)
        b = [sum(row) for row in A]

        try:
            solution = gaussian_elimination(A, b)

            avg_error = sum(abs(x - 1.0) for x in solution) / n

            if n <= 5:
                print(f"Solution: {[round(x, 4) for x in solution]}")
            else:
                print(
                    f"First 3 results: {[round(x, 4) for x in solution[:3]]} ...")

            print(f"Average Error: {avg_error:.2e}")

        except ZeroDivisionError:
            print("Algorithm failed: Matrix is too ill-conditioned (division by zero).")


run_experiment([5, 10, 20, 50, 100])
