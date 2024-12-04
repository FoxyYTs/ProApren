class Lote:
    def __init__(self, id_lote, ubicacion, tipo_lote, ancho, largo, costo_metro_cuadrado):
        
        """
        Inicializa una instancia de Lote con los parámetros proporcionados.

        Args:
        id_lote: El identificador único del lote.
        ubicacion: La ubicación del lote.
        tipo_lote: El tipo de lote.
        ancho: El ancho del lote.
        largo: La longitud del lote.
        costo_metro_cuadrado: El costo por metro cuadrado del lote.

        Establece:
        metro_cuadrado: El área del lote calculada como 'ancho' por 'largo'.
        vendido: Booleano que indica si el lote ha sido vendido, inicialmente establecido en Falso.
        Comprador: El comprador del lote, inicialmente establecido en Ninguno.
        """
        self.id_lote = id_lote
        self.ubicacion = ubicacion
        self.tipo_lote = tipo_lote
        self.metro_cuadrado = ancho * largo
        self.ancho = ancho
        self.largo = largo
        self.costo_metro_cuadrado = costo_metro_cuadrado
        self.vendido = False
        self.Comprador = None

    def cal_costo(self):
        return self.metro_cuadrado * self.costo_metro_cuadrado
    
class Comprador:
    def __init__(self, nombre, telefono, identificacion, nombre_referencia, telefono_referencia):

        """
        Inicializa un objeto de la clase Comprador con los parámetros
        nombre, telefono, identificacion, nombre_referencia y telefono_referencia.
        El comprador se crea sin propiedades.
        """
        self.nombre = nombre
        self.telefono = telefono
        self.identificacion = identificacion
        self.nombre_referencia = nombre_referencia
        self.telefono_referencia = telefono_referencia
        self.lotes = []

def solicitar_datos_lote():
    """
    Solicita los datos de un lote al usuario y devuelve un objeto Lote
    con los datos ingresados.
    
    Returns:
        Lote: Un objeto Lote con los datos ingresados por el usuario.
    """
    id_lote = input("Ingrese la identificación del lote: ")
    ubicacion = input("Ingrese la ubicación del lote: ")
    tipo_lote = input("Ingrese el tipo de lote: ")
    ancho = float(input("Ingrese el ancho del lote en metros: "))
    largo = float(input("Ingrese el largo del lote en metros: "))
    costo_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado: "))
    return Lote(id_lote, ubicacion, tipo_lote, ancho, largo, costo_metro_cuadrado)

def solicitar_datos_comprador():
    """
    Solicita los datos de un comprador al usuario y devuelve un objeto Comprador
    con los datos ingresados.
    
    Returns:
        Comprador: Un objeto Comprador con los datos ingresados por el usuario.
    """
    nombre = input("Ingrese el nombre del comprador: ")
    telefono = input("Ingrese el teléfono del comprador: ")
    identificacion = input("Ingrese la identificación del comprador: ")
    nombre_referencia = input("Ingrese el nombre de la persona de referencia: ")
    telefono_referencia = input("Ingrese el teléfono de la persona de referencia: ")
    return Comprador(nombre, telefono, identificacion, nombre_referencia, telefono_referencia)

def mostrar_lote(lote):
    """
    Muestra la información detallada de un lote.

    Args:
        lote (Lote): El objeto Lote del cual se desea mostrar la información.

    Prints:
        La identificación, ubicación, tipo, metros cuadrados, dimensiones,
        costo por metro cuadrado, estado de venta, y si está vendido, el nombre
        del dueño del lote.
    """
    print("\nIdentificación: ", lote.id_lote)
    print("Ubicación: ", lote.ubicacion)
    print("Tipo de lote: ", lote.tipo_lote)
    print("Metros cuadrados: ", lote.metro_cuadrado)
    print("Ancho: ", lote.ancho)
    print("Largo: ", lote.largo)
    print("Costo por metro cuadrado: ", lote.costo_metro_cuadrado)
    print("Vendido: ", lote.vendido)
    if lote.vendido:
        print("Dueño: ", lote.dueño.nombre)
    print("-----------------------------------------------------------------------------------")

def mostrar_comprador(comprador):
    """
    Muestra la información detallada de un objeto Comprador.

    Prints:
        El nombre, teléfono, identificación, nombre de la persona de referencia
        y teléfono de la persona de referencia del comprador, así como la
        cantidad de propiedades que posee y una lista de dichas propiedades.
    """
    print("\nNombre: ", comprador.nombre)
    print("Teléfono: ", comprador.telefono)
    print("Identificación: ", comprador.identificacion)
    print("Nombre de la persona de referencia: ", comprador.nombre_referencia)
    print("Teléfono de la persona de referencia: ", comprador.telefono_referencia)
    print("Propiedades: ", len(comprador.lotes))
    lista_propiedades(comprador)
    print("===================================================================================")



