def f(x):
    return x**4 + (3 * x**3) + x**2 - (2 * x) - 0.5


def bisection(a, b, eps, max_iteration=100):
    # print(f"\nBetween {a} and {b}")

    iteration = 0
    while (b - a) / 2 > eps and iteration < max_iteration:
        mid = (a + b) / 2
        fx = f(mid)
        # print(f"iteration: {iteration}, x: {mid}, f(x): {fx}")
        if fx == 0:
            break
        if f(a) * fx < 0:
            b = mid
        else:
            a = mid
        iteration += 1

    return (a + b) / 2


def find_multi_roots(a, b, eps, split_count=10):
    step = (b - a) / (split_count - 1)
    values = [a + (i * step) for i in range(split_count)]

    for i in range(len(values) - 1):
        x1 = values[i]
        x2 = values[i+1]

        root = bisection(x1, x2, eps)
        if root is not None:
            print(f"Root between {x1} and {x2}: {root}")


find_multi_roots(-3, 2, 0.0001, 5)
