import numpy as np
import matplotlib.pyplot as plt

# Function definitions
def func1(x):
    return 2**(x + 3)

def func2(x):
    return 2**(5 - x)

def func3(x):
    return 8 / (1 - 2 * (1 / x))

def func4(x):
    return 32 / (1 - (2 * x)**(-1))

# Generate values for x
x_values = np.linspace(0.1, 5, 100)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(x_values, func1(x_values), label=r'$2^{x+3}$')
plt.title('Graph of $2^{x+3}$')
plt.xlabel('x')
plt.ylabel('Function Value')
plt.legend()

plt.subplot(2, 2, 2)
plt.stem(x_values, func2(x_values), label=r'$2^{5-x}$')
plt.title('Graph of $2^{5-x}$')
plt.xlabel('x')
plt.ylabel('Function Value')
plt.legend()

plt.subplot(2, 2, 3)
plt.stem(x_values, func3(x_values), label=r'$\frac{8}{1-2(x^{-1})}$')
plt.title('Graph of $\\frac{8}{1-2(x^{-1})}$')
plt.xlabel('x')
plt.ylabel('Function Value')
plt.legend()

plt.subplot(2, 2, 4)
plt.stem(x_values, func4(x_values), label=r'$\frac{32}{1-(2x)^{-1}}$')
plt.title('Graph of $\\frac{32}{1-(2x)^{-1}}$')
plt.xlabel('x')
plt.ylabel('Function Value')
plt.legend()

plt.tight_layout()
plt.show()
