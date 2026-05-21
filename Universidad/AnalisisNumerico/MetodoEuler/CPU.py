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
# MODELO TEMPERATURA DEL CPU
#
# Variable : C(t) = temperatura del CPU (°C)
# Tiempo   : t en segundos
#
# EDO: dC/dt = -0.1·C + 0.8·t + 15
#   - El término -0.1·C modela la disipación de calor
#     (proporcional a la temperatura actual).
#   - El término +0.8·t modela el calor generado por
#     una carga de trabajo que crece con el tiempo.
#   - La constante +15 representa el calor base del
#     sistema en reposo (fuente ambiental).
#
# Condición inicial: C(0) = 40 °C (temperatura en reposo)
#
# Solución exacta (variación de parámetros):
#   C(t) = (C₀ - δ/γ + ε/γ - δ/γ²)·e^(-γt) + (δ/γ)·t + ε/γ - δ/γ²
# Con γ=0.1, δ=0.8, ε=15  →  simplificado:
#   C(t) = -30·e^(-0.1t) + 8t + 70
# =========================================================

GAMMA = 0.10   # coeficiente de disipación térmica  (1/s)
DELTA = 0.80   # tasa de calor por carga creciente   (°C/s²)
EPSILON = 15.0 # calor base del sistema              (°C/s)
C0 = 40.0      # temperatura inicial en reposo        (°C)

def f(t, C):
    return -GAMMA * C + DELTA * t + EPSILON

def exacta(t):
    # Coeficientes de la solución particular: at + b
    a = DELTA / GAMMA                          # =  8
    b = EPSILON / GAMMA - DELTA / GAMMA**2     # = 70
    A = C0 - b                                 # = -30
    return A * np.exp(-GAMMA * t) + a * t + b

# =========================================================
# SIMULACIONES
# =========================================================

T_FINAL = 60          # segundos de simulación

pasos = [5, 2.5, 1, 0.5, 0.1, 0.01]

plt.figure(figsize=(11, 6))

t_exacta = np.linspace(0, T_FINAL, 1000)
C_exacta = exacta(t_exacta)

plt.plot(t_exacta,
         C_exacta,
         linewidth=3,
         label='Solución exacta')

for h in pasos:

    t, C = euler(f, 0, C0, h, T_FINAL)

    error_abs = abs(exacta(T_FINAL) - C[-1])
    error_rel = 100 * error_abs / abs(exacta(T_FINAL))

    print(f"\n h = {h} s")
    print(f"C({T_FINAL}) Euler   = {C[-1]:.4f} °C")
    print(f"C({T_FINAL}) exacta  = {exacta(T_FINAL):.4f} °C")
    print(f"Error absoluto       = {error_abs:.4f} °C")
    print(f"Error relativo       = {error_rel:.2f}%")

    plt.plot(t, C, 'o--', label=f'Euler h={h}')

plt.xlabel('Tiempo (s)')
plt.ylabel('Temperatura CPU (°C)')

plt.title('Calentamiento del CPU usando Euler\n'
          r'$\frac{dC}{dt} = -0.1C + 0.8t + 15$,  $C(0) = 40$ °C')

plt.grid(True)
plt.legend()

plt.show()
