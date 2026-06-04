"""
Problema 2 - EDO: Comparación de 4 métodos numéricos
Parcial I - Métodos Numéricos (S1 2026)
Politécnico Colombiano Jaime Isaza Cadavid

Métodos comparados:
  1. Euler hacia adelante   + Interpolación Lineal
  2. Euler hacia adelante   + Polinomios de Lagrange
  3. Trapecio Implícito     + Interpolación Lineal     (Crank-Nicolson)
  4. Trapecio Implícito     + Polinomios de Lagrange

Se ejecutan con DOS valores de Δt:
  A) Δt = 5e-4 s  (el indicado en el enunciado) → muestra inestabilidad
  B) Δt = 5e-9 s  (físicamente apropiado)        → todos convergen correctamente

φ(t,q) = dq/dt = -q / (R(q)·C²)    q(0) = 6e-3 C
T_físico ≈ 59 ns  (calculado por Trapecio Compuesto, Problema 1)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ─── Datos del problema ───────────────────────────────────────────────────────

C  = 2.5e-4          # Capacitancia [F]
C2 = C**2            # 6.25e-8  [F²]
q0 = 6e-3            # Carga inicial [C]

q_tabla = np.array([0.0, 1e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3])
R_tabla = np.array([0.05, 0.18, 0.32, 0.45, 0.67, 0.97, 1.17])

# ─── Interpolaciones ──────────────────────────────────────────────────────────

def interp_lineal(q):
    """R(q) por interpolación lineal entre los nodos tabulados.
    Extrapolación constante fuera del rango."""
    q_cl = float(np.clip(q, q_tabla[0], q_tabla[-1]))
    return float(np.interp(q_cl, q_tabla, R_tabla))


def interp_lagrange(q):
    """R(q) por polinomio de Lagrange de grado 6 sobre los 7 nodos."""
    q_cl = float(np.clip(q, q_tabla[0], q_tabla[-1]))
    n, result = len(q_tabla), 0.0
    for k in range(n):
        Lk = 1.0
        for j in range(n):
            if j != k:
                Lk *= (q_cl - q_tabla[j]) / (q_tabla[k] - q_tabla[j])
        result += R_tabla[k] * Lk
    return max(float(result), 1e-6)   # R físicamente positivo


# ─── Derivada ─────────────────────────────────────────────────────────────────

def phi(q, R_func):
    """dq/dt = -q/(R(q)·C²).  Devuelve 0 para q ≤ 0 (descarga completada)."""
    if q <= 0.0:
        return 0.0
    return -q / (R_func(q) * C2)


# ─── Euler hacia adelante ─────────────────────────────────────────────────────

def euler(q0, dt, R_func, max_steps=10_000_000):
    """q_{i+1} = q_i + φ(q_i)·Δt"""
    qs, ts = [q0], [0.0]
    q = q0
    t = 0.0
    for _ in range(max_steps):
        q_new = q + phi(q, R_func) * dt
        t    += dt
        qs.append(q_new)
        ts.append(t)
        q = q_new
        if q <= 0.0 or abs(q) > 100.0:   # descarga o divergencia
            break
    return np.array(ts), np.array(qs)


# ─── Trapecio Implícito (Crank-Nicolson) ─────────────────────────────────────
#
# q_{i+1} = q_i + (Δt/2)·[φ(q_i) + φ(q_{i+1})]
#
# Resuelto con Newton-Raphson sobre F(x) = x - q - (Δt/2)·[φ_i + φ(x)] = 0
#
# F'(x) ≈ 1 + (Δt/2)/(R(x)·C²)   [derivada de -x/(R·C²) respecto a x]
#
# NOTA IMPORTANTE: el clipping max(x,0) se aplica SOLO al valor final,
# NO dentro del loop de Newton — de lo contrario phi(0)=0 crea un punto
# fijo espurio que hace que el método tarde ~25× más pasos.

def trapecio_implicito(q0, dt, R_func, max_steps=10_000_000, tol=1e-12, max_iter=80):
    qs, ts = [q0], [0.0]
    q = q0
    t = 0.0
    for _ in range(max_steps):
        phi_i = phi(q, R_func)
        # Predictor Euler (sin clipear → permite que Newton encuentre la raíz correcta)
        x = q + dt * phi_i
        # Newton-Raphson (sin clipear x dentro del loop)
        for _ in range(max_iter):
            phi_x = phi(max(x, 0.0), R_func)   # phi usa max para evaluar R físico
            F     = x - q - (dt * 0.5) * (phi_i + phi_x)
            R_x   = R_func(max(abs(x), 1e-15))
            Fp    = 1.0 + (dt * 0.5) / (R_x * C2)
            step  = F / Fp
            x    -= step
            if abs(step) < tol:
                break
        # Aplicar condición de física solo al resultado final
        q = max(x, 0.0)
        t += dt
        qs.append(q)
        ts.append(t)
        if q <= 0.0:
            break
    return np.array(ts), np.array(qs)


# ─── Configuración de métodos ─────────────────────────────────────────────────

METODOS = {
    "Euler + Lineal":       (euler,              interp_lineal,   "crimson",        "--",  "o"),
    "Euler + Lagrange":     (euler,              interp_lagrange, "darkorange",     "-.",  "s"),
    "Trapecio + Lineal":    (trapecio_implicito, interp_lineal,   "steelblue",      "-",   "o"),
    "Trapecio + Lagrange":  (trapecio_implicito, interp_lagrange, "mediumseagreen", ":",   "s"),
}

DT_DADO    = 5e-4   # Δt del enunciado
DT_ESTABLE = 5e-9   # Δt físicamente apropiado (< Δt_max ≈ 0.146 μs)

# ─── Encabezado ──────────────────────────────────────────────────────────────

print("=" * 72)
print("PROBLEMA 2 — Comparación de 4 Métodos Numéricos")
print("=" * 72)

# ─── 2.1 Interpolación ───────────────────────────────────────────────────────

print("\n[2.1] ESTRATEGIA DE INTERPOLACIÓN PARA R(q)")
print("-" * 72)
q_test = 5.42e-3
print(f"  q_test = {q_test:.3e} C  (valor intermedio no tabulado)")
print(f"  Lineal   → R = {interp_lineal(q_test):.6f} Ω")
print(f"  Lagrange → R = {interp_lagrange(q_test):.6f} Ω")
print(f"  Diferencia = {abs(interp_lineal(q_test)-interp_lagrange(q_test)):.6f} Ω")

# ─── 2.2 Iteraciones manuales ─────────────────────────────────────────────────

print("\n[2.2] ITERACIONES MANUALES — Euler + Lineal  (Δt = 5e-4 s)")
print("-" * 72)

R0   = interp_lineal(q0)
phi0 = phi(q0, interp_lineal)
q1_E = q0 + phi0 * DT_DADO
lam  = -1.0 / (R0 * C2)
dtmax = 2.0 / abs(lam)

print(f"  t₀→t₁ (0 → 0.5 ms):")
print(f"    q₀    = {q0:.6e} C")
print(f"    R(q₀) = {R0:.4f} Ω  (punto exacto, sin interpolación)")
print(f"    φ(q₀) = -{q0:.4e} / ({R0:.4f}·{C2:.2e}) = {phi0:+.4f} C/s")
print(f"    q₁    = {q0:.4e} + ({phi0:.4f})×{DT_DADO:.2e} = {q1_E:.6e} C  ← DIVERGE")
print(f"\n  Estabilidad Euler: λ={lam:.4e} s⁻¹ → Δt_max={dtmax:.4e} s "
      f"({dtmax*1e6:.4f} μs)")
print(f"  Δt dado = {DT_DADO:.2e} s  →  {DT_DADO/dtmax:.0f}× el máximo estable")

q2_E = q1_E + phi(q1_E, interp_lineal) * DT_DADO
print(f"\n  t₁→t₂ (0.5 → 1.0 ms):")
print(f"    q₁    = {q1_E:.4e} C  (guarda: φ=0 para q≤0)")
print(f"    q₂    = {q2_E:.6e} C  (congelado)")

print("\n[2.2b] ITERACIONES MANUALES — Trapecio Implícito + Lineal  (Δt = 5e-4 s)")
print("-" * 72)

# Paso 1
phi_i = phi(q0, interp_lineal)
x = q0 + DT_DADO * phi_i     # predictor (sin clipear)
for _ in range(80):
    phi_x = phi(max(x, 0.0), interp_lineal)
    F     = x - q0 - (DT_DADO * 0.5) * (phi_i + phi_x)
    R_x   = interp_lineal(max(abs(x), 1e-15))
    Fp    = 1.0 + (DT_DADO * 0.5) / (R_x * C2)
    step  = F / Fp
    x    -= step
    if abs(step) < 1e-12:
        break
q1_T = max(x, 0.0)

print(f"  t₀→t₁ (0 → 0.5 ms):")
print(f"    q₀      = {q0:.6e} C,  φ(q₀) = {phi_i:.4f} C/s")
print(f"    Predictor: q* = {q0+DT_DADO*phi_i:.4e} C")
print(f"    Newton converge → q₁ = {q1_T:.6e} C  ← ESTABLE")

phi_i2 = phi(q1_T, interp_lineal)
x2 = q1_T + DT_DADO * phi_i2
for _ in range(80):
    phi_x = phi(max(x2, 0.0), interp_lineal)
    F     = x2 - q1_T - (DT_DADO * 0.5) * (phi_i2 + phi_x)
    R_x   = interp_lineal(max(abs(x2), 1e-15))
    Fp    = 1.0 + (DT_DADO * 0.5) / (R_x * C2)
    step  = F / Fp
    x2   -= step
    if abs(step) < 1e-12:
        break
q2_T = max(x2, 0.0)

print(f"\n  t₁→t₂ (0.5 → 1.0 ms):")
print(f"    q₁      = {q1_T:.6e} C,  φ(q₁) = {phi_i2:.6f} C/s")
print(f"    Newton converge → q₂ = {q2_T:.6e} C  ← ESTABLE")

# ─── Ejecutar los 4 métodos × 2 escenarios ────────────────────────────────────

escenarios = {
    f"Δt={DT_DADO:.0e} s (enunciado)":  DT_DADO,
    f"Δt={DT_ESTABLE:.0e} s (estable)": DT_ESTABLE,
}

resultados = {}
for label_dt, dt in escenarios.items():
    resultados[label_dt] = {}
    for nombre, (metodo, R_func, *_) in METODOS.items():
        ts, qs = metodo(q0, dt, R_func)
        resultados[label_dt][nombre] = (ts, qs)

# ─── Tabla de resultados ──────────────────────────────────────────────────────

print("\n[2.3] RESUMEN — 4 MÉTODOS × 2 ESCENARIOS")
print("=" * 72)
for label_dt, dt in escenarios.items():
    print(f"\n  {label_dt}")
    print(f"  {'Método':<28} {'Pasos':>7}  {'T final':>13}  {'q_final [C]':>14}  Estado")
    print("  " + "-" * 72)
    for nombre in METODOS:
        ts, qs = resultados[label_dt][nombre]
        pasos  = len(ts) - 1
        T_ns   = ts[-1] * 1e9
        T_ms   = ts[-1] * 1e3
        q_fin  = qs[-1]
        if abs(q_fin) > 10:
            estado = "DIVERGE ✗"
            T_str  = f"{T_ms:.4f} ms"
        elif q_fin <= 1e-12:
            estado = "Descargado ✓"
            T_str  = f"{T_ns:.4f} ns"
        else:
            estado = f"q={q_fin:.2e}"
            T_str  = f"{T_ns:.4f} ns"
        print(f"  {nombre:<28} {pasos:>7}  {T_str:>13}  {q_fin:>14.4e}  {estado}")

# ─── Diferencia entre interpolaciones ────────────────────────────────────────

print("\n[2.4] DIFERENCIA LINEAL vs LAGRANGE (Δt estable)")
print("-" * 72)
lbl_est = f"Δt={DT_ESTABLE:.0e} s (estable)"
for base in ["Euler", "Trapecio"]:
    ts_L, qs_L = resultados[lbl_est][f"{base} + Lineal"]
    ts_G, qs_G = resultados[lbl_est][f"{base} + Lagrange"]
    n = min(len(qs_L), len(qs_G))
    diffs = np.abs(qs_L[:n] - qs_G[:n])
    print(f"  {base:<10} max|Δq| = {diffs.max():.4e} C  "
          f"({diffs.max()/q0*100:.4f}% de q₀)")

print("\n[2.5] ANÁLISIS COMPARATIVO FINAL")
print("-" * 72)
print(f"""
  CON Δt = {DT_DADO:.0e} s (enunciado):
  • Euler: λΔt ≈ -6840 → |1+λΔt| = 6839 ≫ 1 → DIVERGE en el paso 1.
    q₁ ≈ -41 C (primer paso ya sale completamente del rango físico).
  • Trapecio Implícito: A-estable (|(1+λΔt/2)/(1-λΔt/2)| < 1 siempre).
    Newton converge y q₁ → 0 en 1 paso. Matemáticamente estable
    pero Δt ≫ T_físico ≈ 59 ns → la dinámica real se "saltó" en un solo paso.
  • Conclusión: Δt del enunciado es inadecuado para cualquier método,
    ya que es ~8400× mayor que la duración física de la descarga.

  CON Δt = {DT_ESTABLE:.0e} s (físicamente apropiado):
  • Euler: |λΔt| ≈ 0.034 ≪ 2 → ESTABLE. Completa la descarga en ~12 pasos.
  • Trapecio Implícito: también estable, mismos ~12 pasos, pero
    con error global O(Δt²) en lugar de O(Δt) de Euler.
  • Diferencia Lineal vs Lagrange: < 1% de q₀ → equivalentes aquí.
    Lagrange puede oscilar (Runge) en los extremos del rango.

  CONCLUSIÓN GLOBAL:
  • Trapecio Implícito > Euler en orden de precisión y estabilidad.
  • Lineal ≈ Lagrange para esta tabla equiespaciada (Δq = 1e-3 C).
  • La elección de Δt es más crítica que el método de interpolación.
  • El Δt del enunciado sirve para DEMOSTRAR la inestabilidad de Euler
    y la estabilidad del Trapecio, no para simular la descarga real.
