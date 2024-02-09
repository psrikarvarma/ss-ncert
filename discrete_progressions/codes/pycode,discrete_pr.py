import numpy as np
import matplotlib.pyplot as plt

# Values for larger n
n_values_large = np.arange(0, 30, 1)

# Function definitions
def func1(n):
    return (n + 2) / 2

def func2(n):
    return n * (n + 3) / 4

def func3(n):
    return (10 - n) / 2

def func4(n):
    return n * (21 - n) / 4

# Plotting stem graphs for large n
plt.figure(figsize=(12, 10))

plt.subplot(421)
plt.stem(n_values_large, func1(n_values_large), basefmt='b', linefmt='r-', markerfmt='ro')

plt.subplot(422)
plt.stem(n_values_large, func2(n_values_large), basefmt='b', linefmt='r-', markerfmt='ro')

plt.subplot(423)
plt.stem(n_values_large, func3(n_values_large), basefmt='b', linefmt='r-', markerfmt='ro')

plt.subplot(424)
plt.stem(n_values_large, func4(n_values_large), basefmt='b', linefmt='r-', markerfmt='ro')

plt.tight_layout()
plt.show()
