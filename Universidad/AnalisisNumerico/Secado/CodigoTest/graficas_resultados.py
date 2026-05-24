# ============================================
# graficas_resultados.py
# VERSION FINAL CORREGIDA Y VERIFICADA
# ============================================

import numpy as np
import matplotlib.pyplot as plt

from parametros import *
from modelo_marquesina_capas import (
    t_horas,
    T_amb,
    U_capas,
    M_capas,
    M_bulk
)

# ============================================
# CONFIGURACIÓN GENERAL
# ============================================

plt.rcParams["figure.figsize"] = (10, 5)

plt.rcParams["axes.grid"] = True

plt.rcParams["font.size"] = 11

# ============================================
# TEMPERATURA AMBIENTE
# ============================================

plt.figure()

plt.plot(
    t_horas,
    T_amb - 273.15,
    linewidth=2
)

plt.xlabel("Tiempo [h]")

plt.ylabel("Temperatura [°C]")

plt.title(
    "Temperatura Ambiente Durante la Simulación"
)

plt.tight_layout()

plt.savefig(
    "temperatura.png",
    dpi=300
)

# ============================================
# ENERGÍA POR CAPAS
# ============================================

plt.figure()

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

plt.tight_layout()

plt.savefig(
    "energia_capas.png",
    dpi=300
)

# ============================================
# EVAPORACIÓN POR CAPAS
# ============================================

plt.figure()

for i in range(Nc):

    plt.plot(
        t_horas,
        M_capas[i],
        label=f"Capa {i+1}"
    )

plt.xlabel("Tiempo [h]")

plt.ylabel("Masa Evaporada [kg]")

plt.title(
    "Evaporación Acumulada por Capas"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "masa_capas.png",
    dpi=300
)

# ============================================
# HUMEDAD BULK
# ============================================

plt.figure()

plt.plot(
    t_horas,
    M_bulk,
    linewidth=2
)

plt.xlabel("Tiempo [h]")

plt.ylabel("Masa Promedio [kg]")

plt.title(
    "Humedad Bulk Promedio"
)

plt.tight_layout()

plt.savefig(
    "bulk.png",
    dpi=300
)

# ============================================
# COMPARACIÓN SUPERFICIE vs FONDO
# ============================================

plt.figure()

plt.plot(
    t_horas,
    M_capas[0],
    label="Capa Superior"
)

plt.plot(
    t_horas,
    M_capas[-1],
    label="Capa Inferior"
)

plt.xlabel("Tiempo [h]")

plt.ylabel("Masa Evaporada [kg]")

plt.title(
    "Comparación Superficie vs Fondo"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "comparacion_capas.png",
    dpi=300
)

# ============================================
# PERFIL TÉRMICO FINAL
# ============================================

plt.figure()

capas = np.arange(1, Nc + 1)

energia_final = [
    U_capas[i, -1]
    for i in range(Nc)
]

plt.plot(
    capas,
    energia_final,
    marker='o'
)

plt.xlabel("Número de Capa")

plt.ylabel("Energía Final [J]")

plt.title(
    "Perfil Energético Final por Capas"
)

plt.xticks(capas)

plt.tight_layout()

plt.savefig(
    "perfil_final.png",
    dpi=300
)

# ============================================
# RESUMEN FINAL
# ============================================

print("===================================")
print("GRÁFICAS GENERADAS CORRECTAMENTE")
print("===================================")

print("Archivos exportados:")

print("- temperatura.png")

print("- energia_capas.png")

print("- masa_capas.png")

print("- bulk.png")

print("- comparacion_capas.png")

print("- perfil_final.png")

print("===================================")

# ============================================
# MOSTRAR TODAS LAS FIGURAS
# ============================================

plt.show()