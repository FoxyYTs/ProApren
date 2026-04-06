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
A = np.array([[70, 1,  0],
              [60, 100, 1],
              [40, 0,  -1]], dtype=float)

b = np.array([636, 518, 307], dtype=float)

# Valores iniciales
T0 = np.zeros(3)

# Valores iniciales aleatorios
#T0 = np.array([8, 34, 36], dtype=float)
tol = 1e-8
max_iter = 100

iters = []
T_vals = []
err_abs = []
err_rel = []

T = T0.copy()

# ==================================================
# PROCESO – JACOBI
# ==================================================

D = np.diag(np.diag(A))
R = A - D

D_inv = np.linalg.inv(D)

for k in range(1, max_iter+1):

    T_new = D_inv @ (b - R @ T)

    iters.append(k)
    T_vals.append(T_new.copy())

    ea = np.linalg.norm(T_new - T, np.inf)
    er = ea / np.linalg.norm(T_new, np.inf)

    err_abs.append(ea)
    err_rel.append(er)

    if ea < tol:
        break

    T = T_new

# ==================================================
# POSTPROCESO
# ==================================================

print("\nTABLA DE ITERACIONES")
print("Iter |      T1      T2      T3    | Error Abs | Error Rel")
print("----------------------------------------------------------------")

for i in range(len(iters)):
    T1, T2, T3 = T_vals[i]
    print(f"{iters[i]:>3} | {T1:8.4f} {T2:8.4f} {T3:8.4f} | "
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
plt.title('Errores vs Iteraciones - Jacobi')
plt.legend()
plt.grid(True)

plt.figure()
plt.semilogy(iters, err_abs, 'o-', label='Error absoluto')
plt.semilogy(iters, err_round, '--', label='Error redondeo')
plt.semilogy(iters, err_total, 's-', label='Error total')
plt.xlabel('Iteraciones')
plt.ylabel('Error')
plt.title('Composición del Error Numérico - Jacobi')
plt.legend()
plt.grid(True)

plt.show()

# ==================================================
# RESULTADOS FÍSICOS
# ==================================================

T_sol = T_vals[-1]

print("\nRESULTADOS FÍSICOS")
print("T1 =", T_sol[0])
print("T2 =", T_sol[1])
print("T3 =", T_sol[2])

print("\nPerfil completo de temperatura:")
print("T0 = 100°C")
print("T1 =", T_sol[0])
print("T2 =", T_sol[1])
print("T3 =", T_sol[2])
print("T4 = 50°C")