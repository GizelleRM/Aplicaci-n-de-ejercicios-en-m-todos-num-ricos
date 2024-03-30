"""
Ejercicio 24.33:
Suponga que la corriente a través de una resistencia está descrita por la función:

i(t) = (60 – t)^2 + (60 – t) * sen(raiz de t)

y que la resistencia es función de la corriente:
R = 10i + 2i^(2/3)

Calcule el voltaje promedio desde t = 0 hasta 60, con el uso de la
regla de Simpson 1/3 de segmentos múltiples.
"""
import numpy as np

# Definir la función de corriente
def current_function(t):
    return (60 - t)**2 + (60 - t) * np.sin(np.sqrt(t))

# Definir la función de resistencia en términos de la corriente
def resistance_function(i):
    return 10*i + 2*i**(2/3)

# Definir la función de voltaje en términos de la corriente
def voltage_function(i):
    return i * resistance_function(i)

# Regla de Simpson 1/3 de segmentos múltiples
def simpsons_rule(h, y):
    n = len(y) - 1
    result = y[0] + y[n]
    
    for i in range(1, n, 2):
        result += 4 * y[i]
    
    for i in range(2, n-1, 2):
        result += 2 * y[i]
    
    return result * h / 3

# Intervalo de tiempo y número de segmentos
t_start = 0
t_end = 60
num_segments = 1000  # Puedes ajustar este valor según sea necesario

# Crear puntos de evaluación
t_values = np.linspace(t_start, t_end, num_segments + 1)
i_values = current_function(t_values)

# Calcular el voltaje en cada punto de la corriente
v_values = voltage_function(i_values)

# Calcular el voltaje promedio usando la regla de Simpson 1/3
h = (t_end - t_start) / num_segments
average_voltage = simpsons_rule(h, v_values)

print(f"El voltaje promedio es: {average_voltage}")



