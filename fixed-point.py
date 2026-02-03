import math


def g(x):
    return math.sqrt(x + 2)


def fixed_point(initial_guess, eps=0.000000001):
    x = initial_guess
    iteration = 0

    while True:
        print(f"iteration: {iteration}, fixed point: {x}")

        new_x = g(x)
        if abs(new_x - x) < eps:
            break

        x = new_x
        iteration += 1


if __name__ == "__main__":
    fixed_point(1)
