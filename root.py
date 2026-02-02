def func(x):
    return x**2 - 4


a = 0
b = 3
error_margin = 0.0000001


def find_root(func, a, b, margin):
    if func(a) * func(b) >= 0:
        return None

    iteration = 1
    while (b - a) > margin and iteration <= 1000:
        c = (a + b) / 2

        print(f"Step {iteration}: Center = {c}")

        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

        iteration += 1

    return (a + b) / 2


result = find_root(func, a, b, error_margin)
print(f"Root: {result}")
