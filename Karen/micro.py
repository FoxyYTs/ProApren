class Lote:
    def __init__(self, ubicacion, tipo_lote, ancho, largo, costo_metro_cuadrado, vendido):
        self.ubicacion = ubicacion
        self.tipo_lote = tipo_lote
        self.metro_cuadrado = ancho * largo
        self.ancho = ancho
        self.largo = largo
        self.costo_metro_cuadrado = costo_metro_cuadrado
        self.vendido = vendido

    def cal_costo(self):
        return self.metro_cuadrado * self.costo_metro_cuadrado
    
class Comprador:
    def __init__(self, nombre, telefono, identificacion, nombre_referencia, telefono_referencia):
        self.nombre = nombre
        self.telefono = telefono
        self.identificacion = identificacion
        self.nombre_referencia = nombre_referencia
        self.telefono_referencia = telefono_referencia

def solicitar_datos_lote():
    ubicacion = input("Ingrese la ubicación del lote: ")
    tipo_lote = input("Ingrese el tipo de lote: ")
    ancho = float(input("Ingrese el ancho del lote en metros: "))
    largo = float(input("Ingrese el largo del lote en metros: "))
    costo_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado: "))
    return Lote(ubicacion, tipo_lote, ancho, largo, costo_metro_cuadrado, False)

def solicitar_datos_comprador():
    nombre = input("Ingrese el nombre del comprador: ")
    telefono = input("Ingrese el teléfono del comprador: ")
    identificacion = input("Ingrese la identificación del comprador: ")
    nombre_referencia = input("Ingrese el nombre de la persona de referencia: ")
    telefono_referencia = input("Ingrese el teléfono de la persona de referencia: ")
    return Comprador(nombre, telefono, identificacion, nombre_referencia, telefono_referencia)

def menu():
    while True:
        print("\nMenú Principal")
        print("1. Crear nuevo comprador")
        print("2. Crear nuevo lote")
        print("3. Cotizar lote para un comprador")
        print("4. Ver lista de compradores")
        print("5. Ver lista de lotes")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            nuevo_comprador = solicitar_datos_comprador()
            # Aquí deberías agregar el código para guardar al comprador en una lista o base de datos
            print("Comprador creado exitosamente.")
        elif opcion == '2':
            nuevo_lote = solicitar_datos_lote()
            # Aquí deberías agregar el código para guardar el lote en una lista o base de datos
            print("Lote creado exitosamente.")
        elif opcion == '3':
            # Implementa la lógica para buscar un lote, buscar un comprador y generar una cotización
            print("Cotización generada.")
        elif opcion == '4':
            # Implementa la lógica para mostrar la lista de compradores
            print("Lista de compradores:")
            # ...
        elif opcion == '5':
            # Implementa la lógica para mostrar la lista de lotes
            print("Lista de lotes:")
            # ...
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

# Inicialización de listas (o bases de datos) para almacenar los objetos
lista_compradores = []
lista_lotes = []

if __name__ == "__main__":
    menu()