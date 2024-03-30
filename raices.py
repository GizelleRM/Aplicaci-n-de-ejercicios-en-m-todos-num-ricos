def funcion(x):
      return x**3 - 6*x**2 + 11*x - 6

def biseccion(a, b, tolerancia=1e-6, max_iter=100):
    # Verifica si el signo de la función cambia en el intervalo dado
    if funcion(a) * funcion(b) > 0:
        print("La función no cambia de signo en el intervalo dado.")
        return None

    iteracion = 0
    while (b - a) / 2 > tolerancia and iteracion < max_iter:
        c = (a + b) / 2
        if funcion(c) == 0:
            return c  # c es una raíz exacta
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
        iteracion += 1

    # Devuelve el valor aproximado de la raíz
    return (a + b) / 2

# Intervalo inicial [a, b]
a = 0
b = 3

# Encuentra la raíz utilizando el método de bisección
raiz = biseccion(a, b)

if raiz is not None:
    print(f"Raíz aproximada: {raiz}")
else:
    print("No se encontró raíz en el intervalo dado.")
