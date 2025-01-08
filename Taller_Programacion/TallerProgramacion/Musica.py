from CRUD import Crud

class Musica(Crud):
    def __init__(self, id_musica, titulo, artista_banda, duracion, ano_lanzamiento, formato, genero):
        super().__init__()
        self.id_musica = id_musica
        self.titulo = titulo
        self.artista_banda = artista_banda
        self.duracion = duracion
        self.ano_lanzamiento = ano_lanzamiento
        self.formato = formato
        self.genero = genero
    
    def getId(self):
        """Retorna el ID de la musica."""
        return self.id_musica
    
    def getTitulo(self):
        """Retorna el titulo de la musica."""
        return self.titulo
    def getArtistaBanda(self):
        """Retorna el artista de la banda de la musica."""
        return self.artista_banda
    
    def getduracion(self):
        """Retorna la duracion de la musica."""
        return self.duracion
    
    def getAnoLanzamiento(self):
        """Retorna el ano de lanzamiento de la musica."""
        return self.ano_lanzamiento
    
    def getFormato(self):
        """Retorna el formato de la musica."""
        return self.formato
    
    def getGenero(self):
        """Retorna el genero de la musica."""
        return self.genero
    

    
    def setId(self, id_musica):
        """Setea el ID de la musica."""
        self.id_musica = id_musica
    
    def setTitulo(self, titulo):
        """Setea el titulo de la musica."""
        self.titulo = titulo
    
    def setArtistaBanda(self, artista_banda):
        """Setea el artista de la banda de la musica."""
        self.artista_banda = artista_banda
    
    def setDuracion(self, duracion):
        """Setea la duracion de la musica."""
        self.duracion = duracion
    
    def setAnoLanzamiento(self, ano_lanzamiento):
        """Setea el ano de lanzamiento de la musica."""
        self.ano_lanzamiento = ano_lanzamiento
    
    def setFormato(self, formato):
        """Setea el formato de la musica."""
        self.formato = formato
    
    def setGenero(self, genero):
        """Setea el genero de la musica."""
        self.genero = genero