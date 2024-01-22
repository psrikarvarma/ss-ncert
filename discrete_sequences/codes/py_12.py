import matplotlib.pyplot as plt
import numpy as np

# Define the function
def rational_function(z):
    return 32 / (1 - 1/(2*z))

# Generate positive values for 'z'
z_values_positive = np.linspace(0.1, 5, 100)  # Adjust the range as needed

# Calculate corresponding function values
y_values_positive = rational_function(z_values_positive)

# Plot the graph
plt.stem(z_values_positive, y_values_positive, label='32/(1-1/(2z))')
plt.xlabel('z')
plt.ylabel('32/(1-1/(2z))')
plt.title('Graph of 32/(1-1/(2z)) for Positive z')
plt.grid(True)
plt.legend()
plt.show()
