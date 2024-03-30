import numpy as np
import matplotlib.pyplot as plt

def minimos_cuadrados(x, y):
    n = len(x)

    # Calcula las sumas necesarias
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(xi ** 2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Calcula los coeficientes de la línea recta (a y b) utilizando las fórmulas de mínimos cuadrados
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - a * sum_x) / n

    return a, b

def graficar(x, y, a, b):
    plt.scatter(x, y, label='Datos originales')
    plt.plot(x, [a * xi + b for xi in x], color='red', label='Ajuste lineal')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

# Ejemplo de uso
x_datos = [1, 2, 3, 4, 5]
y_datos = [2, 3, 3.5, 4, 5]

a, b = minimos_cuadrados(x_datos, y_datos)
print(f"Coeficiente a: {a}")
print(f"Coeficiente b: {b}")

graficar(x_datos, y_datos, a, b)
