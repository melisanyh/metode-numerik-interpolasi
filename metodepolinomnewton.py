import numpy as np
import matplotlib.pyplot as plt

# Fungsi interpolasi polinom Newton
def newton_interpolation(x, y, xi):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    
    result = coef[0,0]
    for i in range(1, n):
        term = coef[0, i]
        for j in range(i):
            term = term * (xi - x[j])
        result += term
    return result

# Data yang diberikan
x = [1, 2, 3, 4, 5]
y = [2.5, 3.5, 4.5, 6.5, 7.5]

# Definisikan array baru untuk mengevaluasi interpolasi
x_new = np.linspace(min(x), max(x), 100)  # Buat array dengan 100 titik di antara nilai terkecil dan terbesar dari x

# Contoh penggunaan dan plotting hasil interpolasi Newton
y_new_newton = [newton_interpolation(x, y, xi) for xi in x_new]

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_new_newton, '-', label='Newton interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.show()