import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi interpolasi polinom Lagrange
def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Contoh penggunaan dan plotting hasil interpolasi Lagrange
x_new = np.linspace(5, 40, 100)
y_new = [lagrange_interpolation(x, y, xi) for xi in x_new]

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_new, '-', label='Lagrange interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.show()
