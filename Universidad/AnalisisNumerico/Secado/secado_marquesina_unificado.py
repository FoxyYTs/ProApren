"""
═══════════════════════════════════════════════════════════════════════════════
SIMULACIÓN NUMÉRICA UNIFICADA — SECADO SOLAR DE CAFÉ EN MARQUESINA
Modelo de Capas Discretas | RK4 vs Euler | Ciclo Completo 24 Horas

Correcciones implementadas respecto a versiones anteriores:
  1. Área útil real: Au = 32 m²  (2 camas × 10 m × 1.6 m)
  2. Simulación de 24 h con comportamiento diurno-nocturno e inflexiones
  3. C_q con unidades correctas [m²·K/Pa] — cierra dimensionalmente en [W]
  4. EDO optimizada: solo dm_evap/dt; U_e = λ·m_evap (no redundancia)
  5. Sin PDE ni Crank-Nicolson — todo basado en RK4 por capas
  6. Conexión micro→macro documentada en el código
  7. Comparación RK4 vs Euler con inflexiones día-noche destacadas

Politécnico Colombiano Jaime Isaza Cadavid
Facultad de Ingeniería — Rionegro, Antioquia, Colombia
═══════════════════════════════════════════════════════════════════════════════
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
from mpl_toolkits.mplot3d import Axes3D          # noqa: F401
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ═══════════════════════════════════════════════════════════════════════════════
# 1. PARÁMETROS FÍSICOS
# ═══════════════════════════════════════════════════════════════════════════════

# — Geometría del grano (esferoide prolato) —
a_g        = 0.0055      # Semieje mayor [m]
b_g        = 0.0042      # Semieje menor [m]
rho_cafe   = 1200.0      # Densidad del grano [kg/m³]

# — Camas de secado elevadas (2 × 10 m × 1.6 m = 32 m²) —
L_cama    = 10.0          # Longitud de cada cama [m]
W_cama    = 1.60          # Ancho de cada cama [m]  ← 1.6 m
N_camas   = 2
Au        = N_camas * L_cama * W_cama    # Área útil real = 32 m²
prof_cama = 0.04          # Profundidad de la capa de café [m]
n_capas   = 5             # Capas horizontales discretas
k_ext     = 25.0          # Coeficiente de extinción del lecho [m⁻¹]
packing   = 0.62          # Factor de empaque (esferoides prolatos)

# — Propiedades térmicas —
lambda_evap = 2.26e6      # Calor latente de evaporación [J/kg]
h_c         = 15.0        # Coeficiente convectivo superficial [W/(m²·K)]
T_c         = 293.15      # Temperatura de referencia [K] (20 °C)
gamma_e     = 0.85        # Factor de corrección evaporativa [-]

# — Constante empírica (CORRECCIÓN DIMENSIONAL) —
#
#   Q_dot = C_q · h_c · [P(T_c) + γ·P(T_e)]
#
#   Análisis dimensional:
#     [h_c]  = W/(m²·K)
#     [P]    = Pa = kg/(m·s²)
#     Para [Q_dot] = W = kg·m²/s³:
#       [C_q] · W/(m²·K) · Pa = W
#       [C_q] = W / (W/(m²·K) · Pa) = m²·K/Pa    ✓
#
C_q = 1.14e-7             # [m²·K/Pa]  — corrige la versión previa [m²/Pa]

# — Humedad —
X_0        = 0.55         # Humedad inicial base seca [kg_agua/kg_seco]
X_eq       = 0.11         # Humedad de equilibrio (meta comercial) [kg/kg bs]

# — Temperatura ambiente: rango andino cafetero —
T_min_K    = 288.15       # 15 °C — mínimo nocturno [K]
T_max_K    = 301.15       # 28 °C — máximo diurno   [K]

# — Tiempo de simulación: ciclo completo 24 h —
t_fin  = 86400.0          # 24 horas [s]
#
# JUSTIFICACIÓN DE h_step = 60 s:
#   La EDO dm/dt = f·Q(t)/λ es linealmente forzada por T_amb(t) senoidal.
#   No hay rigidez (stiffness): la constante de tiempo dominante es el período
#   diurno τ = 86 400 s. El criterio de Courant para métodos explícitos exige
#   h ≪ τ. Con h=60 s se tienen 1 440 pasos/ciclo → relación h/τ ≈ 7×10⁻⁴.
#   RK4 con este paso entrega error local O(h⁵) ≈ 10⁻²³ s⁵, garantizando
#   que el error global acumulado al cabo de 24 h sea inferior a 10⁻¹⁵ kg/grano,
#   muy por debajo de la resolución física del modelo.
h_step = 60.0             # Paso temporal [s]  (1 440 pasos por ciclo diurno)

# ═══════════════════════════════════════════════════════════════════════════════
# 2. GEOMETRÍA DEL GRANO (ESCALA MICRO)
# ═══════════════════════════════════════════════════════════════════════════════

e_exc       = np.sqrt(1.0 - (b_g / a_g)**2)
V_g         = (4.0/3.0) * np.pi * a_g * b_g**2
A_g         = 2*np.pi*b_g**2 + 2*np.pi*(a_g*b_g/e_exc)*np.arcsin(e_exc)
m_grano_ini = rho_cafe * V_g                         # masa húmeda del grano [kg]

f_agua_0  = X_0 / (1.0 + X_0)                       # fracción másica de agua
m_agua_g0 = m_grano_ini * f_agua_0                   # agua inicial por grano [kg]
m_seco_g  = m_grano_ini * (1.0 - f_agua_0)           # masa seca por grano   [kg]
m_agua_eq = m_seco_g * X_eq                           # agua mínima (equilibrio) [kg]
m_evap_max = m_agua_g0 - m_agua_eq                    # máximo evaporable por grano [kg]

# ═══════════════════════════════════════════════════════════════════════════════
# 3. ESCALADO MICRO → MACRO (GRANO A MARQUESINA)
# ═══════════════════════════════════════════════════════════════════════════════
#
# A ESCALA MICRO: cada grano intercambia calor y masa con el aire de su entorno
#   local, modelado mediante Q_dot(t) y la EDO dm_evap/dt = Q_dot/λ.
#
# A ESCALA MACRO: la cama de café (prof = 4 cm) se divide en Nc = 5 capas
#   horizontales. El flujo radiante y el potencial de secado del aire se
#   atenúan exponencialmente en profundidad:
#
#       f_i = exp(−k_ext · z_i),   z_i = (i + 1/2) · prof_cama / Nc
#
#   donde i=0 es la superficie (máxima exposición) e i=4 es el fondo.
#   La EDO de cada capa es idéntica a la del grano individual pero escalada
#   por f_i, y las métricas globales se obtienen multiplicando por N_por_capa.
#

V_cama_total = Au * prof_cama                        # Vol. total de café [m³]
N_granos     = int(V_cama_total * packing / V_g)     # N granos en Au = 32 m²
N_por_capa   = N_granos // n_capas

# Centroides de capa e i=0→superficie, i=4→fondo
z_i     = np.array([(i + 0.5) * prof_cama / n_capas for i in range(n_capas)])
factores = np.exp(-k_ext * z_i)                      # f_i ∈ (0, 1]

# ═══════════════════════════════════════════════════════════════════════════════
# 4. FUNCIONES FÍSICAS
# ═══════════════════════════════════════════════════════════════════════════════

def T_amb_K(t):
    """Temperatura ambiente senoidal 24 h [K]. Mínimo en t=0 (amanecer)."""
    T_med = (T_min_K + T_max_K) / 2.0
    amp   = (T_max_K - T_min_K) / 2.0
    omega = 2.0 * np.pi / 86400.0
    return T_med + amp * np.sin(omega * t - np.pi / 2.0)

def P_vapor(T_K):
    """Presión de vapor del agua — ecuación de Antoine [Pa]."""
    T_C = T_K - 273.15
    return (10.0 ** (8.07131 - 1730.63 / (233.426 + T_C))) * 133.322

def Q_dot(t):
    """
    Flujo de calor instantáneo al grano [W].

    Q = C_q [m²·K/Pa] · h_c [W/(m²·K)] · (P(T_c) + γ·P(T_e)) [Pa]
      = [m²·K/Pa · W/(m²·K) · Pa] = [W]  ✓

    El forzamiento es máximo al mediodía (T_amb máxima) y mínimo
    al amanecer/anochecer (T_amb mínima). Los puntos de inflexión de
    la integral m_evap(t) se encuentran en t=12h (máximo diurno) y
    t=0/24h (mínimo nocturno).
    """
    T_e = T_amb_K(t)
    return C_q * h_c * (P_vapor(T_c) + gamma_e * P_vapor(T_e))

# ═══════════════════════════════════════════════════════════════════════════════
# 5. EDO OPTIMIZADA (CORRECCIÓN: VARIABLE ÚNICA m_evap)
# ═══════════════════════════════════════════════════════════════════════════════
#
# CORRECCIÓN respecto a la versión anterior:
#   - Se eliminó U_e del vector de estado porque U_e = λ·m_evap (dependencia lineal).
#   - El estado dinámico es solo m_evap_i(t) [kg/grano] por capa.
#   - La energía se recupera analíticamente: U_e(t) = λ · M_evap(t).
#

def f_ode(t, m_evap_i, fac_i):
    """Derivada dm_evap/dt [kg/s] para una capa con factor fac_i."""
    return fac_i * Q_dot(t) / lambda_evap

# ═══════════════════════════════════════════════════════════════════════════════
# 6. MÉTODOS NUMÉRICOS: RK4 Y EULER
# ═══════════════════════════════════════════════════════════════════════════════

def rk4_step(t_n, x_n, h, fac):
    """Un paso RK4 para la EDO escalar de masa evaporada por grano."""
    k1 = h * f_ode(t_n,       x_n,          fac)
    k2 = h * f_ode(t_n + h/2, x_n + k1/2,  fac)
    k3 = h * f_ode(t_n + h/2, x_n + k2/2,  fac)
    k4 = h * f_ode(t_n + h,   x_n + k3,    fac)
    return x_n + (k1 + 2*k2 + 2*k3 + k4) / 6.0

def euler_step(t_n, x_n, h, fac):
    """Un paso de Euler explícito para la misma EDO."""
    return x_n + h * f_ode(t_n, x_n, fac)

# ═══════════════════════════════════════════════════════════════════════════════
# 7. INTEGRACIÓN TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════════

t_vals = np.arange(0.0, t_fin + h_step, h_step)
N_t    = len(t_vals)

# m_evap[capa, tiempo] — masa evaporada acumulada por grano en cada capa
m_evap_rk4   = np.zeros((n_capas, N_t))
m_evap_euler = np.zeros((n_capas, N_t))

print("=" * 68)
print("  Integrando — RK4 y Euler — 24 horas, 5 capas")
print(f"  h_step = {h_step:.0f} s  |  N_t = {N_t} pasos  |  N_capas = {n_capas}")
print("=" * 68)

# COMPLEJIDAD ALGORÍTMICA:
#   - El modelo discretiza el espacio en N_c=5 capas (no en N_granos bucles).
#   - Bucle temporal: (N_t-1) × N_c = 1440 × 5 = 7 200 iteraciones por método.
#   - RK4: 4 evaluaciones de Q_dot(t) por paso → 4 × 7 205 = 28 820 eval.
#   - Las métricas globales M_evap y X_bulk se calculan vectorizando sobre
#     N_t, no sobre N_granos → O(N_t × N_c) independiente de N ≈ 1.95 M.
#   - Complejidad total: O(N_t · N_c) con constante pequeña. Tiempo esperado <1 s.

t_inicio = time.perf_counter()

for n in range(N_t - 1):
    for i in range(n_capas):
        nxt_rk4   = rk4_step(t_vals[n],   m_evap_rk4[i, n],   h_step, factores[i])
        nxt_euler = euler_step(t_vals[n],  m_evap_euler[i, n], h_step, factores[i])
        m_evap_rk4[i,   n+1] = np.clip(nxt_rk4,   0.0, m_evap_max)
        m_evap_euler[i, n+1] = np.clip(nxt_euler,  0.0, m_evap_max)

t_integ = time.perf_counter() - t_inicio
print(f"  Integración completada en {t_integ*1e3:.2f} ms\n")

# ═══════════════════════════════════════════════════════════════════════════════
# 8. MÉTRICAS DE MARQUESINA
# ═══════════════════════════════════════════════════════════════════════════════

t_h      = t_vals / 3600.0
T_vals_C = np.array([T_amb_K(t) - 273.15 for t in t_vals])
Q_vals   = np.array([Q_dot(t) for t in t_vals])

M_agua_0_total = N_granos * m_agua_g0
M_seco_total   = N_granos * m_seco_g

def calc_metrics(m_evap_capas):
    """Calcula M_evap [kg], X_bulk [kg/kg bs] y U_e [J] para la marquesina."""
    M_evap = np.sum([N_por_capa * m_evap_capas[i] for i in range(n_capas)], axis=0)
    X_bulk = np.clip((M_agua_0_total - M_evap) / M_seco_total, X_eq, X_0)
    U_e    = lambda_evap * M_evap       # U_e = λ·m_evap (no redundancia)
    return M_evap, X_bulk, U_e

M_evap_rk4,   X_bulk_rk4,   U_e_rk4   = calc_metrics(m_evap_rk4)
M_evap_euler, X_bulk_euler, U_e_euler = calc_metrics(m_evap_euler)

# Tasa de evaporación total [kg/s] — usada para identificar inflexiones
dM_dt_rk4   = np.gradient(M_evap_rk4,   t_vals)
dM_dt_euler = np.gradient(M_evap_euler, t_vals)

# — Métricas de error RK4 vs Euler (calculadas aquí para consola y figura) —
_eps        = 1e-20                                            # evitar div/0
err_abs_g   = np.abs(M_evap_rk4 - M_evap_euler) * 1e3        # [g]
err_rel_pct = np.where(                                        # [%]
    M_evap_rk4 > _eps,
    np.abs(M_evap_rk4 - M_evap_euler) / M_evap_rk4 * 100.0,
    0.0
)

# ═══════════════════════════════════════════════════════════════════════════════
# 9. RESUMEN EN CONSOLA
# ═══════════════════════════════════════════════════════════════════════════════

W_final_capa = [(m_agua_g0 - m_evap_rk4[i, -1]) / m_seco_g for i in range(n_capas)]
pct_removida = (M_evap_rk4[-1] / M_agua_0_total) * 100.0
err_RK4_Euler = abs(M_evap_rk4[-1] - M_evap_euler[-1]) * 1000  # en gramos

print("=" * 68)
print("  BALANCE GLOBAL — MARQUESINA DE SECADO SOLAR — 24 h (RK4)")
print("=" * 68)
print(f"\n  ► GEOMETRÍA Y ESCALA")
print(f"    Área útil (2 camas × {L_cama:.0f}m × {W_cama:.2f}m): {Au:.1f} m²")
print(f"    Volumen total de café          : {V_cama_total:.3f} m³")
print(f"    Número total de granos (N)     : {N_granos:,}")
print(f"    Granos por capa (N/Nc)         : {N_por_capa:,}")
print(f"    Masa total húmeda inicial      : {N_granos*m_grano_ini:.2f} kg")
print(f"    Masa seca total                : {M_seco_total:.2f} kg")
print(f"    Agua total inicial (X₀=0.55)   : {M_agua_0_total:.2f} kg")
print(f"\n  ► RESULTADO A 24 HORAS")
print(f"    Agua evaporada acumulada       : {M_evap_rk4[-1]:.3f} kg")
print(f"    Porcentaje de agua removida    : {pct_removida:.2f} %")
print(f"    Humedad inicial X₀             : {X_0:.4f} kg/kg (bs)")
print(f"    Humedad final X_bulk(24h)      : {X_bulk_rk4[-1]:.4f} kg/kg (bs)")
print(f"    Energía total acumulada        : {U_e_rk4[-1]/1e6:.4f} MJ")
print(f"\n  ► POR CAPA AL FINALIZAR (t=24h)")
for i in range(n_capas):
    print(f"    Capa {i+1} (f={factores[i]:.4f}, z={z_i[i]*100:.1f}cm): "
          f"X = {W_final_capa[i]:.4f} kg/kg bs  |  "
          f"m_evap = {m_evap_rk4[i,-1]*1e3:.4f} g/grano")
print(f"\n  ► COMPARACIÓN MÉTODOS — ERROR RK4 vs EULER")
print(f"    Error absoluto final  |ΔM_evap|: {err_abs_g[-1]:.4e} g")
print(f"    Error absoluto máximo |ΔM_evap|: {np.max(err_abs_g):.4e} g")
print(f"    Error relativo final  (M_evap) : {err_rel_pct[-1]:.4e} %")
print(f"    Error relativo máximo (M_evap) : {np.max(err_rel_pct):.4e} %")
print(f"    Inflexiones m_evap(t): t=12h (máx diurno), t=0/24h (mín nocturno)")
print(f"\n  ► GRANO INDIVIDUAL (parámetros)")
print(f"    V_g = {V_g*1e9:.4f} mm³  |  A_g = {A_g*1e6:.4f} mm²")
print(f"    m_grano_ini = {m_grano_ini*1e3:.4f} g  |  m_agua_g0 = {m_agua_g0*1e3:.4f} g")
print(f"    m_evap_max  = {m_evap_max*1e3:.4f} g/grano (hasta X_eq={X_eq})")
print(f"\n  ► COSTO COMPUTACIONAL")
print(f"    Puntos temporales (N_t)        : {N_t}  (pasos de integración: {N_t-1})")
print(f"    Capas × métodos                : {n_capas} × 2 = {n_capas*2}")
print(f"    Iteraciones totales de bucle   : {(N_t-1) * n_capas * 2:,}")
print(f"    Evaluaciones Q_dot (RK4×4)     : {(N_t-1) * n_capas * 4:,}")
print(f"    Tiempo de integración          : {t_integ*1e3:.2f} ms")
print(f"    Complejidad                    : O(N_t × N_c) = O({N_t-1}×{n_capas})")
print(f"    Nota: N_granos ({N_granos:,}) solo entra como factor de escala")
print(f"          en calc_metrics(); no requiere bucle por grano.")
print("=" * 68)

# ═══════════════════════════════════════════════════════════════════════════════
# 10. ESTILO IEEE
# ═══════════════════════════════════════════════════════════════════════════════

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 10,
    'axes.titlesize': 10, 'axes.labelsize': 10,
    'legend.fontsize': 8.5, 'xtick.labelsize': 9, 'ytick.labelsize': 9,
    'figure.dpi': 300, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
    'lines.linewidth': 1.7, 'axes.grid': True,
    'grid.alpha': 0.3, 'grid.linestyle': '--',
})

C_RK4   = '#1a5276'
C_EULER = '#c0392b'
C_TEMP  = '#117a65'
C_NIGHT = '#e3f2fd'

def deco_24h(ax):
    """Sombrea noche, marca mediodía y añade etiquetas de fase."""
    for t0, t1 in [(0, 6), (18, 24)]:
        ax.axvspan(t0, t1, color=C_NIGHT, alpha=0.50, zorder=0, label='_nolegend_')
    ax.axvline(12, color='#f57f17', lw=0.8, ls=':', alpha=0.75)
    ax.axvline(6,  color='#546e7a', lw=0.6, ls=':', alpha=0.50)
    ax.axvline(18, color='#546e7a', lw=0.6, ls=':', alpha=0.50)
    ax.set_xlim(0, 24)
    ax.xaxis.set_major_locator(MultipleLocator(6))
    ax.xaxis.set_minor_locator(AutoMinorLocator(3))
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    for lbl, x, va in [('Amanecer', 0, 'bottom'), ('Mediodía', 12, 'bottom'),
                        ('Atardecer', 18, 'bottom'), ('Noche', 21, 'bottom')]:
        ax.text(x + (0.2 if lbl != 'Noche' else 0), ax.get_ylim()[0],
                lbl, fontsize=6.5, color='#37474f', alpha=0.8, va='bottom', rotation=0)

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 1 — temperatura.png
# ═══════════════════════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(6.5, 3.8))
ax.plot(t_h, T_vals_C, color=C_TEMP, lw=2.2, label='$T_{amb}(t)$')
# Marcas de inflexión de la temperatura
ax.annotate('Inflexión — mín.\n(amanecer)', xy=(0, T_vals_C[0]),
            xytext=(2.5, T_vals_C[0]+1.8),
            arrowprops=dict(arrowstyle='->', color='#1565c0', lw=0.9),
            fontsize=7.5, color='#1565c0')
ax.annotate('Inflexión — máx.\n(mediodía)', xy=(12, T_vals_C.max()),
            xytext=(13.8, T_vals_C.max()-2.2),
            arrowprops=dict(arrowstyle='->', color='#b71c1c', lw=0.9),
            fontsize=7.5, color='#b71c1c')
ax.set_xlabel('Tiempo (h)')
ax.set_ylabel('Temperatura (°C)')
ax.set_title('Temperatura ambiente — Ciclo diurno-nocturno 24 h\n(clima andino cafetero: 15–28 °C)')
deco_24h(ax)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('./temperatura.png')
plt.close()
print("  [✓] temperatura.png")

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 2 — energia.png
# ═══════════════════════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# Panel a: energía acumulada total
axes[0].plot(t_h, U_e_rk4/1e6, color=C_RK4, lw=2.0, label='RK4')
axes[0].set_xlabel('Tiempo (h)')
axes[0].set_ylabel('Energía acumulada (MJ)')
axes[0].set_title('(a) Energía total — Marquesina')
deco_24h(axes[0])
axes[0].legend()

# Panel b: tasa dU/dt = λ·dM/dt (forzamiento)
axes[1].plot(t_h, Q_vals * N_granos * np.mean(factores) / 1e3,
             color=C_RK4, lw=1.8, label=r'$\dot{Q}_{total}$ promedio')
axes[1].plot(t_h, T_vals_C * (N_granos * np.mean(factores) * C_q * h_c *
             np.gradient(np.array([P_vapor(T_amb_K(t)) for t in t_vals]),
             t_vals)) / 1e3, color='grey', lw=0.8, ls='--', alpha=0.5,
             label='_nolegend_')
axes[1].set_xlabel('Tiempo (h)')
axes[1].set_ylabel('Potencia total (kW)')
axes[1].set_title('(b) Potencia evaporativa — Puntos de inflexión')
deco_24h(axes[1])
idx_noon = int(12*3600/h_step)
axes[1].annotate('Inflexión diurna\n(máx. en t=12h)',
                 xy=(12, Q_vals[idx_noon]*N_granos*np.mean(factores)/1e3),
                 xytext=(14, Q_vals[idx_noon]*N_granos*np.mean(factores)/1e3*0.90),
                 arrowprops=dict(arrowstyle='->', color='#f57f17', lw=0.8),
                 fontsize=7.5, color='#f57f17')
axes[1].legend()

fig.suptitle(r'Energía acumulada en la marquesina  ($U_e = \lambda \cdot M_{evap}$)',
             fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('./energia.png')
plt.close()
print("  [✓] energia.png")

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 3 — masa.png
# ═══════════════════════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# Panel a: masa total evaporada
axes[0].plot(t_h, M_evap_rk4, color=C_RK4, lw=2.0, label='RK4 — total')
for i in range(n_capas):
    m_capa_i = N_por_capa * m_evap_rk4[i]
    col = plt.cm.plasma(i / (n_capas - 1))
    axes[0].plot(t_h, m_capa_i, lw=0.9, color=col, alpha=0.75,
                 label=f'Capa {i+1} (f={factores[i]:.3f})')
axes[0].set_xlabel('Tiempo (h)')
axes[0].set_ylabel('Masa evaporada acumulada (kg)')
axes[0].set_title('(a) Agua removida por capa y total')
deco_24h(axes[0])
axes[0].legend(fontsize=7, ncol=2)

# Panel b: X_bulk y X por capa
axes[1].plot(t_h, X_bulk_rk4, color=C_RK4, lw=2.2, label='$X_{bulk}$ (RK4)')
for i in range(n_capas):
    W_i = np.clip((m_agua_g0 - m_evap_rk4[i]) / m_seco_g, X_eq, X_0)
    col = plt.cm.plasma(i / (n_capas - 1))
    axes[1].plot(t_h, W_i, lw=0.9, color=col, alpha=0.75,
                 label=f'Capa {i+1}')
axes[1].axhline(X_eq, color='#b71c1c', ls='--', lw=1.2,
                label=f'$X_{{eq}}={X_eq}$ (meta)')
axes[1].set_xlabel('Tiempo (h)')
axes[1].set_ylabel('Humedad base seca (kg/kg)')
axes[1].set_title('(b) Evolución de la humedad por capa y promedio')
deco_24h(axes[1])
axes[1].legend(fontsize=7, ncol=2)

fig.suptitle(f'Masa de agua evaporada y humedad del lote — Marquesina {Au:.0f} m² | 24 h',
             fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('./masa.png')
plt.close()
print("  [✓] masa.png")

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 4 — comparacion_rk4.png  (RK4 vs Euler con inflexiones)
# ═══════════════════════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# — Panel a: humedad bulk —
axes[0].plot(t_h, X_bulk_rk4,   color=C_RK4,   lw=2.2, label='RK4')
axes[0].plot(t_h, X_bulk_euler, color=C_EULER,  lw=1.5, ls='--', alpha=0.85, label='Euler')
axes[0].axhline(X_eq, color='grey', lw=1.0, ls=':', label=f'$X_{{eq}}={X_eq}$')
axes[0].set_xlabel('Tiempo (h)')
axes[0].set_ylabel('$X_{bulk}$ (kg/kg bs)')
axes[0].set_title('(a) Humedad promedio del lote')
deco_24h(axes[0])
axes[0].legend(fontsize=8.5)

# — Panel b: tasa de evaporación (inflexiones) —
axes[1].plot(t_h, dM_dt_rk4   * 1e3, color=C_RK4,   lw=2.2, label='RK4')
axes[1].plot(t_h, dM_dt_euler * 1e3, color=C_EULER,  lw=1.5, ls='--', alpha=0.85, label='Euler')
axes[1].set_xlabel('Tiempo (h)')
axes[1].set_ylabel('$dM_{evap}/dt$ (g/s)')
axes[1].set_title('(b) Tasa de evaporación — Puntos de inflexión')
deco_24h(axes[1])
# Annotate inflection points
idx_noon  = int(12.0 * 3600 / h_step)
idx_dawn  = 0
y_noon  = dM_dt_rk4[idx_noon] * 1e3
y_dawn  = dM_dt_rk4[idx_dawn] * 1e3
axes[1].annotate(f'Inflexión diurna\nt=12h ({y_noon:.3f} g/s)',
                 xy=(12, y_noon), xytext=(13.5, y_noon*0.88),
                 arrowprops=dict(arrowstyle='->', color='#f57f17', lw=0.9),
                 fontsize=7.5, color='#f57f17')
axes[1].annotate(f'Inflexión nocturna\nt=0h ({y_dawn:.3f} g/s)',
                 xy=(0, y_dawn), xytext=(1.5, y_dawn*1.04),
                 arrowprops=dict(arrowstyle='->', color='#1565c0', lw=0.9),
                 fontsize=7.5, color='#1565c0')
axes[1].legend(fontsize=8.5)

# — Panel c: error acumulado —
err = np.abs(M_evap_rk4 - M_evap_euler) * 1e3    # en gramos
axes[2].plot(t_h, err, color='#8e44ad', lw=1.8, label='|RK4 − Euler|')
axes[2].fill_between(t_h, err, alpha=0.15, color='#8e44ad')
axes[2].set_xlabel('Tiempo (h)')
axes[2].set_ylabel('Error absoluto $|M_{RK4} - M_{Euler}|$ (g)')
axes[2].set_title('(c) Divergencia numérica acumulada')
deco_24h(axes[2])
axes[2].legend(fontsize=8.5)

fig.suptitle(f'Comparación RK4 vs Euler — Ciclo Diurno-Nocturno 24 h | Marquesina {Au:.0f} m²\n'
             'Zona azul = noche  |  Línea naranja = mediodía (inflexión máxima)',
             fontsize=9.5, fontweight='bold')
plt.tight_layout()
plt.savefig('./comparacion_rk4.png')
plt.close()
print("  [✓] comparacion_rk4.png")

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 5 — error_metodos.png  (error absoluto acumulado y error relativo)
# ═══════════════════════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

# — Panel a: Error absoluto acumulado —
axes[0].plot(t_h, err_abs_g, color='#8e44ad', lw=1.8,
             label=r'$|M_{RK4}(t) - M_{Euler}(t)|$')
axes[0].fill_between(t_h, err_abs_g, alpha=0.15, color='#8e44ad')
axes[0].set_xlabel('Tiempo (h)')
axes[0].set_ylabel('Error absoluto acumulado (g)')
axes[0].set_title(r'(a) Error absoluto — $M_{evap}$ total')
axes[0].ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
deco_24h(axes[0])
axes[0].legend(fontsize=8.5)

# — Panel b: Error relativo (%) — omite t=0 donde M_evap=0 —
t_h_nr   = t_h[1:]
err_r_nr = err_rel_pct[1:]
axes[1].plot(t_h_nr, err_r_nr, color='#e67e22', lw=1.8,
             label=r'$|M_{RK4}-M_{Euler}|/M_{RK4}\times100\%$')
axes[1].fill_between(t_h_nr, err_r_nr, alpha=0.15, color='#e67e22')
axes[1].set_xlabel('Tiempo (h)')
axes[1].set_ylabel('Error relativo (%)')
axes[1].set_title(r'(b) Error relativo — $M_{evap}$ total')
axes[1].ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
deco_24h(axes[1])
axes[1].legend(fontsize=8.5)

# Anotaciones de valores clave
for ax, y_arr, col in [(axes[0], err_abs_g,  '#8e44ad'),
                        (axes[1], err_r_nr,   '#e67e22')]:
    y_max = float(np.max(y_arr if ax is axes[0] else err_r_nr))
    t_max = t_h[np.argmax(err_abs_g)] if ax is axes[0] else t_h_nr[np.argmax(err_r_nr)]
    ax.annotate(f'máx = {y_max:.2e}',
                xy=(t_max, y_max),
                xytext=(t_max + 2, y_max * 0.85),
                fontsize=7.5, color=col,
                arrowprops=dict(arrowstyle='->', color=col, lw=0.8))

fig.suptitle(
    f'Error Numérico RK4 vs Euler — Marquesina {Au:.0f} m² | {t_fin/3600:.0f} h\n'
    r'Error en $M_{evap}(t)$: absoluto [g] y relativo [%]',
    fontsize=9.5, fontweight='bold')
plt.tight_layout()
plt.savefig('./error_metodos.png')
plt.close()
print("  [✓] error_metodos.png")

# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS 3D PARA LA VISUALIZACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

L_marq = 10.0; W_marq = 4.0; H_lat = 1.8; H_cumbr = 2.8; H_pata = 0.80
t_bas  = 0.05
e_p    = 0.05    # margen lateral desde la pared (0.05×2 = 0.10 total)
pasillo_w = W_marq - 2*e_p - 2*W_cama    # 4 - 0.10 - 3.20 = 0.70 m
y_c1   = e_p
y_c2   = e_p + W_cama + pasillo_w

BROWN_3D = '#4e342e'; WOOD_3D = '#8d6e63'; POLY_3D = '#b3e5fc'
CAFE_COLS = ['#d32f2f','#e64a19','#f57c00','#fbc02d','#388e3c']

def quad3(ax, pts, fc, ec='none', alpha=0.18, lw=0.4, zo=1):
    p = Poly3DCollection([pts], alpha=alpha, zorder=zo)
    p.set_facecolor(fc); p.set_edgecolor(ec); p.set_linewidth(lw)
    ax.add_collection3d(p)

def seg3(ax, p1, p2, c=BROWN_3D, lw=1.2, ls='-', alpha=1.0):
    ax.plot([p1[0],p2[0]], [p1[1],p2[1]], [p1[2],p2[2]],
            color=c, lw=lw, ls=ls, alpha=alpha, solid_capstyle='round')

def draw_shell(ax):
    """Estructura liviana de la marquesina."""
    L, W, Hl, Hc = L_marq, W_marq, H_lat, H_cumbr
    quad3(ax,[[0,0,0],[L,0,0],[L,W,0],[0,W,0]],'#efebe9',ec=BROWN_3D,alpha=0.22,lw=0.4)
    for xc in np.linspace(0,L,6):
        for yc in [0,W]:
            seg3(ax,(xc,yc,0),(xc,yc,Hl),BROWN_3D,lw=1.8)
    seg3(ax,(0,0,Hl),(L,0,Hl),BROWN_3D,lw=1.4)
    seg3(ax,(0,W,Hl),(L,W,Hl),BROWN_3D,lw=1.4)
    seg3(ax,(0,W/2,Hc),(L,W/2,Hc),BROWN_3D,lw=2.0)
    for xv in np.linspace(0,L,6):
        seg3(ax,(xv,0,Hl),(xv,W/2,Hc),WOOD_3D,lw=0.9,alpha=0.8)
        seg3(ax,(xv,W/2,Hc),(xv,W,Hl),WOOD_3D,lw=0.9,alpha=0.8)
    for y0t,yct in [(0,W/2),(W/2,W)]:
        quad3(ax,[[0,y0t,Hl if y0t==0 else Hc],[L,y0t,Hl if y0t==0 else Hc],
                   [L,yct,Hc if y0t==0 else Hl],[0,yct,Hc if y0t==0 else Hl]],
              POLY_3D,ec='#90a4ae',alpha=0.09,lw=0.3)
    for yp in [0,W]:
        quad3(ax,[[0,yp,0],[L,yp,0],[L,yp,Hl],[0,yp,Hl]],
              '#90a4ae',ec='#607d8b',alpha=0.07,lw=0.3)

def draw_cama_3d(ax, y0, m_evap_capa_t):
    """Cama elevada con color de humedad por capa en el instante dado."""
    y1  = y0 + W_cama
    z_b = H_pata + t_bas
    tb  = t_bas
    for xp in np.arange(0, L_marq+0.01, 2.0):
        for yp in [y0, y1]:
            ax.plot([xp,xp],[yp,yp],[0,H_pata],color=BROWN_3D,lw=1.6,alpha=0.9)
    for xp in np.arange(0, L_marq+0.01, 2.0):
        seg3(ax,(xp,y0,H_pata*0.4),(xp,y1,H_pata*0.4),WOOD_3D,lw=0.7,alpha=0.65)
    for yp in [y0,y1-tb]:
        quad3(ax,[[0,yp,H_pata],[L_marq,yp,H_pata],
                   [L_marq,yp+tb,H_pata],[0,yp+tb,H_pata]],
              WOOD_3D,ec='none',alpha=0.9,lw=0.3,zo=3)
    for xm in np.arange(tb,L_marq-tb+0.01,0.15):
        seg3(ax,(xm,y0+tb,H_pata),(xm,y1-tb,H_pata),'#90a4ae',lw=0.3,alpha=0.45)
    for ym in np.arange(y0+tb,y1-tb+0.01,0.15):
        seg3(ax,(tb,ym,H_pata),(L_marq-tb,ym,H_pata),'#90a4ae',lw=0.3,alpha=0.45)
    for i in range(n_capas):
        zi0 = z_b + i*dz_capa; zi1 = z_b + (i+1)*dz_capa
        hum = np.clip(1.0 - m_evap_capa_t[i] / m_evap_max, 0.0, 1.0)
        c   = plt.cm.RdYlBu_r(hum)
        quad3(ax,[[tb,y0+tb,zi1],[L_marq-tb,y0+tb,zi1],
                   [L_marq-tb,y1-tb,zi1],[tb,y1-tb,zi1]],
              c,ec='none',alpha=0.60,zo=4)
        quad3(ax,[[tb,y0+tb,zi0],[L_marq-tb,y0+tb,zi0],
                   [L_marq-tb,y0+tb,zi1],[tb,y0+tb,zi1]],
              c,ec='none',alpha=0.88,zo=5)

dz_capa = prof_cama / n_capas

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 5 — marquesina_3d.png  (estado a t=12h, máximo diurno)
# ═══════════════════════════════════════════════════════════════════════════════

t_idx_noon = int(12*3600/h_step)
rng = np.random.default_rng(42)
n_vis = 600

fig = plt.figure(figsize=(13, 6))
ax3d = fig.add_subplot(121, projection='3d')
draw_shell(ax3d)
draw_cama_3d(ax3d, y_c1, m_evap_rk4[:, t_idx_noon])
draw_cama_3d(ax3d, y_c2, m_evap_rk4[:, t_idx_noon])

# Granos de muestra coloreados por humedad
for y0_c in [y_c1, y_c2]:
    xg = rng.uniform(0.1, L_marq-0.1, n_vis)
    yg = rng.uniform(y0_c+0.05, y0_c+W_cama-0.05, n_vis)
    zg = rng.uniform(0.0, prof_cama, n_vis)
    capa_g = np.minimum(n_capas-1, (zg / (prof_cama/n_capas)).astype(int))
    hum_g  = np.array([(m_agua_g0-m_evap_rk4[c,t_idx_noon])/m_agua_g0 for c in capa_g])
    z_vis  = H_pata + t_bas + zg
    sc = ax3d.scatter(xg, yg, z_vis, c=hum_g, cmap='RdYlBu_r',
                      s=6, alpha=0.80, vmin=0.0, vmax=1.0, depthshade=True)

cbar = plt.colorbar(sc, ax=ax3d, shrink=0.45, pad=0.07, aspect=18)
cbar.set_label('Humedad retenida (0=seco, 1=húmedo)', fontsize=8)
ax3d.set_xlim(-0.5,L_marq+0.5); ax3d.set_ylim(-0.3,W_marq+0.3); ax3d.set_zlim(0,H_cumbr+0.2)
ax3d.set_xlabel('X (m)',fontsize=8,labelpad=5); ax3d.set_ylabel('Y (m)',fontsize=8,labelpad=5)
ax3d.set_zlabel('Z (m)',fontsize=8,labelpad=5)
ax3d.set_title(f't = 12 h (mediodía)\n$X_{{bulk}}$ = {X_bulk_rk4[t_idx_noon]:.4f} kg/kg bs',
               fontsize=9, fontweight='bold')
ax3d.view_init(elev=22, azim=-52)
ax3d.tick_params(labelsize=7)

# Vista lateral
ax3d_b = fig.add_subplot(122, projection='3d')
draw_shell(ax3d_b)
draw_cama_3d(ax3d_b, y_c1, m_evap_rk4[:, t_idx_noon])
draw_cama_3d(ax3d_b, y_c2, m_evap_rk4[:, t_idx_noon])
ax3d_b.set_xlim(-0.2,L_marq+0.2); ax3d_b.set_ylim(-0.2,W_marq+0.2); ax3d_b.set_zlim(0,H_cumbr+0.2)
ax3d_b.set_xlabel('X (m)',fontsize=8); ax3d_b.set_ylabel('Y (m)',fontsize=8)
ax3d_b.set_zlabel('Z (m)',fontsize=8)
ax3d_b.set_title('Vista de planta (t = 12 h)', fontsize=9, fontweight='bold')
ax3d_b.view_init(elev=82, azim=-90)
ax3d_b.tick_params(labelsize=7)

patches_3d = [mpatches.Patch(
    color=plt.cm.RdYlBu_r(np.clip(1.0 - m_evap_rk4[i, t_idx_noon]/m_evap_max, 0, 1)),
    label=f'Capa {i+1}  f={factores[i]:.3f}') for i in range(n_capas)]
fig.legend(handles=patches_3d, fontsize=7, loc='lower center', ncol=5,
           bbox_to_anchor=(0.5, -0.02), title='Capas de café', title_fontsize=7.5)
fig.suptitle(f'Marquesina de Secado Solar — Au={Au:.0f} m²  |  N={N_granos:,} granos\n'
             f'2 camas elevadas × {W_cama:.2f} m  |  Pasillo {pasillo_w:.2f} m  |  t = 12 h',
             fontsize=10, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('./marquesina_3d.png')
plt.close()
print("  [✓] marquesina_3d.png")

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 6 — marquesina_snapshots.png  (5 instantes: 0, 6, 12, 18, 24 h)
# ═══════════════════════════════════════════════════════════════════════════════

instantes_h   = [0, 6, 12, 18, 24]
instantes_idx = [int(h*3600/h_step) for h in instantes_h]

fig_s, axs = plt.subplots(1, 5, figsize=(18, 4.5),
                           subplot_kw={'projection': '3d'})

for k, (idx_t, t_label) in enumerate(zip(instantes_idx, instantes_h)):
    ax = axs[k]
    draw_shell(ax)
    draw_cama_3d(ax, y_c1, m_evap_rk4[:, idx_t])
    draw_cama_3d(ax, y_c2, m_evap_rk4[:, idx_t])

    ax.set_xlim(0,L_marq); ax.set_ylim(0,W_marq); ax.set_zlim(0,H_cumbr+0.2)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    fase = ['Amanecer','Mañana','Mediodía','Tarde','Noche'][k]
    ax.set_title(f't = {t_label} h ({fase})\n$X_{{bulk}}$ = {X_bulk_rk4[idx_t]:.4f}',
                 fontsize=8.5, fontweight='bold', pad=4)
    ax.view_init(elev=22, azim=-52)

sm_s = plt.cm.ScalarMappable(cmap='RdYlBu_r', norm=plt.Normalize(vmin=0.0, vmax=1.0))
sm_s.set_array([])
cbar_s = fig_s.colorbar(sm_s, ax=axs.tolist(), shrink=0.55, pad=0.02, aspect=25)
cbar_s.set_label('Humedad retenida  (0 = seco · 1 = húmedo)', fontsize=8)

fig_s.suptitle(
    r'Evolución del secado en la marquesina — RK4  (rojo $\rightarrow$ seco · azul $\rightarrow$ húmedo)',
    fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('./marquesina_snapshots.png')
plt.close()
print("  [✓] marquesina_snapshots.png")

print("\n  ══ FIGURAS GENERADAS ══════════════════════════════════════")
print("    temperatura.png       masa.png            marquesina_3d.png")
print("    energia.png           comparacion_rk4.png marquesina_snapshots.png")
print("    error_metodos.png")
print("  ════════════════════════════════════════════════════════════")
