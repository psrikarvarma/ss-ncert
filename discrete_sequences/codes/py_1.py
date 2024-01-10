import matplotlib.pyplot as plt
import numpy as np

# Define the function 2^(n+4)
def function(n):
    return 2**(n + 4)

# Generate x values (n values)
n_values = np.arange(0, 10, 1)  # You can adjust the range as needed

# Calculate corresponding y values using the function
y_values = function(n_values)

# Plot the graph
plt.plot(n_values, y_values, label='2^(n+4)')

# Add labels and title
plt.xlabel('n')
plt.ylabel('2^(n+4)')
plt.title('Graph of 2^(n+4)')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
