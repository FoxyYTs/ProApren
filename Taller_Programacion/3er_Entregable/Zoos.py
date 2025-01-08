from Conexion import Conexion

class Zoo(Conexion):
    
    def __init__(self, nombre="", ubicacion=""):
        """
        Inicializa una nueva instancia de la clase.

        Parámetros:
            nombre (str): El nombre de la instancia. Por defecto, una cadena vacía.
            ubicacion (str): La ubicación de la instancia. Por defecto, una cadena vacía.

        Retorna:
            Ninguno
        """
        Conexion.__init__(self)
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.crear()

    def crear(self):
        """
        Crea un nuevo objeto "Zoos".

        Esta función crea un nuevo objeto "Zoos" llamando al método `create` con los parámetros "Zoos" y "Zoo".

        Parámetros:
            self: La instancia actual de la clase.

        Retorna:
            Ninguno
        """
        self.create("Zoos", "Zoo")

    def leer(self):
        """
        Lee los datos de la tabla "Zoos" y los asigna al atributo 'datosEnLaTabla'.
        Esta función no toma ningún parámetro.
        Esta función no devuelve ningún valor.
        """
        self.datosEnLaTabla = self.read("Zoos")

    def editar(self, nuevoDato, columna, id):
        """
        Actualiza un registro en la tabla "Zoos" con un nuevo valor para una columna especificada y un id.

        :param nuevoDato: El nuevo valor para actualizar el registro.
        :type nuevoDato: Cualquier tipo
        :param columna: El nombre de la columna a actualizar.
        :type columna: str
        :param id: El id del registro a actualizar.
        :type id: int
        :return: True si el registro se actualizó correctamente, False de lo contrario.
        :rtype: bool
        """
        if self.update(nuevoDato, "Zoos", columna, id):
            return True
        else:
            return False

    def eliminar(self, id):
        """
        Elimina un registro de la tabla "Zoos" basado en el ID proporcionado.

        :param id: El ID del registro a eliminar.
        :type id: int

        :return: True si el registro se eliminó correctamente, False de lo contrario.
        :rtype: bool
        """
        if self.delete("Zoos", id):
            return True
        else:
            return False

    def insertar(self):
        """
        Inserta un nuevo registro en la tabla "Zoos" con el nombre y ubicación dados.

        Parámetros:
            self (objeto): La instancia de la clase.
        
        Retorna:
            Ninguno
        """
        datos = [
            (f"{self.nombre}", f"{self.ubicacion}")
        ]
        self.insert("Zoos", 2, datos)