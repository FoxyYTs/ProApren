import os
import time
from Rock import Rock,datos 

opcion = 1
while (opcion != 5):
    selecto = True
    while selecto:
        key = input("Ingresa la llave foranea: ")
        try:
            cancion = Rock(key)
        except:
            print("ERROR FATAL")
        else:
            selecto = False
            try:
                cancion.IniciarTabla()
            except:
                continue
    os.system("cls")
    opcion = int(input("Que opcion deseas realizar\n1) Crear Dato en la BD\n2) Mostrar Dato en la BD\n3) Actualizar Dato en la BD\n4) Eliminar Dato en la BD\n5) Salir\nELECCION: "))
    if opcion == 1:
        cancion.agregarDatos()
    elif opcion == 2:
        cancion.LeerDatos()
        
    elif opcion == 3:
        cancion.LeerDatos()
        print("Ingrese qué numero de dato del vehiculo desea modificar:")
        datoAct = int(input())
        print(f"Ingrese el valor por el que desea modificar {datos[datoAct-1]}")
        datoCambio = input()
        cancion.ActualizarDatos(datoAct, datoCambio)
    elif opcion == 4:
        cancion.EliminarDatos()

    elif opcion == 5:
        os.system("cls")
        time.sleep(1)
        print("Cerrando Programa...")
        continue
    else:
        print("Opcion no valida")
        continue