"""
Modelo PDE de Difusión de Humedad en la Cama de Café
Crank-Nicolson 1D + temperatura quasi-estacionaria
Equivalente numérico del script FlexPDE secado_cafe.fde

z=0 → fondo (impermeable, adiabático)
z=L → superficie expuesta al aire

Politécnico Colombiano Jaime Isaza Cadavid
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# ═══════════════════════════════════════════════════════════
# 1. PARÁMETROS FÍSICOS
# ═══════════════════════════════════════════════════════════

rho_b    = 350.0        # Densidad aparente seca [kg/m³]
Cp_b     = 1800.0       # Calor específico [J/(kg·K)]
k_b      = 0.15         # Conductividad térmica [W/(m·K)]
D_eff    = 5.0e-10      # Difusividad efectiva de humedad [m²/s]
lambda_e = 2.26e6       # Calor latente de evaporación [J/kg]

h_conv   = 15.0         # Coeficiente convectivo [W/(m²·K)]
h_mass   = 1.0e-7       # Coeficiente de transferencia de masa [m/s]
W_eq     = 0.12         # Humedad de equilibrio [kg/kg bs]
W_ini    = 0.55         # Humedad inicial [kg/kg bs]
T_ini_K  = 288.15       # Temperatura inicial [K]

# ═══════════════════════════════════════════════════════════
# 2. MALLA ESPACIO-TEMPORAL
# ═══════════════════════════════════════════════════════════

L_bed = 0.04        # Profundidad [m]
N_z   = 200         # Nodos espaciales
dz    = L_bed / N_z
z     = np.linspace(dz/2, L_bed - dz/2, N_z)   # centros de celda

dt    = 60.0                    # Paso temporal [s]
t_fin = 3600.0 * 8.0
N_t   = int(t_fin / dt) + 1
t_s   = np.linspace(0, t_fin, N_t)

Bi_m = h_mass * L_bed / D_eff
r_W  = D_eff * dt / (2.0 * dz**2)
beta_W = h_mass * dz / D_eff

print("=" * 60)
print("  MODELO PDE — DIFUSIÓN 1D EN CAMA DE CAFÉ")
print("=" * 60)
print(f"  Malla: {N_z} nodos, dz = {dz*1000:.2f} mm, dt = {dt:.0f} s")
print(f"  D_eff = {D_eff:.2e} m²/s  |  τ_D = {L_bed**2/D_eff/3600:.0f} h")
print(f"  Bi_m  = {Bi_m:.2f}  |  r_W = {r_W:.4f}")
print("=" * 60)

# ─── Temperatura ambiente senoidal ────────────────────────
def T_amb_K(t_s):
    T_med = (288.15 + 301.15) / 2.0
    amp   = (301.15 - 288.15) / 2.0
    return T_med + amp * np.sin(2*np.pi*t_s/86400.0 - np.pi/2.0)

# ═══════════════════════════════════════════════════════════
# 3. SISTEMA TRIDIAGONAL — CRANK-NICOLSON PARA W
# ═══════════════════════════════════════════════════════════
#
# ∂W/∂t = D_eff · ∂²W/∂z²
#
# BC fondo   (z=0):  ∂W/∂z = 0  → nodo fantasma W_{-1} = W_1
# BC superficie (z=L):  D_eff·∂W/∂z = −h_m·(W_N−1 − W_eq)
#   → nodo fantasma W_N = W_{N-2} − 2β_W·(W_{N-1}−W_eq)
#   → diagonal superficie: 1 + 2r(1+β_W)
#   → subdiagonal superficie: −2r
#   → RHS superficie: W_old*(1−2r(1+β_W)) + 2r*W_{N-2,old} + 4r·β_W·W_eq
#

def build_tridiag():
    a = np.full(N_z, -r_W);   a[0] = 0.0           # subdiagonal
    b = np.full(N_z,  1 + 2*r_W)                    # diagonal
    c = np.full(N_z, -r_W);   c[-1] = 0.0           # superdiagonal

    b[0]   = 1 + 2*r_W          # fondo: coef. simétrico (W_{-1}=W_1 → c[0]=-2r)
    c[0]   = -2*r_W

    b[-1]  = 1 + 2*r_W*(1 + beta_W)    # superficie: Robin
    a[-1]  = -2*r_W                     # coef. de W_{N-2} desde ghost node
    return a, b, c

a_mat, b_mat, c_mat = build_tridiag()

def compute_rhs(W_old):
    rhs = np.empty(N_z)
    # Interior
    rhs[1:-1] = W_old[1:-1] + r_W*(W_old[2:] - 2*W_old[1:-1] + W_old[:-2])
    # Fondo (Neumann simétrico)
    rhs[0]    = W_old[0]    + r_W*(2*W_old[1] - 2*W_old[0])
    # Superficie (Robin)  —  derivado del CN exacto con ghost node
    rhs[-1]   = (W_old[-1]*(1 - 2*r_W*(1 + beta_W))
                 + 2*r_W*W_old[-2]
                 + 4*r_W*beta_W*W_eq)
    return rhs

def tdma(a, b, c, d):
    """Algoritmo de Thomas (TDMA) — O(N) para tridiagonal."""
    n = len(d)
    c_ = np.empty(n); d_ = np.empty(n); x = np.empty(n)
    c_[0] = c[0]/b[0];  d_[0] = d[0]/b[0]
    for i in range(1, n):
        m    = b[i] - a[i]*c_[i-1]
        c_[i] = c[i] / m
        d_[i] = (d[i] - a[i]*d_[i-1]) / m
    x[-1] = d_[-1]
    for i in range(n-2, -1, -1):
        x[i] = d_[i] - c_[i]*x[i+1]
    return x

# ═══════════════════════════════════════════════════════════
# 4. INTEGRACIÓN TEMPORAL
# ═══════════════════════════════════════════════════════════

W_hist = np.zeros((N_t, N_z))
W_hist[0] = W_ini
W_cur = np.full(N_z, W_ini)

# Temperatura quasi-estacionaria: T equilibra mucho más rápido que W
# (Fo_T = α·dt/dz² ≈ 357 >> 1), por lo que T ≈ T_amb - ΔT_evap
T_surf_hist = np.zeros(N_t)          # temperatura superficial [°C]
T_surf_hist[0] = T_ini_K - 273.15

print("\n  Integrando PDE (Crank-Nicolson)...")
for n in range(N_t - 1):
    rhs   = compute_rhs(W_cur)
    W_new = tdma(a_mat, b_mat, c_mat, rhs)
    W_new = np.clip(W_new, W_eq, W_ini)
    W_cur = W_new
    W_hist[n+1] = W_cur

    # Temperatura quasi-estacionaria en la superficie
    J_ev = lambda_e * rho_b * h_mass * max(0.0, W_cur[-1] - W_eq)
    Ta   = T_amb_K(t_s[n+1])
    T_surf_hist[n+1] = Ta - J_ev / h_conv - 273.15

print("  Completado.\n")

t_h = t_s / 3600.0

print("=" * 60)
print("  RESULTADOS PDE (8 horas)")
print("=" * 60)
print(f"  W superficie  : {W_hist[-1, -1]:.4f} kg/kg")
print(f"  W centro      : {W_hist[-1, N_z//2]:.4f} kg/kg")
print(f"  W fondo       : {W_hist[-1,  0]:.4f} kg/kg")
print(f"  δ penetración : {2*np.sqrt(D_eff*t_fin)*100:.2f} cm")
print(f"  T sup (t=8h)  : {T_surf_hist[-1]:.2f} °C")
print("=" * 60)

# ═══════════════════════════════════════════════════════════
# 5. ESTILO IEEE
# ═══════════════════════════════════════════════════════════

plt.rcParams.update({
    'font.family':'serif', 'font.size':10, 'axes.titlesize':10,
    'axes.labelsize':10, 'legend.fontsize':8.5, 'figure.dpi':300,
    'savefig.dpi':300, 'savefig.bbox':'tight', 'lines.linewidth':1.6,
    'axes.grid':True, 'grid.alpha':0.3, 'grid.linestyle':'--',
})

# ═══════════════════════════════════════════════════════════
# 6. FIGURA 1 — MAPA ESPACIO-TEMPORAL W(z,t)
# ═══════════════════════════════════════════════════════════

Z_m, T_m = np.meshgrid(z*100, t_h)   # z en cm desde fondo

fig1, axes1 = plt.subplots(1, 2, figsize=(10, 4))

pcm = axes1[0].pcolormesh(T_m, Z_m, W_hist, cmap='RdYlBu_r',
                           vmin=W_eq, vmax=W_ini, shading='auto')
plt.colorbar(pcm, ax=axes1[0], label='$W$ (kg/kg bs)')
axes1[0].set_xlabel('Tiempo (h)');  axes1[0].set_ylabel('Profundidad z (cm)')
axes1[0].set_title('(a) Mapa W(z,t) — Humedad base seca')
axes1[0].set_xlim(0, 8)
axes1[0].xaxis.set_minor_locator(AutoMinorLocator())

axes1[1].plot(t_h, T_surf_hist, color='#8e44ad', lw=1.8, label='$T$ superficie')
axes1[1].plot(t_h, T_amb_K(t_s) - 273.15, color='grey', ls='--', lw=1.2, label='$T_{amb}$')
axes1[1].set_xlabel('Tiempo (h)');  axes1[1].set_ylabel('Temperatura (°C)')
axes1[1].set_title('(b) Temperatura superficial quasi-estacionaria')
axes1[1].legend(fontsize=8);  axes1[1].set_xlim(0, 8)
axes1[1].xaxis.set_minor_locator(AutoMinorLocator())
axes1[1].yaxis.set_minor_locator(AutoMinorLocator())

fig1.suptitle('Modelo PDE — Evolución espacio-temporal en la cama de café',
              fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('./pde_mapa_espacio_tiempo.png')
plt.close()
print("  [✓] pde_mapa_espacio_tiempo.png guardada")

# ═══════════════════════════════════════════════════════════
# 7. FIGURA 2 — PERFILES W(z) A DISTINTOS TIEMPOS
# ═══════════════════════════════════════════════════════════

instantes_h  = [0, 2, 4, 6, 8]
instantes_idx = [int(h*3600/dt) for h in instantes_h]
col_p = plt.cm.viridis(np.linspace(0, 1, len(instantes_h)))

fig2, ax2 = plt.subplots(figsize=(5, 4.5))
for k, (idx, h) in enumerate(zip(instantes_idx, instantes_h)):
    # z va de 0 (fondo) a L (superficie); invertimos eje para superficie arriba
    ax2.plot(W_hist[idx], z*100, color=col_p[k], lw=1.8, label=f't = {h} h')
ax2.axvline(W_eq, color='#c0392b', ls='--', lw=1.2, label=f'$W_{{eq}}={W_eq}$')
ax2.set_xlabel('Humedad base seca $W$ (kg/kg)')
ax2.set_ylabel('Profundidad z (cm)  [superficie ↑]')
ax2.set_title('Perfiles $W(z,t)$ en la cama de café')
ax2.legend(fontsize=8)
ax2.invert_yaxis();  ax2.set_ylim(L_bed*100, 0)
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
plt.tight_layout()
plt.savefig('./pde_perfiles.png')
plt.close()
print("  [✓] pde_perfiles.png guardada")

# ═══════════════════════════════════════════════════════════
# 8. FIGURA 3 — HISTORIAL W(t) POR PROFUNDIDAD
# ═══════════════════════════════════════════════════════════

prof_cm  = [0, 1, 2, 3, 4]   # cm desde la superficie
col_hist = plt.cm.plasma(np.linspace(0.1, 0.9, len(prof_cm)))

fig3, ax3 = plt.subplots(figsize=(5.5, 4))
for k, d in enumerate(prof_cm):
    z_pos = L_bed - d/100.0
    i_z   = np.argmin(np.abs(z - z_pos))
    lbl   = 'Superficie' if d == 0 else f'{d} cm de prof.'
    ax3.plot(t_h, W_hist[:, i_z], color=col_hist[k], lw=1.6, label=lbl)
ax3.axhline(W_eq, color='#c0392b', ls='--', lw=1.2, label=f'$W_{{eq}}$')
ax3.set_xlabel('Tiempo (h)');  ax3.set_ylabel('$W$ (kg/kg bs)')
ax3.set_title('Humedad $W(t)$ según profundidad desde la superficie')
ax3.legend(fontsize=8, title='Posición')
ax3.set_xlim(0, 8)
ax3.xaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())
plt.tight_layout()
plt.savefig('./pde_historiales.png')
plt.close()
print("  [✓] pde_historiales.png guardada")

# ═══════════════════════════════════════════════════════════
# 9. FIGURA 4 — COMPARACIÓN PDE vs ODE (MODELO POR CAPAS)
# ═══════════════════════════════════════════════════════════

# Recalcular modelo ODE por capas (mismo dt y t_fin)
C_q_ode = 1.14e-7; gamma_ode = 0.85; hc_ode = 15.0; Tc_ode = 293.15
lam_ode = 2.26e6;  n_cap = 5;  prof_ode = 0.04;  kext_ode = 25.0

def Pv(T_K):
    return (10**(8.07131 - 1730.63/(233.426 + T_K - 273.15))) * 133.322

def Qdot_ode(t_s):
    Te = T_amb_K(t_s)
    return C_q_ode * hc_ode * (Pv(Tc_ode) + gamma_ode * Pv(Te))

facs = np.exp(-kext_ode * ((np.arange(n_cap)+0.5) * prof_ode / n_cap))

# masa de agua inicial por grano
a_g = 0.0055; b_g = 0.0042
V_g = (4/3)*np.pi*a_g*b_g**2
m_g = 1200.0*V_g
f_a = 0.55/1.55
m_agua_g0 = m_g * f_a

# Integración ODE (RK4) por capa
x_cap = np.zeros((n_cap, N_t, 2))   # [U_e, m_evap]

def rk4_ode(t_n, x_n, h, fac):
    def f(t, x):
        Q = fac * Qdot_ode(t)
        return np.array([Q, Q/lam_ode])
    k1 = h*f(t_n,       x_n)
    k2 = h*f(t_n+h/2,   x_n+k1/2)
    k3 = h*f(t_n+h/2,   x_n+k2/2)
    k4 = h*f(t_n+h,     x_n+k3)
    return x_n + (k1+2*k2+2*k3+k4)/6

for n in range(N_t - 1):
    for i in range(n_cap):
        nxt = rk4_ode(t_s[n], x_cap[i, n], dt, facs[i])
        nxt[1] = min(nxt[1], m_agua_g0)
        x_cap[i, n+1] = nxt

# Convertir m_evap a humedad base seca W_ode(i, t)
m_seco_g = m_g * (1 - f_a)
W_ode = np.zeros((n_cap, N_t))
for i in range(n_cap):
    m_agua_i = np.clip(m_agua_g0 - x_cap[i, :, 1], 0, m_agua_g0)
    W_ode[i] = m_agua_i / m_seco_g   # base seca

# Centroides de las capas ODE como profundidad desde la superficie [cm]
z_ode_cm = [(i + 0.5) * prof_ode / n_cap * 100 for i in range(n_cap)]

fig4, axes4 = plt.subplots(1, 2, figsize=(10, 4.5))

for ax, t_idx, titulo in zip(axes4,
                              [int(4*3600/dt), N_t-1],
                              ['t = 4 h', 't = 8 h']):
    # PDE: perfil continuo  (profundidad desde superficie = L_bed - z)
    depth_cm = (L_bed - z) * 100
    ax.plot(W_hist[t_idx], depth_cm, color='#1a5276', lw=2.0,
            label='PDE (Crank-Nicolson)')

    # ODE: puntos discretos por capa
    ax.scatter(W_ode[:, t_idx], z_ode_cm,
               color='#c0392b', s=70, zorder=5, label='ODE (capas RK4)')

    ax.axvline(W_eq, color='grey', ls=':', lw=1.2, label=f'$W_{{eq}}$')
    ax.set_xlabel('Humedad base seca $W$ (kg/kg)')
    ax.set_ylabel('Profundidad desde la superficie (cm)')
    ax.set_title(f'Comparación PDE vs ODE — {titulo}')
    ax.legend(fontsize=8)
    ax.set_ylim(0, L_bed*100);  ax.invert_yaxis()
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

fig4.suptitle('Comparación del perfil de humedad: Modelo PDE vs Modelo ODE por Capas',
              fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('./pde_comparacion_ode.png')
plt.close()
print("  [✓] pde_comparacion_ode.png guardada")
print("\n  Todas las figuras PDE generadas.")
