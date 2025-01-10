class Cine:
    def __init__(self, nombre, direccion, capacidadTotal, numeroSalas, telefono, correoElectronico):
        self._nombre = nombre
        self._direccion = direccion
        self._capacidadTotal = capacidadTotal
        self._numeroSalas = numeroSalas
        self._telefono = telefono
        self._correoElectronico = correoElectronico

    def __str__(self):
        return f"Cine {self._nombre} | Dirección: {self._direccion} | Capacidad Total: {self._capacidadTotal} | Número de Salas: {self._numeroSalas} | Teléfono: {self._telefono} | Correo Electrónico: {self._correoElectronico}"

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_capacidadTotal(self):
        return self._capacidadTotal

    def set_capacidadTotal(self, capacidadTotal):
        self._capacidadTotal = capacidadTotal

    def get_numeroSalas(self):
        return self._numeroSalas

    def set_numeroSalas(self, numeroSalas):
        self._numeroSalas = numeroSalas

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_correoElectronico(self):
        return self._correoElectronico

    def set_correoElectronico(self, correoElectronico):
        self._correoElectronico = correoElectronico
