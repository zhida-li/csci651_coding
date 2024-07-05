"""
    @authors Zhida Li
    @email zli74@nyit.edu
    @date July 4, 2024
    @version: 1.0.0
    @description:
                CSCI 651, Polynomial curve fitting example.
    @copyright Copyright (c) July 4, 2024
        All Rights Reserved
    @date edited: July 4, 2024
"""

print(__doc__)

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# Generate synthetic stock price data
np.random.seed(0)
days = np.linspace(0, 99, 100)  # Time steps
prices = np.cumsum(np.random.normal(0, 2, size=days.size))  # Random walk
trend = 0.3 * days  # Adding a slight upward trend
synthetic_stock_prices = prices + trend + 100  # Base price adjustment

# Split the data into training and testing
x_train = days[:80].reshape(-1, 1)
y_train = synthetic_stock_prices[:80]
x_test = days[80:].reshape(-1, 1)
y_test = synthetic_stock_prices[80:]

# Define the range of degrees for the subplots and error analysis
degrees = range(1, 7)
train_errors = []
test_errors = []

# Create figure for the polynomial models
plt.figure(figsize=(15, 10))

for i, degree in enumerate(degrees, 1):
    # Polynomial transformation for the current degree
    poly_features = PolynomialFeatures(degree=degree)
    x_train_poly = poly_features.fit_transform(x_train)
    x_test_poly = poly_features.transform(x_test)
    x_full_poly = poly_features.transform(days.reshape(-1, 1))

    # Train the model
    model = LinearRegression()
    model.fit(x_train_poly, y_train)

    # Predict and calculate errors
    y_full_pred = model.predict(x_full_poly)
    y_train_pred = model.predict(x_train_poly)
    y_test_pred = model.predict(x_test_poly)
    train_error = mean_squared_error(y_train, y_train_pred)
    test_error = mean_squared_error(y_test, y_test_pred)
    train_errors.append(train_error)
    test_errors.append(test_error)

    # Subplot
    plt.subplot(2, 3, i)
    plt.scatter(x_train, y_train, color='blue', label='Training data')
    plt.scatter(x_test, y_test, color='green', label='Test data')
    plt.plot(days, y_full_pred, color='red', label=f'Degree {degree}')
    plt.title(f'Polynomial Regression Degree {degree}')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()

    # Print errors for each degree
    print(f"Degree {degree} - Training Error: {train_error:.2f}, Testing Error: {test_error:.2f}")

# Adjust layout
plt.tight_layout()
plt.show()

# Plot training and testing errors
plt.figure(figsize=(10, 5))
plt.plot(degrees, train_errors, marker='o', linestyle='-', color='blue', label='Training Error')
plt.plot(degrees, test_errors, marker='o', linestyle='-', color='green', label='Testing Error')

# Annotate each point with its error value, color-coordinated
for i, (tr_err, te_err) in enumerate(zip(train_errors, test_errors)):
    plt.annotate(f'{tr_err:.2f}', (degrees[i], train_errors[i]), textcoords="offset points", 
                 xytext=(0, -20), ha='center', color='blue')  # Offset training errors downwards
    plt.annotate(f'{te_err:.2f}', (degrees[i], test_errors[i]), textcoords="offset points", 
                 xytext=(0, 10), ha='center', color='green')  # Offset testing errors upwards

plt.title('Training and Testing Errors for Different Polynomial Degrees')
plt.xlabel('Polynomial Degree')
plt.ylabel('Mean Squared Error')
plt.xticks(degrees)
plt.legend()
plt.grid(True)
plt.show()
