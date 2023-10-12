from conexion import DataBase

class Vehiculo(DataBase):
    def __init__(self, id="", nombre="", anio=0, marca="", tipo="", combustible="", precio=0.0):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.anio = anio
        self.marca = marca
        self.tipo = tipo
        self.combustible = combustible
        self.precio = precio
    
     # GETTERS
    def getId(self):
        """Retorna el ID del vehículo."""
        return self.id

    def getNombre(self):
        """Retorna el nombre del vehículo."""
        return self.nombre

    def getAnio(self):
        """Retorna el año del vehículo."""
        return self.anio

    def getMarca(self):
        """Retorna la marca/fabricante del vehículo."""
        return self.marca
    
    def getTipo(self):
        """Retorna el tipo del vehículo."""
        return self.tipo

    def getCombustible(self):
        """Retorna el tipo de combustible que usa el vehiculo."""
        return self.combustible

    def getPrecio(self):
        """Retorna el precio del vehículo."""
        return self.precio

    # SETTERS

    def setId(self, id):
        """
        Establece el ID del vehículo.

        Args:
            id(string): El nuevo ID del vehículo.
        """
        self.id = id

    def setNombre(self, nombre):
        """
        Establece el nombre del vehículo.

        Args:
            nombre(str): El nuevo nombre del vehículo.
        """
        self.nombre = nombre

    def setAnio(self, anio):
        """
        Establece el año del vehículo.

        Args:
            anio(int): El nuevo año del vehículo.
        """
        self.anio = anio

    def setMarca(self, marca):
        """
        Establece la marca del vehículo.

        Args:
            marca(str): La nueva marca del vehículo.
        """
        self.marca = marca

    def setTipo(self, tipo):
        """
        Establece el tipo del vehículo.

        Args:
            tipo(str): El nuevo tipo del vehículo.
        """
        self.tipo = tipo

    def setCombustible(self, combustible):
        """
        Establece el combustible del vehículo.

        Args:
            combustible(str): El nuevo combustible del vehículo.
        """
        self.combustible = combustible

    def setPrecio(self, precio):
        """
        Establece el precio del vehículo.

        Args:
            precio(float): El nuevo precio del vehículo.
        """
        self.precio = precio
            
