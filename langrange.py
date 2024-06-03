import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Lagrange Interpolation
def lagrange_interpolation(x_values, y_values, x):
    def basis(j):
        p = [(x - x_values[m])/(x_values[j] - x_values[m]) for m in range(len(x_values)) if m != j]
        return np.prod(p, axis=0) * y_values[j]

    return sum(basis(j) for j in range(len(x_values)))

# Newton Interpolation
def newton_interpolation(x_values, y_values, x):
    def divided_diff(x_values, y_values):
        n = len(y_values)
        coef = np.zeros([n, n])
        coef[:,0] = y_values
        
        for j in range(1,n):
            for i in range(n-j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x_values[i+j] - x_values[i])
        
        return coef[0, :]
    
    coef = divided_diff(x_values, y_values)
    n = len(coef)
    polynomial = coef[n-1]
    for k in range(1, n):
        polynomial = coef[n-1-k] + (x - x_values[n-1-k])*polynomial
    return polynomial

# Plotting the interpolation
x_plot = np.linspace(5, 40, 1000)
y_lagrange = [lagrange_interpolation(x, y, i) for i in x_plot]
y_newton = [newton_interpolation(x, y, i) for i in x_plot]

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_plot, y_lagrange, '-', label='Lagrange Interpolation')
plt.plot(x_plot, y_newton, '--', label='Newton Interpolation')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu Patah (jam)')
plt.legend()
plt.title('Interpolasi Polinom Lagrange dan Newton')
plt.grid(True)
plt.show()
