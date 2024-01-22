import matplotlib.pyplot as plt
import numpy as np

# Define the function
def exponential_function(n):
    return 2**(n + 3)

# Generate positive values for 'n'
n_values_positive = np.arange(0, 11, 1)  # Adjust the range and step size as needed

# Calculate corresponding function values
y_values_positive = exponential_function(n_values_positive)

# Plot the graph
plt.stem(n_values_positive, y_values_positive, label='2^(n+3)')
plt.xlabel('n')
plt.ylabel('2^(n+3)')
plt.title('Graph of 2^(n+3) for Positive n')
plt.grid(True)
plt.legend()
plt.show()
