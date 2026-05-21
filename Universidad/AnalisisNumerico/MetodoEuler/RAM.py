import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# MÉTODO DE EULER
# =========================================================

def euler(f, x0, y0, h, xf):

    N = int((xf - x0) / h)

    x = np.zeros(N + 1)
    y = np.zeros(N + 1)

    x[0] = x0
    y[0] = y0

    for i in range(N):

        x[i+1] = x[i] + h
        y[i+1] = y[i] + h * f(x[i], y[i])

    return x, y

# =========================================================
# MODELO RAM LIBRE DISPONIBLE
#
# Variable : R(t) = RAM libre disponible (GB)
# Tiempo   : t en minutos
#
# EDO: dR/dt = -0.05·R - 0.1·t
#   - El término -0.05·R modela el consumo proporcional
#     a la memoria actualmente libre (presión de procesos).
#   - El término -0.1·t modela una carga creciente con
#     el tiempo (más tareas se acumulan).
#
# Condición inicial: R(0) = 16 GB (RAM libre total)
#
# Solución exacta (variación de parámetros):
#   R(t) = (R₀ - β/α²)·e^(-α·t) - (β/α)·t + β/α²
# Con α=0.05, β=0.1:
#   R(t) = -24·e^(-0.05t) - 2t + 40
# =========================================================

ALPHA = 0.05   # tasa de consumo proporcional  (1/min)
BETA  = 0.10   # tasa de carga creciente        (GB/min²)
R0    = 16.0   # RAM libre inicial              (GB)

def f(t, R):
    return -ALPHA * R - BETA * t

def exacta(t):
    return (R0 - BETA / ALPHA**2) * np.exp(-ALPHA * t) \
           - (BETA / ALPHA) * t \
           + BETA / ALPHA**2

# =========================================================
# SIMULACIONES
# =========================================================

T_FINAL = 14          # minutos antes de agotar la RAM

pasos = [5, 2.5, 1, 0.5, 0.1, 0.01]

plt.figure(figsize=(11, 6))

t_exacta = np.linspace(0, T_FINAL, 1000)
R_exacta = exacta(t_exacta)

plt.plot(t_exacta,
         R_exacta,
         linewidth=3,
         label='Solución exacta')

for h in pasos:

    t, R = euler(f, 0, R0, h, T_FINAL)

    error_abs = abs(exacta(T_FINAL) - R[-1])
    error_rel = 100 * error_abs / abs(exacta(T_FINAL))

    print(f"\n h = {h} min")
    print(f"R({T_FINAL}) Euler   = {R[-1]:.4f} GB")
    print(f"R({T_FINAL}) exacta  = {exacta(T_FINAL):.4f} GB")
    print(f"Error absoluto       = {error_abs:.4f} GB")
    print(f"Error relativo       = {error_rel:.2f}%")

    plt.plot(t, R, 'o--', label=f'Euler h={h}')

plt.xlabel('Tiempo (min)')
plt.ylabel('RAM libre disponible (GB)')

plt.title('Consumo de RAM libre usando Euler\n'
          r'$\frac{dR}{dt} = -0.05R - 0.1t$,  $R(0) = 16$ GB')

plt.grid(True)
plt.legend()

plt.show()
