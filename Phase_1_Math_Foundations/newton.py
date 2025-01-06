def newtons_method(f, df, x0, epsilon=0.001, max_iter=10):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < epsilon:
            return x
        if dfx == 0:
            raise ValueError("Derivative is zero")
        x_new = x - fx / dfx
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
    raise ValueError("Method did not converge within the maximum iterations")

# the function and its derivative
f = lambda x: x**2 - 2
df = lambda x: 2 * x

# Initial guess
x0 = 1

root = newtons_method(f, df, x0)
print(f"Approximate root: {root}")
