"""
Problema 2 - EDO: Método de Euler hacia adelante (Forward Euler)
Parcial I - Métodos Numéricos (S1 2026)
Politécnico Colombiano Jaime Isaza Cadavid

Simula la descarga del circuito RLC resolviendo directamente:
    dq/dt = -q / (R(q) * C^2)
con q(0) = 6e-3 C, Δt = 5e-4 s, hasta q ≤ 0.
"""

import numpy as np

# ─── Datos del problema ───────────────────────────────────────────────────────

C = 2.5e-4   # Capacitancia [F]
q0 = 6e-3    # Carga inicial [C]
dt = 5e-4    # Paso de tiempo [s] = 0.5 ms

# Puntos tabulados de R(q) — de menor a mayor carga
q_tabla = np.array([0, 1e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3])
R_tabla = np.array([0.05, 0.18, 0.32, 0.45, 0.67, 0.97, 1.17])

# ─── Interpolación lineal de R(q) ────────────────────────────────────────────
#
# Para q fuera de la tabla o entre puntos, se interpola linealmente:
#   R(q) ≈ R_i + (q - q_i)/(q_{i+1} - q_i) * (R_{i+1} - R_i)
#
# Si q < 0 se usa R(0)=0.05. Si q > 6e-3 se usa R(6e-3)=1.17.


def interpolar_R(q):
    """Retorna R(q) interpolando linealmente en la tabla."""
    if q <= q_tabla[0]:
        return R_tabla[0]
    if q >= q_tabla[-1]:
        return R_tabla[-1]
    # np.interp hace interpolación lineal directamente
    return float(np.interp(q, q_tabla, R_tabla))


# ─── Derivada: φ(t, q) = dq/dt ───────────────────────────────────────────────

def phi(q):
    """dq/dt = -q / (R(q) * C^2). Para q<=0 retorna 0."""
    if q <= 0:
        return 0.0
    R = interpolar_R(q)
    return -q / (R * C**2)


# ─── Encabezado ──────────────────────────────────────────────────────────────

print("=" * 70)
print("PROBLEMA 2 — Método de Euler hacia adelante (Forward Euler)")
print("=" * 70)

# ─── Sección 2.1: Estrategia de interpolación ────────────────────────────────

print("\n[2.1] ESTRATEGIA DE INTERPOLACIÓN PARA R(q)")
print("-" * 70)
print("  En cada paso Euler, se necesita R(q_i). Los datos solo existen para")
print("  q = 0, 1e-3, ..., 6e-3 C. Si q_i cae en un valor intermedio (ej.")
print("  q = 5.42e-3), se aplica INTERPOLACIÓN LINEAL entre los dos puntos")
print("  tabulados más cercanos:")
print()
print("    R(q) ≈ R_k + (q - q_k)/(q_{k+1} - q_k) · (R_{k+1} - R_k)")
print()
print("  Justificación: con 7 puntos y Δq=1e-3, la interpolación lineal")
print("  introduce un error O(Δq²) ≈ 1e-6, suficientemente pequeño.")
print("  Alternativa de mayor orden: Polinomios de Lagrange (mayor costo")
print("  computacional, útil si se necesita precisión extra).")

# ─── Sección 2.2: Iteraciones manuales ───────────────────────────────────────

print("\n[2.2] SIMULACIÓN MANUAL — Primeras 2 iteraciones")
print("-" * 70)

# Iteración 0 → 1
q_i = q0
t_i = 0.0

R0 = interpolar_R(q_i)
phi0 = phi(q_i)

print(f"\n  ITERACIÓN 1: t₀ = {t_i*1000:.1f} ms  →  t₁ = {(t_i+dt)*1000:.1f} ms")
print(f"    q₀ = {q_i:.6e} C")
print(f"    R(q₀) = R({q_i:.3e}) = {R0:.2f} Ω  ← punto EXACTO de la tabla, no requiere interpolación")
print(f"    φ(t₀, q₀) = -q₀ / (R(q₀)·C²)")
print(f"              = -{q_i:.4e} / ({R0:.2f} × ({C:.2e})²)")
print(f"              = -{q_i:.4e} / ({R0:.2f} × {C**2:.2e})")
print(f"              = {phi0:.6f} C/s")
print(f"    q₁ = q₀ + φ(t₀,q₀)·Δt")
print(f"       = {q_i:.6e} + ({phi0:.6f}) × {dt:.4e}")

q1 = q_i + phi0 * dt
print(f"       = {q_i:.6e} + ({phi0*dt:.6e})")
print(f"    q₁ = {q1:.6e} C")

# ─── Alerta de inestabilidad ─────────────────────────────────────────────────
print()
print("  *** ANÁLISIS DE ESTABILIDAD DE EULER ***")
print(f"  La constante de tiempo del sistema es:")
tau = 1.17 * C  # τ = R*C (tiempo de referencia RC)
print(f"    τ = R·C = 1.17 × {C:.2e} = {tau:.2e} s = {tau*1000:.4f} ms")
lambda_euler = -1.0 / (1.17 * C**2)
dt_max = 2.0 / abs(lambda_euler)
print(f"    λ = -1/(R·C²) ≈ {lambda_euler:.3e} s⁻¹")
print(f"    Δt_max estabilidad Euler = 2/|λ| ≈ {dt_max:.2e} s = {dt_max*1e6:.4f} μs")
print(f"    Δt usado = {dt:.2e} s = {dt*1e6:.1f} μs")
print(f"    Ratio Δt/Δt_max ≈ {dt/dt_max:.0f}x  →  EULER INESTABLE con este Δt")
print(f"    Resultado físico esperado: q₁ debería estar entre 0 y {q0:.3e} C")
print(f"    Resultado obtenido: q₁ = {q1:.3e} C  (divergencia numérica)")

