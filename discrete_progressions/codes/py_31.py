import numpy as np
import matplotlib.pyplot as plt

# Function definition
def custom_function(z):
    return (2 - 1/z) / (2 * (1 - 1/z)**2)

# Generate values for Z (positive values)
z_values = np.linspace(0.01, 5, 100)  # Adjust the range as needed

# Calculate function values for each Z
y_values = custom_function(z_values)

# Plotting the graph
plt.stem(z_values, y_values, label=r'$\frac{2 - Z^{-1}}{2(1 - Z^{-1})^2}$')
plt.xlabel('Z')
plt.ylabel('Function Value')
plt.title('Graph of the Function')
plt.legend()
plt.grid(True)
plt.show()
