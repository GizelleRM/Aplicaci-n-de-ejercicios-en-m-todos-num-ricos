import numpy as np

def is_diagonally_dominant(A):
    # Verifica si la matriz A es diagonalmente dominante
    
    diagonal = np.abs(A.diagonal())
    row_sums = np.sum(np.abs(A), axis=1) - diagonal
    
    return np.all(diagonal >= row_sums)

def jacobi_method(A, b, max_iterations=100, tolerance=1e-8):
    n = len(A)
    x = np.zeros(n)

    if not is_diagonally_dominant(A):
        raise ValueError("La matriz no es diagonalmente dominante. El método de Jacobi puede no converger.")

    for k in range(max_iterations):
        x_new = np.zeros(n)
        
        for i in range(n):
            sigma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i, i]

        if np.sqrt(np.sum((x_new - x)**2)) < tolerance:
            print(f"Convergencia alcanzada en la iteración {k + 1}.")
            break

        x = x_new.copy()

    return x_new

# Matriz de coeficientes A y vector del lado derecho b
A = np.array([[4, -1, 0,0], [-1, 4, -1,0], [0, -1, 4,-1],[0, 0, -1, 3]])
b = np.array([15, 10, 10,10])

print("Matriz de coeficientes A:")
print(A)
print("\nVector del lado derecho b:")
print(b)

if is_diagonally_dominant(A):
    solution = jacobi_method(A, b)
    print("\nSolución del sistema de ecuaciones:")
    print(solution)
else:
    print("\nLa matriz no es diagonalmente dominante. El método de Jacobi puede no converger.")
