
def secuencia():
    x = float(input("Ingrese el valor inicial: "))
    for i in range(1, int(input("Ingrese el numero de iteraciones: "))+1):
        x = x ** 2 
        print("Iteracion: ",i ," Valor de x: ", x)

def secuencia2():
    x = float(input("Ingrese el valor inicial: "))
    for i in range(1, int(input("Ingrese el numero de iteraciones: "))+1):
        x = 2*(x ** 2) 
        print("Iteracion: ",i ," Valor de x: ", x)
        
if __name__ == "__main__":
    opcion = int(input("1) para la secuencia x^2 - 1 \n2) para la secuencia 2*x^2 - 1\nIngrese su opcion: "))

    if opcion == 1:
        secuencia()
    elif opcion == 2:
        secuencia2()