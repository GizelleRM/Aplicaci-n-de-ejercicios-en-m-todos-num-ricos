""" utiliza un metodo cerrado para La velocidad u de un paracaidista que cae está dada por
 v= (gm/c)(1- e^(-c/m t))
donde g = 9.81 m/s2 Para un paracaidista con coeficiente de resis-
tencia de c = 15 kg/s, calcule la masa m de modo que la velocidad
sea y = 36 m/s en t = 10 s. Utilice el método de la falsa posición para
determinar m a un nivel de es = 0.1%."""

import math

def parachute_velocity(m, t, c=15, g=9.81):
    return (g * m / c) * (1 - math.exp(-c / m * t)) - 36

def bisection_method(a, b, t_target, c=15, g=9.81, tolerance=0.1, max_iterations=100):
    iterations = 0
    error_rel_porcentual = 100.0

    while error_rel_porcentual > tolerance and iterations < max_iterations:
        m_mid = (a + b) / 2
        f_a = parachute_velocity(a, t_target, c, g)
        f_mid = parachute_velocity(m_mid, t_target, c, g)

        if f_a * f_mid < 0:
            b = m_mid
        else:
            a = m_mid

        if m_mid != 0:
            error_rel_porcentual = abs((b - a) / m_mid) * 100

        iterations += 1

    return (a + b) / 2

# Parámetros dados
t_target = 10.0  # segundos
c = 15  # kg/s
g = 9.81  # m/s^2

# Intervalo inicial [a, b]
a = 1.0
b = 100.0

# Aplicar el método de la bisección
result_mass = bisection_method(a, b, t_target, c, g)

print("Masa calculada:", result_mass, "kg")
