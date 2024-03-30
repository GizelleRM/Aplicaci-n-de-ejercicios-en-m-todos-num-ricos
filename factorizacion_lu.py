import numpy as np

def lu_factorization(A):
    """
    Factorización LU de una matriz A en L y U.

    :param A: La matriz a factorizar.
    :return: Matrices L y U.
    """
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))

    for k in range(n):
        # Calcula los elementos de U
        for j in range(k, n):
            U[k, j] = A[k, j] - np.dot(L[k, :k], U[:k, j])

        # Calcula los elementos de L
        for i in range(k + 1, n):
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]

    return L, U

# Ejemplo de uso:
A = np.array([[2, -1, 1],
              [1, 3, 2],
              [3, 2, -2]])

L, U = lu_factorization(A)

print("Matriz original A:")
print(A)

print("\nMatriz L:")
print(L)

print("\nMatriz U:")
print(U)
