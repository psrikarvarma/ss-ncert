import matplotlib.pyplot as plt
import numpy as np

# Define the function n(n+3)/4
def function(n):
    return (n * (n + 3)) / 4

# Generate x values (n values)
x_values = np.arange(-10, 11, 1)  # You can adjust the range as needed

# Calculate corresponding y values using the function
y_values = function(x_values)

# Plot the graph
plt.plot(x_values, y_values, label='n(n+3)/4')

# Add labels and title
plt.xlabel('n')
plt.ylabel('n(n+3)/4')
plt.title('Graph of n(n+3)/4')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
