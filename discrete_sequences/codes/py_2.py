import matplotlib.pyplot as plt
import numpy as np

# Define the function 16 * (1/2)^n
def function(n):
    return 16 * (1/2)**n

# Generate x values (n values)
n_values = np.arange(0, 10, 1)  # You can adjust the range as needed

# Calculate corresponding y values using the function
y_values = function(n_values)

# Plot the graph
plt.stem(n_values, y_values, label='16 * (1/2)^n')

# Add labels and title
plt.xlabel('n')
plt.ylabel('16 * (1/2)^n')
plt.title('Graph of 16 * (1/2)^n')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
