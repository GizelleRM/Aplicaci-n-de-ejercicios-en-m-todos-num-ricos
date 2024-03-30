import numpy as np
import matplotlib.pyplot as plt

def minimos_cuadrados(x, y):
    # Calcula la pendiente (m) y la intersección (b) de la línea de mejor ajuste
    n = len(x)
    m = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(x**2) - (np.sum(x))**2)
    b = (np.sum(y) - m*np.sum(x)) / n
    return m, b

def plot_line(x, y, m, b):
    # Dibuja los datos y la línea de mejor ajuste
    plt.scatter(x, y, label='Datos')
    plt.plot(x, m*x + b, color='red', label='Línea de mejor ajuste')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

# Ejemplo de datos
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 3, 3.5, 4, 5, 5.5, 6, 7, 8, 9])

# Calcula los coeficientes de la línea de mejor ajuste
m, b = minimos_cuadrados(x, y)

# Muestra los resultados y grafica la línea de mejor ajuste
print(f"Pendiente (m): {m}")
print(f"Intersección (b): {b}")
plot_line(x, y, m, b)
