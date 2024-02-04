import numpy as np
import matplotlib.pyplot as plt

# Function definitions
def func1(n):
    return np.where((2 < n) & (n < 5), 2**(n + 3), 0)

def func2(n):
    return np.where((2 < n) & (n < 5), 2**(5 - n), 0)

def func3(z):
    return np.where(abs(z) > 2, 8 / (1 - 2 * z**(-1)), 0)

def func4(z):
    return np.where(abs(z) > 2, 32 / (1 - 1/(2*z)), 0)

# Generate values for n and z
n_values = np.arange(2.1, 5, 0.1)
z_values = np.arange(2.1, 5, 0.1)

# Calculate corresponding y values for each function
y_values1 = func1(n_values)
y_values2 = func2(n_values)
y_values3 = func3(z_values)
y_values4 = func4(z_values)

# Plotting the stem graphs
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(n_values, y_values1, basefmt='b', linefmt='r-', markerfmt='ro')
plt.title('$2^{n+3}$')
plt.xlabel('$n$')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 2)
plt.stem(n_values, y_values2, basefmt='b', linefmt='r-', markerfmt='ro')
plt.title('$2^{5-n}$')
plt.xlabel('$n$')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 3)
plt.stem(z_values, y_values3, basefmt='b', linefmt='r-', markerfmt='ro')
plt.title('$\\frac{8}{1-2z^{-1}}$')
plt.xlabel('$z$')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 4)
plt.stem(z_values, y_values4, basefmt='b', linefmt='r-', markerfmt='ro')
plt.title('$\\frac{32}{1-\\frac{1}{2z}}$')
plt.xlabel('$z$')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
