import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for z
z_values = np.linspace(0.1, 2, 100)

# Define the functions
def f1(z):
    return (z + 2) / 2

def f2(z):
    return z * (z + 3) / 4

def f3(z):
    return (10 - z) / 2

def f4(z):
    return z * (21 - z) / 4

def f5(z):
    return (2 - z**(-1)) / (2 * (1 - z**(-1))**2)

def f6(z):
    return (10 - 11 * z**(-1)) / (2 * (1 - z**(-1))**2)

def f7(z):
    return z * (z - 1/2) / (z - 1)**3

def f8(z):
    return z * (5 * z - 11/2) / (z - 1)**3

# Plot each function
plt.figure(figsize=(12, 8))

plt.subplot(2, 4, 1)
plt.stem(z_values, f1(z_values))
plt.title('(n+2)/2')

plt.subplot(2, 4, 2)
plt.stem(z_values, f2(z_values))
plt.title('n(n+3)/4')

plt.subplot(2, 4, 3)
plt.stem(z_values, f3(z_values))
plt.title('(10-n)/2')

plt.subplot(2, 4, 4)
plt.stem(z_values, f4(z_values))
plt.title('n(21-n)/4')

plt.subplot(2, 4, 5)
plt.stem(z_values, f5(z_values))
plt.title('(2-z^{-1})/2(1-z^{-1})^2')

plt.subplot(2, 4, 6)
plt.stem(z_values, f6(z_values))
plt.title('(10-11z^{-1})/2(1-z^{-1})^2')

plt.subplot(2, 4, 7)
plt.stem(z_values, f7(z_values))
plt.title('z(z-(1/2))/(z-1)^3')

plt.subplot(2, 4, 8)
plt.stem(z_values, f8(z_values))
plt.title('z(5z-(11/2))/(z-1)^3')

plt.tight_layout()
plt.show()
