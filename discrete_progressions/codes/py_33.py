import numpy as np
import matplotlib.pyplot as plt

# Function definition
def custom_function(z):
    return (z * (z - 1/2)) / (z - 1)**3

# Generate values for Z
z_values = np.linspace(-5, 5, 200)  # Adjust the range as needed

# Calculate function values for each Z
y_values = custom_function(z_values)

# Plotting the graph
plt.stem(z_values, y_values, label=r'$\frac{Z(Z-\frac{1}{2})}{(Z-1)^3}$')
plt.xlabel('Z')
plt.ylabel('Function Value')
plt.title('Graph of the Function')
plt.legend()
plt.grid(True)
plt.show()
