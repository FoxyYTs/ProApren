import numpy as np
import matplotlib.pyplot as plt

class PerceptronSimple:
    def __init__(self, tasa_aprendizaje=0.1, epocas=100):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = None
        self.sesgo = None
        self.errores = []
    
    def funcion_activacion(self, x):
        """Función escalón: 1 si x >= 0, 0 en otro caso"""
        return 1 if x >= 0 else 0
    
    def predecir(self, x):
        """Hace una predicción para una entrada x"""
        suma = np.dot(x, self.pesos) + self.sesgo
        return self.funcion_activacion(suma)
    
    def entrenar(self, X, y):
        """Entrena el perceptrón con los datos X y las etiquetas y"""
        # Inicializar pesos y sesgo aleatoriamente
        n_caracteristicas = X.shape[1]
        self.pesos = np.random.rand(n_caracteristicas)
        self.sesgo = np.random.rand()
        
        print("Iniciando entrenamiento...")
        print(f"Pesos iniciales: {self.pesos}, Sesgo inicial: {self.sesgo:.3f}")
        
        for epoca in range(self.epocas):
            error_total = 0
            for i in range(len(X)):
                # Predicción
                prediccion = self.predecir(X[i])
                
                # Calcular error
                error = y[i] - prediccion
                error_total += abs(error)
                
                # Actualizar pesos y sesgo
                self.pesos += self.tasa_aprendizaje * error * X[i]
                self.sesgo += self.tasa_aprendizaje * error
            
            self.errores.append(error_total)
            
            if epoca % 20 == 0:
                print(f"Época {epoca}: Error = {error_total}")
            
            # Si no hay error, terminar temprano
            if error_total == 0:
                print(f"¡Entrenamiento completado en la época {epoca}!")
                break
    
    def graficar_aprendizaje(self):
        """Grafica la curva de aprendizaje"""
        plt.figure(figsize=(10, 6))
        plt.plot(self.errores)
        plt.title('Curva de Aprendizaje del Perceptrón')
        plt.xlabel('Época')
        plt.ylabel('Error Total')
        plt.grid(True)
        plt.show()

# Datos de entrenamiento: Compuerta AND
# Entradas: [x1, x2], Salida: y
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])  # Salidas esperadas para AND

print("=== DATOS DE ENTRENAMIENTO ===")
print("Compuerta AND:")
for i in range(len(X)):
    print(f"Entrada: {X[i]} -> Salida esperada: {y[i]}")

# Crear y entrenar el perceptrón
print("\n=== ENTRENAMIENTO ===")
perceptron = PerceptronSimple(tasa_aprendizaje=0.1, epocas=100)
perceptron.entrenar(X, y)

# Probar el modelo entrenado
print("\n=== PRUEBAS ===")
print("Probando el perceptrón entrenado:")
for i in range(len(X)):
    prediccion = perceptron.predecir(X[i])
    print(f"Entrada: {X[i]} -> Predicción: {prediccion} (Esperado: {y[i]})")

# Mostrar pesos finales
print(f"\nPesos finales: {perceptron.pesos}")
print(f"Sesgo final: {perceptron.sesgo:.3f}")

# Graficar el aprendizaje
perceptron.graficar_aprendizaje()

# Probar con nuevas entradas
print("\n=== PREDICCIONES CON NUEVAS ENTRADAS ===")
nuevas_entradas = [
    [0.5, 0.5],
    [0.8, 0.2],
    [0.9, 0.9]
]

for entrada in nuevas_entradas:
    prediccion = perceptron.predecir(entrada)
    print(f"Entrada: {entrada} -> Predicción: {prediccion}")