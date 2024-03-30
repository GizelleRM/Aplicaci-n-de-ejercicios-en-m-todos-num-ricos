"""El balance de masa de un contaminante en un lago bien mez-
clado se expresa así:

V = dc
dt W Qc kV c – –
Dados los valores de parámetros V = 1 × 106
m3
, Q = l × 105
m3
/año,

W = l × 106

g/año y k = 0.25 m0.5/g0.5/año, use el método de la secan-
te modificado para resolver para la concentración de estado estable.

Emplee un valor inicial c = 4 g/m3

y d = 0.5. Realice tres iteraciones
y determine el error relativo porcentual después de la tercera iteración. """

def contaminant_concentration(c, W, Q, k, V):
    return (W * Q * c) / (k * V) - c

def contaminant_concentration_derivative(c, W, Q, k, V):
    return -1 + (W * Q) / (k * V)

def newton_raphson_method(c0, W, Q, k, V, max_iterations=3):
    iterations = 0
    error_rel_porcentual = 0.0

    while iterations < max_iterations:
        f_c0 = contaminant_concentration(c0, W, Q, k, V)
        f_prime_c0 = contaminant_concentration_derivative(c0, W, Q, k, V)

        c_next = c0 - f_c0 / f_prime_c0

        error_rel_porcentual = abs((c_next - c0) / c_next) * 100

        c0 = c_next
        iterations += 1

    return c0, error_rel_porcentual

# Parámetros dados
V = 1e6  # m^3
Q = 1e5  # m^3/año
W = 1e6  # g/año
k = 0.25  # m^0.5/g^0.5/año

# Valor inicial
c0 = 4.0  # g/m^3

# Aplicar el método de Newton-Raphson
result_c, error_percentage = newton_raphson_method(c0, W, Q, k, V)

print("Concentración de estado estable:", result_c)
print("Error relativo porcentual después de la tercera iteración:", error_percentage)
