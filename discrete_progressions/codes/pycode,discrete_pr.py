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

def func5(z):
    return (2 - z**(-1)) / (2 * (1 - z**(-1))**2)

def func6(z):
    return (10 - 11 * z**(-1)) / (2 * (1 - z**(-1))**2)

def func7(z):
    return z * (z - 0.5) / (z - 1)**3

def func8(z):
    return z * (5 * z - 5.5) / (z - 1)**3

# Plotting stem graphs for large n
plt.figure(figsize=(12, 10))

plt.subplot(421)
plt.stem(n_values_large, func1(n_values_large), basefmt='b', linefmt='r-', markerfmt='ro')
plt.title(r'$\frac{n+2}{2}$')

plt.subplot(422)
plt.stem(n_values_large, func2(n_values_large), basefmt='b', linefmt='r-', markerfmt='ro')
plt.title(r'$\frac{n(n+3)}{4}$')

plt.subplot(423)
plt.stem(n_values_large, func3(n_values_large), basefmt='b', linefmt='r-', markerfmt='ro')
plt.title(r'$\frac{10-n}{2}$')

plt.subplot(424)
plt.stem(n_values_large, func4(n_values_large), basefmt='b', linefmt='r-', markerfmt='ro')
plt.title(r'$\frac{n(21-n)}{4}$')

# Plotting stem graphs for z-transform expressions
z_values = np.linspace(0.1, 2, 100)
plt.subplot(425)
plt.stem(z_values, func5(1/z_values), basefmt='b', linefmt='r-', markerfmt='ro')
plt.title(r'$\frac{2 - z^{-1}}{2(1 - z^{-1})^2}$')

plt.subplot(426)
plt.stem(z_values, func6(1/z_values), basefmt='b', linefmt='r-', markerfmt='ro')
plt.title(r'$\frac{10 - 11z^{-1}}{2(1 - z^{-1})^2}$')

plt.subplot(427)
plt.stem(z_values, func7(1/z_values), basefmt='b', linefmt='r-', markerfmt='ro')
plt.title(r'$\frac{z(z - \frac{1}{2})}{(z - 1)^3}$')

plt.subplot(428)
plt.stem(z_values, func8(1/z_values), basefmt='b', linefmt='r-', markerfmt='ro')
plt.title(r'$\frac{z(5z - \frac{11}{2})}{(z - 1)^3}$')

plt.tight_layout()
plt.show()
