import numpy as np
import matplotlib.pyplot as plt

def ecuacion_caracteristica(edades):
    promedio = np.mean(edades)
    desviacion_estandar = np.std(edades)
    x = np.linspace(promedio - 3 * desviacion_estandar, promedio + 3 * desviacion_estandar, 100)
    y = (1/1000) * (x - promedio)**2
    return x, y

def graficar_comportamiento(edades):
    x, y = ecuacion_caracteristica(edades)
    plt.plot(x, y, color="red")
    plt.title("Comportamiento del conjunto de edades")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.show()

edades = np.array([20, 25, 30, 35, 40, 45, 50])

graficar_comportamiento(edades)