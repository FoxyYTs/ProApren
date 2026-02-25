import numpy as np
import matplotlib.pyplot as plt

# Configuración inicial para mostrar los resultados con más decimales
np.set_printoptions(precision=6, suppress=True)

# --- 1. Definición de la función y el método de búsqueda ---
def f(x):
    """La función para la cual queremos encontrar las raíces: 2^x - x^2 = 0."""
    return 2*x - x*2

def busqueda_incremental(intervalo_inicio, intervalo_fin, paso_inicial, tolerancia=1e-6):
    """
    Realiza una búsqueda incremental para encontrar raíces de f(x)=0.
    Muestra las iteraciones y refina las raíces encontradas.
    """
    x_izq = intervalo_inicio
    paso = paso_inicial
    raices_encontradas = []

    print("--- Iniciando búsqueda incremental ---")
    print(f"Rango: [{intervalo_inicio}, {intervalo_fin}], Paso inicial: {paso}\n")

    while x_izq <= intervalo_fin:
        x_der = x_izq + paso
        f_izq = f(x_izq)
        f_der = f(x_der)

        # Mostrar la iteración actual
        print(f"Iter: x=[{x_izq:.4f}, {x_der:.4f}], f(x) = [{f_izq:.6f}, {f_der:.6f}]")

        # Criterio de cambio de signo para detectar una raíz
        if f_izq * f_der < 0:
            print(f"  ---> Cambio de signo detectado. Refinando...")
            
            # Refinamiento local (similar al método de bisección)
            a, b = x_izq, x_der
            fa, fb = f_izq, f_der
            paso_fino = (b - a) / 2
            
            while paso_fino > tolerancia:
                x_medio = (a + b) / 2
                f_medio = f(x_medio)
                
                if fa * f_medio <= 0:
                    b, fb = x_medio, f_medio
                else:
                    a, fa = x_medio, f_medio
                paso_fino = (b - a) / 2
            
            raiz_aprox = (a + b) / 2
            raices_encontradas.append(raiz_aprox)
            print(f"  >>> Raíz aproximada: x = {raiz_aprox:.8f}, f(x) = {f(raiz_aprox):.2e}\n")
        
        x_izq = x_der
    
    return raices_encontradas

# --- 2. Ejecutar la búsqueda ---
# Buscamos en un rango que cubra las raíces conocidas (2,4) y la negativa.
rango = [-2, 5]
raices = busqueda_incremental(rango[0], rango[1], paso_inicial=0.5, tolerancia=1e-8)

print("\n--- Resumen de raíces encontradas ---")
for i, r in enumerate(raices):
    print(f"Raíz {i+1}: x = {r:.8f}")

# --- 3. Graficar los resultados ---
# Generamos datos para las curvas
x_vals = np.linspace(rango[0], rango[1], 400)
y1 = 2**x_vals          # Función exponencial
y2 = x_vals**2          # Función cuadrática
y_diferencia = f(x_vals) # Diferencia (2^x - x^2)

# Crear la figura con subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# --- Gráfica 1: Las funciones por separado ---
ax1.plot(x_vals, y1, 'b-', linewidth=2, label=r'$2^x$')
ax1.plot(x_vals, y2, 'r--', linewidth=2, label=r'$x^2$')
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.grid(True, alpha=0.3, linestyle='--')

# Marcar las raíces (puntos de intersección)
for i, r in enumerate(raices):
    ax1.plot(r, 2**r, 'go', markersize=8, label=f'Raíz {i+1}' if i == 0 else "")
    ax1.plot(r, r**2, 'go', markersize=8)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title(r'Intersección de $2^x$ y $x^2$')
ax1.legend()
ax1.set_xlim(rango)

# --- Gráfica 2: La función diferencia f(x) = 2^x - x^2 ---
ax2.plot(x_vals, y_diferencia, 'm-', linewidth=1.5, label=r'$f(x) = 2^x - x^2$')
ax2.axhline(0, color='black', linewidth=1)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.grid(True, alpha=0.3, linestyle='--')

# Marcar las raíces (donde la función cruza el cero)
for i, r in enumerate(raices):
    ax2.plot(r, 0, 'ro', markersize=6)
    ax2.text(r, 0.5, f' x={r:.3f}', fontsize=9, verticalalignment='bottom')

ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.set_title(r'$f(x) = 2^x - x^2$ (Los ceros son las raíces)')
ax2.legend()
ax2.set_xlim(rango)
ax2.set_ylim(-5, 20)

plt.tight_layout()
plt.show()