# Iteración 1 → 2
q_i = q1
t_i += dt

# Verificar si q1 es punto exacto
es_exacto = any(abs(q_i - qt) < 1e-12 for qt in q_tabla)
R1 = interpolar_R(q_i)
phi1 = phi(q_i)

print(f"\n  ITERACIÓN 2: t₁ = {t_i*1000:.1f} ms  →  t₂ = {(t_i+dt)*1000:.1f} ms")
print(f"    q₁ = {q_i:.6e} C")

if es_exacto:
    print(f"    R(q₁) = {R1:.4f} Ω  ← punto EXACTO de la tabla, no requiere interpolación")
else:
    # Encontrar los puntos vecinos
    idx = np.searchsorted(q_tabla, q_i) - 1
    idx = max(0, min(idx, len(q_tabla) - 2))
    q_k = q_tabla[idx]
    q_k1 = q_tabla[idx + 1]
    R_k = R_tabla[idx]
    R_k1 = R_tabla[idx + 1]
    print(f"    R(q₁): q₁ = {q_i:.4e} NO es punto exacto → SE INTERPOLA")
    print(f"      Vecinos: q_k={q_k:.3e} (R={R_k}),  q_{{k+1}}={q_k1:.3e} (R={R_k1})")
    print(f"      R(q₁) = {R_k} + ({q_i:.4e} - {q_k:.3e})/({q_k1:.3e} - {q_k:.3e}) × ({R_k1} - {R_k})")
    print(f"             = {R1:.6f} Ω")

print(f"    φ(t₁, q₁) = -q₁ / (R(q₁)·C²)")
print(f"              = -{q_i:.4e} / ({R1:.6f} × {C**2:.2e})")
print(f"              = {phi1:.6f} C/s")
print(f"    q₂ = q₁ + φ(t₁,q₁)·Δt")
print(f"       = {q_i:.6e} + ({phi1:.6f}) × {dt:.4e}")

q2 = q_i + phi1 * dt
print(f"    q₂ = {q2:.6e} C")

# ─── Simulación completa hasta q ≤ 0 ─────────────────────────────────────────

print("\n[2.3] SIMULACIÓN COMPLETA (hasta q ≤ 0)")
print("-" * 70)
print(f"  {'Paso':>5}  {'t [ms]':>8}  {'q [C]':>14}  {'R(q) [Ω]':>10}  {'dq/dt [C/s]':>14}")
print("  " + "-" * 58)

q_sim = [q0]
t_sim = [0.0]

q_i = q0
t_i = 0.0
max_steps = 100000  # seguro

for step in range(max_steps):
    R_i = interpolar_R(q_i)
    phi_i = phi(q_i)

    if step < 5 or q_i < 0.5e-3:
        print(f"  {step:>5}  {t_i*1000:>8.3f}  {q_i:>14.6e}  {R_i:>10.4f}  {phi_i:>14.4f}")

    q_next = q_i + phi_i * dt
    t_next = t_i + dt

    if q_next <= 0:
        print(f"  {step+1:>5}  {t_next*1000:>8.3f}  {q_next:>14.6e}  {'—':>10}  {'—':>14}  ← q ≤ 0, FIN")
        q_sim.append(q_next)
        t_sim.append(t_next)
        break

    q_sim.append(q_next)
    t_sim.append(t_next)
    q_i = q_next
    t_i = t_next

q_sim = np.array(q_sim)
t_sim = np.array(t_sim)

T_euler_ms = t_sim[-1] * 1000
print("  " + "-" * 58)
print(f"\n  Pasos totales     : {len(t_sim) - 1}")
print(f"  Tiempo de descarga: T_Euler ≈ {T_euler_ms:.4f} ms")

# ─── Comparación con Problema 1 ──────────────────────────────────────────────

print("\n[2.3] ANÁLISIS COMPARATIVO: Trapecio vs Euler")
print("-" * 70)

# Importar resultado del problema 1 recalculándolo aquí directamente
q_tab = np.array([0, 1e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3])
R_tab = np.array([0.05, 0.18, 0.32, 0.45, 0.67, 0.97, 1.17])
f_tab = np.array([R * C**2 / q if q > 0 else 0.0 for q, R in zip(q_tab, R_tab)])
delta_q = 1e-3
coef = np.ones(7); coef[1:-1] = 2.0
T_trapecio_s = (delta_q / 2) * np.dot(coef, f_tab)
T_trapecio_ms = T_trapecio_s * 1000

print(f"\n  Método Trapecio Compuesto (Problema 1): T ≈ {T_trapecio_ms:.4f} ms")
print(f"  Método Euler hacia adelante (Problema 2): T ≈ {T_euler_ms:.4f} ms")
diff = abs(T_euler_ms - T_trapecio_ms)
print(f"  Diferencia absoluta                     : {diff:.4f} ms")
print()
print("  DISCUSIÓN:")
print("  • Trapecio Compuesto: error de truncamiento global O(Δq²) = O(1e-6).")
print("    Con 6 subintervalos (Δq=1e-3), la aproximación es relativamente buena")
print("    si f(q) es suave. Su error no acumula con el tiempo.")
print()
print("  • Euler hacia adelante: error local O(Δt²), error global O(Δt).")
print("    Con Δt=5e-4, el error acumula en cada paso. Para T/Δt pasos, el error")
print("    global crece linealmente con el tiempo de simulación.")
print()
print("  • CONCLUSIÓN: Euler acumula mayor error de truncamiento global porque")
print("    su error es O(Δt) acumulativo, mientras que Trapecio da una estimación")
print("    directa (no acumulativa) con error O(Δq²). Además, Euler depende de")
print("    la interpolación de R(q) en cada paso, añadiendo error adicional.")
print("=" * 70)
