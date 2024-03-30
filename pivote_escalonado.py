import numpy as np

def elimination_with_partial_pivoting(A, b):
    n = len(b)
    # Combinar la matriz A y el vector b en una sola matriz aumentada
    augmented_matrix = np.concatenate((A.astype(float), b.reshape(-1, 1).astype(float)), axis=1)

    print("Matriz aumentada:")
    print(augmented_matrix)

    for i in range(n):
        # Encontrar el índice del máximo elemento en la columna actual (pivote parcial)
        max_row_index = np.argmax(np.abs(augmented_matrix[i:, i])) + i

        # Intercambiar filas para realizar el pivoteo parcial
        augmented_matrix[[i, max_row_index]] = augmented_matrix[[max_row_index, i]]

        # Eliminación gaussiana
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    # Sustitución hacia atrás para encontrar la solución
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] / augmented_matrix[i, i]
        for j in range(i - 1, -1, -1):
            augmented_matrix[j, -1] -= augmented_matrix[j, i] * x[i]

    print("\nSolución del sistema de ecuaciones lineales:")
    print(x)

# Permitir al usuario elegir el tamaño de la matriz
matrix_size = 4

if matrix_size == 3:
    A = np.array([  [2, -1, 1],
                    [1, 3, 2],
                    [3, 2, -2]])
elif matrix_size == 4:
    A = np.array([  [2, -1, 1, 3],
                    [1, 3, 2, 1],
                    [3, 2, -2, 2],
                    [4, 5, 7, 1]])
else:
    print("Tamaño de matriz no válido. Debe ser 3 o 4.")
    exit()

b = np.array([8, 13, 1]) if matrix_size == 3 else np.array([10, 12, 3, 5])

elimination_with_partial_pivoting(A, b)
