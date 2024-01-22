import matplotlib.pyplot as plt
import numpy as np

# Define the function n(21-n)/4
def function(n):
    return n * (21 - n) / 4

# Generate x values (n values)
x_values = np.arange(0, 22, 1)  # You can adjust the range as needed

# Calculate corresponding y values using the function
y_values = function(x_values)

# Plot the graph
plt.stem(x_values, y_values, label='n(21-n)/4')

# Add labels and title
plt.xlabel('n')
plt.ylabel('n(21-n)/4')
plt.title('Graph of n(21-n)/4')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
