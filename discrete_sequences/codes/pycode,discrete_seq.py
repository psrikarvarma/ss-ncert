import numpy as np
import matplotlib.pyplot as plt

# Function definitions
def func1(n):
    return np.where((2 < n) & (n < 5), 2**(n + 3), 0)

def func2(n):
    return np.where((2 < n) & (n < 5), 2**(5 - n), 0)

# Generate values for n
n_values = np.arange(2.1, 5, 0.1)

# Calculate corresponding y values for each function
y_values1 = func1(n_values)
y_values2 = func2(n_values)

# Plotting the stem graphs
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(n_values, y_values1, basefmt='b', linefmt='r-', markerfmt='ro')
plt.xlabel('$n$')

plt.subplot(2, 2, 2)
plt.stem(n_values, y_values2, basefmt='b', linefmt='r-', markerfmt='ro')
plt.xlabel('$n$')

plt.tight_layout()
plt.show()
