# ============================================
# estructura_3D.py
# VERSION FINAL CORREGIDA Y VERIFICADA
# ============================================

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

from parametros import *

# ============================================
# GEOMETRÍA DE LA MARQUESINA
# ============================================

# Dimensiones
longitud = L
ancho = W
profundidad = pc

# ============================================
# MALLA 3D
# ============================================

x = np.linspace(0, longitud, 40)

y = np.linspace(0, ancho, 20)

X, Y = np.meshgrid(x, y)

# ============================================
# SUPERFICIES DE CAPAS
# ============================================

capas_z = []

for i in range(Nc):

    z_i = -(
        (i + 1)
        * profundidad
        / Nc
    )

    Z = np.full_like(X, z_i)

    capas_z.append(Z)

# ============================================
# FIGURA 3D
# ============================================

fig = plt.figure(figsize=(12, 7))

ax = fig.add_subplot(
    111,
    projection='3d'
)

# ============================================
# DIBUJAR CAPAS
# ============================================

for i in range(Nc):

    ax.plot_surface(
        X,
        Y,
        capas_z[i],
        alpha=0.55
    )

# ============================================
# SUPERFICIE SUPERIOR
# ============================================

Z_superior = np.zeros_like(X)

ax.plot_surface(
    X,
    Y,
    Z_superior,
    alpha=0.35
)

# ============================================
# CONFIGURACIÓN
# ============================================

ax.set_xlabel("Longitud [m]")

ax.set_ylabel("Ancho [m]")

ax.set_zlabel("Profundidad [m]")

ax.set_title(
    "Modelo 3D de la Marquesina por Capas"
)

# ============================================
# AJUSTE VISUAL
# ============================================

ax.view_init(
    elev=28,
    azim=-60
)

# límites
ax.set_xlim(0, longitud)

ax.set_ylim(0, ancho)

ax.set_zlim(-profundidad, 0)

# ============================================
# GUARDAR FIGURA
# ============================================

plt.tight_layout()

plt.savefig(
    "estructura_3D.png",
    dpi=300
)

# ============================================
# RESULTADOS
# ============================================

print("===================================")
print("MODELO 3D GENERADO")
print("===================================")

print(
    f"Dimensiones: "
    f"{longitud}m x {ancho}m"
)

print(
    f"Número de capas: {Nc}"
)

print(
    f"Profundidad total: "
    f"{profundidad} m"
)

print("===================================")

# ============================================
# MOSTRAR FIGURA
# ============================================

plt.show()