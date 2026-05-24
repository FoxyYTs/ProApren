# ============================================
# parametros.py
# ============================================

import numpy as np

# ============================================
# PARÁMETROS GEOMÉTRICOS DEL GRANO
# ============================================

# Semieje mayor del grano [m]
a = 0.0055

# Semieje menor del grano [m]
b = 0.0042

# Excentricidad geométrica
e = np.sqrt(1 - (b**2 / a**2))

# Volumen del grano [m^3]
Vg = (4/3) * np.pi * a * b**2

# ============================================
# PARÁMETROS TÉRMICOS
# ============================================

# Coeficiente convectivo [W/(m²·K)]
hc = 15

# Conductividad térmica del aire [W/(m·K)]
k_air = 0.026

# Longitud característica [m]
Lc = 0.01

# Número de Nusselt
Nu = (hc * Lc) / k_air

# Calor latente de evaporación [J/kg]
lambda_evap = 2.26e6

# Constante empírica del sistema
Cq = 0.85

# Factor correctivo evaporativo
gamma_e = 0.65

# ============================================
# PARÁMETROS DE LA MARQUESINA
# ============================================

# Longitud de la marquesina [m]
L = 10

# Ancho de la marquesina [m]
W = 4

# Profundidad de la cama de café [m]
pc = 0.04

# Número de capas
Nc = 5

# Factor de empaquetamiento
eta = 0.64

# Coeficiente de extinción térmica
k_ext = 18

# ============================================
# PARÁMETROS TEMPORALES
# ============================================

# Simulación de 7 días
dias = 7

# Horas totales
horas_totales = dias * 24

# Tiempo total en segundos
t_total = horas_totales * 3600

# Paso temporal [s]
dt = 60

# Vector de tiempo
t = np.arange(0, t_total + dt, dt)

# ============================================
# TEMPERATURA AMBIENTE
# ============================================

# Temperatura promedio [K]
Ta = 293.15

# Amplitud térmica [K]
A_temp = 8

# Frecuencia angular día/noche
omega = 2 * np.pi / (24 * 3600)

# Desfase temporal
t_a = 6 * 3600

# Función térmica ambiental
def temperatura_ambiente(t):

    return Ta + A_temp * np.sin(
        omega * (t - t_a)
    )

# ============================================
# PRESIÓN DE VAPOR
# ============================================

def presion_vapor(T):

    """
    Presión de vapor aproximada
    usando Antoine simplificada.
    """

    T_celsius = T - 273.15

    return 610.78 * np.exp(
        (17.27 * T_celsius) /
        (T_celsius + 237.3)
    )

# ============================================
# CONDICIONES INICIALES
# ============================================

# Energía interna inicial [J]
U0 = 0

# Masa evaporada inicial [kg]
m0 = 0

# Temperatura inicial [K]
T0 = 288.15

# ============================================
# NÚMERO TOTAL DE GRANOS
# ============================================

N_granos = int(
    (L * W * pc * eta) / Vg
)

# ============================================
# PROFUNDIDAD DE CAPAS
# ============================================

z = np.array([
    ((i + 0.5) * pc / Nc)
    for i in range(Nc)
])

# Factores de atenuación térmica
f_capas = np.exp(-k_ext * z)

# ============================================
# IMPRESIÓN DE CONTROL
# ============================================

print("====================================")
print("PARÁMETROS DEL MODELO")
print("====================================")

print(f"Número total de granos: {N_granos:,}")
print(f"Número de capas: {Nc}")
print(f"Tiempo total: {dias} días")
print(f"Paso temporal: {dt} s")
print(f"Número de pasos: {len(t)}")

print("====================================")