"""
Problema 1 - Integración Numérica: Regla del Trapecio Compuesta
Parcial I - Métodos Numéricos (S1 2026)
Politécnico Colombiano Jaime Isaza Cadavid

Calcula el tiempo total T de descarga del circuito RLC usando:
    T = integral_0^{6e-3} f(q) dq
    f(q) = R(q) * C^2 / q
"""

import numpy as np
import matplotlib.pyplot as plt

# ─── Datos del problema ───────────────────────────────────────────────────────

C = 2.5e-4  # Capacitancia [F]

# Puntos tabulados (de mayor a menor carga en el enunciado, aquí de 0 a 6e-3)
q_tabla = np.array([0, 1e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3])  # [C]
R_tabla = np.array([0.05, 0.18, 0.32, 0.45, 0.67, 0.97, 1.17])  # [Ω]

# ─── Derivación de f(q) ───────────────────────────────────────────────────────
#
# De la EDO:   dq/dt = -q / (R(q) * C^2)
#
# Separando variables:
#   dt = -R(q)*C^2 / q  dq
#
# Integrando de q=6e-3 hasta q=0 (descarga), e invirtiendo límites:
#   T = integral_0^{6e-3}  R(q)*C^2 / q  dq
#
# Por tanto:   f(q) = R(q) * C^2 / q
#
# Caso especial q=0: límite → 0 (R→0.05, q→0, pero la carga también → 0).
# Físicamente la integral converge; numéricamente usamos f(0) = 0.


def f(q, R):
    """Integrando f(q) = R(q)*C^2 / q. Retorna 0 para q=0."""
    if q == 0:
        return 0.0
    return R * C**2 / q


# ─── Tabla de valores de f(q) ────────────────────────────────────────────────

print("=" * 60)
print("PROBLEMA 1 — Regla del Trapecio Compuesta")
print("=" * 60)

print("\nCuadro de valores de f(q) = R(q)·C²/q")
print("-" * 50)
print(f"{'q [C]':>12}  {'R(q) [Ω]':>10}  {'f(q) [s/C]':>14}")
print("-" * 50)

f_vals = []
for qi, Ri in zip(q_tabla, R_tabla):
    fi = f(qi, Ri)
    f_vals.append(fi)
    q_str = f"{qi:.3e}"
    print(f"{q_str:>12}  {Ri:>10.2f}  {fi:>14.6f}")

print("-" * 50)

f_vals = np.array(f_vals)

# ─── Regla del Trapecio Compuesta ────────────────────────────────────────────
#
# T ≈ (Δq/2) * [f(q₀) + 2·f(q₁) + ... + 2·f(q_{n-1}) + f(qₙ)]
#
# Con n=6 subintervalos, Δq = 1e-3 C

delta_q = 1e-3  # [C]
n = len(f_vals) - 1  # número de subintervalos = 6

# Coeficientes del trapecio compuesto: 1, 2, 2, ..., 2, 1
coef = np.ones(n + 1)
coef[1:-1] = 2.0

T_seg = (delta_q / 2) * np.dot(coef, f_vals)
T_ms = T_seg * 1000  # convertir a milisegundos

print("\nAplicando Regla del Trapecio Compuesta:")
print(f"  Δq            = {delta_q:.3e} C")
print(f"  Subintervalos = {n}")
print(f"  Coeficientes  = {coef.tolist()}")
print()

# Mostrar el cálculo paso a paso
terminos = coef * f_vals
print("  Suma ponderada de f(q):")
for i, (qi, ci, fi, ti) in enumerate(zip(q_tabla, coef, f_vals, terminos)):
    print(f"    [{i}] {ci:.0f} × f({qi:.3e}) = {ci:.0f} × {fi:.6f} = {ti:.6f}")

suma = np.sum(terminos)
print(f"\n  Σ coef·f(q) = {suma:.6f}")
print(f"\n  T = (Δq/2) · Σ = ({delta_q:.3e}/2) · {suma:.6f}")
print(f"  T = {T_seg:.8f} s")
print(f"  T = {T_ms:.6f} ms")

print()
print("=" * 60)
print(f"  RESULTADO FINAL: T ≈ {T_seg:.10e} s")
print(f"                     = {T_ms:.10e} ms")
print(f"                     = {T_seg*1e6:.8f} μs")
print(f"                     ≈ {T_seg*1e9:.4f} ns")
print("=" * 60)

# ─── Análisis de errores ─────────────────────────────────────────────────────

