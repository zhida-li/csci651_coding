import random

def approximate_pi_monte_carlo(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_approx = (inside_circle / num_samples) * 4
    return pi_approx

# Using 1 million samples for a good approximation
num_samples = 1000000
pi_estimate = approximate_pi_monte_carlo(num_samples)
print(f"Approximation of pi using Monte Carlo method with {num_samples} samples: {pi_estimate}")
