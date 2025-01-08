class Espectador:
    def __init__(self, nombre, apellido, dni, fechaNacimiento, telefono, correoElectronico):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._fechaNacimiento = fechaNacimiento
        self._telefono = telefono
        self._correoElectronico = correoElectronico

    def __str__(self):
        return f"Espectador {self._nombre} {self._apellido} | DNI: {self._dni} | Fecha de Nacimiento: {self._fechaNacimiento} | Teléfono: {self._telefono} | Correo Electrónico: {self._correoElectronico}"

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        self._dni = dni

    def get_fechaNacimiento(self):
        return self._fechaNacimiento

    def set_fechaNacimiento(self, fechaNacimiento):
        self._fechaNacimiento = fechaNacimiento

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_correoElectronico(self):
        return self._correoElectronico

    def set_correoElectronico(self, correoElectronico):
        self._correoElectronico = correoElectronico
