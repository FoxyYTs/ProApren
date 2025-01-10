num1 = 2
num2 = 2
entero = 0
decimales = 0

# Dividir la parte entera
while num1 >= num2:
    num1 -= num2
    entero += 1.0

# Verificar si hay una parte decimal
if num1 > 0:
    num1 *= 100

# Dividir la parte decimal
while num1 >= num2:
    num1 -= num2
    decimales += 0.01

print(entero + decimales)
