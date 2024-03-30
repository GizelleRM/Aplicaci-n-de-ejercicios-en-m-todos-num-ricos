import math
import numpy as np

def trapecio_compuesto(funcion, inicio, fin, num_intervalos):
    h = (fin - inicio) / num_intervalos
    suma = 0.5 * (funcion(inicio) + funcion(fin))

    for i in range(1, num_intervalos):
        suma += funcion(inicio + i * h)

    resultado = h * suma
    return resultado

# Intervalo [inicio, fin]
inicio = 0
fin = math.pi / 2

# Número de repeticiones
num_intervalos = 7

# Aplicar la función seno directamente en el cálculo
resultado = trapecio_compuesto(math.sin, inicio, fin, num_intervalos)
print(f"El resultado es: {resultado}")
