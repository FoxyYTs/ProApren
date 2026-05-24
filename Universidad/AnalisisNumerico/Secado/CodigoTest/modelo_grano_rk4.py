# ============================================
# modelo_grano_rk4.py
# VERSION FINAL ESTABLE Y CORREGIDA
# ============================================

import numpy as np
import matplotlib.pyplot as plt

from parametros import *

# ============================================
# PARÁMETROS AJUSTADOS
# ============================================

# disipación térmica
beta = 0.002

# ajuste evaporativo
alpha = 0.08

# ============================================
# FUNCIÓN DE FLUJO DE CALOR
# ============================================

def flujo_calor(T):

    """
    Flujo térmico corregido y estable.
    """

    # temperatura en °C
    Tc = T - 273.15

    # presión simplificada estable
    P = 1 + 0.03 * Tc

    # flujo térmico
    Q = (
        Cq
        * hc
        * P
    )

    return Q

# ============================================
# ECUACIÓN DE ENERGÍA
# ============================================

def dUdt(U, T):

    Qin = flujo_calor(T)

    # disipación térmica
    Qloss = beta * U

    return Qin - Qloss

# ============================================
# ECUACIÓN DE EVAPORACIÓN
# ============================================

def dmdt(T):

    return (
        alpha
        * flujo_calor(T)
        / lambda_evap
    )

# ============================================
# VARIABLES
# ============================================

N = len(t)

U = np.zeros(N)

m_evap = np.zeros(N)

T_amb = np.zeros(N)

# ============================================
# CONDICIONES INICIALES
# ============================================

U[0] = U0

m_evap[0] = m0

# ============================================
# MÉTODO RK4
# ============================================

for i in range(N - 1):

    # ========================================
    # TEMPERATURA AMBIENTE
    # ========================================

    T1 = temperatura_ambiente(t[i])

    T2 = temperatura_ambiente(
        t[i] + dt/2
    )

    T3 = T2

    T4 = temperatura_ambiente(
        t[i] + dt
    )

    T_amb[i] = T1

    # ========================================
    # RK4 ENERGÍA
    # ========================================

    k1U = dt * dUdt(U[i], T1)

    k2U = dt * dUdt(
        U[i] + k1U/2,
        T2
    )

    k3U = dt * dUdt(
        U[i] + k2U/2,
        T3
    )

    k4U = dt * dUdt(
        U[i] + k3U,
        T4
    )

    U[i+1] = U[i] + (
        k1U
        + 2*k2U
        + 2*k3U
        + k4U
    ) / 6

    # ========================================
    # RK4 MASA EVAPORADA
    # ========================================

    k1m = dt * dmdt(T1)

    k2m = dt * dmdt(T2)

    k3m = dt * dmdt(T3)

    k4m = dt * dmdt(T4)

    m_evap[i+1] = m_evap[i] + (
        k1m
        + 2*k2m
        + 2*k3m
        + k4m
    ) / 6

# última temperatura
T_amb[-1] = temperatura_ambiente(
    t[-1]
)

# ============================================
# TIEMPO EN HORAS
# ============================================

t_horas = t / 3600

# ============================================
# TEMPERATURA
# ============================================

plt.figure(figsize=(10,4))

plt.plot(
    t_horas,
    T_amb - 273.15
)

plt.xlabel("Tiempo [h]")

plt.ylabel("Temperatura [°C]")

plt.title(
    "Temperatura Ambiente"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "temperatura.png",
    dpi=300
)

# ============================================
# ENERGÍA
# ============================================

plt.figure(figsize=(10,4))

plt.plot(
    t_horas,
    U
)

plt.xlabel("Tiempo [h]")

plt.ylabel("Energía Interna [J]")

plt.title(
    "Energía Interna del Sistema"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "energia.png",
    dpi=300
)

# ============================================
# MASA EVAPORADA
# ============================================

plt.figure(figsize=(10,4))

plt.plot(
    t_horas,
    m_evap
)

plt.xlabel("Tiempo [h]")

plt.ylabel("Masa Evaporada [kg]")

plt.title(
    "Masa Evaporada Acumulada"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "masa.png",
    dpi=300
)

# ============================================
# COMPARACIÓN
# ============================================

plt.figure(figsize=(10,4))

plt.plot(
    t_horas,
    U,
    label="RK4"
)

plt.xlabel("Tiempo [h]")

plt.ylabel("Energía [J]")

plt.title(
    "Comportamiento Energético"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "comparacion.png",
    dpi=300
)

# ============================================
# RESULTADOS
# ============================================

print("===================================")
print("SIMULACIÓN COMPLETADA")
print("===================================")

print(f"Energía final: {U[-1]:.2f} J")

print(
    f"Masa evaporada final: "
    f"{m_evap[-1]:.6f} kg"
)

print(
    f"Temperatura máxima: "
    f"{np.max(T_amb)-273.15:.2f} °C"
)

print(
    f"Temperatura mínima: "
    f"{np.min(T_amb)-273.15:.2f} °C"
)

print("===================================")

# ============================================
# MOSTRAR
# ============================================

plt.show()