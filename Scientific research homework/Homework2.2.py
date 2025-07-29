import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.random.randint(0, 200, 15)
y = 0.5 * x**2 - 20 * x + 300 + np.random.normal(0, 500, 15)

degree = 2
coefficients = np.polyfit(x, y, degree)
poly_func = np.poly1d(coefficients)

x_pred = 255
y_pred = poly_func(x_pred)

x_smooth = np.linspace(min(x), max(x), 100)
y_smooth = poly_func(x_smooth)

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_smooth, y_smooth, color='red', label=f'Polynomial Regression (deg={degree})')
plt.scatter(x_pred, y_pred, color='green', marker='x', s=100, label=f'Prediction (x=255, y={y_pred:.2f})')

plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.title("Polynomial Regression Fit")
plt.show()
print(f"Predicted value at x = {x_pred}: y = {y_pred:.2f}")
