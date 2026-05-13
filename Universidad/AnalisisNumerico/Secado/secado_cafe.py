"""
Simulación Numérica del Proceso de Secado de Café
Método de Runge-Kutta de Cuarto Orden (RK4)

Autores:
    Jose Andres Daza Gallego
    Jose Miguel Calderon Castano
    Juan David Vega Canizares
    Valentina Sanchez Loaiza

Politécnico Colombiano Jaime Isaza Cadavid
Facultad de Ingeniería — Rionegro, Antioquia, Colombia
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import AutoMinorLocator

# ─────────────────────────────────────────────
# 1. PARÁMETROS DEL MODELO
# ─────────────────────────────────────────────

# Geometría del grano (esferoide prolato)
a = 0.0055          # Semieje mayor [m]
b = 0.0042          # Semieje menor [m]

# Propiedades térmicas
lambda_evap = 2.26e6    # Calor latente de evaporación [J/kg]
h_c         = 15.0      # Coeficiente convectivo [W/m²·K]
k_aire      = 0.0263    # Conductividad térmica del aire [W/m·K]
rho_cafe    = 1200.0    # Densidad del grano de café [kg/m³]

# Temperatura de referencia (condensador / ambiente base)
T_c = 293.15            # Temperatura de referencia [K] (~20 °C)

# Parámetros del flujo de calor
C_q    = 1.14e-7         # Constante del sistema [unidades adimensionales]
gamma_e = 0.85          # Factor de corrección evaporativa [-]

# Simulación temporal
h_step = 0.01           # Paso temporal [s]
t_ini  = 0.0            # Tiempo inicial [s]
t_fin  = 3600.0 * 8     # Tiempo final: 8 horas [s]

# Condiciones iniciales
U_e0     = 0.0          # Energía interna inicial [J]
m_evap0  = 0.0          # Masa evaporada inicial [kg]

# ─────────────────────────────────────────────
# 2. GEOMETRÍA DEL GRANO
# ─────────────────────────────────────────────

def geometria_grano(a, b):
    """Calcula volumen y área superficial del esferoide prolato."""
    e = np.sqrt(1 - (b**2 / a**2))          # Excentricidad
    V_g = (4/3) * np.pi * a * b**2          # Volumen [m³]
    A_g = 2*np.pi*b**2 + 2*np.pi*(a*b/e)*np.arcsin(e)  # Área superficial [m²]
    return V_g, A_g, e

V_g, A_g, e_exc = geometria_grano(a, b)

# Masa inicial del grano
m_grano_ini = rho_cafe * V_g

print("=" * 55)
print("  PARÁMETROS GEOMÉTRICOS DEL GRANO DE CAFÉ")
print("=" * 55)
print(f"  Semieje mayor (a)      : {a*1000:.2f} mm")
print(f"  Semieje menor (b)      : {b*1000:.2f} mm")
print(f"  Excentricidad (e)      : {e_exc:.4f}")
print(f"  Volumen (V_g)          : {V_g*1e9:.4f} mm³")
print(f"  Área superficial (A_g) : {A_g*1e6:.4f} mm²")
print(f"  Masa inicial del grano : {m_grano_ini*1000:.4f} g")
print("=" * 55)

# ─────────────────────────────────────────────
# 3. TEMPERATURA AMBIENTE VARIABLE (SENOIDAL)
# ─────────────────────────────────────────────

def temperatura_ambiente(t):
    """
    Temperatura ambiente con oscilación senoidal diaria.
    T_min ≈ 15°C (mañana), T_max ≈ 28°C (mediodía)
    Representativa de clima cafetero andino colombiano.
    """
    T_min_K = 288.15    # 15 °C en Kelvin
    T_max_K = 301.15    # 28 °C en Kelvin
    T_med   = (T_max_K + T_min_K) / 2.0
    amp     = (T_max_K - T_min_K) / 2.0
    omega   = 2 * np.pi / (3600 * 24)      # Frecuencia diaria [rad/s]
    phi     = -np.pi / 2                    # Mínimo al inicio (amanecer)
    return T_med + amp * np.sin(omega * t + phi)

# ─────────────────────────────────────────────
# 4. PRESIÓN DE VAPOR (Antoine simplificada)
# ─────────────────────────────────────────────

def presion_vapor(T_K):
    """
    Presión de vapor del agua usando ecuación de Antoine simplificada.
    Válida para T entre 60°C y 150°C (extrapolada aquí para el modelo).
    Retorna presión en [Pa].
    """
    T_C = T_K - 273.15
    # Constantes de Antoine para agua (log10, P en mmHg, T en °C)
    A, B, C = 8.07131, 1730.63, 233.426
    log_P_mmHg = A - B / (C + T_C)
    P_mmHg = 10 ** log_P_mmHg
    return P_mmHg * 133.322    # Conversión mmHg → Pa

# ─────────────────────────────────────────────
# 5. FLUJO DE CALOR INSTANTÁNEO
# ─────────────────────────────────────────────

def Q_punto(t):
    """
    Flujo de calor instantáneo asociado al proceso evaporativo.
    Basado en diferencia de presiones de vapor.
    """
    T_e = temperatura_ambiente(t)
    P_Tc = presion_vapor(T_c)
    P_Te = presion_vapor(T_e)
    return C_q * h_c * (P_Tc + gamma_e * P_Te)

# ─────────────────────────────────────────────
# 6. SISTEMA DE EDOs ACOPLADAS
# ─────────────────────────────────────────────

def f(t, x):
    """
    Sistema de ecuaciones diferenciales ordinarias acopladas.

    Estado: x = [U_e, m_evap]
        dx[0]/dt = dU_e/dt     = Q_punto(t)
        dx[1]/dt = dm_evap/dt  = Q_punto(t) / lambda_evap
    """
    Q = Q_punto(t)
    dUe_dt     = Q
    dmevap_dt  = Q / lambda_evap
    return np.array([dUe_dt, dmevap_dt])

# ─────────────────────────────────────────────
# 7. MÉTODO DE RUNGE-KUTTA 4 (RK4)
# ─────────────────────────────────────────────

def rk4_paso(f, t_n, x_n, h):
    """Un paso del método RK4."""
    k1 = h * f(t_n,           x_n)
    k2 = h * f(t_n + h/2,     x_n + k1/2)
    k3 = h * f(t_n + h/2,     x_n + k2/2)
    k4 = h * f(t_n + h,       x_n + k3)
    return x_n + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

# ─────────────────────────────────────────────
# 8. MÉTODO DE EULER (para comparación)
# ─────────────────────────────────────────────

def euler_paso(f, t_n, x_n, h):
    """Un paso del método de Euler explícito."""
    return x_n + h * f(t_n, x_n)

# ─────────────────────────────────────────────
# 9. INTEGRACIÓN NUMÉRICA
# ─────────────────────────────────────────────

t_vals  = np.arange(t_ini, t_fin + h_step, h_step)
N       = len(t_vals)

# Arrays de resultados — RK4
x_rk4       = np.zeros((N, 2))
x_rk4[0]    = [U_e0, m_evap0]

# Arrays de resultados — Euler
x_euler      = np.zeros((N, 2))
x_euler[0]   = [U_e0, m_evap0]

# Temperatura y flujo de calor en cada paso
T_amb_vals  = np.zeros(N)
Q_vals      = np.zeros(N)

T_amb_vals[0] = temperatura_ambiente(t_ini)
Q_vals[0]     = Q_punto(t_ini)

print("\n  Ejecutando integración numérica...")

for n in range(N - 1):
    t_n = t_vals[n]

    # RK4
    x_rk4[n+1]  = rk4_paso(f, t_n, x_rk4[n],  h_step)

    # Euler
    x_euler[n+1] = euler_paso(f, t_n, x_euler[n], h_step)

    # Temperatura y calor
    T_amb_vals[n+1] = temperatura_ambiente(t_vals[n+1])
    Q_vals[n+1]     = Q_punto(t_vals[n+1])

print("  Integración completada.\n")

# Conversión de unidades para visualización
t_horas = t_vals / 3600.0       # Tiempo en horas
T_amb_C = T_amb_vals - 273.15   # Temperatura en °C
U_e_rk4     = x_rk4[:, 0]      # Energía interna RK4 [J]
m_evap_rk4  = x_rk4[:, 1] * 1000  # Masa evaporada RK4 [g]
U_e_euler   = x_euler[:, 0]
m_evap_euler = x_euler[:, 1] * 1000

# Mostrar resultados finales
print("=" * 55)
print("  RESULTADOS FINALES DE LA SIMULACIÓN")
print("=" * 55)
print(f"  Tiempo total simulado       : {t_fin/3600:.1f} horas")
print(f"  Temperatura mínima ambiente : {T_amb_C.min():.2f} °C")
print(f"  Temperatura máxima ambiente : {T_amb_C.max():.2f} °C")
print(f"  Energía interna final (RK4) : {U_e_rk4[-1]:.4f} J")
print(f"  Masa evaporada final (RK4)  : {m_evap_rk4[-1]:.6f} g")
print(f"  Masa evaporada / masa total : {(m_evap_rk4[-1]/1000)/m_grano_ini*100:.4f} %")
print(f"  Error RK4 vs Euler (masa)   : {abs(m_evap_rk4[-1]-m_evap_euler[-1]):.2e} g")
print("=" * 55)

# ─────────────────────────────────────────────
# 10. VISUALIZACIÓN — ESTILO PAPER IEEE
# ─────────────────────────────────────────────

plt.rcParams.update({
    'font.family'      : 'serif',
    'font.size'        : 11,
    'axes.titlesize'   : 11,
    'axes.labelsize'   : 11,
    'xtick.labelsize'  : 10,
    'ytick.labelsize'  : 10,
    'legend.fontsize'  : 10,
    'figure.dpi'       : 300,
    'savefig.dpi'      : 300,
    'savefig.bbox'     : 'tight',
    'lines.linewidth'  : 1.5,
    'axes.grid'        : True,
    'grid.alpha'       : 0.3,
    'grid.linestyle'   : '--',
})

COLOR_RK4   = '#1a5276'   # Azul oscuro
COLOR_EULER = '#c0392b'   # Rojo
COLOR_TEMP  = '#117a65'   # Verde oscuro

# ── Figura 1: Temperatura ambiente ──────────────────────────────────
fig1, ax1 = plt.subplots(figsize=(5, 3.2))
ax1.plot(t_horas, T_amb_C, color=COLOR_TEMP, linewidth=1.8)
ax1.set_xlabel('Tiempo (h)')
ax1.set_ylabel('Temperatura (°C)')
ax1.set_title('Temperatura ambiente durante la simulación')
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax1.set_xlim([0, t_fin/3600])
plt.tight_layout()
plt.savefig('./temperatura.png')
plt.close()
print("  [✓] temperatura.png guardada")

# ── Figura 2: Energía interna ────────────────────────────────────────
fig2, ax2 = plt.subplots(figsize=(5, 3.2))
ax2.plot(t_horas, U_e_rk4, color=COLOR_RK4, linewidth=1.8)
ax2.set_xlabel('Tiempo (h)')
ax2.set_ylabel('Energía interna $U_e$ (J)')
ax2.set_title('Evolución temporal de la energía interna')
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax2.set_xlim([0, t_fin/3600])
plt.tight_layout()
plt.savefig('./energia.png')
plt.close()
print("  [✓] energia.png guardada")

# ── Figura 3: Masa evaporada ─────────────────────────────────────────
fig3, ax3 = plt.subplots(figsize=(5, 3.2))
ax3.plot(t_horas, m_evap_rk4, color=COLOR_RK4, linewidth=1.8)
ax3.set_xlabel('Tiempo (h)')
ax3.set_ylabel('Masa evaporada acumulada (g)')
ax3.set_title('Masa evaporada acumulada durante el secado')
ax3.xaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())
ax3.set_xlim([0, t_fin/3600])
plt.tight_layout()
plt.savefig('./masa.png')
plt.close()
print("  [✓] masa.png guardada")

# ── Figura 4: RK4 — Energía interna y Masa evaporada ─────────────────
fig4, axes4 = plt.subplots(1, 2, figsize=(9, 3.5))

axes4[0].plot(t_horas, U_e_rk4, color=COLOR_RK4, linewidth=1.8)
axes4[0].set_xlabel('Tiempo (h)')
axes4[0].set_ylabel('Energía interna $U_e$ (J)')
axes4[0].set_title('Energía interna — RK4')
axes4[0].xaxis.set_minor_locator(AutoMinorLocator())
axes4[0].yaxis.set_minor_locator(AutoMinorLocator())
axes4[0].set_xlim([0, t_fin/3600])

axes4[1].plot(t_horas, m_evap_rk4, color=COLOR_RK4, linewidth=1.8)
axes4[1].set_xlabel('Tiempo (h)')
axes4[1].set_ylabel('Masa evaporada acumulada (g)')
axes4[1].set_title('Masa evaporada — RK4')
axes4[1].xaxis.set_minor_locator(AutoMinorLocator())
axes4[1].yaxis.set_minor_locator(AutoMinorLocator())
axes4[1].set_xlim([0, t_fin/3600])

fig4.suptitle('Resultados — Método RK4', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('./comparacion_rk4.png')
plt.close()
print("  [✓] comparacion_rk4.png guardada")

# ── Figura 5: Euler — Energía interna y Masa evaporada ───────────────
fig5, axes5 = plt.subplots(1, 2, figsize=(9, 3.5))

axes5[0].plot(t_horas, U_e_euler, color=COLOR_EULER, linewidth=1.8, linestyle='--')
axes5[0].set_xlabel('Tiempo (h)')
axes5[0].set_ylabel('Energía interna $U_e$ (J)')
axes5[0].set_title('Energía interna — Euler')
axes5[0].xaxis.set_minor_locator(AutoMinorLocator())
axes5[0].yaxis.set_minor_locator(AutoMinorLocator())
axes5[0].set_xlim([0, t_fin/3600])

axes5[1].plot(t_horas, m_evap_euler, color=COLOR_EULER, linewidth=1.8, linestyle='--')
axes5[1].set_xlabel('Tiempo (h)')
axes5[1].set_ylabel('Masa evaporada acumulada (g)')
axes5[1].set_title('Masa evaporada — Euler')
axes5[1].xaxis.set_minor_locator(AutoMinorLocator())
axes5[1].yaxis.set_minor_locator(AutoMinorLocator())
axes5[1].set_xlim([0, t_fin/3600])

fig5.suptitle('Resultados — Método de Euler', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('./comparacion_euler.png')
plt.close()
print("  [✓] comparacion_euler.png guardada")

print("\n  Todas las figuras generadas exitosamente.")
print("  Archivos listos para incluir en el paper LaTeX.")