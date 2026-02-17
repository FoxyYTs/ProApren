import sys
import math
import matplotlib as plit
#PRE PROCESO
x = 0.3 #Valor Semilla

#PROCESO
iteration = 0
values = []
iterations = []

print("precision de la maquina (float info): ")
print(f"Maximo: {sys.float_info.max} Supremo")
print(f"Minimo: {sys.float_info.min} Infimo")
print(f"Epsilon: {sys.float_info.epsilon} Error")

while x != 0.0:
    values.append(x)
    iterations.append(iteration)
    
    if x < sys.float_info.min:
        print(f"Iteracion: {iteration}: {x} <- Subnormal")
        
    else:
        print(f"Iteracion: {iteration}: {x}")
        x = x**2
        iteration += 1
    print("-"*60)
    print(f"Underflow a 0.0 en iteracion: {iteration}")