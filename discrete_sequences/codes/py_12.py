import numpy as np
import matplotlib.pyplot as plt

# Define the function x(z)
def x(z):
    return 16 / (1 - 1 / (2 * z))

# Generate values for z
z_values = np.linspace(-10, 10, 100)  # Adjust the range as needed

# Calculate corresponding x values
x_values = x(z_values)

# Plot the graph
plt.stem(z_values, x_values, label=r'$x(z) = \frac{16}{1 - \frac{1}{2z}}$')
plt.xlabel('z')
plt.ylabel('x(z)')
plt.title('Graph of $x(z) = \\frac{16}{1 - \\frac{1}{2z}}$')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
