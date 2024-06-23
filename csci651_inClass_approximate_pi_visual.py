"""
Estimating the value of pi using a Monte Carlo simulation

"""
import random
import matplotlib.pyplot as plt

def approximate_pi_monte_carlo(num_samples, plot_frequency=10000):
    inside_circle = 0
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')  # Maintain the aspect ratio of the plot

    # Define limits for clarity in visualization
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.add_artist(plt.Circle((0, 0), 1, edgecolor='r', facecolor='none'))  # Draw the unit circle

    # Loop over the specified number of samples
    for i in range(num_samples):
        # Generate random x, y coordinates between -1 and 1
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        # Check if the point lies inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
            ax.plot(x, y, 'ro', markersize=1)  # Plot points inside the circle as green
        else:
            ax.plot(x, y, 'bo', markersize=1)  # Plot points outside the circle as blue

        # Update the plot and print pi approximation every 'plot_frequency' points
        if (i + 1) % plot_frequency == 0:
            current_pi_approx = (inside_circle / (i + 1)) * 4  # Current approximation of pi
            print(f"Current approximation of pi after {i + 1} samples: {current_pi_approx}")
            plt.pause(0.001)  # Pause to update the plot

    # Calculate the final approximation of pi
    pi_approx = (inside_circle / num_samples) * 4
    plt.show()
    return pi_approx

# Specify the number of samples to use
num_samples = 1000000
# Call the function and store the result
pi_estimate = approximate_pi_monte_carlo(num_samples, plot_frequency=1000)
# Print the final approximation result
print(f"Final approximation of pi using Monte Carlo method with {num_samples} samples: {pi_estimate}")
