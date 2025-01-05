from sympy import symbols, diff
class GradientDescent:
    # for using this class you should pas gradient to main gradientDescent class and your first x and learning rate 
    # to the learn method
    def __init__(self, gradient):
        self.gradient = gradient
    
    def learn(self, x, learning_rate):
        i = 1  
        while True:
            old_x = x  
            x = x - learning_rate * self.gradient(x)  # Use self.gradient
            difference = x - old_x
            if abs(difference) < 0.001:
                return (f'Attempt {i}: new x = {x:.3f}, old x = {old_x:.3f}')
            i += 1

class LinearRegression:
    def __init__(self,data):
        self.data = data
    def calculate(data, m, b):
        mse = 0
        for x, y in data.items():
            mse += (y - (m * x + b)) ** 2
        return mse / (2 * len(data))

    def compute_derivative(expression, variable):
        return diff(expression, variable)

    # Calculate initial derivatives
    def train_model(self,alpha,m0,b0):
        L = LinearRegression
        m, b = symbols('m b')
        derivative_m = L.compute_derivative(L.calculate(self.data, m, b), m)
        derivative_b = L.compute_derivative(L.calculate(self.data, m, b), b)
    # Gradient Descent
        self.m0 = m0
        self.b0 = b0
        max_iterations = 1000
        tolerance = 1e-5

        for _ in range(max_iterations):
            current_loss = L.calculate(self.data, m0, b0)

            grad_m = derivative_m.subs({m: m0, b: b0})
            grad_b = derivative_b.subs({m: m0, b: b0})

            m0 = m0 - alpha * grad_m
            b0 = b0 - alpha * grad_b

            new_loss = L.calculate(self.data, m0, b0)

            if abs(new_loss - current_loss) < tolerance:
                break

        return f'm0 : {m0} , b0 : {b0}'
