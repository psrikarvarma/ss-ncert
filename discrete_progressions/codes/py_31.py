import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return (1 + 2 * (1 - 1 / x)) / (2 * (1 - 1 / x)**2)

# Generate values for x
x_values = np.linspace(0.1, 10, 100)  # Adjust the range as needed

# Calculate corresponding y values
y_values = f(x_values)

# Plot the graph
plt.stem(x_values, y_values, label=r'$\frac{{1 + 2(1 - \frac{1}{x})}}{{2(1 - \frac{1}{x})^2}}$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of the given function')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
