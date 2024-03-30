"""
Ejercicio:
El flujo de calor q es la cantidad de calor que fluye a través
de una unidad de área de cierto material por unidad de tiempo. Se
calcula con la ley de Fourier: J = -k  dT/dx  donde J está en unidades de J/m2
/s o W/m2
, y k es un coeficiente de la conductividad térmica que parametriza las propiedades conductoras
de calor del material y se expresa en unidades de W/(°C · m). T =
temperatura (°C); y x = distancia (m) a lo largo de la trayectoria del
flujo de calor. La ley de Fourier la emplean en forma rutinaria los ingenieros arquitectos
para determinar el flujo de calor a través de las paredes. Se midieron las temperaturas
siguientes a partir de la superficie (x = 0) de una pared de piedra:
    x, m       0      0.08    0.16
    T, °C      20     17      15

Si el flujo en x = 0 es de 60 W/m2, calcule el valor de k.
"""

# Datos proporcionados
x_values = [0, 0.08, 0.16]  # Posiciones (m)
T_values = [20, 17, 15]      # Temperaturas (°C)
flux_at_x0 = 60              # Flujo de calor en x = 0 (W/m^2)

# ...

# Cambiar el nombre de la función
def calculate_k_values(x_values, T_values, flux_at_x):
    h = x_values[1] - x_values[0]  # Tamaño del paso
    k_values = []  # Lista para almacenar los valores de k

    for i in range(len(T_values)):
        # Caso especial para el primer y último punto
        if i == 0:
            dT_dx = (T_values[i + 1] - T_values[i]) / (x_values[i + 1] - x_values[i])
        elif i == len(T_values) - 1:
            dT_dx = (T_values[i] - T_values[i - 1]) / (x_values[i] - x_values[i - 1])
        else:
            dT_dx = (T_values[i + 1] - T_values[i - 1]) / (x_values[i + 1] - x_values[i - 1])

        # Calcular el valor de k y almacenarlo en la lista
        k_values.append(-flux_at_x / dT_dx)

    return k_values

# Calcular los valores de k para cada intervalo
k_values = calculate_k_values(x_values, T_values, flux_at_x0)

# Imprimir la tabla de resultados
print("Intervalo  | Valor de k (W/(°C · m))")
print("----------------------------------")
for i in range(len(k_values)):
    print(f"Intervalo {i + 1} | {k_values[i]}")
