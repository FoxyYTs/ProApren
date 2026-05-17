"""
Modelo 3D de Marquesina de Secado de Café
Extensión del modelo de grano individual a N granos en capas (RK4)

Politécnico Colombiano Jaime Isaza Cadavid
Facultad de Ingeniería — Rionegro, Antioquia, Colombia
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D          # noqa: F401
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import AutoMinorLocator

# ═══════════════════════════════════════════════════════
# 1. PARÁMETROS DEL GRANO (del modelo original)
# ═══════════════════════════════════════════════════════

a           = 0.0055        # Semieje mayor [m]
b           = 0.0042        # Semieje menor [m]
lambda_evap = 2.26e6        # Calor latente de evaporación [J/kg]
h_c         = 15.0          # Coeficiente convectivo [W/m²·K]
rho_cafe    = 1200.0        # Densidad del grano [kg/m³]
T_c         = 293.15        # Temperatura de referencia [K]
C_q         = 1.14e-7       # Constante del sistema
gamma_e     = 0.85          # Factor de corrección evaporativa

# ═══════════════════════════════════════════════════════
# 2. GEOMETRÍA DEL GRANO
# ═══════════════════════════════════════════════════════

e_exc       = np.sqrt(1.0 - (b / a) ** 2)
V_g         = (4.0 / 3.0) * np.pi * a * b ** 2
A_g         = 2*np.pi*b**2 + 2*np.pi*(a*b/e_exc)*np.arcsin(e_exc)
m_grano_ini = rho_cafe * V_g                       # [kg] masa total húmeda por grano

# ═══════════════════════════════════════════════════════
# 3. PARÁMETROS DE LA MARQUESINA
# ═══════════════════════════════════════════════════════

# Dimensiones estructurales
L_marq  = 10.0      # Longitud [m]
W_marq  = 4.0       # Ancho [m]
H_lat   = 1.8       # Altura de las paredes laterales [m]
H_cumbr = 2.8       # Altura de la cumbrera [m]

# Cama de café
prof_cama = 0.04    # Profundidad de la capa de café [m]  (4 cm)
n_capas   = 5       # Número de capas para el gradiente de secado
k_ext     = 25.0    # Coeficiente de extinción [1/m]
packing   = 0.62    # Factor de empaque de esferoides prolatos

# Humedad inicial (café recién lavado / cereza despulpada)
X_0       = 0.55    # Base seca [kg_agua / kg_seco]
f_agua_0  = X_0 / (1.0 + X_0)              # Fracción másica de agua
m_agua_g0 = m_grano_ini * f_agua_0         # [kg] agua inicial por grano
m_seco_g  = m_grano_ini * (1.0 - f_agua_0) # [kg] masa seca por grano

# Número total de granos en la cama
V_cama    = L_marq * W_marq * prof_cama
N_granos  = int(V_cama * packing / V_g)
N_por_capa = N_granos // n_capas

print("=" * 60)
print("  MARQUESINA — PARÁMETROS")
print("=" * 60)
print(f"  Dimensiones          : {L_marq} m × {W_marq} m")
print(f"  Profundidad cama     : {prof_cama*100:.0f} cm  ({n_capas} capas)")
print(f"  Vol. cama de café    : {V_cama:.2f} m³")
print(f"  Vol. grano (V_g)     : {V_g*1e9:.4f} mm³")
print(f"  N° total de granos   : {N_granos:,}")
print(f"  Masa total (húmedo)  : {N_granos * m_grano_ini:.2f} kg")
print(f"  Agua total inicial   : {N_granos * m_agua_g0:.2f} kg")
print(f"  Humedad inicial X₀   : {X_0:.2f} kg/kg (bs)")
print("=" * 60)

# ═══════════════════════════════════════════════════════
# 4. FUNCIONES DEL MODELO FÍSICO
# ═══════════════════════════════════════════════════════

def T_amb(t):
    """Temperatura ambiente senoidal [K] — clima andino cafetero."""
    T_med = (288.15 + 301.15) / 2.0
    amp   = (301.15 - 288.15) / 2.0
    omega = 2.0 * np.pi / 86400.0
    return T_med + amp * np.sin(omega * t - np.pi / 2.0)

def P_vap(T_K):
    """Presión de vapor del agua por ecuación de Antoine [Pa]."""
    T_C = T_K - 273.15
    return (10.0 ** (8.07131 - 1730.63 / (233.426 + T_C))) * 133.322

def Q_dot(t):
    """Flujo de calor instantáneo en superficie libre [W]."""
    return C_q * h_c * (P_vap(T_c) + gamma_e * P_vap(T_amb(t)))

def factor_capa(i):
    """
    Factor de atenuación exponencial para la capa i.
    i=0 → superficie (factor máximo); i=n_capas-1 → fondo (factor mínimo).
    """
    z_mid = (i + 0.5) * (prof_cama / n_capas)
    return np.exp(-k_ext * z_mid)

factores = np.array([factor_capa(i) for i in range(n_capas)])
print(f"\n  Factores por capa    : {factores.round(4).tolist()}")

# ═══════════════════════════════════════════════════════
# 5. INTEGRACIÓN RK4 POR CAPAS
# ═══════════════════════════════════════════════════════

h_step = 60.0               # Paso temporal [s]
t_ini  = 0.0
t_fin  = 3600.0 * 8.0       # 8 horas [s]
t_vals = np.arange(t_ini, t_fin + h_step, h_step)
N_t    = len(t_vals)

def f_ode(t, x, fac):
    """EDO por capa:  x = [U_e [J],  m_evap [kg]]."""
    Q = fac * Q_dot(t)
    return np.array([Q, Q / lambda_evap])

def rk4_step(t_n, x_n, h, fac):
    k1 = h * f_ode(t_n,       x_n,          fac)
    k2 = h * f_ode(t_n + h/2, x_n + k1/2,  fac)
    k3 = h * f_ode(t_n + h/2, x_n + k2/2,  fac)
    k4 = h * f_ode(t_n + h,   x_n + k3,    fac)
    return x_n + (k1 + 2*k2 + 2*k3 + k4) / 6.0

# Arrays de resultados por capa: shape (N_t, 2)
x_capas = [np.zeros((N_t, 2)) for _ in range(n_capas)]

print("\n  Ejecutando integración RK4 por capas...")
for n in range(N_t - 1):
    for i in range(n_capas):
        x_nxt = rk4_step(t_vals[n], x_capas[i][n], h_step, factores[i])
        x_nxt[1] = min(x_nxt[1], m_agua_g0)   # no evaporar más agua de la disponible
        x_capas[i][n+1] = x_nxt

print("  Integración completada.\n")

# ═══════════════════════════════════════════════════════
# 6. MÉTRICAS GLOBALES DE LA MARQUESINA
# ═══════════════════════════════════════════════════════

t_h      = t_vals / 3600.0
T_vals_C = np.array([T_amb(t) - 273.15 for t in t_vals])

# Masa total de agua evaporada de la marquesina [kg]
M_evap_marq = sum(N_por_capa * x_capas[i][:, 1] for i in range(n_capas))

# Humedad promedio bulk base seca X_bulk(t)
m_agua_ini_total = N_granos * m_agua_g0
m_seco_total     = N_granos * m_seco_g
X_bulk           = np.clip((m_agua_ini_total - M_evap_marq) / m_seco_total, 0, X_0)

# Porcentaje de agua removida
pct_removida = (M_evap_marq / m_agua_ini_total) * 100.0

print("=" * 60)
print("  RESULTADOS FINALES — MARQUESINA COMPLETA (8 h)")
print("=" * 60)
print(f"  Agua total inicial         : {m_agua_ini_total:.2f} kg")
print(f"  Agua evaporada acumulada   : {M_evap_marq[-1]:.3f} kg")
print(f"  Porcentaje de agua removida: {pct_removida[-1]:.2f} %")
print(f"  Humedad inicial X₀         : {X_0:.4f} kg/kg (bs)")
print(f"  Humedad final X(8h)        : {X_bulk[-1]:.4f} kg/kg (bs)")
print("=" * 60)

# ═══════════════════════════════════════════════════════
# 7. ESTILO GLOBAL DE FIGURAS (IEEE)
# ═══════════════════════════════════════════════════════

plt.rcParams.update({
    'font.family'    : 'serif',
    'font.size'      : 10,
    'axes.titlesize' : 10,
    'axes.labelsize' : 10,
    'legend.fontsize': 9,
    'figure.dpi'     : 300,
    'savefig.dpi'    : 300,
    'savefig.bbox'   : 'tight',
    'lines.linewidth': 1.6,
    'axes.grid'      : True,
    'grid.alpha'     : 0.3,
    'grid.linestyle' : '--',
})

# ═══════════════════════════════════════════════════════
# 8. FIGURA 1 — MODELO 3D DE LA MARQUESINA
# ═══════════════════════════════════════════════════════

def draw_marquesina_frame(ax, L, W, H_l, H_c):
    """Dibuja el armazón estructural de la marquesina en el eje 3D."""
    col = '#4e342e'     # madera oscura
    lw  = 1.3

    # Piso (base)
    for xs, ys, zs in [([0,L],[0,0],[0,0]),([L,L],[0,W],[0,0]),
                        ([L,0],[W,W],[0,0]),([0,0],[W,0],[0,0])]:
        ax.plot(xs, ys, zs, color=col, lw=lw)

    # Cuatro columnas verticales en esquinas
    for xc, yc in [(0,0),(L,0),(L,W),(0,W)]:
        ax.plot([xc,xc], [yc,yc], [0, H_l], color=col, lw=lw)

    # Vigas perimetrales superiores
    ax.plot([0,L],[0,0],[H_l,H_l], color=col, lw=lw)
    ax.plot([0,L],[W,W],[H_l,H_l], color=col, lw=lw)

    # Cumbrera central
    ax.plot([0,L], [W/2,W/2], [H_c,H_c], color=col, lw=lw*1.4)

    # Rafters (vigas del techo) cada 2 m a lo largo de L
    for xv in np.linspace(0, L, int(L/2)+1):
        ax.plot([xv,xv],[0,W/2],  [H_l,H_c], color=col, lw=lw*0.7, alpha=0.7)
        ax.plot([xv,xv],[W/2,W],  [H_c,H_l], color=col, lw=lw*0.7, alpha=0.7)

    # Planos del techo semitransparentes
    for verts in [
        [[0,0,H_l],[L,0,H_l],[L,W/2,H_c],[0,W/2,H_c]],
        [[0,W/2,H_c],[L,W/2,H_c],[L,W,H_l],[0,W,H_l]],
    ]:
        ax.add_collection3d(
            Poly3DCollection([verts], alpha=0.12,
                             facecolor='#e3f2fd', edgecolor='none'))

    # Paredes laterales semitransparentes
    for y0 in [0, W]:
        ax.add_collection3d(
            Poly3DCollection([[[0,y0,0],[L,y0,0],[L,y0,H_l],[0,y0,H_l]]],
                             alpha=0.07, facecolor='#b3e5fc', edgecolor='none'))

# ─── Posiciones aleatorias de muestra de granos ───────────
rng   = np.random.default_rng(42)
n_vis = 800
xg    = rng.uniform(0.15, L_marq - 0.15, n_vis)
yg    = rng.uniform(0.15, W_marq - 0.15, n_vis)
zg    = rng.uniform(0.0,  prof_cama,     n_vis)   # posición real dentro la cama

# Capa de cada grano: 0=superficie (menor z desde arriba), n-1=fondo
step_c = prof_cama / n_capas
capa_g = np.minimum(n_capas - 1,
                    ((prof_cama - zg) / step_c).astype(int))

# ─── Visualización en t = 4 h ─────────────────────────────
t_idx_mid = N_t // 2
hum_ret   = [max(0, m_agua_g0 - x_capas[i][t_idx_mid, 1]) / m_agua_g0
             for i in range(n_capas)]
hum_g     = np.array([hum_ret[c] for c in capa_g])

zg_vis = zg * 10.0     # escala ×10 para que la cama sea visible en la figura

fig3d = plt.figure(figsize=(11, 6.5))
ax3d  = fig3d.add_subplot(111, projection='3d')

draw_marquesina_frame(ax3d, L_marq, W_marq, H_lat, H_cumbr)

sc = ax3d.scatter(xg, yg, zg_vis,
                  c=hum_g, cmap='RdYlBu_r',
                  s=10, alpha=0.85,
                  vmin=0.0, vmax=1.0, depthshade=True)

cbar = plt.colorbar(sc, ax=ax3d, shrink=0.45, pad=0.08, aspect=18)
cbar.set_label('Humedad retenida\n(0 = seco,  1 = húmedo inicial)', fontsize=9)
cbar.set_ticks([0.0, 0.25, 0.5, 0.75, 1.0])

ax3d.set_xlabel('Longitud (m)', labelpad=8)
ax3d.set_ylabel('Ancho (m)',    labelpad=8)
ax3d.set_zlabel('Altura (m)\n(cama: escala ×10)', labelpad=8)
ax3d.set_xlim(0, L_marq);  ax3d.set_ylim(0, W_marq);  ax3d.set_zlim(0, H_cumbr)
ax3d.set_title(
    f'Marquesina de Secado  —  t = {t_h[t_idx_mid]:.1f} h\n'
    f'N = {N_granos:,} granos  |  '
    f'Agua evaporada = {M_evap_marq[t_idx_mid]:.2f} kg  |  '
    f'$X_{{bulk}}$ = {X_bulk[t_idx_mid]:.3f} kg/kg',
    fontsize=9, fontweight='bold', pad=10)
ax3d.view_init(elev=22, azim=-52)

plt.tight_layout()
plt.savefig('./marquesina_3d.png')
plt.close()
print("  [✓] marquesina_3d.png guardada")

# ═══════════════════════════════════════════════════════
# 9. FIGURA 2 — MÉTRICAS GLOBALES (4 paneles)
# ═══════════════════════════════════════════════════════

fig2, axes = plt.subplots(2, 2, figsize=(10, 6.5))

# (a) Humedad promedio bulk
axes[0,0].plot(t_h, X_bulk, color='#1a5276', lw=2.0, label='$X_{bulk}$ (RK4)')
axes[0,0].axhline(0.11, color='#c0392b', ls='--', lw=1.3, label='Meta $X=0.11$')
axes[0,0].set_xlabel('Tiempo (h)')
axes[0,0].set_ylabel('Humedad base seca $X$ (kg/kg)')
axes[0,0].set_title('(a) Humedad promedio — Marquesina completa')
axes[0,0].legend(fontsize=8); axes[0,0].set_xlim(0, 8)
axes[0,0].xaxis.set_minor_locator(AutoMinorLocator())
axes[0,0].yaxis.set_minor_locator(AutoMinorLocator())

# (b) Masa total evaporada
axes[0,1].plot(t_h, M_evap_marq, color='#117a65', lw=2.0)
axes[0,1].set_xlabel('Tiempo (h)')
axes[0,1].set_ylabel('Masa evaporada acumulada (kg)')
axes[0,1].set_title('(b) Agua removida total — Marquesina')
axes[0,1].set_xlim(0, 8)
axes[0,1].xaxis.set_minor_locator(AutoMinorLocator())
axes[0,1].yaxis.set_minor_locator(AutoMinorLocator())

# (c) Masa evaporada por grano según capa
cols_c = plt.cm.plasma(np.linspace(0.1, 0.85, n_capas))
for i in range(n_capas):
    axes[1,0].plot(t_h, x_capas[i][:, 1] * 1e6,
                   color=cols_c[i], lw=1.6,
                   label=f'Capa {i+1}  (f={factores[i]:.3f})')
axes[1,0].set_xlabel('Tiempo (h)')
axes[1,0].set_ylabel('$m_{evap}$ por grano (×10⁻⁶ kg)')
axes[1,0].set_title('(c) Secado por capa — gradiente de profundidad')
axes[1,0].legend(fontsize=7.5, loc='upper left'); axes[1,0].set_xlim(0, 8)
axes[1,0].xaxis.set_minor_locator(AutoMinorLocator())
axes[1,0].yaxis.set_minor_locator(AutoMinorLocator())

# (d) Temperatura ambiente
axes[1,1].plot(t_h, T_vals_C, color='#8e44ad', lw=1.8)
axes[1,1].set_xlabel('Tiempo (h)')
axes[1,1].set_ylabel('Temperatura (°C)')
axes[1,1].set_title('(d) Temperatura ambiente durante la simulación')
axes[1,1].set_xlim(0, 8)
axes[1,1].xaxis.set_minor_locator(AutoMinorLocator())
axes[1,1].yaxis.set_minor_locator(AutoMinorLocator())

fig2.suptitle(
    f'Simulación de Secado — Marquesina {L_marq:.0f}×{W_marq:.0f} m'
    f'  |  N = {N_granos:,} granos',
    fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('./marquesina_metricas.png')
plt.close()
print("  [✓] marquesina_metricas.png guardada")

# ═══════════════════════════════════════════════════════
# 10. FIGURA 3 — SNAPSHOTS TEMPORALES (5 instantes)
# ═══════════════════════════════════════════════════════

instantes = [0, N_t//4, N_t//2, 3*N_t//4, N_t-1]
fig_s, ax_s = plt.subplots(1, 5, figsize=(16, 3.8),
                            subplot_kw={'projection': '3d'})

col_m = '#4e342e'
for k, idx_t in enumerate(instantes):
    ax = ax_s[k]

    # Humedad retenida por capa en este instante
    hr      = [max(0, m_agua_g0 - x_capas[i][idx_t, 1]) / m_agua_g0
               for i in range(n_capas)]
    hum_sn  = np.array([hr[c] for c in capa_g])

    ax.scatter(xg, yg, zg_vis, c=hum_sn,
               cmap='RdYlBu_r', s=4, alpha=0.8, vmin=0.0, vmax=1.0)

    L, W = L_marq, W_marq
    ax.plot([0,L,L,0,0], [0,0,W,W,0], [0,0,0,0,0], color=col_m, lw=0.8)
    ax.plot([0,L], [W/2,W/2], [H_cumbr,H_cumbr], color=col_m, lw=1.0)
    for xv in [0, L]:
        ax.plot([xv,xv],[0,0],   [0,H_lat],   color=col_m, lw=0.7)
        ax.plot([xv,xv],[W,W],   [0,H_lat],   color=col_m, lw=0.7)
        ax.plot([xv,xv],[0,W/2], [H_lat,H_cumbr], color=col_m, lw=0.7)
        ax.plot([xv,xv],[W/2,W], [H_cumbr,H_lat], color=col_m, lw=0.7)

    ax.set_xlim(0, L_marq); ax.set_ylim(0, W_marq); ax.set_zlim(0, H_cumbr)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.set_title(f't = {t_h[idx_t]:.0f} h\n$X$ = {X_bulk[idx_t]:.3f} kg/kg',
                 fontsize=8, pad=2)
    ax.view_init(elev=25, azim=-55)

fig_s.suptitle(
    'Evolución del secado en la marquesina'
    r'  (rojo $\rightarrow$ seco · azul $\rightarrow$ húmedo)',
    fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('./marquesina_snapshots.png')
plt.close()
print("  [✓] marquesina_snapshots.png guardada")

# ═══════════════════════════════════════════════════════
# 11. RESUMEN FINAL
# ═══════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  RESUMEN — MARQUESINA COMPLETA")
print("=" * 60)
print(f"  Dimensiones          : {L_marq}m × {W_marq}m  (techo a {H_cumbr}m)")
print(f"  Profundidad cama     : {prof_cama*100:.0f} cm  |  {n_capas} capas  |  k_ext={k_ext}")
print(f"  Factor de empaque    : {packing}")
print(f"  N° total de granos   : {N_granos:,}")
print(f"  Masa total (húmedo)  : {N_granos * m_grano_ini:.2f} kg")
print(f"  Agua total inicial   : {m_agua_ini_total:.2f} kg")
print(f"  Agua evaporada (8 h) : {M_evap_marq[-1]:.3f} kg")
print(f"  Porcentaje removido  : {pct_removida[-1]:.2f} %")
print(f"  X inicial            : {X_0:.4f} kg/kg (bs)")
print(f"  X final (8 h)        : {X_bulk[-1]:.4f} kg/kg (bs)")
print("=" * 60)
print("\n  Figuras generadas:")
print("    · marquesina_3d.png")
print("    · marquesina_metricas.png")
print("    · marquesina_snapshots.png")