def lista_propiedades(comprador):
    """
    Muestra la lista de las propiedades de un comprador.

    Si el comprador no tiene propiedades, se muestra un mensaje indicando esto.
    De lo contrario, se muestra la lista de propiedades del comprador, con todos
    sus detalles.

    Args:
        comprador (Comprador): El objeto Comprador del cual se desea mostrar la lista de propiedades.
    """
    if not comprador.lotes:
        print("El comprador no tiene propiedades.")
        return
    print("-----------------------------------------------------------------------------------")
    for lote in comprador.lotes:
        mostrar_lote(lote)


def listas_compradores():
    """
    Muestra la lista de todos los compradores creados hasta el momento.

    Prints:
        La lista de todos los compradores con sus respectivos datos.
    """
    print("Lista de compradores:")
    for comprador in lista_compradores:
        mostrar_comprador(comprador)

def listas_lotes():
    """
    Muestra la lista de todos los lotes creados hasta el momento.

    Prints:
        La lista de todos los lotes con sus respectivos datos.
    """

    print("Lista de lotes:")
    for lote in lista_lotes:
        mostrar_lote(lote)

def vender_lote():
    
    """
    Vende un lote a un comprador registrado en la lista de compradores.

    Solicita al usuario la identificación del lote a vender y la 
    identificación del comprador. Si el comprador y el lote existen,
    y el lote no ha sido vendido, cambia el estado del lote a vendido,
    asocia el lote al comprador y registra la transacción.

    Prints:
        Mensaje de éxito si la venta se realiza correctamente, o un mensaje
        de error si el lote ya está vendido, o si no se encuentra el lote o
        el comprador.
    """
    id_lote = int(input("Ingrese la identificación del lote a vender: "))
    identificacion = input("Ingrese la identificación del comprador: ")
    cliente = None

    for comprador in lista_compradores:
        if comprador.identificacion == identificacion:
            cliente = comprador
            break


    for lote in lista_lotes:
        if lote.id_lote == id_lote:
            if lote.vendido == False:
                lote.vendido = True
                lote.dueño = cliente
                cliente.lotes.append(lote)
                print("Lote vendido exitosamente.")
                input("")
                return
            else:
                print("El lote ya tiene dueño.")
                input("")
                return

    print("No se encontró el lote o el comprador")
    input("")
    

def menu():
    """
    Muestra el menú principal de la aplicación y permite al usuario
    interactuar con las diferentes opciones.

    Opciones:
        1. Crear nuevo comprador
        2. Crear nuevo lote
        3. Vender lote
        4. Ver lista de compradores
        5. Ver lista de lotes
        6. Salir

    La función se encarga de evaluar la opción ingresada por el usuario y
    llamar a la función correspondiente.
    """
    while True:
        print("\nMenú Principal")
        print("1. Crear nuevo comprador")
        print("2. Crear nuevo lote")
        print("3. Vender Lote")
        print("4. Ver lista de compradores")
        print("5. Ver lista de lotes")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            
            nuevo_comprador = solicitar_datos_comprador()
            lista_compradores.append(nuevo_comprador)
            print("Comprador creado exitosamente.")
        elif opcion == '2':
            
            nuevo_lote = solicitar_datos_lote()
            lista_lotes.append(nuevo_lote)
            print("Lote creado exitosamente.")
        elif opcion == '3':
            vender_lote()
        elif opcion == '4':
            
            listas_compradores()
        elif opcion == '5':
            
            listas_lotes()
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")



lista_compradores = []
lista_lotes = []

def generador_compradores():
    """
    Genera y agrega 10 objetos Comprador ficticios a la lista_compradores.

    Cada objeto Comprador se crea con un nombre, ID, número de teléfono, referencia y 
    número de contacto alternativo únicos, utilizando el índice de iteración actual para garantizar la unicidad.
    """
    for i in range(10):
        comprador = Comprador(f"Comprador {i}", i, f"1{i}", f"Referencia {i}", f"987654321{i}")
        lista_compradores.append(comprador)
def generador_lotes():
    """
    Genera y agrega 10 objetos Lote ficticios a la lista_lotes.

    Cada objeto Lote se crea con un ID, ubicación, tipo, área, precio y cantidad de habitaciones únicos, utilizando 
    el índice de iteración actual para garantizar la unicidad.
    """
    for i in range(10):
        lote = Lote(i, f"Ubicación {i}", f"Tipo {i}", i, i, i)
        lista_lotes.append(lote)

if __name__ == "__main__":
    generador_compradores()
    generador_lotes()
    menu()