import numpy as np
import matplotlib.pyplot as plt

C = 2.5e-4
dt = 5e-4

q_tabla = np.array([0.000,0.001,0.002,0.003,0.004,0.005,0.006])

R_tabla = np.array([0.05,0.18,0.32,0.45,0.67,0.97,1.17])

def R_interpolada(q):

    return np.interp(q, q_tabla, R_tabla)

def f(q):

    Rq = R_interpolada(q)

    E = (q**2)/(2*C)

    return -(1/(Rq*C))*np.sqrt((2*E)/C)

t = 0
q = 6e-3

print("CONDICIÓN INICIAL")
print(f"t0 = {t:.6f} s")
print(f"q0 = {q:.6f} C")

q1 = q + dt*f(q)

print("\nPRIMERA ITERACIÓN")

print(f"q1 = {q1:.6f} C")

if q1 < 0:

    print("\nERROR NUMÉRICO DETECTADO")

    print(
        "La primera iteración produjo una "
        "carga negativa."
    )

    print(
        "El valor obtenido está fuera del "
        "rango físico y experimental."
    )

    print(
        "No es posible calcular q2 porque "
        "se requeriría evaluar R(q) para "
        "una carga fuera de la tabla."
    )

    print(
        "La simulación se detiene por "
        "inestabilidad numérica del método."
    )

else:

    q2 = q1 + dt*f(q1)

    print("\nSEGUNDA ITERACIÓN")
    print(f"q2 = {q2:.6f} C")