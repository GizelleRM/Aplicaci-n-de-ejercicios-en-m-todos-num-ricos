import numpy as np

def doolittle_factorization(A):
    """
    Factorización de Doolittle de una matriz A en L y U.

    :param A: La matriz a factorizar.
    :return: Matrices L y U.
    """
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        # Calcular elementos de U
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        # Calcular elementos de L
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    return L, U

# Ejemplo de uso:
A = np.array([[2, -1, 1],
              [1, 3, 2],
              [3, 2, -2]])

L, U = doolittle_factorization(A)

print("Matriz original A:")
print(A)

print("\nMatriz L:")
print(L)

print("\nMatriz U:")
print(U)
