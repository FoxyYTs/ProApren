class Pelicula:

    def __init__(self, titulo, director, duracion, genero, clasificacion, añoProduccion):
        self._titulo = titulo
        self._director = director
        self._duracion = duracion
        self._genero = genero
        self._clasificacion = clasificacion
        self._añoProduccion = añoProduccion

    def __str__(self):
        return f"Película {self._titulo} | Director: {self._director} | Duración: {self._duracion} | Género: {self._genero} | Clasificación: {self._clasificacion} | Año de Producción: {self._añoProduccion}"

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_director(self):
        return self._director

    def set_director(self, director):
        self._director = director

    def get_duracion(self):
        return self._duracion

    def set_duracion(self, duracion):
        self._duracion = duracion

    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero

    def get_clasificacion(self):
        return self._clasificacion

    def set_clasificacion(self, clasificacion):
        self._clasificacion = clasificacion

    def get_añoProduccion(self):
        return self._añoProduccion

    def set_añoProduccion(self, añoProduccion):
        self._añoProduccion = añoProduccion
