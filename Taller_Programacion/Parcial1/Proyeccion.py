from Cine import Cine
from Espectador import Espectador
class Proyeccion(Cine, Espectador):

    def __init__(self, sala, horaInicio, cine, espectador, precio):
        self._sala = sala
        self._horaInicio = horaInicio
        self._precio = precio

    def __str__(self):
        return f"Proyección | Sala: {self.sala} | Hora de Inicio: {self.horaInicio} | Cine: {self.nombre} | Película: {self.titulo} | Espectador: {self.nombre} {self.apellido} | Precio: {self.precio}"

    def get_sala(self):
        return self._sala

    def set_sala(self, sala):
        self._sala = sala

    def get_horaInicio(self):
        return self._horaInicio
    
    def set_horaInicio(self, horaInicio):
        self._horaInicio = horaInicio