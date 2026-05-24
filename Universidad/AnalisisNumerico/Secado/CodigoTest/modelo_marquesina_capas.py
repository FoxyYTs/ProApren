# ============================================
# modelo_marquesina_capas.py
# VERSION FINAL CORREGIDA Y ESTABLE
# ============================================

import numpy as np
import matplotlib.pyplot as plt

from parametros import *

# ============================================
# PARÁMETROS DEL MODELO
# ============================================

# disipación térmica
beta = 0.002

# evaporación ajustada
alpha = 0.08

# ============================================
# VARIABLES
# ============================================

N_tiempo = len(t)

# energía por capa
U_capas = np.zeros((Nc, N_tiempo))

# masa evaporada por capa
M_capas = np.zeros((Nc, N_tiempo))

# temperatura ambiente
T_amb = np.zeros(N_tiempo)

# humedad bulk promedio
M_bulk = np.zeros(N_tiempo)

# ============================================
# FUNCIÓN DE FLUJO DE CALOR
# ============================================

def flujo_calor(T, f):

    """
    Flujo térmico por capa.
    """

    Tc = T - 273.15

    # presión simplificada estable
    P = 1 + 0.03 * Tc

    Q = (
        Cq
        * hc
        * P
        * f
    )

    return Q

# ============================================
# ECUACIONES DIFERENCIALES
# ============================================

def dUdt(U, T, f):

    Qin = flujo_calor(T, f)

    Qloss = beta * U

    return Qin - Qloss

def dmdt(T, f):

    return (
        alpha
        * flujo_calor(T, f)
        / lambda_evap
    )

# ============================================
# CONDICIONES INICIALES
# ============================================

U_capas[:, 0] = U0

M_capas[:, 0] = m0

# ============================================
# SIMULACIÓN RK4
# ============================================

for n in range(N_tiempo - 1):

    # temperatura ambiente
    T1 = temperatura_ambiente(t[n])

    T2 = temperatura_ambiente(
        t[n] + dt/2
    )

    T3 = T2

    T4 = temperatura_ambiente(
        t[n] + dt
    )

    T_amb[n] = T1

    # ========================================
    # CAPAS
    # ========================================

    for i in range(Nc):

        # atenuación térmica
        f = f_capas[i]

        # ====================================
        # ENERGÍA RK4
        # ====================================

        k1U = dt * dUdt(
            U_capas[i, n],
            T1,
            f
        )

        k2U = dt * dUdt(
            U_capas[i, n] + k1U/2,
            T2,
            f
        )

        k3U = dt * dUdt(
            U_capas[i, n] + k2U/2,
            T3,
            f
        )

        k4U = dt * dUdt(
            U_capas[i, n] + k3U,
            T4,
            f
        )

        U_capas[i, n+1] = (
            U_capas[i, n]
            +
            (
                k1U
                + 2*k2U
                + 2*k3U
                + k4U
            ) / 6
        )

        # ====================================
        # MASA EVAPORADA RK4
        # ====================================

        k1M = dt * dmdt(T1, f)

        k2M = dt * dmdt(T2, f)

        k3M = dt * dmdt(T3, f)

        k4M = dt * dmdt(T4, f)

        M_capas[i, n+1] = (
            M_capas[i, n]
            +
            (
                k1M
                + 2*k2M
                + 2*k3M
                + k4M
            ) / 6
        )

    # ========================================
    # HUMEDAD BULK PROMEDIO
    # ========================================

    M_bulk[n] = np.mean(
        M_capas[:, n]
    )

# última temperatura
T_amb[-1] = temperatura_ambiente(
    t[-1]
)

# último bulk
M_bulk[-1] = np.mean(
    M_capas[:, -1]
)

# ============================================
# TIEMPO EN HORAS
# ============================================

t_horas = t / 3600

# ============================================
# TEMPERATURA AMBIENTE
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
# ENERGÍA POR CAPAS
# ============================================

plt.figure(figsize=(10,5))

for i in range(Nc):

    plt.plot(
        t_horas,
        U_capas[i],
        label=f"Capa {i+1}"
    )

plt.xlabel("Tiempo [h]")

plt.ylabel("Energía [J]")

plt.title(
    "Energía Interna por Capas"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "energia_capas.png",
    dpi=300
)

# ============================================
# MASA EVAPORADA POR CAPAS
# ============================================

plt.figure(figsize=(10,5))

for i in range(Nc):

    plt.plot(
        t_horas,
        M_capas[i],
        label=f"Capa {i+1}"
    )

plt.xlabel("Tiempo [h]")

plt.ylabel("Masa Evaporada [kg]")

plt.title(
    "Evaporación por Capas"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "masa_capas.png",
    dpi=300
)

# ============================================
# HUMEDAD BULK
# ============================================

plt.figure(figsize=(10,4))

plt.plot(
    t_horas,
    M_bulk
)

plt.xlabel("Tiempo [h]")

plt.ylabel("Masa Promedio [kg]")

plt.title(
    "Humedad Bulk Promedio"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "bulk.png",
    dpi=300
)

# ============================================
# RESULTADOS
# ============================================

print("===================================")
print("SIMULACIÓN MARQUESINA COMPLETA")
print("===================================")

print(
    f"Número total de granos: "
    f"{N_granos:,}"
)

print(
    f"Humedad bulk final: "
    f"{M_bulk[-1]:.6f} kg"
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