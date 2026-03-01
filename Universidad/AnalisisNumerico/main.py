import matplotlib.pyplot as plt
from sympy import *

def biseccion_con_grafica(f, v, a, b, e):
    lista_errores = []
    iteraciones = []
    i = 0
    
    # Error inicial (longitud del intervalo)
    ancho_intervalo = abs(b - a)
    
    while ancho_intervalo >= e:
        c = (a + b) / 2
        
        # El error máximo posible en la iteración i es la mitad del intervalo actual
        error_actual = ancho_intervalo / 2
        lista_errores.append(error_actual)
        iteraciones.append(i)
        
        # Lógica de bisección
        if f.subs(v, c) == 0:
            break
        if f.subs(v, a) * f.subs(v, c) > 0:
            a = c
        else:
            b = c
            
        ancho_intervalo = abs(b - a)
        i += 1
    
    # --- Generación de la Gráfica ---
    plt.figure(figsize=(10, 6))
    plt.plot(iteraciones, lista_errores, marker='o', color='b', linestyle='-')
    
    # Aplicamos escala logarítmica para ver la convergencia lineal
    plt.yscale('log') 
    
    plt.title('Convergencia del Método de Bisección: Error vs Iteración')
    plt.xlabel('Número de Iteración ($n$)')
    plt.ylabel('Error estimado ($log_{10}$)')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.show()

    return c, lista_errores

# Ejemplo de uso:
x = symbols('x')
funcion = x**2 - 2  # Buscamos raíz de 2 (~1.4142)
raiz, errores = biseccion_con_grafica(funcion, x, 1, 2, 1e-5)

print(f"Raíz aproximada: {raiz}")
print(f"Número de iteraciones: {len(errores)}")
