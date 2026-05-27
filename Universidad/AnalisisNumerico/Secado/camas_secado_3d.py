"""
Modelo 3D de Camas de Secado de Café — Diseño Conceptual Detallado
Incluye: estructura elevada, bastidor, malla, capa de café (5 capas)
y ensamble completo dentro de la marquesina.

Politécnico Colombiano Jaime Isaza Cadavid
Facultad de Ingeniería — Rionegro, Antioquia, Colombia
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D          # noqa: F401
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ═══════════════════════════════════════════════════════════════════
# PARÁMETROS ESTRUCTURALES
# ═══════════════════════════════════════════════════════════════════

# Marquesina
L_marq  = 10.0   # longitud [m]
W_marq  = 4.0    # ancho [m]
H_lat   = 1.8    # altura paredes laterales [m]
H_cumbr = 2.8    # altura cumbrera [m]

# Camas de secado (2 camas paralelas con pasillo central)
H_cama   = 0.80   # altura de las patas [m]
W_cama   = 1.60   # ancho de cada cama [m]
e_pared  = 0.05   # margen lateral desde la pared [m]  (0.05×2 = 0.10 total)
pasillo  = W_marq - 2*e_pared - 2*W_cama   # 4 - 0.10 - 3.20 = 0.70 m
y_c1     = e_pared                           # borde Y cama 1
y_c2     = e_pared + W_cama + pasillo        # borde Y cama 2

# Bastidor de madera del armazón de cama
t_bastidor = 0.05   # espesor del bastidor [m]
paso_pata  = 2.0    # distancia entre patas a lo largo de X [m]

# Capa de café
prof_cafe = 0.04    # profundidad capa café [m]
n_capas   = 5
dz_capa   = prof_cafe / n_capas

# Malla (representada como puntos de la grilla)
paso_malla = 0.15   # separación de la malla [m]

# ═══════════════════════════════════════════════════════════════════
# COLORES
# ═══════════════════════════════════════════════════════════════════
BROWN   = '#4e342e'
WOOD    = '#8d6e63'
MALLA   = '#90a4ae'
POLY    = '#b3e5fc'
CAFE    = ['#d32f2f','#e64a19','#f57c00','#fbc02d','#388e3c']
PISO    = '#efebe9'
GRIS    = '#b0bec5'

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 9,
    'axes.titlesize': 9.5, 'figure.dpi': 180,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

# ═══════════════════════════════════════════════════════════════════
# HELPERS 3D
# ═══════════════════════════════════════════════════════════════════

def quad(ax, pts, fc, ec='none', alpha=0.18, lw=0.5, zorder=1):
    p = Poly3DCollection([pts], alpha=alpha, zorder=zorder)
    p.set_facecolor(fc); p.set_edgecolor(ec); p.set_linewidth(lw)
    ax.add_collection3d(p)

def seg(ax, p1, p2, c=BROWN, lw=1.4, ls='-', alpha=1.0):
    ax.plot([p1[0],p2[0]], [p1[1],p2[1]], [p1[2],p2[2]],
            color=c, lw=lw, ls=ls, alpha=alpha, solid_capstyle='round')

def box(ax, x0,x1,y0,y1,z0,z1, fc, ec=BROWN, alpha=0.85, lw=0.6):
    """Paralelepípedo sólido (6 caras)."""
    faces = [
        [[x0,y0,z0],[x1,y0,z0],[x1,y1,z0],[x0,y1,z0]],  # bottom
        [[x0,y0,z1],[x1,y0,z1],[x1,y1,z1],[x0,y1,z1]],  # top
        [[x0,y0,z0],[x1,y0,z0],[x1,y0,z1],[x0,y0,z1]],  # front
        [[x0,y1,z0],[x1,y1,z0],[x1,y1,z1],[x0,y1,z1]],  # back
        [[x0,y0,z0],[x0,y1,z0],[x0,y1,z1],[x0,y0,z1]],  # left
        [[x1,y0,z0],[x1,y1,z0],[x1,y1,z1],[x1,y0,z1]],  # right
    ]
    for f in faces:
        quad(ax, f, fc, ec=ec, alpha=alpha, lw=lw, zorder=3)

# ═══════════════════════════════════════════════════════════════════
# DIBUJAR UNA CAMA DE SECADO COMPLETA
# ═══════════════════════════════════════════════════════════════════

def draw_cama(ax, y0, con_cafe=True, con_malla=True, alpha_cafe=0.85):
    """
    Dibuja una cama de secado elevada entre x=[0,L_marq] y y=[y0, y0+W_cama].
    La base de la cama está a z=0; las patas suben hasta H_cama.
    """
    y1   = y0 + W_cama
    z_m  = H_cama                  # z de la malla (superficie inferior del bastidor)
    z_b  = H_cama + t_bastidor     # z de la superficie superior del bastidor
    z_cf = z_b + prof_cafe         # z del tope de la capa de café

    tb = t_bastidor

    # ── Patas (cada paso_pata metros) ──────────────────────────────
    xs_pata = np.arange(0, L_marq + 0.01, paso_pata)
    for xp in xs_pata:
        for yp in [y0, y1]:
            box(ax, xp-0.025, xp+0.025, yp-0.025, yp+0.025, 0, H_cama,
                fc=BROWN, alpha=0.95, lw=0.4)

    # Riostras transversales bajas (a media altura)
    z_riostra = H_cama * 0.45
    for xp in xs_pata:
        seg(ax, (xp, y0, z_riostra), (xp, y1, z_riostra), WOOD, lw=0.8, alpha=0.7)

    # Riostras longitudinales inferiores
    for yp in [y0+0.05, y1-0.05]:
        seg(ax, (0, yp, z_riostra), (L_marq, yp, z_riostra), WOOD, lw=0.6, alpha=0.5, ls='--')

    # ── Bastidor perimetral (4 vigas del marco) ────────────────────
    # Vigas longitudinales (a lo largo de X)
    for yp in [y0, y1]:
        box(ax, 0, L_marq, yp, yp+tb if yp==y0 else yp-tb, z_m, z_b,
            fc=WOOD, alpha=0.95, lw=0.4)

    # Vigas transversales (en x=0 y x=L_marq)
    for xp in [0, L_marq]:
        box(ax, xp, xp+tb if xp==0 else xp-tb, y0+tb, y1-tb, z_m, z_b,
            fc=WOOD, alpha=0.95, lw=0.4)

    # Travesaños intermedios cada paso_pata
    for xp in xs_pata[1:-1]:
        box(ax, xp-0.025, xp+0.025, y0+tb, y1-tb, z_m, z_b,
            fc=WOOD, alpha=0.90, lw=0.4)

    # ── Malla (grilla de alambres) ─────────────────────────────────
    if con_malla:
        xs_m = np.arange(tb, L_marq - tb + 0.01, paso_malla)
        ys_m = np.arange(y0+tb, y1-tb + 0.01, paso_malla)
        for xm in xs_m:
            seg(ax, (xm, y0+tb, z_m), (xm, y1-tb, z_m), MALLA, lw=0.4, alpha=0.5)
        for ym in ys_m:
            seg(ax, (0+tb, ym, z_m), (L_marq-tb, ym, z_m), MALLA, lw=0.4, alpha=0.5)

    # ── Capas de café (5 capas con colores) ───────────────────────
    if con_cafe:
        for i in range(n_capas):
            # i=0 es la capa superior (mayor exposición solar)
            # z crece desde z_b (fondo de la cama) hacia arriba
            zi0 = z_b + i * dz_capa
            zi1 = z_b + (i+1) * dz_capa
            # Solo mostramos la cara superior de cada capa y frentes
            quad(ax,
                 [[0+tb, y0+tb, zi1],[L_marq-tb, y0+tb, zi1],
                  [L_marq-tb, y1-tb, zi1],[0+tb, y1-tb, zi1]],
                 CAFE[n_capas-1-i], ec='none', alpha=alpha_cafe*0.7, zorder=4)
        # Frente de capas visible (en y=y0)
        for i in range(n_capas):
            zi0 = z_b + i * dz_capa
            zi1 = z_b + (i+1) * dz_capa
            quad(ax,
                 [[0+tb, y0+tb, zi0],[L_marq-tb, y0+tb, zi0],
                  [L_marq-tb, y0+tb, zi1],[0+tb, y0+tb, zi1]],
                 CAFE[n_capas-1-i], ec='none', alpha=alpha_cafe, zorder=5)
        # Frente lateral izquierdo (en x=0)
        for i in range(n_capas):
            zi0 = z_b + i * dz_capa
            zi1 = z_b + (i+1) * dz_capa
            quad(ax,
                 [[tb, y0+tb, zi0],[tb, y1-tb, zi0],
                  [tb, y1-tb, zi1],[tb, y0+tb, zi1]],
                 CAFE[n_capas-1-i], ec='none', alpha=alpha_cafe, zorder=5)

    return z_b, z_b + prof_cafe   # retorna rango Z de la capa de café


# ═══════════════════════════════════════════════════════════════════
# DIBUJAR ESTRUCTURA DE MARQUESINA (simplificada)
# ═══════════════════════════════════════════════════════════════════

def draw_marquesina_shell(ax):
    """Estructura liviana de la marquesina (sin detalles de cama)."""
    L, W = L_marq, W_marq
    Hl, Hc = H_lat, H_cumbr

    # Piso
    quad(ax, [[0,0,0],[L,0,0],[L,W,0],[0,W,0]], PISO, ec=BROWN, alpha=0.25, lw=0.5)

    # Columnas
    for xc in np.linspace(0, L, 6):
        for yc in [0, W]:
            seg(ax, (xc,yc,0), (xc,yc,Hl), BROWN, lw=1.8)

    # Vigas perimetrales altas
    seg(ax,(0,0,Hl),(L,0,Hl),BROWN,lw=1.4)
    seg(ax,(0,W,Hl),(L,W,Hl),BROWN,lw=1.4)
    seg(ax,(0,0,0),(0,W,0),  BROWN,lw=1.0,alpha=0.5)
    seg(ax,(L,0,0),(L,W,0),  BROWN,lw=1.0,alpha=0.5)

    # Cumbrera
    seg(ax,(0,W/2,Hc),(L,W/2,Hc),BROWN,lw=2.0)

    # Cerchas
    for xv in np.linspace(0, L, 6):
        seg(ax,(xv,0,Hl),(xv,W/2,Hc),WOOD,lw=0.9,alpha=0.8)
        seg(ax,(xv,W/2,Hc),(xv,W,Hl),WOOD,lw=0.9,alpha=0.8)

    # Paneles de techo
    for y0t, yct in [(0, W/2), (W/2, W)]:
        panel = [
            [0, y0t, Hl if y0t==0 else Hc],
            [L, y0t, Hl if y0t==0 else Hc],
            [L, yct, Hc if y0t==0 else Hl],
            [0, yct, Hc if y0t==0 else Hl],
        ]
        quad(ax, panel, POLY, ec=GRIS, alpha=0.10, lw=0.4)

    # Paredes laterales (malla)
    for yp in [0, W]:
        quad(ax,[[0,yp,0],[L,yp,0],[L,yp,Hl],[0,yp,Hl]],
             '#90a4ae',ec='#607d8b',alpha=0.07,lw=0.3)


# ═══════════════════════════════════════════════════════════════════
# FIGURA 1 — CAMAS EN LA MARQUESINA (vista isométrica completa)
# ═══════════════════════════════════════════════════════════════════

fig1 = plt.figure(figsize=(14, 7))
ax1  = fig1.add_subplot(111, projection='3d')

draw_marquesina_shell(ax1)
draw_cama(ax1, y_c1, con_cafe=True, con_malla=True)
draw_cama(ax1, y_c2, con_cafe=True, con_malla=True)

# Pasillo — flechas de texto
ax1.text(L_marq/2, y_c1+W_cama+pasillo/2, 0.02,
         f'Pasillo\n{pasillo:.2f} m', ha='center', va='bottom',
         fontsize=7.5, color='#1565c0',
         bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.7))

# Cotas de camas
off = 0.3
seg(ax1,(0,-off,H_cama),(L_marq,-off,H_cama),'#1565c0',lw=0.9)
ax1.text(L_marq/2,-off-0.15,H_cama,f'L={L_marq:.0f} m',
         ha='center',va='top',fontsize=7.5,color='#1565c0')

seg(ax1,(-off,y_c1,H_cama),(-off,y_c1+W_cama,H_cama),'#6a1b9a',lw=0.9)
ax1.text(-off-0.1,y_c1+W_cama/2,H_cama,f'W_c={W_cama:.2f} m',
         ha='right',va='center',fontsize=7,color='#6a1b9a',rotation=0)

seg(ax1,(L_marq+off,0,0),(L_marq+off,0,H_cama),'#b71c1c',lw=0.9)
ax1.text(L_marq+off+0.05,0,H_cama/2,f'h={H_cama:.2f} m',
         ha='left',va='center',fontsize=7,color='#b71c1c')

# Leyenda capas
patches = [mpatches.Patch(color=CAFE[n_capas-1-i],
           label=f'Capa {i+1}  (sup→fondo): f={np.exp(-25*(i+0.5)*dz_capa):.3f}')
           for i in range(n_capas)]
patches += [
    mpatches.Patch(color=WOOD,  alpha=0.9, label='Bastidor de madera'),
    mpatches.Patch(color=MALLA, alpha=0.8, label='Malla metálica'),
    mpatches.Patch(color=BROWN, alpha=0.9, label='Patas estructurales'),
]
ax1.legend(handles=patches, fontsize=6.5, loc='upper left',
           bbox_to_anchor=(0.0, 1.02), title='Componentes de la cama',
           title_fontsize=7, framealpha=0.88)

ax1.set_xlim(-0.5, L_marq+1.2)
ax1.set_ylim(-0.7, W_marq+0.3)
ax1.set_zlim(0, H_cumbr+0.2)
ax1.set_xlabel('Longitud X (m)', labelpad=6, fontsize=8)
ax1.set_ylabel('Ancho Y (m)',    labelpad=6, fontsize=8)
ax1.set_zlabel('Altura Z (m)',   labelpad=6, fontsize=8)
ax1.set_title(
    f'Marquesina de Secado con Camas Elevadas\n'
    f'2 camas × {W_cama:.2f} m ancho  |  '
    f'Pasillo central {pasillo:.2f} m  |  '
    f'Altura de camas {H_cama:.2f} m',
    fontsize=9, fontweight='bold', pad=10)
ax1.view_init(elev=22, azim=-52)
ax1.tick_params(labelsize=7)

plt.tight_layout()
plt.savefig('./camas_en_marquesina.png')
plt.close()
print("  [✓] camas_en_marquesina.png guardada")


# ═══════════════════════════════════════════════════════════════════
# FIGURA 2 — DETALLE ISOMÉTRICO DE UNA SOLA CAMA
# ═══════════════════════════════════════════════════════════════════

fig2 = plt.figure(figsize=(13, 5.5))

# ─── 2a: Vista completa de una cama (sin marquesina) ────────────────
ax2a = fig2.add_subplot(121, projection='3d')

# Dibujamos solo una cama con L=4m (sección representativa)
L_rep = 4.0
W_marq_rep = W_cama + 0.1

def draw_cama_detalle(ax, y0=0.05, L=4.0):
    """Dibuja una cama individual con fragmento de L metros."""
    y1   = y0 + W_cama
    z_m  = H_cama
    z_b  = H_cama + t_bastidor
    tb   = t_bastidor

    xs_pata = np.arange(0, L + 0.01, paso_pata)

    # Patas
    for xp in xs_pata:
        for yp in [y0, y1]:
            box(ax, xp-0.03, xp+0.03, yp-0.03, yp+0.03, 0, H_cama,
                fc=BROWN, alpha=0.95, lw=0.4)

    # Riostras transversales
    for xp in xs_pata:
        seg(ax,(xp,y0,H_cama*0.4),(xp,y1,H_cama*0.4),WOOD,lw=1.0,alpha=0.75)

    # Riostras diagonales (cruces de San Andrés)
    for xi in range(len(xs_pata)-1):
        x0r, x1r = xs_pata[xi], xs_pata[xi+1]
        for yp in [y0+0.04, y1-0.04]:
            seg(ax,(x0r,yp,0),(x1r,yp,H_cama*0.75),WOOD,lw=0.6,alpha=0.5,ls='--')
            seg(ax,(x1r,yp,0),(x0r,yp,H_cama*0.75),WOOD,lw=0.6,alpha=0.5,ls='--')

    # Bastidor: vigas longitudinales
    box(ax, 0, L, y0, y0+tb, z_m, z_b, fc=WOOD, alpha=0.95, lw=0.4)
    box(ax, 0, L, y1-tb, y1, z_m, z_b, fc=WOOD, alpha=0.95, lw=0.4)
    # Vigas transversales extremos y travesaños
    for xp in np.concatenate(([0], xs_pata[1:-1], [L])):
        box(ax, xp-0.025, xp+0.025, y0+tb, y1-tb, z_m, z_b,
            fc=WOOD, alpha=0.90, lw=0.4)

    # Malla
    for xm in np.arange(tb, L-tb+0.01, paso_malla):
        seg(ax,(xm,y0+tb,z_m),(xm,y1-tb,z_m),MALLA,lw=0.5,alpha=0.55)
    for ym in np.arange(y0+tb, y1-tb+0.01, paso_malla):
        seg(ax,(tb,ym,z_m),(L-tb,ym,z_m),MALLA,lw=0.5,alpha=0.55)

    # Capas de café
    for i in range(n_capas):
        zi0 = z_b + i*dz_capa
        zi1 = z_b + (i+1)*dz_capa
        c   = CAFE[n_capas-1-i]
        # cara superior
        quad(ax,[[tb,y0+tb,zi1],[L-tb,y0+tb,zi1],[L-tb,y1-tb,zi1],[tb,y1-tb,zi1]],
             c, ec='none', alpha=0.65, zorder=4)
        # cara frontal (y=y0)
        quad(ax,[[tb,y0+tb,zi0],[L-tb,y0+tb,zi0],[L-tb,y0+tb,zi1],[tb,y0+tb,zi1]],
             c, ec='none', alpha=0.90, zorder=5)
        # cara lateral (x=0)
        quad(ax,[[tb,y0+tb,zi0],[tb,y1-tb,zi0],[tb,y1-tb,zi1],[tb,y0+tb,zi1]],
             c, ec='none', alpha=0.90, zorder=5)

    # Cotas con líneas
    col_c = '#1565c0'
    # Longitud
    seg(ax,(0,y0-0.12,0),(L,y0-0.12,0),col_c,lw=0.8)
    ax.text(L/2,y0-0.2,0,f'{L:.0f} m',ha='center',va='top',fontsize=7,color=col_c)
    # Ancho
    seg(ax,(0,y0,H_cama+0.12),(0,y1,H_cama+0.12),col_c,lw=0.8)
    ax.text(0,(y0+y1)/2,H_cama+0.22,f'{W_cama:.2f} m',
            ha='center',va='bottom',fontsize=7,color=col_c)
    # Altura patas
    seg(ax,(L+0.15,y1,0),(L+0.15,y1,H_cama),'#b71c1c',lw=0.8)
    ax.text(L+0.2,y1,H_cama/2,f'{H_cama:.2f} m',
            ha='left',va='center',fontsize=6.5,color='#b71c1c')
    # Espesor café
    seg(ax,(L+0.15,y1,z_b),(L+0.15,y1,z_b+prof_cafe),'#388e3c',lw=1.0)
    ax.text(L+0.2,y1,z_b+prof_cafe/2,f'{prof_cafe*100:.0f} cm\ncafé',
            ha='left',va='center',fontsize=6,color='#388e3c')

draw_cama_detalle(ax2a, y0=0.05, L=4.0)

ax2a.set_xlim(-0.2, 4.8); ax2a.set_ylim(-0.3, W_cama+0.3); ax2a.set_zlim(0, 1.05)
ax2a.set_xlabel('X (m)', fontsize=7.5, labelpad=4)
ax2a.set_ylabel('Y (m)', fontsize=7.5, labelpad=4)
ax2a.set_zlabel('Z (m)', fontsize=7.5, labelpad=4)
ax2a.set_title('(a) Cama de secado — Vista isométrica\n(sección de 4 m, estructura completa)',
               fontsize=8.5, pad=6)
ax2a.view_init(elev=24, azim=-48)
ax2a.tick_params(labelsize=6.5)

# ─── 2b: Vista del extremo (sección transversal 3D) ─────────────────
ax2b = fig2.add_subplot(122, projection='3d')
draw_cama_detalle(ax2b, y0=0.05, L=4.0)

ax2b.set_xlim(-0.2, 4.8); ax2b.set_ylim(-0.3, W_cama+0.3); ax2b.set_zlim(0, 1.05)
ax2b.set_xlabel('X (m)', fontsize=7.5, labelpad=4)
ax2b.set_ylabel('Y (m)', fontsize=7.5, labelpad=4)
ax2b.set_zlabel('Z (m)', fontsize=7.5, labelpad=4)
ax2b.set_title('(b) Cama de secado — Vista frontal\n(detalle de capas en la sección X=0)',
               fontsize=8.5, pad=6)
ax2b.view_init(elev=12, azim=-90)
ax2b.tick_params(labelsize=6.5)

patches_d = [mpatches.Patch(color=CAFE[n_capas-1-i],
             label=f'Capa {i+1}: f={np.exp(-25*(i+0.5)*dz_capa):.3f}')
             for i in range(n_capas)]
patches_d += [
    mpatches.Patch(color=WOOD,  label='Bastidor'),
    mpatches.Patch(color=MALLA, label='Malla'),
    mpatches.Patch(color=BROWN, label='Pata'),
]
fig2.legend(handles=patches_d, fontsize=6.5, loc='lower center',
            ncol=4, title='Componentes', title_fontsize=7,
            bbox_to_anchor=(0.5, -0.01), framealpha=0.9)

fig2.suptitle('Detalle Estructural de la Cama de Secado Elevada\n'
              f'Patas cada {paso_pata:.0f} m  |  Bastidor {t_bastidor*100:.0f} cm  |  '
              f'Malla paso {paso_malla*100:.0f} cm  |  Café {prof_cafe*100:.0f} cm ({n_capas} capas)',
              fontsize=9, fontweight='bold')
plt.tight_layout(rect=[0,0.06,1,1])
plt.savefig('./camas_detalle_estructural.png')
plt.close()
print("  [✓] camas_detalle_estructural.png guardada")


# ═══════════════════════════════════════════════════════════════════
# FIGURA 3 — PLANO TÉCNICO 2D (sección transversal + planta)
# ═══════════════════════════════════════════════════════════════════

fig3 = plt.figure(figsize=(14, 9))
gs   = gridspec.GridSpec(2, 2, figure=fig3,
                          height_ratios=[1.6, 1], hspace=0.38, wspace=0.32)

# ── 3a: Sección transversal (Y-Z) ─────────────────────────────────
ax3a = fig3.add_subplot(gs[0, :])
ax3a.set_facecolor('#f5f5f5')
ax3a.set_aspect('equal')

z_b = H_cama + t_bastidor

# Piso
ax3a.fill_between([0, W_marq], [-0.06]*2, [0]*2, color='#bcaaa4', zorder=1)
ax3a.plot([0, W_marq],[0,0],color=BROWN,lw=1.5,zorder=2)

# Columnas marquesina
for yp in [0, W_marq]:
    ax3a.fill_between([yp-0.04, yp+0.04], [0]*2, [H_lat]*2,
                      color=BROWN, alpha=0.9, zorder=5)

# Techo marquesina
ax3a.plot([0, W_marq/2, W_marq],[H_lat, H_cumbr, H_lat],color=BROWN,lw=2.0,zorder=5)
ax3a.fill([0, W_marq/2, W_marq, W_marq, 0],
          [H_lat, H_cumbr, H_lat, H_lat-0.04, H_lat-0.04],
          color=POLY,alpha=0.30,zorder=4)

# Cama 1
for i in range(n_capas):
    zi0 = z_b + i*dz_capa; zi1 = z_b + (i+1)*dz_capa
    ax3a.fill_between([y_c1, y_c1+W_cama], [zi0]*2, [zi1]*2,
                      color=CAFE[i], alpha=0.80, zorder=4)
    ax3a.text(y_c1+W_cama/2, (zi0+zi1)/2,
              f'C{i+1}  f={np.exp(-25*((i+0.5)*dz_capa)):.3f}',
              ha='center', va='center', fontsize=6.5,
              color='white', fontweight='bold')

# Bastidor cama 1
ax3a.fill_between([y_c1, y_c1+W_cama],[H_cama]*2,[z_b]*2,
                  color=WOOD, alpha=0.85, zorder=3)
ax3a.plot([y_c1, y_c1+W_cama],[H_cama,H_cama],color=MALLA,lw=1.2,ls='--',alpha=0.7)

# Patas cama 1
for yp in [y_c1+0.03, y_c1+W_cama-0.03]:
    ax3a.fill_between([yp-0.025, yp+0.025],[0]*2,[H_cama]*2,
                      color=BROWN,alpha=0.9,zorder=5)

# Cama 2
for i in range(n_capas):
    zi0 = z_b + i*dz_capa; zi1 = z_b + (i+1)*dz_capa
    ax3a.fill_between([y_c2, y_c2+W_cama], [zi0]*2, [zi1]*2,
                      color=CAFE[i], alpha=0.80, zorder=4)
    ax3a.text(y_c2+W_cama/2, (zi0+zi1)/2,
              f'C{i+1}  f={np.exp(-25*((i+0.5)*dz_capa)):.3f}',
              ha='center', va='center', fontsize=6.5,
              color='white', fontweight='bold')
ax3a.fill_between([y_c2, y_c2+W_cama],[H_cama]*2,[z_b]*2,
                  color=WOOD, alpha=0.85, zorder=3)
ax3a.plot([y_c2, y_c2+W_cama],[H_cama,H_cama],color=MALLA,lw=1.2,ls='--',alpha=0.7)
for yp in [y_c2+0.03, y_c2+W_cama-0.03]:
    ax3a.fill_between([yp-0.025, yp+0.025],[0]*2,[H_cama]*2,
                      color=BROWN,alpha=0.9,zorder=5)

# Pasillo
y_pas_0 = y_c1+W_cama; y_pas_1 = y_c2
ax3a.fill_between([y_pas_0, y_pas_1],[0]*2,[0.12]*2,
                  color='#b0bec5', alpha=0.4, zorder=2)
ax3a.annotate('', xy=(y_pas_1, -0.04), xytext=(y_pas_0, -0.04),
              arrowprops=dict(arrowstyle='<->', color='#1565c0', lw=1.0))
ax3a.text((y_pas_0+y_pas_1)/2, -0.065, f'Pasillo\n{pasillo:.2f} m',
          ha='center', va='top', fontsize=7.5, color='#1565c0')

# Flechas de radiación solar
for y_r in np.linspace(0.4, W_marq-0.4, 6):
    ax3a.annotate('', xy=(y_r, z_b+prof_cafe+0.01),
                  xytext=(y_r, H_cumbr-0.15),
                  arrowprops=dict(arrowstyle='->', color='#f57f17', lw=1.0))
ax3a.text(W_marq/2, H_cumbr+0.06, 'Radiación solar + convección',
          ha='center', fontsize=8, color='#f57f17', style='italic')

# Cotas
cc = '#1a237e'
ax3a.annotate('',xy=(W_marq,-0.14),xytext=(0,-0.14),
              arrowprops=dict(arrowstyle='<->',color=cc,lw=1.0))
ax3a.text(W_marq/2,-0.17,f'Ancho total = {W_marq:.1f} m',
          ha='center',va='top',fontsize=8,color=cc)
ax3a.annotate('',xy=(W_marq+0.25,H_lat),xytext=(W_marq+0.25,0),
              arrowprops=dict(arrowstyle='<->',color='#6a1b9a',lw=1.0))
ax3a.text(W_marq+0.30,H_lat/2,f'H_l={H_lat}m',ha='left',va='center',
          fontsize=7,color='#6a1b9a')
ax3a.annotate('',xy=(W_marq/2-0.2,H_cumbr),xytext=(W_marq/2-0.2,0),
              arrowprops=dict(arrowstyle='<->',color='#6a1b9a',lw=1.0))
ax3a.text(W_marq/2-0.25,H_cumbr*0.55,f'H_c={H_cumbr}m',ha='right',va='center',
          fontsize=7,color='#6a1b9a',rotation=90)
ax3a.annotate('',xy=(y_c1-0.18,z_b+prof_cafe),xytext=(y_c1-0.18,0),
              arrowprops=dict(arrowstyle='<->',color='#b71c1c',lw=1.0))
ax3a.text(y_c1-0.21,H_cama/2,f'h={H_cama}m',ha='right',va='center',
          fontsize=7,color='#b71c1c',rotation=90)

ax3a.text(y_c1+W_cama/2, z_b+prof_cafe+0.03, 'CAMA 1',
          ha='center', fontsize=8, fontweight='bold', color=BROWN)
ax3a.text(y_c2+W_cama/2, z_b+prof_cafe+0.03, 'CAMA 2',
          ha='center', fontsize=8, fontweight='bold', color=BROWN)

ax3a.set_xlim(-0.3, W_marq+0.55); ax3a.set_ylim(-0.25, H_cumbr+0.25)
ax3a.set_xlabel('Posición transversal Y (m)', fontsize=9)
ax3a.set_ylabel('Altura Z (m)', fontsize=9)
ax3a.set_title('(a) Sección transversal A–A — Marquesina con camas de secado elevadas',
               fontsize=9.5, fontweight='bold')
ax3a.grid(True, alpha=0.2, ls='--')
ax3a.tick_params(labelsize=8)

# ── 3b: Plano de planta ────────────────────────────────────────────
ax3b = fig3.add_subplot(gs[1, 0])
ax3b.set_facecolor('#eceff1')
ax3b.set_aspect('equal')

# Contorno
rect_m = plt.Polygon([[0,0],[L_marq,0],[L_marq,W_marq],[0,W_marq]],
                      fill=False, edgecolor=BROWN, lw=1.8, zorder=5)
ax3b.add_patch(rect_m)

# Camas
for (ya, yb) in [(y_c1, y_c1+W_cama), (y_c2, y_c2+W_cama)]:
    rect_c = plt.Polygon([[0.05,ya],[L_marq-0.05,ya],
                           [L_marq-0.05,yb],[0.05,yb]],
                          facecolor='#a1887f', alpha=0.5,
                          edgecolor=BROWN, lw=1.0, zorder=3)
    ax3b.add_patch(rect_c)
    ax3b.text(L_marq/2, (ya+yb)/2, f'CAMA DE SECADO\n{L_marq:.0f} m × {W_cama:.2f} m',
              ha='center', va='center', fontsize=7.5, color='#3e2723', fontweight='bold')

# Pasillo
rect_p = plt.Polygon([[0,y_c1+W_cama],[L_marq,y_c1+W_cama],
                        [L_marq,y_c2],[0,y_c2]],
                       facecolor='#e0f7fa', alpha=0.6, edgecolor='#0288d1',
                       lw=0.8, ls='--', zorder=3)
ax3b.add_patch(rect_p)
ax3b.text(L_marq/2,(y_c1+W_cama+y_c2)/2,'Pasillo\nde trabajo',
          ha='center',va='center',fontsize=7.5,color='#01579b',style='italic')

# Columnas
for xc in np.linspace(0, L_marq, 6):
    for yc in [0, W_marq]:
        circ = plt.Circle((xc,yc), 0.10, color=BROWN, zorder=6)
        ax3b.add_patch(circ)

# Patas de camas
for ya in [y_c1, y_c2]:
    for xp in np.arange(0, L_marq+0.01, paso_pata):
        for yp in [ya+0.04, ya+W_cama-0.04]:
            circ = plt.Circle((xp,yp), 0.05, color=WOOD, zorder=6)
            ax3b.add_patch(circ)

ax3b.plot([0,L_marq],[W_marq/2,W_marq/2],color='#b71c1c',lw=0.9,ls='-.',
          label='Eje cumbrera')

# Cotas
ax3b.annotate('',xy=(L_marq,-0.3),xytext=(0,-0.3),
              arrowprops=dict(arrowstyle='<->',color='#1565c0',lw=0.9))
ax3b.text(L_marq/2,-0.42,f'L = {L_marq:.0f} m',ha='center',va='top',
          fontsize=7.5,color='#1565c0')
ax3b.annotate('',xy=(-0.4,W_marq),xytext=(-0.4,0),
              arrowprops=dict(arrowstyle='<->',color='#1565c0',lw=0.9))
ax3b.text(-0.5,W_marq/2,f'W = {W_marq:.0f} m',ha='right',va='center',
          fontsize=7.5,color='#1565c0',rotation=90)

ax3b.set_xlim(-0.7, L_marq+0.4); ax3b.set_ylim(-0.65, W_marq+0.3)
ax3b.set_xlabel('Longitud X (m)', fontsize=8.5)
ax3b.set_ylabel('Ancho Y (m)', fontsize=8.5)
ax3b.set_title('(b) Plano de planta', fontsize=9, fontweight='bold')
ax3b.legend(fontsize=7.5, loc='upper right')
ax3b.grid(True, alpha=0.2, ls='--')
ax3b.tick_params(labelsize=7.5)

# ── 3c: Detalle de capas (ampliación) ─────────────────────────────
ax3c = fig3.add_subplot(gs[1, 1])
ax3c.set_facecolor('#fafafa')

# Ampliar sección de las capas
for i in range(n_capas):
    zi0 = i*dz_capa; zi1 = (i+1)*dz_capa
    z_mid = (i+0.5)*dz_capa
    f_i = np.exp(-25*z_mid)
    ax3c.barh(zi0*100, f_i, height=dz_capa*100*0.88,
              align='edge', color=CAFE[i], alpha=0.82,
              edgecolor='white', lw=0.7)
    ax3c.text(0.01, (zi0+zi1)/2*100,
              f'Capa {i+1}  —  z = {z_mid*100:.1f} cm  —  f = {f_i:.4f}',
              ha='left', va='center', fontsize=7.5, color='white', fontweight='bold')

ax3c.axhline(0, color=MALLA, lw=1.5, ls='--', label='Malla metálica')
ax3c.text(0.85, -0.15, 'Malla', ha='center', va='top', fontsize=7, color=MALLA)
ax3c.fill_between([0,1],[-dz_capa*100*0.5,-dz_capa*100*0.5],[0,0],
                  color=WOOD, alpha=0.5, label='Bastidor')

ax3c.set_xlim(0, 1.05); ax3c.set_ylim(-dz_capa*100*0.6, prof_cafe*100+0.2)
ax3c.invert_yaxis()
ax3c.set_xlabel('Factor de extinción  $f_i$', fontsize=8.5)
ax3c.set_ylabel('Profundidad desde la superficie (cm)', fontsize=8.5)
ax3c.set_title('(c) Gradiente de secado por capa\n'
               r'$f_i = e^{-k_{ext} z_i}$,  $k_{ext}=25\,\mathrm{m}^{-1}$',
               fontsize=9, fontweight='bold')
ax3c.legend(fontsize=7.5, loc='lower right')
ax3c.grid(True, axis='x', alpha=0.3, ls='--')
ax3c.tick_params(labelsize=7.5)
ax3c.text(1.02, -0.05, '← Sup.', ha='left', va='center',
          fontsize=7, color='#c62828', style='italic')
ax3c.text(1.02, prof_cafe*100+0.1, '← Fondo\n   (malla)', ha='left', va='top',
          fontsize=7, color='#1b5e20', style='italic')

fig3.suptitle(
    'Planos Técnicos — Marquesina de Secado Solar de Café con Camas Elevadas\n'
    f'Distribución: 2 camas × {W_cama:.2f} m ancho  |  Pasillo central {pasillo:.2f} m  |  '
    f'Cama elevada a {H_cama:.2f} m del piso',
    fontsize=10, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('./camas_planos_tecnicos.png')
plt.close()
print("  [✓] camas_planos_tecnicos.png guardada")

# ── Resumen ────────────────────────────────────────────────────────
print(f"""
  ══════════════════════════════════════════════════════
  DISEÑO CONCEPTUAL — CAMAS DE SECADO
  ══════════════════════════════════════════════════════
  Marquesina        : {L_marq:.0f} m × {W_marq:.0f} m
  Número de camas   : 2
  Dimensiones cama  : {L_marq:.0f} m × {W_cama:.2f} m cada una
  Área total secado : {2*L_marq*W_cama:.1f} m²
  Pasillo central   : {pasillo:.2f} m
  Altura de patas   : {H_cama:.2f} m
  Espesor bastidor  : {t_bastidor*100:.0f} cm
  Paso entre patas  : {paso_pata:.0f} m
  Capa de café      : {prof_cafe*100:.0f} cm ({n_capas} capas de {dz_capa*10:.1f} mm)
  Malla             : paso {paso_malla*100:.0f} cm
  ══════════════════════════════════════════════════════
  Archivos generados:
    · camas_en_marquesina.png        (ensamble completo 3D)
    · camas_detalle_estructural.png  (detalle de una cama)
    · camas_planos_tecnicos.png      (sección + planta + capas)
  ══════════════════════════════════════════════════════
""")
