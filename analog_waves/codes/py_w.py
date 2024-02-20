import numpy as np
import matplotlib.pyplot as plt

def sound_wave(A, k, omega, t, x):
    return A * np.sin(k * x) * np.cos(omega * t)

def reflected_sound_wave(A, k, omega, t, x):
    return -A * np.sin(k * x) * np.cos(omega * t)

# Parameters
A = 1.0
k = 2.0
omega = 1.0
t = 0.0

# Generate x values
x_values = np.linspace(0, 10, 1000)

# Generate y values for the original and reflected sound waves
y_values_original = sound_wave(A, k, omega, t, x_values)
y_values_reflected = reflected_sound_wave(A, k, omega, t, x_values)

# Combine the two waves
y_values_combined = y_values_original + y_values_reflected

# Plot the original and reflected sound waves combined
plt.plot(x_values, y_values_original, label='Original Sound Wave')
plt.plot(x_values, y_values_reflected, label='Reflected Sound Wave')
plt.plot(x_values, y_values_combined, label='Combined Waves', linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('ncert-physics/11/15/23/figs/py_w.png')
plt.show()
