import random
import matplotlib.pyplot as plt
import numpy as np

# Inicializar el vector con 120 elementos
vector = [0] * 120

for i in range(120):
    numero_aleatorio = random.randint(1, 50)
    vector[i] = numero_aleatorio

# Funciones para calcular los valores
def log_base_n(x, base):
    return np.log(x) / np.log(base)

def lineal(x):
    return x

def logaritmica_base_2(x):
    return log_base_n(x, 2)

def semilogaritmica(x):
    return x * logaritmica_base_2(x)

def logaritmica_base_8(x):
    return 120 * log_base_n(x, 8)

def cuadratica(x):
    return x ** 2

def cubica(x):
    return x ** 3

def exponencial(x):
    return 2 ** x

# Valores del eje x
x = np.arange(10, 1210,10) 

print(x) # desde 1 hasta 120

# Calcular los valores de las funciones
y_lineal = lineal(x)
y_log2 = logaritmica_base_2(x)
y_semilog = semilogaritmica(x)
y_log8 = logaritmica_base_8(x)
y_cuadratica = cuadratica(x)
y_cubica = cubica(x)
y_exponencial = exponencial(x)

# Crear subplots
fig, axs = plt.subplots(2, 3, figsize=(18, 12))

# Gráfica Lineal
axs[0, 0].plot(x, y_lineal, label='Lineal')
axs[0, 0].set_title('Gráfica Lineal')
axs[0, 0].set_xlabel('Cantidad de datos')
axs[0, 0].set_ylabel('Valor de la función')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Gráficas Logarítmicas
axs[0, 1].plot(x, y_log2, label='Logarítmica base 2')
axs[0, 1].plot(x, y_semilog, label='Semilogarítmica')
axs[0, 1].plot(x, y_log8, label='Logarítmica base 8')
axs[0, 1].set_title('Gráficas Logarítmicas')
axs[0, 1].set_xlabel('Cantidad de datos')
axs[0, 1].set_ylabel('Valor de la función')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Gráfica Cuadrática
axs[0, 2].plot(x, y_cuadratica, label='Cuadrática')
axs[0, 2].set_title('Gráfica Cuadrática')
axs[0, 2].set_xlabel('Cantidad de datos')
axs[0, 2].set_ylabel('Valor de la función')
axs[0, 2].legend()
axs[0, 2].grid(True)

# Gráfica Exponencial
x_exponencial = np.arange(1, 28)
y_exponencial_27 = exponencial(x_exponencial)
axs[1, 0].plot(x_exponencial, y_exponencial_27, label='Exponencial')
axs[1, 0].set_title('Gráfica Exponencial')
axs[1, 0].set_xlabel('Cantidad de datos')
axs[1, 0].set_ylabel('Valor de la función')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Gráfica Cúbica
axs[1, 1].plot(x, y_cubica, label='Cúbica')
axs[1, 1].set_title('Gráfica Cúbica')
axs[1, 1].set_xlabel('Cantidad de datos')
axs[1, 1].set_ylabel('Valor de la función')
axs[1, 1].legend()
axs[1, 1].grid(True)

# Ocultar el último subplot que no se está utilizando
axs[1, 2].axis('off')

# Ajustar el espacio entre subplots
plt.tight_layout()

# Mostrar los subplots
plt.show()