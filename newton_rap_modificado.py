import numpy as np
from scipy.linalg import solve

def funcion(x):
    # Define tu sistema de ecuaciones 
    f1 = x[0]**2 + x[1]**2 - 4
    f2 = x[0]*x[1] - 1
    return np.array([f1, f2])

def jacobiano(x):
    # Calcula la matriz jacobiana de las derivadas parciales.
    df1_dx0 = 2 * x[0]
    df1_dx1 = 2 * x[1]
    df2_dx0 = x[1]
    df2_dx1 = x[0]
    return np.array([[df1_dx0, df1_dx1],
                     [df2_dx0, df2_dx1]])

def newton_multivariable(x0, tolerancia=1e-6, max_iter=100):
    for i in range(max_iter):
        f = funcion(x0)
        J = jacobiano(x0)

        delta_x = solve(J, -f)

        x0 = x0 + delta_x

        # Verifica la convergencia
        norma_delta_x = np.linalg.norm(delta_x)
        if norma_delta_x < tolerancia:
            print(f"Convergencia alcanzada en la iteración {i+1}.")
            return x0

    print("El método de Newton no convergió después de", max_iter, "iteraciones.")
    return None

# Ejemplo de uso
x_inicial = np.array([1.5, 1.5])
raiz_aproximada = newton_multivariable(x_inicial)

if raiz_aproximada is not None:
    print("Raíz aproximada:", raiz_aproximada)
else:
    print("No se encontró una raíz en las iteraciones dadas.")
