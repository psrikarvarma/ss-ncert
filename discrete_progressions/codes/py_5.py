import matplotlib.pyplot as plt
import numpy as np

# Define the function (10-n)/2
def function(n):
    return (10 - n) / 2

# Generate x values (n values)
x_values = np.arange(-10, 11, 1)  # You can adjust the range as needed

# Calculate corresponding y values using the function
y_values = function(x_values)

# Plot the graph
plt.stem(x_values, y_values, label='(10-n)/2')

# Add labels and title
plt.xlabel('n')
plt.ylabel('(10-n)/2')
plt.title('Graph of (10-n)/2')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
