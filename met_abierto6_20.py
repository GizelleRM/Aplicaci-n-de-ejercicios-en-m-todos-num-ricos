""" con un metodo abierto calcular La ecuación de Manning se puede escribir para un flujo en un
canal abierto rectangular como
Q =
√S(B H)5/3
n(B + 2H)2/3
donde Q = flujo [m3/s], S = pendiente [m/m], H = profundidad [m]

y n = coeficiente de rugosidad de Manning. Desarrolle un esque-
ma de iteración para despejar H de esta ecuación dado Q = 5, S =

0.0002, B = 20 y n = 0.03. Pruebe que su esquema converge para
todos los valores iniciales mayores que cero o iguales a cero.
"""

import math

def manning_equation(H, B, S, n):
    return math.sqrt(S * (B * H)**(5/3)) / (n * (B + 2 * H)**(2/3))

def manning_equation_derivative(H, B, S, n):
    return (5/6) * math.sqrt(S) * B**(5/3) / (n * (B + 2 * H)**(5/3))

def newton_raphson(Q, B, S, n, initial_guess, tolerance=1e-6, max_iterations=100):
    H = initial_guess
    iterations = 0

    while iterations < max_iterations:
        F = manning_equation(H, B, S, n) - Q
        F_prime = manning_equation_derivative(H, B, S, n)

        H -= F / F_prime

        if abs(F) < tolerance:
            return H

        iterations += 1

    raise ValueError("El método no converge en el número máximo de iteraciones")

# Parámetros dados
Q = 5
S = 0.0002
B = 20
n = 0.03

# Valor inicial de H
initial_guess = 1.0

# Aplicar el método de Newton-Raphson
result_H = newton_raphson(Q, B, S, n, initial_guess)

print("Profundidad (H) calculada:", result_H)
