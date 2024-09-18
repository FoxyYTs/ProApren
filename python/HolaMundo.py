operacion = int(input("1) Sumar\n2) Restar\nIngresa Opcion: "))
x = float(input("Ingresa un numero"))
y = float(input("Ingresa otro numero"))
if operacion == 1:
    print("La Suma es: ", x + y)
elif operacion == 2:
    print("La Resta es: ", x - y)
