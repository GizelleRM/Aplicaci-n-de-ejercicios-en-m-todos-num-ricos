def lagrange_interpolation(x_values, y_values, x):
    """
    Realiza la interpolación de Lagrange para encontrar el valor correspondiente a x.

    :param x_values: Lista de valores x conocidos.
    :param y_values: Lista de valores y conocidos.
    :param x: Valor para el cual se desea realizar la interpolación.
    :return: Valor interpolado correspondiente a x.
    """
    result = sum(y_values[j] * lagrange_basis(x_values, j, x) for j in range(len(x_values)))
    return result

def lagrange_basis(x_values, j, x):
    """
    Calcula la base de Lagrange correspondiente al índice j.

    :param x_values: Lista de valores x conocidos.
    :param j: Índice de la base de Lagrange.
    :param x: Valor para el cual se desea calcular la base.
    :return: Valor de la base de Lagrange correspondiente a x.
    """
    numerator = [(x - x_values[m]) for m in range(len(x_values)) if m != j]
    denominator = [(x_values[j] - x_values[m]) for m in range(len(x_values)) if m != j]
    result = (1.0 * prod(numerator)) / prod(denominator)
    return result

def prod(numbers):
    """
    Calcula el producto de una lista de números.

    :param numbers: Lista de números.
    :return: Producto de los números en la lista.
    """
    result = 1
    for number in numbers:
        result *= number
    return result

# Ejemplo de uso
x_values = [1, 2, 4]
y_values = [2, 3, 1]

x_interpolate = 3
result = lagrange_interpolation(x_values, y_values, x_interpolate)

print(f"El valor interpolado para x = {x_interpolate} es {result}")
