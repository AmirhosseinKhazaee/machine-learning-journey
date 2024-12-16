# Example: Gradient Descent for a Real-Valued Function
# Function: f(x) = (x-3)^2 + 5
# Gradient (derivative): f'(x) = 2x - 6

# Define the gradient function
gradient = lambda x: (2 * x) - 6  # Derivative of the function

# Starting point
x = 2  

# Learning rate (step size)
learning_rate = 0.1  

# For tracking the number of attempts
i = 1  

# Main gradient descent loop
while True:
    old_x = x  # Store the old value of x
    x = x - learning_rate * gradient(x)  # Update x using gradient descent
    difference = x - old_x  # Calculate the change in x
    
    # Check if the update is small enough to stop
    if abs(difference) < 0.005:
        break
    
    # Print progress
    print(f'attempt {i} new x: {x:.3f} and old x: {old_x:.3f}')
    i += 1

# Final result
print(f'Optimal x: {x:.3f}')
