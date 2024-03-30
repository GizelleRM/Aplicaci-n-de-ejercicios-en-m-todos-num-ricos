def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    """
    Realiza el método de iteración de punto fijo para encontrar la raíz de la ecuación x = g(x).

    :param g: Función de iteración.
    :param x0: Aproximación inicial.
    :param tol: Tolerancia para la convergencia.
    :param max_iter: Número máximo de iteraciones.
    :return: Aproximación de la raíz.
    """
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("El método de iteración de punto fijo no convergió en el número máximo de iteraciones.")

# Ejemplo de uso
def g(x):
    return x**2 / 4  # Función de iteración, x = g(x)

initial_guess = 1.0
root = fixed_point_iteration(g, initial_guess)

print(f"La raíz aproximada es: {root}")
