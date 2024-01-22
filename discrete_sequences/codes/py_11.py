import matplotlib.pyplot as plt
import numpy as np

# Define the function
def rational_function(x):
    return 8 / (1 - 2/x)

# Generate positive values for 'x'
x_values_positive = np.linspace(0.1, 5, 100)  # Adjust the range as needed

# Calculate corresponding function values
y_values_positive = rational_function(x_values_positive)

# Plot the graph
plt.stem(x_values_positive, y_values_positive, label='8/(1-2/x)')
plt.xlabel('x')
plt.ylabel('8/(1-2/x)')
plt.title('Graph of 8/(1-2/x) for Positive x')
plt.grid(True)
plt.legend()
plt.show()
