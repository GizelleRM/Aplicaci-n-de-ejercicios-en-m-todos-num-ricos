import numpy as np

def verifica_matriz(A):
    try:
        cholesky_manual(A)
        return True
    except ValueError:
        return False

def cholesky_manual(A):
    # Devuelve L, la matriz triangular inferior.

    # Verifica si la diagonal principal de A es diferente de 0
    if not all(np.diagonal(A)):
        raise ValueError("La diagonal principal de la matriz debe ser diferente de 0.")

    # Verifica si A es simétrica
    if not np.all(A == A.T):
        raise ValueError("La matriz debe ser simétrica.")

    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                # Calcula la suma de los cuadrados de los elementos anteriores en la fila
                suma_l = sum(L[i, k] ** 2 for k in range(j))
                suma_u = sum(U[j, k] ** 2 for k in range(j))
                # Calcula el elemento diagonal de L y U
                L[i, j] = np.sqrt(A[i, i] - suma_l)
                U[j, i] = np.sqrt(A[i, i] - suma_u)
            else:
                # Calcula la suma de los productos de elementos anteriores en las filas correspondientes
                suma_l = sum(L[i, k] * L[j, k] for k in range(j))
                suma_u = sum(U[j, k] * U[i, k] for k in range(j))
                # Calcula el elemento fuera de la diagonal de L y U
                L[i, j] = (A[i, j] - suma_l) / L[j, j]
                U[j, i] = (A[i, j] - suma_u) / U[j, j]

    return L, U

def get_matrix_size():
    # Función para obtener el tamaño de la matriz del usuario
    while True:
        try:
            size = 3
            if size == 3 or size == 4:
                return size
            else:
                print("Por favor, ingrese un tamaño válido (3 o 4).")
        except ValueError:
            print("Por favor, ingrese un número entero.")

# Obtener el tamaño de la matriz del usuario
matrix_size = get_matrix_size()

# Crear una matriz de ejemplo según el tamaño seleccionado
if matrix_size == 3:
    A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
elif matrix_size == 4:
    A = np.array([[18, 22, 54, 42], [22, 70, 86, 62], [54, 86, 174, 134], [42, 62, 134, 106]])

# Verificar si A es simétrica y definida positiva antes de aplicar Cholesky
if np.all(A == A.T) and np.all(np.linalg.eigvals(A) > 0):
    try:
        L, U = cholesky_manual(A)
        print("\nMatriz original:")
        print(A)
        print("\nMatriz triangular inferior (L) de Cholesky:")
        print(L)
        print("\nMatriz triangular superior (U) de Cholesky:")
        print(U)
    except ValueError as e:
        print(f"Error: {e}")
else:
    print("La matriz no cumple con las condiciones para la descomposición de Cholesky.")
