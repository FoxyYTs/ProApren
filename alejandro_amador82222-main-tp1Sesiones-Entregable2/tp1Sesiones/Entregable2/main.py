from Automovil import Automovil,datos

# CREADOR POR: Alejandro Amador Ruiz (1007480914) y Andrés Felipe Montoya Lopez(1000758778)

print("Instrucciones: Deberá ingresar el id/placa del vehiculo según aparece en el excel, pues lo que hace este programa es pasar los datos que se encuentran en el excel a la base de datos de sqlite llamada database. Si un vehiculo no se encuentra en la base de datos, deberá ingresarlo con la opcion 1 del menú. Podrá eliminar el vehiculo en cuestión de la base de datos, leer los datos que contiene, y actualizar datos (Nota: actualizar los datos del vehiculo en la base de datos no los actualiza en el excel).")
print("\nCREADOR POR: Alejandro Amador Ruiz (1007480914) y Andrés Felipe Montoya Lopez(1000758778)\n")
opcion=1
while(opcion != 0):
    selecting=True
    while selecting:
        print("Ingrese el id o placa del vehiculo. (Tal como aparece en Excel):")
        id = input()
        try:
            carro = Automovil(id)
        except:
            print("Ese ID no se encuentra en la tabla de excel.")
        else:
            selecting=False
            try:
                carro.IniciarTabla()
            except:
                continue
    print(" ======= CRUD ENTRE EXCEL Y BASE DE DATOS ======= ")
    print(f"Que desea hacer con {id}?")
    print("1. Ingresar Datos.")
    print("2. Leer datos.")
    print("3. Actualizar datos.")
    print("4. Eliminar datos.")
    print("0. Salir.")
    opcion = int(input())
    match(opcion):
        case 1:
            try:
                carro.agregarDatos()
            except:
                print("No se pudo realizar la accion.")
        case 2:
            try:
                carro.LeerDatos()
            except:
                print("No se pudo realizar la accion.")
        case 3:
            try:
                carro.LeerDatos()
            except:
                print("No se pudo realizar la accion.")
                
            print("Ingrese qué numero de dato del vehiculo desea modificar:")
            datoAct = int(input())
            try:
                print(f"Ingrese el valor por el que desea modificar {datos[datoAct-1]}")
                datoCambio = input()
                carro.ActualizarDatos(datoAct, datoCambio)
            except: 
                print("No se pudo realizar la accion.")
        case 4:
            try:
                carro.EliminarDatos()
            except:
                print("No se pudo realizar la accion.")
        case 0:
            continue
        case  _:
            print("Opcion no valida.")    















/give FoxyYTs dungeons_gear:firebrand{Enchantments:[{id:fire_aspect,lvl:10}],Display:{Name:"Pedro"}} 1
/give @p 397 1 4 {display:{Name:"Nombre"}}