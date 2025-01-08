from Conexion import Conexion

class Animal(Conexion):
    def __init__(self, nombre="", especie = "", zooID = 0):
        """
        Inicializa una nueva instancia de la clase.

        Args:
            nombre (str): El nombre del objeto. Por defecto, una cadena vacía.
            especie (str): La especie del objeto. Por defecto, una cadena vacía.
            zooID (int): El ID del zoo. Por defecto, 0.

        Returns:
            None
        """
        Conexion.__init__(self)
        self.nombre = nombre
        self.especie = especie
        self.zooID = zooID
        self.crear()

    def crear(self):
        """
        Crea un nuevo objeto "Animals" de tipo "Animal".

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        self.create("Animals", "Animal")

    def leer(self):
        """
        Lee los datos de la tabla "Animales" y los asigna al atributo `datosEnLaTabla`.

        Parámetros:
        - Ninguno

        Retorna:
        - Ninguno
        """
        self.datosEnLaTabla = self.read("Animals")

    def editar(self, nuevoDato, columna, id):
        """
        Edita una columna específica en la tabla "Animals" con los nuevos datos proporcionados.

        :param nuevoDato: Los nuevos datos que se actualizarán en la columna especificada.
        :type nuevoDato: Cualquier tipo
        :param columna: El nombre de la columna que se actualizará.
        :type columna: str
        :param id: El identificador único de la fila que se actualizará.
        :type id: int
        :return: True si la actualización fue exitosa, False de lo contrario.
        :rtype: bool
        """
        if self.update(nuevoDato, "Animals", columna, id):
            return True
        else:
            return False

    def eliminar(self, id):
        """
        Elimina un animal con el ID dado de la tabla "Animals".

        Parámetros:
            id (int): El ID del animal a eliminar.

        Retorna:
            bool: True si el animal fue eliminado exitosamente, False de lo contrario.
        """
        if self.delete("Animals", id):
            return True
        else:
            return False

    def insertar(self):
        """
        Inserta un nuevo registro en la tabla "Animals" con los datos proporcionados.

        Parámetros:
            Ninguno

        Retorna:
            Ninguno
        """
        datos = [
            (f"{self.nombre}", f"{self.especie}", f"{self.zooID}")
        ]
        self.insert("Animals", 3, datos)

    def eliminarTodo(self, id = 0):
        """
        Elimina todos los registros de la tabla "Animals".

        :param id: Un entero que representa el ID del registro a eliminar. Por defecto es 0.
        :type id: int

        :return: Ninguno
        """
        self.deleteAll("Animals",id)