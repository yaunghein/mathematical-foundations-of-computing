def gradient_descent(f, f_prime, start_x, lr=0.1, iters=50):
    x = start_x
    for i in range(iters):
        prev_x = x
        x -= lr * f_prime(x)
        print(f"Iteration {i+1}: x = {round(x, 4)}, f(x) = {round(f(x), 4)}")

        if abs(x - prev_x) < 0.001:
            break

    return x


def f(x):
    return (x - 3)**2 + 3


def f_prime(x):
    return 2 * (x - 3)


final_x = gradient_descent(f, f_prime, start_x=10.0, lr=0.1, iters=40)

print(f"\nFinal Result: Minimum found at x ≈ {round(final_x, 2)}")