""")

# ─── GRÁFICAS ─────────────────────────────────────────────────────────────────

lbl_dado = f"Δt={DT_DADO:.0e} s (enunciado)"
lbl_est  = f"Δt={DT_ESTABLE:.0e} s (estable)"

fig = plt.figure(figsize=(16, 12))
gs  = gridspec.GridSpec(3, 2, figure=fig, hspace=0.52, wspace=0.32)

# ── Panel A: Δt dado — divergencia Euler vs. estabilidad Trapecio ─────────────
axA = fig.add_subplot(gs[0, 0])

for nombre, (_, _, color, ls, mk) in METODOS.items():
    ts, qs = resultados[lbl_dado][nombre]
    if "Euler" in nombre:
        # Mostrar solo el vector de divergencia (q₀ → q₁ out of range)
        axA.annotate(
            "", xy=(ts[1]*1000, -0.8),
            xytext=(ts[0]*1000, qs[0]*1e3),
            arrowprops=dict(arrowstyle="-|>", color=color, lw=2.5,
                            mutation_scale=18)
        )
        axA.scatter([], [], color=color, marker=mk, s=60, label=f"{nombre}  (q₁≈−41 C, DIVERGE)")
    else:
        axA.plot(ts * 1000, qs * 1e3, color=color, ls=ls, lw=2,
                 marker=mk, markersize=7, label=nombre)

axA.axhline(0, color="black", lw=0.8, ls=":")
axA.set_ylim(-1.0, 7.5)
axA.set_xlabel("Tiempo [ms]", fontsize=10)
axA.set_ylabel("Carga q [mC]", fontsize=10)
axA.set_title(f"A)  Δt = {DT_DADO:.0e} s  (enunciado)\n"
              "Euler diverge — Trapecio se mantiene estable", fontsize=10)
axA.legend(fontsize=7.5, loc="upper right")
axA.grid(True, alpha=0.3)
axA.text(0.03, 0.30,
         f"Euler: q₁ ≈ −41 C\n(flechas salen del eje)\n\n"
         f"Δt_max Euler ≈ {dtmax*1e6:.2f} μs\nΔt dado / Δt_max ≈ {DT_DADO/dtmax:.0f}×",
         transform=axA.transAxes, fontsize=7.5, color="gray",
         va="center",
         bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.85))

# ── Panel B: Δt estable — todos convergen ─────────────────────────────────────
axB = fig.add_subplot(gs[0, 1])

for nombre, (_, _, color, ls, mk) in METODOS.items():
    ts, qs = resultados[lbl_est][nombre]
    axB.plot(ts * 1e9, qs * 1e3, color=color, ls=ls, lw=2,
             marker=mk, markersize=4, label=nombre, markevery=2)

axB.axhline(0, color="black", lw=0.8, ls=":")
axB.set_xlabel("Tiempo [ns]", fontsize=10)
axB.set_ylabel("Carga q [mC]", fontsize=10)
axB.set_title(f"B)  Δt = {DT_ESTABLE:.0e} s  (físicamente apropiado)\n"
              "Los 4 métodos convergen", fontsize=10)
axB.legend(fontsize=7.5)
axB.grid(True, alpha=0.3)

# ── Panel C: Euler — Lineal vs. Lagrange (Δt estable) ────────────────────────
axC = fig.add_subplot(gs[1, 0])

for nombre, (_, _, color, ls, mk) in METODOS.items():
    if "Euler" in nombre:
        ts, qs = resultados[lbl_est][nombre]
        axC.plot(ts * 1e9, qs * 1e3, color=color, ls=ls, lw=2,
                 marker=mk, markersize=5, label=nombre)

axC.axhline(0, color="black", lw=0.8, ls=":")
axC.set_xlabel("Tiempo [ns]", fontsize=10)
axC.set_ylabel("Carga q [mC]", fontsize=10)
axC.set_title("C)  Euler — Lineal vs Lagrange\n(Δt estable)", fontsize=10)
axC.legend(fontsize=9)
axC.grid(True, alpha=0.3)

# ── Panel D: Trapecio — Lineal vs. Lagrange (Δt estable) ─────────────────────
axD = fig.add_subplot(gs[1, 1])

for nombre, (_, _, color, ls, mk) in METODOS.items():
    if "Trapecio" in nombre:
        ts, qs = resultados[lbl_est][nombre]
        axD.plot(ts * 1e9, qs * 1e3, color=color, ls=ls, lw=2,
                 marker=mk, markersize=5, label=nombre)

axD.axhline(0, color="black", lw=0.8, ls=":")
axD.set_xlabel("Tiempo [ns]", fontsize=10)
axD.set_ylabel("Carga q [mC]", fontsize=10)
axD.set_title("D)  Trapecio Implícito — Lineal vs Lagrange\n(Δt estable)", fontsize=10)
axD.legend(fontsize=9)
axD.grid(True, alpha=0.3)

# ── Panel E: |Euler Lineal − Euler Lagrange| ──────────────────────────────────
axE = fig.add_subplot(gs[2, 0])

ts_EL, qs_EL = resultados[lbl_est]["Euler + Lineal"]
ts_EG, qs_EG = resultados[lbl_est]["Euler + Lagrange"]
n = min(len(qs_EL), len(qs_EG))
diff_E = np.abs(qs_EL[:n] - qs_EG[:n]) * 1e6   # en μC

axE.semilogy(ts_EL[:n] * 1e9, diff_E + 1e-20, color="crimson", lw=1.8)
axE.fill_between(ts_EL[:n] * 1e9, diff_E + 1e-20, 1e-20,
                 alpha=0.15, color="crimson")
axE.set_xlabel("Tiempo [ns]", fontsize=10)
axE.set_ylabel("|Δq| [μC]   (log)", fontsize=10)
axE.set_title("E)  Euler: |Lineal − Lagrange|\n(escala log, Δt estable)", fontsize=10)
axE.grid(True, alpha=0.3, which="both")
axE.text(0.05, 0.85,
         f"máx = {diff_E.max():.3e} μC\n({diff_E.max()/q0*1e3:.3f}‰ de q₀)",
         transform=axE.transAxes, fontsize=9, color="crimson",
         bbox=dict(boxstyle="round", fc="white", ec="crimson", alpha=0.8))

# ── Panel F: |Trapecio Lineal − Trapecio Lagrange| ───────────────────────────
axF = fig.add_subplot(gs[2, 1])

ts_TL, qs_TL = resultados[lbl_est]["Trapecio + Lineal"]
ts_TG, qs_TG = resultados[lbl_est]["Trapecio + Lagrange"]
n = min(len(qs_TL), len(qs_TG))
diff_T = np.abs(qs_TL[:n] - qs_TG[:n]) * 1e6

axF.semilogy(ts_TL[:n] * 1e9, diff_T + 1e-20, color="steelblue", lw=1.8)
axF.fill_between(ts_TL[:n] * 1e9, diff_T + 1e-20, 1e-20,
                 alpha=0.15, color="steelblue")
axF.set_xlabel("Tiempo [ns]", fontsize=10)
axF.set_ylabel("|Δq| [μC]   (log)", fontsize=10)
axF.set_title("F)  Trapecio: |Lineal − Lagrange|\n(escala log, Δt estable)", fontsize=10)
axF.grid(True, alpha=0.3, which="both")
axF.text(0.05, 0.85,
         f"máx = {diff_T.max():.3e} μC\n({diff_T.max()/q0*1e3:.3f}‰ de q₀)",
         transform=axF.transAxes, fontsize=9, color="steelblue",
         bbox=dict(boxstyle="round", fc="white", ec="steelblue", alpha=0.8))

fig.suptitle(
    "Problema 2 — Comparación de 4 Métodos Numéricos\n"
    "Euler hacia adelante  vs  Trapecio Implícito  ·  "
    "Interpolación Lineal  vs  Polinomios de Lagrange",
    fontsize=13, fontweight="bold"
)

plt.savefig("grafica_trapecio.png", dpi=150, bbox_inches="tight")
print("Gráfica guardada en: grafica_trapecio.png")
plt.show()
