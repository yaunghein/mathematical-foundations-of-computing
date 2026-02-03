def f(x):
    return x ** 2 - 2


def f_prime(x):
    return 2 * x


def complare_algos(a, b, x0, alpha, eps):
    print("\nBisection Algo:")

    step = 0
    while (b - a) / 2 > eps:
        mid = (a + b) / 2
        fx = f(mid)
        print(f"iteration: {step}, x: {mid}, f(x): {fx}")
        if fx == 0:
            break
        if f(a) * fx < 0:
            b = mid
        else:
            a = mid
        step += 1

    print("\nNewton Algo:")

    curr_x = x0
    step = 0
    while True:
        fx = f(curr_x)
        print(f"iteration: {step}, x: {curr_x}, f(x): {fx}")
        df = f_prime(curr_x)
        if df == 0:
            break
        next_x = curr_x - fx / df
        if abs(next_x - curr_x) < eps:
            break
        curr_x = next_x
        step += 1

    print("\nRelaxation Algo:")

    curr_x = x0
    step = 0
    while True:
        fx = f(curr_x)
        print(f"iteration: {step}, x: {curr_x}, f(x): {fx}")
        next_x = curr_x + alpha * fx
        if abs(next_x - curr_x) < eps or step > 100:
            break
        curr_x = next_x
        step += 1


if __name__ == "__main__":
    complare_algos(1, 3, 1.5, -0.2, 1e-6)