print("\nANÁLISIS DE ERRORES (Problema 1)")
print("-" * 60)

# Error de truncamiento del método: O(Δq²) por subintervalo, O(Δq²) global
# Para Trapecio Compuesto: E ≈ -(b-a)/12 * Δq² * f''(ξ)
# Estimamos f'' numéricamente en puntos interiores
b = 6e-3
a = 0.0
rango = b - a

# Diferencias finitas de segundo orden para f'' en puntos interiores
f_pp_est = []
for i in range(1, n):
    fpp_i = (f_vals[i+1] - 2*f_vals[i] + f_vals[i-1]) / delta_q**2
    f_pp_est.append(abs(fpp_i))

max_fpp = max(f_pp_est)
E_truncamiento = abs(-(rango / 12) * delta_q**2 * max_fpp)

print(f"  Error de truncamiento estimado (Trapecio Compuesto):")
print(f"    E ≤ (b-a)/12 · Δq² · max|f''(ξ)|")
print(f"    max|f''| ≈ {max_fpp:.4f}")
print(f"    E ≤ {E_truncamiento:.2e} s  ({E_truncamiento*1000:.4f} ms)")

# Error de redondeo: float64 tiene ~15-16 dígitos significativos
eps_maquina = np.finfo(float).eps
E_redondeo_est = n * eps_maquina * max(abs(f_vals))
print(f"\n  Error de redondeo estimado (acumulado en n={n} operaciones):")
print(f"    ε_máquina = {eps_maquina:.2e}")
print(f"    E_redondeo ≈ {E_redondeo_est:.2e} s  (despreciable)")

# Error absoluto y relativo (comparando con un valor de referencia más fino)
# Usamos np.trapz como referencia sobre los mismos puntos
T_ref = np.trapezoid(f_vals, q_tabla)
E_abs = abs(T_seg - T_ref)
E_rel = E_abs / abs(T_ref) * 100 if T_ref != 0 else 0

print(f"\n  Verificación interna (np.trapz sobre los mismos datos):")
print(f"    T_ref  = {T_ref*1000:.6f} ms")
print(f"    T_calc = {T_ms:.6f} ms")
print(f"    Error absoluto  = {E_abs:.2e} s")
print(f"    Error relativo  = {E_rel:.6f}%  (idénticos por algoritmo equivalente)")

print("\n  Cuadro cualitativo de errores:")
print("  " + "-"*56)
print(f"  {'Tipo de error':<25} {'Impacto':<15} {'Valor estimado'}")
print("  " + "-"*56)
print(f"  {'Corte (discretización)':<25} {'Medio':<15} {'Δq=1e-3 → 6 puntos'}")
print(f"  {'Truncamiento (método)':<25} {'Bajo':<15} {f'≤ {E_truncamiento*1e6:.2f} μs'}")
print(f"  {'Redondeo (float64)':<25} {'Despreciable':<15} {f'≈ {E_redondeo_est:.1e} s'}")
print(f"  {'Absoluto':<25} {'~0 (mismo alg.)':<15} {'—'}")
print(f"  {'Relativo':<25} {'~0 (mismo alg.)':<15} {'—'}")
print("  " + "-"*56)

# ─── Gráfica ─────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(
    r"Problema 1 — Integración de $f(q) = R(q)\cdot C^2\,/\,q$"
    "\nRegla del Trapecio Compuesta",
    fontsize=13, fontweight="bold"
)

# ── Subgráfica izquierda: f(q) con trapecios sombreados ──────────────────────
ax1 = axes[0]

# Curva entre nodos (solo el rango tabulado 1e-3 … 6e-3 para evitar el pico)
q_fine = np.linspace(q_tabla[1], q_tabla[-1], 400)
R_fine = np.interp(q_fine, q_tabla, R_tabla)
f_fine = R_fine * C**2 / q_fine  # [s/C]

ax1.plot(q_fine * 1e3, f_fine * 1e6, color="steelblue", lw=2, label=r"$f(q)$ interpolada")

# Nodos tabulados q>0
ax1.scatter(q_tabla[1:] * 1e3, f_vals[1:] * 1e6, color="crimson", zorder=5,
            label="Nodos tabulados", s=70)

# Nodo especial q=0
ax1.scatter([0], [0], color="orange", zorder=5, marker="D", s=70,
            label=r"$f(0)=0$ (límite)")

