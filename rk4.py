import numpy as np
import matplotlib.pyplot as plt

def system_equations(t, u):
    """ sistema de ecuaciones."""
    u1, u2 = u
    du1dt = u2
    du2dt = 2*u2 - 2*u1 + np.exp(t/2) * np.sin(t)
    return np.array([du1dt, du2dt])

def runge_kutta_4th_order(t, u, h, system_equations):
    k1 = h * system_equations(t, u)
    k2 = h * system_equations(t + h/2, u + k1/2)
    k3 = h * system_equations(t + h/2, u + k2/2)
    k4 = h * system_equations(t + h, u + k3)
    
    u_next = u + (k1 + 2*k2 + 2*k3 + k4) / 6
    t_next = t + h
    
    return t_next, u_next

# Parámetros iniciales
t0 = 0
u0 = np.array([0, 1])  
h = 1/100  # Tamaño del paso de tiempo b-a /n 
num_steps = int(10/h)

# Listas para almacenar los resultados
t_values = [t0]
u_values = [u0]

# Iteración con RK4 para el sistema de ecuaciones
for _ in range(num_steps):
    t0, u0 = runge_kutta_4th_order(t0, u0, h, system_equations)
    t_values.append(t0)
    u_values.append(u0)

# Convertir los resultados a una matriz numpy para facilitar el acceso a las componentes y y y'
u_values = np.array(u_values)

# Graficar los resultados
plt.plot(t_values, u_values[:, 0], label='y(t)')
plt.plot(t_values, u_values[:, 1], label="y'(t)")
plt.title("Solución del sistema de ecuaciones diferenciales")
plt.xlabel("")
plt.legend()
plt.show()
