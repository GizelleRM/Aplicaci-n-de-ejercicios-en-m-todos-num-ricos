"""La parte baja del río Colorado consiste en una serie de cuatro

almacenamientos como se ilustra en la figura P12.8. Pueden escri-
birse los balances de masa para cada uno de ellos, lo que da por re-
sultado el conjunto siguiente de ecuaciones algebraicas lineales

simultáneas:

donde el vector del lado derecho consiste en las cargas de cloruro

hacia cada uno de los cuatro lagos y c1, c2, c3 y c4 = las concentracio-
nes de cloruro resultantes en los lagos Powell, Mead, Mohave y

Havasu, respectivamente.
a) Use la matriz inversa para resolver cuáles son las concentraciones
en cada uno de los cuatro lagos.
b) ¿En cuánto debe reducirse la carga del lago Powell para que la
concentración de cloruro en el lago Havasu sea de 75?
c) Con el uso de la norma columna-suma, calcule el número de
condición y diga cuántos dígitos sospechosos se generarían al
resolver este sistema. """
import numpy as np

# Inciso a) Resolución del sistema de ecuaciones lineales
# Define la matriz de coeficientes A y el vector del lado derecho B
A = np.array([[13.422, 0, 0, 0],
              [-13.422, 12.252, 0, 0],
              [0, -12.252, 12.377, 0],
              [0, 0, -12.377, 11.767]])

B = np.array([750.5, 300, 102, 30])

# Resuelve el sistema de ecuaciones lineales usando la matriz inversa
concentrations = np.linalg.solve(A, B)

# Imprime las concentraciones en cada lago
print("a) Concentraciones en cada lago:", concentrations)


# Inciso c) Cálculo del número de condición y dígitos sospechosos
# Calcula el número de condición
condition_number = np.linalg.cond(A, p=np.inf)

print("c) Número de condición:", condition_number)

# Calcula la cantidad de dígitos sospechosos
digits_suspected = np(condition_number)

print("   Dígitos sospechosos:", digits_suspected)