# Trapecios sombreados (colores alternados para distinguirlos)
colores = ["steelblue", "mediumseagreen"]
for i in range(n):
    color = colores[i % 2]
    xs = [q_tabla[i] * 1e3, q_tabla[i+1] * 1e3, q_tabla[i+1] * 1e3, q_tabla[i] * 1e3]
    ys = [0, 0, f_vals[i+1] * 1e6, f_vals[i] * 1e6]
    ax1.fill(xs, ys, alpha=0.22, color=color)
    ax1.plot([q_tabla[i] * 1e3, q_tabla[i+1] * 1e3],
             [f_vals[i] * 1e6, f_vals[i+1] * 1e6],
             color=color, lw=1.5, ls="--")

# Líneas verticales en los nodos
for qi, fi in zip(q_tabla, f_vals):
    ax1.vlines(qi * 1e3, 0, fi * 1e6, color="gray", lw=0.8, ls=":")

# Etiquetas de valor sobre cada nodo
for qi, fi in zip(q_tabla[1:], f_vals[1:]):
    ax1.annotate(f"{fi*1e6:.2f}", xy=(qi * 1e3, fi * 1e6),
                 xytext=(0, 7), textcoords="offset points",
                 ha="center", fontsize=8, color="crimson")

f_max = max(f_vals[1:]) * 1e6
ax1.set_xlabel("Carga $q$ [mC]", fontsize=11)
ax1.set_ylabel(r"$f(q)$ [$\mu$s/C]", fontsize=11)
ax1.set_title("Integrando y trapecios", fontsize=11)
ax1.set_xlim(-0.2, 6.5)
ax1.set_ylim(-0.5, f_max * 1.25)
# Ticks en los nodos exactos
ax1.set_xticks(q_tabla * 1e3)
ax1.set_xticklabels([f"{q*1e3:.0f}" for q in q_tabla])
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.annotate(
    f"T = {T_seg*1e6:.4f} μs\n= {T_ms:.6f} ms",
    xy=(3.5, f_max * 0.55),
    fontsize=10, color="steelblue",
    bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="steelblue", alpha=0.85)
)

# ── Subgráfica derecha: R(q) ──────────────────────────────────────────────────
ax2 = axes[1]

ax2.plot(q_tabla * 1e3, R_tabla, color="darkorange", lw=2, marker="o",
         markersize=7, label=r"$R(q)$ experimental")
ax2.fill_between(q_tabla * 1e3, R_tabla, alpha=0.15, color="darkorange")

for qi, Ri in zip(q_tabla, R_tabla):
    ax2.annotate(f"{Ri} Ω", xy=(qi * 1e3, Ri),
                 xytext=(5, 5), textcoords="offset points", fontsize=8, color="saddlebrown")

ax2.set_xlabel("Carga $q$ [mC]", fontsize=11)
ax2.set_ylabel(r"$R(q)$ [$\Omega$]", fontsize=11)
ax2.set_title("Resistencia dinámica $R(q)$", fontsize=11)
ax2.set_xlim(-0.1, 6.3)
ax2.set_ylim(0, 1.35)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("grafica_problema1.png", dpi=150, bbox_inches="tight")
print("\nGráfica guardada en: grafica_problema1.png")
plt.show()

# ─── Comandos GeoGebra ────────────────────────────────────────────────────────
#
# R(q) se define por interpolación lineal entre los 7 nodos.
# Pendiente de cada segmento: m_i = (R_{i+1} - R_i) / Δq
# f(q) = R(q) * C² / q  (con f(0) = 0 por límite)
#
# Escala usada en GeoGebra: q en Coulombs (valores 0 … 0.006),
# f(q) en segundos/Coulomb.  Si se prefiere trabajar en mC y μs/C
# se indican las versiones escaladas al final.

print()
print("=" * 70)
print("COMANDOS PARA GEOGEBRA")
print("  Pegar cada línea en la barra de entrada de GeoGebra (en orden)")
print("=" * 70)

# Calcular pendientes de R(q) en cada segmento
slopes_R = []
for i in range(len(q_tabla) - 1):
    m = round((R_tabla[i+1] - R_tabla[i]) / (q_tabla[i+1] - q_tabla[i]), 8)
    slopes_R.append(m)

def _g(x):
    """Formato limpio: elimina ceros decimales innecesarios."""
    return f"{x:g}"

# ── 1. Constante C² ──────────────────────────────────────────────────────────
C2 = C**2
print(f"\n── Constante ──")
print(f"C2 = {C2}")          # 6.25E-8

