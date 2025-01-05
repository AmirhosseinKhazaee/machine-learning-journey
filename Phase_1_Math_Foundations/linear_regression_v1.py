from sympy import symbols, diff

m, b = symbols('m b')

data = {
    500: 150,
    750: 200,
    1000: 250,
    1250: 300,
    1500: 350,
    1750: 400,
    2000: 450
}

def calculate(data, m, b):
    mse = 0
    for x, y in data.items():
        mse += (y - (m * x + b)) ** 2
    return mse / (2 * len(data))

def compute_derivative(expression, variable):
    return diff(expression, variable)

# Calculate initial derivatives
derivative_m = compute_derivative(calculate(data, m, b), m)
derivative_b = compute_derivative(calculate(data, m, b), b)
print(f"Initial Derivative wrt m: {derivative_m}")
print(f"Initial Derivative wrt b: {derivative_b}")

# Gradient Descent
alpha = 0.001
m0 = 1
b0 = 1
max_iterations = 1000
tolerance = 1e-5

for i in range(max_iterations):
    current_loss = calculate(data, m0, b0)

    grad_m = derivative_m.subs({m: m0, b: b0})
    grad_b = derivative_b.subs({m: m0, b: b0})

    m0 = m0 - alpha * grad_m
    b0 = b0 - alpha * grad_b

    new_loss = calculate(data, m0, b0)

    if abs(new_loss - current_loss) < tolerance:
        break

print(f"Final m: {m0}")
print(f"Final b: {b0}")