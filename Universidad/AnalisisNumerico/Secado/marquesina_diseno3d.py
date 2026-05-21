"""
Diseño Conceptual 3D — Marquesina de Secado Solar de Café
Vista arquitectónica y de detalle estructural con camas elevadas

Politécnico Colombiano Jaime Isaza Cadavid
Facultad de Ingeniería — Rionegro, Antioquia, Colombia
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D          # noqa: F401
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ═══════════════════════════════════════════════════════════════════
# PARÁMETROS ESTRUCTURALES
# ═══════════════════════════════════════════════════════════════════

# Marquesina
L    = 10.0    # Longitud [m]
W    = 4.0     # Ancho [m]
H_l  = 1.8    # Altura de paredes laterales [m]
H_c  = 2.8    # Altura de cumbrera [m]

# Camas elevadas (2 camas con pasillo central)
H_cama   = 0.80    # altura de patas [m]
W_cama   = 1.50    # ancho de cada cama [m]
t_bas    = 0.05    # espesor del bastidor [m]
e_pared  = 0.10    # margen desde la pared lateral [m]
pasillo  = W - 2*e_pared - 2*W_cama   # ancho pasillo central [m]
y_c1     = e_pared                     # inicio cama 1
y_c2     = e_pared + W_cama + pasillo  # inicio cama 2

# Capa de café
prof_cafe = 0.04
n_capas   = 5
dz_capa   = prof_cafe / n_capas
paso_pata = 2.0    # distancia entre patas [m]
paso_malla = 0.15  # paso de la malla [m]

# ═══════════════════════════════════════════════════════════════════
# COLORES
# ═══════════════════════════════════════════════════════════════════
BROWN    = '#4e342e'
WOOD     = '#8d6e63'
MALLA_C  = '#90a4ae'
POLY     = '#b3e5fc'
PISO_C   = '#efebe9'
GRIS     = '#b0bec5'
CAFE_C   = ['#d32f2f','#e64a19','#f57c00','#fbc02d','#388e3c']

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 9,
    'axes.titlesize': 10, 'figure.dpi': 180,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

# ═══════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════

def quad(ax, pts, fc, ec='none', alpha=0.18, lw=0.5, zorder=1):
    p = Poly3DCollection([pts], alpha=alpha, zorder=zorder)
    p.set_facecolor(fc); p.set_edgecolor(ec); p.set_linewidth(lw)
    ax.add_collection3d(p)

def seg(ax, p1, p2, c=BROWN, lw=1.2, ls='-', alpha=1.0):
    ax.plot([p1[0],p2[0]], [p1[1],p2[1]], [p1[2],p2[2]],
            color=c, lw=lw, ls=ls, alpha=alpha, solid_capstyle='round')

def box(ax, x0,x1,y0,y1,z0,z1, fc, ec=BROWN, alpha=0.90, lw=0.5):
    faces = [
        [[x0,y0,z0],[x1,y0,z0],[x1,y1,z0],[x0,y1,z0]],
        [[x0,y0,z1],[x1,y0,z1],[x1,y1,z1],[x0,y1,z1]],
        [[x0,y0,z0],[x1,y0,z0],[x1,y0,z1],[x0,y0,z1]],
        [[x0,y1,z0],[x1,y1,z0],[x1,y1,z1],[x0,y1,z1]],
        [[x0,y0,z0],[x0,y1,z0],[x0,y1,z1],[x0,y0,z1]],
        [[x1,y0,z0],[x1,y1,z0],[x1,y1,z1],[x1,y0,z1]],
    ]
    for f in faces:
        quad(ax, f, fc, ec=ec, alpha=alpha, lw=lw, zorder=3)

# ═══════════════════════════════════════════════════════════════════
# DIBUJAR CAMA ELEVADA
# ═══════════════════════════════════════════════════════════════════

def draw_cama(ax, y0):
    """Dibuja una cama elevada de café entre y0 y y0+W_cama, a lo largo de X=[0,L]."""
    y1  = y0 + W_cama
    z_m = H_cama              # nivel de la malla
    z_b = H_cama + t_bas      # nivel del tope del bastidor (superficie del café)
    tb  = t_bas

    xs_pata = np.arange(0, L + 0.01, paso_pata)

    # Patas
    for xp in xs_pata:
        for yp in [y0, y1]:
            box(ax, xp-0.025, xp+0.025, yp-0.025, yp+0.025, 0, H_cama,
                fc=BROWN, alpha=0.95, lw=0.3)

    # Riostras transversales (a 40% de altura)
    for xp in xs_pata:
        seg(ax,(xp,y0,H_cama*0.40),(xp,y1,H_cama*0.40), WOOD, lw=0.8, alpha=0.7)

    # Riostras longitudinales bajas
    for yp in [y0+0.04, y1-0.04]:
        seg(ax,(0,yp,H_cama*0.40),(L,yp,H_cama*0.40), WOOD, lw=0.6, alpha=0.5, ls='--')

    # Bastidor perimetral: vigas longitudinales
    box(ax, 0, L, y0, y0+tb, z_m, z_b, fc=WOOD, alpha=0.95, lw=0.3)
    box(ax, 0, L, y1-tb, y1, z_m, z_b, fc=WOOD, alpha=0.95, lw=0.3)
    # Travesaños extremos e intermedios
    for xp in np.concatenate(([0], xs_pata[1:-1], [L])):
        box(ax, max(0,xp-0.025), min(L,xp+0.025), y0+tb, y1-tb, z_m, z_b,
            fc=WOOD, alpha=0.90, lw=0.3)

    # Malla metálica
    for xm in np.arange(tb, L-tb+0.01, paso_malla):
        seg(ax,(xm,y0+tb,z_m),(xm,y1-tb,z_m), MALLA_C, lw=0.4, alpha=0.50)
    for ym in np.arange(y0+tb, y1-tb+0.01, paso_malla):
        seg(ax,(tb,ym,z_m),(L-tb,ym,z_m), MALLA_C, lw=0.4, alpha=0.50)

    # Capas de café: i=0 es la capa SUPERIOR (mayor exposición solar)
    for i in range(n_capas):
        zi0 = z_b + i * dz_capa
        zi1 = z_b + (i+1) * dz_capa
        c = CAFE_C[n_capas - 1 - i]
        # Cara superior
        quad(ax,[[tb,y0+tb,zi1],[L-tb,y0+tb,zi1],[L-tb,y1-tb,zi1],[tb,y1-tb,zi1]],
             c, ec='none', alpha=0.60, zorder=4)
        # Cara frontal visible (y=y0)
        quad(ax,[[tb,y0+tb,zi0],[L-tb,y0+tb,zi0],[L-tb,y0+tb,zi1],[tb,y0+tb,zi1]],
             c, ec='none', alpha=0.88, zorder=5)
        # Cara lateral visible (x=0)
        quad(ax,[[tb,y0+tb,zi0],[tb,y1-tb,zi0],[tb,y1-tb,zi1],[tb,y0+tb,zi1]],
             c, ec='none', alpha=0.88, zorder=5)

# ═══════════════════════════════════════════════════════════════════
# DIBUJAR ESTRUCTURA DE LA MARQUESINA
# ═══════════════════════════════════════════════════════════════════

def draw_marquesina(ax, label_cotas=True):
    """Estructura completa de la marquesina con camas elevadas."""

    # Piso
    quad(ax,[[0,0,0],[L,0,0],[L,W,0],[0,W,0]], PISO_C, ec=BROWN, alpha=0.25, lw=0.5)

    # Camas de secado elevadas
    draw_cama(ax, y_c1)
    draw_cama(ax, y_c2)

    # Indicador de pasillo
    ax.text(L/2, y_c1+W_cama+pasillo/2, 0.02,
            f'Pasillo\n{pasillo:.2f} m', ha='center', va='bottom',
            fontsize=6.5, color='#01579b',
            bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.75))

    # Columnas de la marquesina
    col_x = np.linspace(0, L, 6)
    for xc in col_x:
        for yc in [0, W]:
            seg(ax,(xc,yc,0),(xc,yc,H_l), BROWN, lw=2.0)

    # Vigas perimetrales altas
    seg(ax,(0,0,H_l),(L,0,H_l), BROWN, lw=1.6)
    seg(ax,(0,W,H_l),(L,W,H_l), BROWN, lw=1.6)

    # Viga de cumbrera
    seg(ax,(0,W/2,H_c),(L,W/2,H_c), BROWN, lw=2.2)

    # Cerchas
    for xv in col_x:
        seg(ax,(xv,0,H_l),  (xv,W/2,H_c), WOOD, lw=1.0, alpha=0.85)
        seg(ax,(xv,W/2,H_c),(xv,W,H_l),   WOOD, lw=1.0, alpha=0.85)
        seg(ax,(xv,0,H_l),  (xv,W,H_l),   WOOD, lw=0.7, ls='--', alpha=0.45)

    # Paneles de techo (policarbonato)
    for y0t, yct in [(0, W/2), (W/2, W)]:
        panel = [
            [0,  y0t, H_l if y0t==0 else H_c],
            [L,  y0t, H_l if y0t==0 else H_c],
            [L,  yct, H_c if y0t==0 else H_l],
            [0,  yct, H_c if y0t==0 else H_l],
        ]
        quad(ax, panel, POLY, ec=GRIS, alpha=0.10, lw=0.4)

    # Paredes laterales (malla)
    for yp in [0, W]:
        quad(ax,[[0,yp,0],[L,yp,0],[L,yp,H_l],[0,yp,H_l]],
             '#90a4ae', ec='#607d8b', alpha=0.07, lw=0.3)

    # Hastiales
    for xv in [0, L]:
        quad(ax,[[xv,0,H_l],[xv,W,H_l],[xv,W/2,H_c]],
             '#90a4ae', ec='#607d8b', alpha=0.12, lw=0.3)

    # Cotas en 3D
    if label_cotas:
        off = 0.38
        cc, pc, rc = '#1565c0', '#6a1b9a', '#b71c1c'
        # Longitud L
        seg(ax,(0,-off,0),(L,-off,0),cc,lw=1.0)
        seg(ax,(0,0,0),(0,-off,0),cc,lw=0.6,ls='--',alpha=0.45)
        seg(ax,(L,0,0),(L,-off,0),cc,lw=0.6,ls='--',alpha=0.45)
        ax.text(L/2,-off-0.2,0.0,f'L = {L:.0f} m',ha='center',va='top',fontsize=7.5,color=cc)
        # Ancho W
        seg(ax,(-off,0,0),(-off,W,0),cc,lw=1.0)
        seg(ax,(0,0,0),(-off,0,0),cc,lw=0.6,ls='--',alpha=0.45)
        seg(ax,(0,W,0),(-off,W,0),cc,lw=0.6,ls='--',alpha=0.45)
        ax.text(-off-0.15,W/2,0.0,f'W = {W:.0f} m',ha='right',va='center',fontsize=7.5,color=cc)
        # Altura lateral H_l
        seg(ax,(L+off,0,0),(L+off,0,H_l),pc,lw=1.0)
        seg(ax,(L,0,0),(L+off,0,0),pc,lw=0.6,ls='--',alpha=0.45)
        seg(ax,(L,0,H_l),(L+off,0,H_l),pc,lw=0.6,ls='--',alpha=0.45)
        ax.text(L+off+0.1,0,H_l/2,f'H_l={H_l}m',ha='left',va='center',fontsize=7,color=pc)
        # Altura cumbrera H_c
        seg(ax,(L+off,W/2,0),(L+off,W/2,H_c),pc,lw=1.0)
        seg(ax,(L,W/2,0),(L+off,W/2,0),pc,lw=0.6,ls='--',alpha=0.45)
        seg(ax,(L,W/2,H_c),(L+off,W/2,H_c),pc,lw=0.6,ls='--',alpha=0.45)
        ax.text(L+off+0.1,W/2,H_c/2,f'H_c={H_c}m',ha='left',va='center',fontsize=7,color=pc)
        # Altura de camas
        seg(ax,(-off,y_c1,0),(-off,y_c1,H_cama),rc,lw=1.0)
        seg(ax,(0,y_c1,0),(-off,y_c1,0),rc,lw=0.6,ls='--',alpha=0.45)
        seg(ax,(0,y_c1,H_cama),(-off,y_c1,H_cama),rc,lw=0.6,ls='--',alpha=0.45)
        ax.text(-off-0.12,y_c1,H_cama/2,f'h={H_cama}m',ha='right',va='center',
                fontsize=6.5,color=rc,rotation=0)


# ═══════════════════════════════════════════════════════════════════
# FIGURA 1 — VISTAS ISOMÉTRICA Y DE PLANTA
# ═══════════════════════════════════════════════════════════════════

fig1 = plt.figure(figsize=(14, 7))

ax1 = fig1.add_subplot(121, projection='3d')
draw_marquesina(ax1, label_cotas=True)
ax1.set_xlim(-0.6, L+1.3); ax1.set_ylim(-0.8, W+0.3); ax1.set_zlim(0, H_c+0.3)
ax1.set_xlabel('Longitud (m)', labelpad=6, fontsize=8)
ax1.set_ylabel('Ancho (m)',    labelpad=6, fontsize=8)
ax1.set_zlabel('Altura (m)',   labelpad=6, fontsize=8)
ax1.set_title('(a) Vista isométrica — marquesina con camas elevadas', fontsize=9, pad=8)
ax1.view_init(elev=22, azim=-52)
ax1.tick_params(labelsize=7)

patches = [mpatches.Patch(color=CAFE_C[n_capas-1-i],
           label=f'Capa {i+1}  (f={np.exp(-25*(i+0.5)*dz_capa):.3f})')
           for i in range(n_capas)]
patches += [
    mpatches.Patch(color=POLY,    alpha=0.5, label='Policarbonato'),
    mpatches.Patch(color=WOOD,    alpha=0.9, label='Bastidor / cercha'),
    mpatches.Patch(color=MALLA_C, alpha=0.9, label='Malla metálica'),
    mpatches.Patch(color=BROWN,   alpha=0.9, label='Estructura madera'),
]
ax1.legend(handles=patches, loc='upper left', fontsize=6.2,
           title='Elementos', title_fontsize=7,
           bbox_to_anchor=(0.0, 1.04), framealpha=0.88)

ax2 = fig1.add_subplot(122, projection='3d')
draw_marquesina(ax2, label_cotas=False)
ax2.set_xlim(-0.2, L+0.3); ax2.set_ylim(-0.2, W+0.3); ax2.set_zlim(0, H_c+0.2)
ax2.set_xlabel('Longitud (m)', labelpad=4, fontsize=8)
ax2.set_ylabel('Ancho (m)',    labelpad=4, fontsize=8)
ax2.set_zlabel('Altura (m)',   labelpad=4, fontsize=8)
ax2.set_title('(b) Vista de planta — disposición de camas y cerchas', fontsize=9, pad=8)
ax2.view_init(elev=84, azim=-90)
ax2.tick_params(labelsize=7)

fig1.suptitle(
    'Diseño Conceptual — Marquesina de Secado Solar de Café con Camas Elevadas\n'
    f'{L:.0f} m × {W:.0f} m  |  Cumbrera {H_c:.1f} m  |  '
    f'2 camas × {W_cama:.2f} m  |  Pasillo {pasillo:.2f} m  |  '
    f'Camas a {H_cama:.2f} m del piso',
    fontsize=9.5, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('./marquesina_diseno_conceptual.png')
plt.close()
print("  [✓] marquesina_diseno_conceptual.png guardada")


# ═══════════════════════════════════════════════════════════════════
# FIGURA 2 — 4 PROYECCIONES ORTOGONALES
# ═══════════════════════════════════════════════════════════════════

fig2 = plt.figure(figsize=(14, 10))
vistas = [
    ('(a) Vista frontal (Y−Z)',   90,  -90, 221),
    ('(b) Vista lateral (X−Z)',   90,    0, 222),
    ('(c) Isométrica SE',         22,  -45, 223),
    ('(d) Isométrica NW',         22,  135, 224),
]
for titulo, elev, azim, pos in vistas:
    ax = fig2.add_subplot(pos, projection='3d')
    draw_marquesina(ax, label_cotas=False)
    ax.view_init(elev=elev, azim=azim)
    ax.set_xlim(0, L); ax.set_ylim(0, W); ax.set_zlim(0, H_c+0.2)
    ax.set_title(titulo, fontsize=8.5, pad=6)
    ax.set_xlabel('X (m)', fontsize=7, labelpad=3)
    ax.set_ylabel('Y (m)', fontsize=7, labelpad=3)
    ax.set_zlabel('Z (m)', fontsize=7, labelpad=3)
    ax.tick_params(labelsize=6.5)

fig2.suptitle('Marquesina de Secado — Proyecciones Técnicas Ortogonales',
              fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('./marquesina_vistas_tecnicas.png')
plt.close()
print("  [✓] marquesina_vistas_tecnicas.png guardada")


# ═══════════════════════════════════════════════════════════════════
# FIGURA 3 — SECCIÓN TRANSVERSAL A-A CON CAMAS ELEVADAS
# ═══════════════════════════════════════════════════════════════════

fig3, axes3 = plt.subplots(1, 2, figsize=(13, 5.8))
ax_s = axes3[0]
ax_s.set_facecolor('#f5f5f5')
ax_s.set_aspect('equal')

z_b = H_cama + t_bas

# Piso
ax_s.fill_between([0,W],[-0.07]*2,[0]*2, color='#bcaaa4', zorder=1)
ax_s.plot([0,W],[0,0], color=BROWN, lw=1.5, zorder=2)

# Columnas de marquesina
for yp in [0, W]:
    ax_s.fill_between([yp-0.05,yp+0.05],[0]*2,[H_l]*2, color=BROWN, alpha=0.9, zorder=5)

# Techo
ax_s.plot([0, W/2, W],[H_l,H_c,H_l], color=BROWN, lw=2.0, zorder=5)
ax_s.fill([0,W/2,W,W,0],[H_l,H_c,H_l,H_l-0.04,H_l-0.04], color=POLY, alpha=0.28, zorder=4)

# Tirante cercha
ax_s.plot([0,W],[H_l,H_l], color=WOOD, lw=1.0, ls='--', alpha=0.6)

def draw_cama_2d(ax, y0, label):
    """Sección 2D de una cama elevada."""
    y1 = y0 + W_cama
    # Patas
    for yp in [y0+0.04, y1-0.04]:
        ax.fill_between([yp-0.04,yp+0.04],[0]*2,[H_cama]*2, color=BROWN, alpha=0.9, zorder=5)
    # Riostra baja
    ax.plot([y0+0.04,y1-0.04],[H_cama*0.38]*2, color=WOOD, lw=1.2, alpha=0.7, zorder=4)
    # Bastidor (malla)
    ax.fill_between([y0,y1],[H_cama]*2,[z_b]*2, color=WOOD, alpha=0.80, zorder=4)
    ax.plot([y0,y1],[H_cama,H_cama], color=MALLA_C, lw=1.5, ls='--', alpha=0.85, zorder=5)
    # Capas de café
    for i in range(n_capas):
        zi0 = z_b + i*dz_capa; zi1 = z_b + (i+1)*dz_capa
        ax.fill_between([y0+0.02,y1-0.02],[zi0]*2,[zi1]*2,
                        color=CAFE_C[i], alpha=0.82, zorder=4)
        ax.text((y0+y1)/2, (zi0+zi1)/2,
                f'C{i+1}  f={np.exp(-25*((i+0.5)*dz_capa)):.3f}',
                ha='center', va='center', fontsize=6.5, color='white', fontweight='bold')
    ax.text((y0+y1)/2, z_b+prof_cafe+0.04, label,
            ha='center', fontsize=8, fontweight='bold', color=BROWN)

draw_cama_2d(ax_s, y_c1, 'CAMA 1')
draw_cama_2d(ax_s, y_c2, 'CAMA 2')

# Pasillo
ax_s.fill_between([y_c1+W_cama, y_c2],[0]*2,[0.10]*2, color='#b0bec5', alpha=0.40, zorder=2)
ax_s.text((y_c1+W_cama+y_c2)/2, 0.04,
          f'Pasillo\n{pasillo:.2f} m', ha='center', va='bottom',
          fontsize=7.5, color='#01579b', style='italic')

# Flechas de radiación
for y_r in np.linspace(0.4, W-0.4, 6):
    ax_s.annotate('', xy=(y_r, z_b+prof_cafe+0.01),
                  xytext=(y_r, H_c-0.12),
                  arrowprops=dict(arrowstyle='->', color='#f57f17', lw=1.0))
ax_s.text(W/2, H_c+0.07, 'Radiación solar + convección',
          ha='center', fontsize=8, color='#f57f17', style='italic')

# Cotas
cc = '#1565c0'; pc = '#6a1b9a'; rc = '#b71c1c'
ax_s.annotate('',xy=(W,-0.17),xytext=(0,-0.17),
              arrowprops=dict(arrowstyle='<->',color=cc,lw=1.0))
ax_s.text(W/2,-0.21,f'Ancho = {W:.1f} m',ha='center',va='top',fontsize=8,color=cc)
ax_s.annotate('',xy=(W+0.22,H_l),xytext=(W+0.22,0),
              arrowprops=dict(arrowstyle='<->',color=pc,lw=1.0))
ax_s.text(W+0.27,H_l/2,f'H_l={H_l} m',ha='left',va='center',fontsize=7,color=pc)
ax_s.annotate('',xy=(W/2-0.18,H_c),xytext=(W/2-0.18,0),
              arrowprops=dict(arrowstyle='<->',color=pc,lw=1.0))
ax_s.text(W/2-0.22,H_c*0.55,f'H_c={H_c} m',ha='right',va='center',
          fontsize=7,color=pc,rotation=90)
ax_s.annotate('',xy=(y_c1-0.20,H_cama),xytext=(y_c1-0.20,0),
              arrowprops=dict(arrowstyle='<->',color=rc,lw=1.0))
ax_s.text(y_c1-0.24,H_cama/2,f'h={H_cama} m',ha='right',va='center',
          fontsize=7,color=rc,rotation=90)
ax_s.annotate('',xy=(y_c1-0.20,z_b+prof_cafe),xytext=(y_c1-0.20,H_cama),
              arrowprops=dict(arrowstyle='<->',color='#1b5e20',lw=0.9))
ax_s.text(y_c1-0.24,z_b+prof_cafe/2+H_cama/2,
          f'{prof_cafe*100:.0f} cm\ncafé',ha='right',va='center',
          fontsize=6.5,color='#1b5e20',rotation=90)

ax_s.set_xlim(-0.45, W+0.50); ax_s.set_ylim(-0.28, H_c+0.28)
ax_s.set_xlabel('Posición transversal Y (m)', fontsize=9)
ax_s.set_ylabel('Altura Z (m)', fontsize=9)
ax_s.set_title('(a) Sección A–A — Camas de secado elevadas\ncon gradiente de capas y cercha del techo',
               fontsize=9.5, fontweight='bold')
ax_s.grid(True, alpha=0.22, ls='--')
ax_s.tick_params(labelsize=8)

# Panel derecho: gráfico de extinción por capa
ax_d = axes3[1]
ax_d.set_facecolor('#fafafa')
dz = prof_cafe / n_capas
for i in range(n_capas):
    z0 = i*dz; z1 = (i+1)*dz; z_mid = (i+0.5)*dz
    f_i = np.exp(-25*z_mid)
    ax_d.barh(z0*100, f_i, height=dz*100*0.88,
              align='edge', color=CAFE_C[i], alpha=0.80,
              edgecolor='white', lw=0.7)
    ax_d.text(0.01, (z0+z1)/2*100,
              f'Capa {i+1}  z={z_mid*100:.1f} cm  f={f_i:.4f}',
              ha='left', va='center', fontsize=7.5, color='white', fontweight='bold')

ax_d.axhline(0, color=MALLA_C, lw=1.5, ls='--', label='Malla metálica')
ax_d.fill_between([0,1],[-dz*100*0.5]*2,[0]*2, color=WOOD, alpha=0.45, label='Bastidor')
ax_d.set_xlim(0, 1.05); ax_d.set_ylim(-dz*100*0.6, prof_cafe*100+0.2)
ax_d.invert_yaxis()
ax_d.set_xlabel('Factor de extinción  $f_i = e^{-k_{ext}\\,z_i}$', fontsize=9)
ax_d.set_ylabel('Profundidad desde la superficie (cm)', fontsize=9)
ax_d.set_title(f'(b) Gradiente de extinción por capa\n'
               r'$f_i = e^{-k_{ext}z_i}$,  $k_{ext}=25\,\mathrm{m}^{-1}$',
               fontsize=9.5, fontweight='bold')
ax_d.legend(fontsize=8, loc='lower right')
ax_d.grid(True, axis='x', alpha=0.3, ls='--')
ax_d.tick_params(labelsize=8)
ax_d.text(1.03, -0.05, '← Sup.', ha='left', va='center',
          fontsize=7, color='#c62828', style='italic')
ax_d.text(1.03, prof_cafe*100+0.1, '← Fondo\n   (malla)',
          ha='left', va='top', fontsize=7, color='#1b5e20', style='italic')

fig3.suptitle('Detalles Constructivos — Sección Transversal y Gradiente de Secado',
              fontsize=10.5, fontweight='bold')
plt.tight_layout()
plt.savefig('./marquesina_detalle_seccion.png')
plt.close()
print("  [✓] marquesina_detalle_seccion.png guardada")


# ═══════════════════════════════════════════════════════════════════
# FIGURA 4 — PLANO DE PLANTA 2D
# ═══════════════════════════════════════════════════════════════════

fig4, ax_p = plt.subplots(figsize=(13, 5.2))
ax_p.set_facecolor('#eceff1')
ax_p.set_aspect('equal')

# Contorno exterior
rect = plt.Polygon([[0,0],[L,0],[L,W],[0,W]], fill=False,
                   edgecolor=BROWN, lw=2.0, zorder=5)
ax_p.add_patch(rect)

# Camas (vista de planta)
for (ya, yb) in [(y_c1, y_c1+W_cama), (y_c2, y_c2+W_cama)]:
    r = plt.Polygon([[0.05,ya],[L-0.05,ya],[L-0.05,yb],[0.05,yb]],
                    facecolor='#a1887f', alpha=0.55,
                    edgecolor=BROWN, lw=1.0, zorder=3)
    ax_p.add_patch(r)
    ax_p.text(L/2, (ya+yb)/2,
              f'CAMA DE SECADO\n{L:.0f} m × {W_cama:.2f} m = {L*W_cama:.1f} m²',
              ha='center', va='center', fontsize=8, color='#3e2723', fontweight='bold')
    # Travesaños (patas vistas desde arriba)
    for xp in np.arange(0, L+0.01, paso_pata):
        for yp in [ya+0.06, yb-0.06]:
            circ = plt.Circle((xp,yp), 0.07, color=BROWN, zorder=6)
            ax_p.add_patch(circ)

# Pasillo
r_pas = plt.Polygon([[0,y_c1+W_cama],[L,y_c1+W_cama],[L,y_c2],[0,y_c2]],
                     facecolor='#e0f7fa', alpha=0.70,
                     edgecolor='#0288d1', lw=0.8, ls='--', zorder=3)
ax_p.add_patch(r_pas)
ax_p.text(L/2,(y_c1+W_cama+y_c2)/2,'Pasillo de trabajo',
          ha='center',va='center',fontsize=8.5,color='#01579b',style='italic')

# Columnas de marquesina
for xc in np.linspace(0, L, 6):
    for yc in [0, W]:
        ax_p.add_patch(plt.Circle((xc,yc), 0.10, color=BROWN, zorder=7))

# Eje de cumbrera
ax_p.plot([0,L],[W/2,W/2], color='#b71c1c', lw=1.0, ls='-.', label='Eje cumbrera')
ax_p.text(L+0.1,W/2,'Cumbrera', fontsize=7.5, va='center', color='#b71c1c', style='italic')

# Rejillas de ventilación lateral
for y_v in np.linspace(0.5, W-0.5, 4):
    for x_v in [0, L]:
        ax_p.plot([x_v,x_v],[y_v-0.18,y_v+0.18], color='#0288d1', lw=3.5,
                  solid_capstyle='round', zorder=8)
ax_p.plot([],[],color='#0288d1',lw=3,label='Rejillas de ventilación')

# Norte
ax_p.annotate('N', xy=(L+1.6,W-0.3), xytext=(L+1.6,W-1.1),
              fontsize=11, ha='center', fontweight='bold', color='#1a237e',
              arrowprops=dict(arrowstyle='->',color='#1a237e',lw=1.5))

# Cotas
cc = '#1565c0'
ax_p.annotate('',xy=(L,-0.38),xytext=(0,-0.38),
              arrowprops=dict(arrowstyle='<->',color=cc,lw=1.0))
ax_p.text(L/2,-0.50,f'L = {L:.0f} m',ha='center',va='top',fontsize=8.5,color=cc)
ax_p.annotate('',xy=(-0.45,W),xytext=(-0.45,0),
              arrowprops=dict(arrowstyle='<->',color=cc,lw=1.0))
ax_p.text(-0.55,W/2,f'W = {W:.0f} m',ha='right',va='center',
          fontsize=8.5,color=cc,rotation=90)
ax_p.annotate('',xy=(-0.45,y_c1+W_cama),xytext=(-0.45,y_c1),
              arrowprops=dict(arrowstyle='<->',color='#6a1b9a',lw=0.9))
ax_p.text(-0.55,(y_c1+y_c1+W_cama)/2,f'{W_cama:.2f} m',
          ha='right',va='center',fontsize=7.5,color='#6a1b9a',rotation=90)

ax_p.set_xlim(-0.8, L+2.0); ax_p.set_ylim(-0.75, W+0.4)
ax_p.set_xlabel('Longitud X (m)', fontsize=9)
ax_p.set_ylabel('Ancho Y (m)', fontsize=9)
ax_p.set_title(
    'Plano de Planta — Marquesina de Secado Solar de Café\n'
    f'2 camas elevadas × {W_cama:.2f} m  |  Pasillo central {pasillo:.2f} m  |  '
    f'Columnas cada 2 m  |  Área útil = {2*L*W_cama:.0f} m²',
    fontsize=9.5, fontweight='bold')
ax_p.legend(loc='upper right', fontsize=8, framealpha=0.9)
ax_p.grid(True, alpha=0.22, ls='--')
ax_p.tick_params(labelsize=8)

plt.tight_layout()
plt.savefig('./marquesina_plano_planta.png')
plt.close()
print("  [✓] marquesina_plano_planta.png guardada")

print(f"""
  Diseño actualizado — camas elevadas integradas en todos los planos
  · marquesina_diseno_conceptual.png
  · marquesina_vistas_tecnicas.png
  · marquesina_detalle_seccion.png
  · marquesina_plano_planta.png
  Pasillo central: {pasillo:.2f} m  |  Área útil: {2*L*W_cama:.0f} m²
""")
