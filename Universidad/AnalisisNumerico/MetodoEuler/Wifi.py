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
# MODELO WIFI
# =========================================================

def f(d, P):
    return -0.5 * P - 0.1 * d

# Solución exacta
def exacta(d):

    return np.exp(-0.5*d)*(100 + 0.2*d + 0.04) \
           - 0.2*d - 0.04

# =========================================================
# SIMULACIONES
# =========================================================

pasos = [5, 2.5, 1, 0.5, 0.1, 0.01]

plt.figure(figsize=(11,6))

d_exacta = np.linspace(0, 50, 1000)
P_exacta = exacta(d_exacta)

plt.plot(d_exacta,
         P_exacta,
         linewidth=3,
         label='Solución exacta')

for h in pasos:

    d, P = euler(f, 0, 100, h, 50)

    error_abs = abs(exacta(50) - P[-1])
    error_rel = 100 * error_abs / abs(exacta(50))

    print(f"\n h = {h}")
    print(f"P(50) Euler = {P[-1]:.4f} dBm")
    print(f"Error absoluto = {error_abs:.4f}")
    print(f"Error relativo = {error_rel:.2f}%")

    plt.plot(d, P, 'o--',
             label=f'Euler h={h}')

plt.xlabel('Distancia (m)')
plt.ylabel('Potencia WiFi (dBm)')

plt.title('Atenuación WiFi usando Euler')

plt.grid(True)
plt.legend()

plt.show()