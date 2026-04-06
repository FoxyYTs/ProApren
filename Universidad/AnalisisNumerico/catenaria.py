#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:22:59 2026
@author: vigo and Gipi IA
"""

# ==================================================
# PREPROCESO
# ==================================================

import numpy as np
import matplotlib.pyplot as plt

# Matriz del sistema (muro 1D)
A = np.array([[70, 1,  5, 7],
              [60, 1, 1, 17],
              [40, 0,  -1, 0],
              [10, 50, 65, 12]], dtype=float)

b = np.array([636, 518, 307, 70], dtype=float)

# Valores iniciales
#T0 = np.zeros(3)

# Valores iniciales aleatorios
T0 = np.array([1, 76, 100, 40], dtype=float)

tol = 1e-8
max_iter = 100

iters = []
T_vals = []
err_abs = []
err_rel = []

T = T0.copy()

# ==================================================
# PROCESO – GAUSS-SEIDEL
# ==================================================

for k in range(1, max_iter+1):

    T_old = T.copy()

    # Actualización secuencial (usa valores nuevos inmediatamente)
    for i in range(len(b)):
        suma1 = np.dot(A[i, :i], T[:i])          # ya actualizados
        suma2 = np.dot(A[i, i+1:], T_old[i+1:])  # aún no actualizados
        
        T[i] = (b[i] - suma1 - suma2) / A[i, i]

    iters.append(k)
    T_vals.append(T.copy())

    ea = np.linalg.norm(T - T_old, np.inf)
    er = ea / np.linalg.norm(T, np.inf)

    err_abs.append(ea)
    err_rel.append(er)

    if ea < tol:
        break

# ==================================================
# POSTPROCESO
# ==================================================

print("\nVector inicial utilizado:", T0)

print("\nTABLA DE ITERACIONES")
print("Iter |      T1      T2      T3    | Error Abs | Error Rel")
print("----------------------------------------------------------------")

for i in range(len(iters)):
    T1, T2, T3, T4 = T_vals[i]
    print(f"{iters[i]:>3} | {T1:8.4f} {T2:8.4f} {T3:8.4f} {T:8.4f} | "
          f"{err_abs[i]:.3e} | {err_rel[i]:.3e}")

# ==================================================
# ERRORES NUMÉRICOS
# ==================================================

eps = np.finfo(float).eps
err_round = [eps for _ in iters]
err_total = np.array(err_abs) + np.array(err_round)

# ==================================================
# GRÁFICAS
# ==================================================

plt.figure()
plt.semilogy(iters, err_abs, 'o-', label='Error absoluto')
plt.semilogy(iters, err_rel, 's-', label='Error relativo')
plt.xlabel('Iteraciones')
plt.ylabel('Error')
plt.title('Errores vs Iteraciones - Gauss-Seidel')
plt.legend()
plt.grid(True)

plt.figure()
plt.semilogy(iters, err_abs, 'o-', label='Error absoluto')
plt.semilogy(iters, err_round, '--', label='Error redondeo')
plt.semilogy(iters, err_total, 's-', label='Error total')
plt.xlabel('Iteraciones')
plt.ylabel('Error')
plt.title('Composición del Error Numérico - Gauss-Seidel')
plt.legend()
plt.grid(True)

plt.show()

# ==================================================
# RESULTADOS FÍSICOS
# ==================================================

print("\nRESULTADOS FÍSICOS")
print("T1 =", T[0])
print("T2 =", T[1])
print("T3 =", T[2])

print("\nPerfil completo de temperatura:")
print("T0 = 100°C")
print("T1 =", T[0])
print("T2 =", T[1])
print("T3 =", T[2])
print("T4 = 50°C")