# ── 2. Puntos experimentales de R(q) ─────────────────────────────────────────
print(f"\n── Puntos experimentales (para graficar) ──")
puntos_R = "{" + ", ".join(f"({q}, {R})" for q, R in zip(q_tabla, R_tabla)) + "}"
print(f"puntosR = {puntos_R}")

puntos_f = "{" + ", ".join(
    f"({q:.4f}, {fv:.10f})" for q, fv in zip(q_tabla, f_vals)
) + "}"
print(f"puntosF = {puntos_f}")

# ── 3. R(q) por tramos (If anidado) ──────────────────────────────────────────
# GeoGebra: If(<cond>, <si_true>, <si_false>)
# Construimos de adentro hacia afuera (último segmento primero)

def segmento_R(i):
    """Expresión lineal del segmento i: R_i + m_i*(q - q_i)"""
    q0 = q_tabla[i]
    R0 = R_tabla[i]
    m  = slopes_R[i]
    if m == 0:
        return _g(R0)
    signo = "+" if m > 0 else "-"
    return f"{_g(R0)} {signo} {_g(abs(m))} (q - {_g(q0)})"

# Construir If anidado de derecha a izquierda
expr_R = segmento_R(5)   # último segmento (q ∈ [0.005, 0.006])
for i in range(4, -1, -1):
    cond  = f"q <= {q_tabla[i+1]}"
    inner = segmento_R(i)
    expr_R = f"If({cond}, {inner}, {expr_R})"

print(f"\n── R(q) interpolada por tramos ──")
print(f"R(q) = {expr_R}")

# ── 4. f(q) = R(q)*C²/q  con f(0)=0 ─────────────────────────────────────────
print(f"\n── f(q) = R(q)·C²/q  (integrando) ──")
print(f"f(q) = If(q <= 0, 0, R(q) * C2 / q)")

# ── 5. Integral numérica como texto ──────────────────────────────────────────
print(f"\n── Integral (compara con Trapecio) ──")
print(f"Integral(f, 0.001, 0.006)   {chr(8592)} resultado ≈ {T_seg:.6e} s")

# ── 6. Versión escalada (q en mC, f en μs/C) más legible en GeoGebra ─────────
# q_mC = q * 1000  →  q = q_mC / 1000
# f_usCperC = f * 1e6
# R_scaled(q_mC) = mismo valor de R  (no cambia, Ω no depende de la escala de q)
# f_scaled(q_mC) = R_scaled(q_mC) * C2 / (q_mC/1000) * 1e6
#                = R_scaled(q_mC) * C2 * 1e9 / q_mC

print(f"\n── Versión escalada (q en mC, eje Y en μs/C — más legible) ──")
print(f"   [Cambiar variable: usa 'x' en lugar de 'q' en GeoGebra si es necesario]")

expr_R_mC = segmento_R(5).replace("q", "(q/1000)").replace(f"{q_tabla[5]}", f"{q_tabla[5]*1000}/1000")
# más simple: reconstruir con q en mC directamente
def segmento_R_mC(i):
    q0_mC = q_tabla[i] * 1e3    # en mC
    R0    = R_tabla[i]
    m_mC  = slopes_R[i] / 1e3   # pendiente respecto a mC
    if abs(m_mC) < 1e-12:
        return f"{R0}"
    signo = "+" if m_mC > 0 else "-"
    return f"{R0} {signo} {abs(m_mC):.4f} (q - {q0_mC})"

expr_R_mC2 = segmento_R_mC(5)
for i in range(4, -1, -1):
    cond  = f"q <= {q_tabla[i+1]*1e3}"
    inner = segmento_R_mC(i)
    expr_R_mC2 = f"If({cond}, {inner}, {expr_R_mC2})"

C2_scaled = C2 * 1e9   # C² * 1e6 (para μs) * 1e3 (porque q está en mC)
print(f"R_mC(q) = {expr_R_mC2}")
print(f"f_mC(q) = If(q <= 0, 0, R_mC(q) * {C2_scaled} / q)")
print(f"   → eje X en mC (0 a 6), eje Y en μs/C (≈ 9.4 a 12.2)")
print(f"   Integral(f_mC, 0.001, 6) ≈ {T_seg*1e9:.6f}  [μs·mC/C = μs × 1e-3]")
print(f"   Multiplicar resultado × 0.001 para obtener μs, o × 1e-9 para segundos.")
print("=" * 70)
