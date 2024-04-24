"""
Estimating the value of pi using a Monte Carlo simulation

"""
import random

def approximate_pi_monte_carlo(num_samples):
    inside_circle = 0
    # Loop over the specified number of samples
    for _ in range(num_samples):
        # Generate random x, y coordinates between -1 and 1
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        # Check if the point lies inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
    # Calculate the approximation of pi
    pi_approx = (inside_circle / num_samples) * 4
    return pi_approx

# Specify the number of samples to use
num_samples = 1000000
# Call the function and store the result
pi_estimate = approximate_pi_monte_carlo(num_samples)
# Print the approximation result
print(f"Approximation of pi using Monte Carlo method with {num_samples} samples: {pi_estimate}")
