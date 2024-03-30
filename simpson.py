import numpy as np

def simpson(funcion, inicio, fin, m):
    h = (fin - inicio) / m
    x = np.linspace(inicio, fin, m+1)
    y = funcion(x)
    
    integral = h/3 * (y[0] + 4*np.sum(y[1:m:2]) + 2*np.sum(y[2:m-1:2]) + y[m])
    
    return integral

inicio = 0
fin = np.pi/2

m = 14

resultado = simpson(np.sin, inicio, fin, m)
print("Resultado de la aproximación:", resultado)
