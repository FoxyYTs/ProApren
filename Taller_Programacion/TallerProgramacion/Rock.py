from Musica import Musica
import openpyxl
import pandas as pd
datos=["id_musica", "titulo", "artista_banda", "duracion", "ano_lanzamiento", "formato", "genero","subgenero","conciertos_dados","pais_origen","letra","musica"]
datosExcel=["id", "titulo", "artista_banda", "duracion", "ano_lanzamiento", "formato", "genero","subgenero","conciertos_dados","pais_origen","letra","musica"]

class Rock(Musica):
    def __init__(self, id=""):
        self.Hijo = pd.read_excel("TallerProgramacion/Archivo.xlsx","ClaseHijo",index_col="musica")
        self.Padre = pd.read_excel("TallerProgramacion/Archivo.xlsx","ClasePadre",index_col="id")
        """Rock
            id (int): Identificacion de la musica
            titulo (String): Titulo de la cancion
            artista_banda (String): Nombre del artista o banda
            duracion (String): cuanto dura la cancion
            ano_lanzamiento (int): En que año salio la cancion
            formato (String): En que formato esta la cancion
            genero (String): Genero de la cancion
            subgenero (String): SubGenero de la cancion
            conciertos_dados (int): En cuantos conciertos a sonado esta cancion
            pais_origen (int): De que pais es la Banda
            letra (String): Letra de la cancion
            musica (String): id

        Args:
            id (String) =  Identificacion de la musica
        """
        super().__init__(id, self.Padre.loc[id, "titulo"], self.Padre.loc[id, "artista_banda"], self.Padre.loc[id, "duracion"], int(self.Padre.loc[id, "ano_lanzamiento"]),self.Padre.loc[id, "formato"],(self.Padre.loc[id, "genero"]))
        self.musica = id
        self.subgenero = self.Hijo.loc[id, "subgenero"]
        self.conciertos_dados = int(self.Hijo.loc[id, "conciertos_dados"])
        self.pais_origen = self.Hijo.loc[id, "pais_origen"]
        self.letra = self.Hijo.loc[id, "letra"]
        self.musica = self.Hijo.loc[id, "musica"]

    def IniciarTabla(self):
        """
            Crea la Tabla
        """
        self.create_table_musica("Musica", "ColumnasMusica")
        self.create_table_rock("Rock","ColumnasRock")

    def agregarDatos(self):
        """
            Inserta los datos a la base de datos ya creada
        """
        datosM = [
            (self.id_musica,self.titulo, self.artista_banda, self.duracion, self.ano_lanzamiento, self.formato, self.genero)
        ]
        self.registrar_musica("Musica","?,?,?,?,?,?,?",datosM)
        datosR = [
            (self.id_musica,self.subgenero,self.conciertos_dados,self.pais_origen,self.letra,self.musica)
        ]
        self.registrar_rock("Rock","?,?,?,?,?,?",datosR)
        print("Datos Agregados.")
    
    def EliminarDatos(self):
        """
            Elimina los datos dependiendo de su clave foranea
        """
        self.eliminar("Musica", self.id_musica)
        self.eliminar("Rock", self.id_musica)
        print("Datos eliminados.")
    
    def LeerDatos(self):
        """
            Muestra los registros de la base de datos
        """
        print("============================")
        datosM = self.mostrar_base_datos("Musica", self.id_musica)
        print(f"1. ID: {datosM[0]}\n2. Titulo: {datosM[1]}\n3. Artista: {datosM[2]}\n4. Duracion: {datosM[3]}\n5. Año Lanzamiento: {datosM[4]}\n6. Formato: {datosM[5]}\n7. Genero: {datosM[6]}")
        datosR = self.mostrar_base_datos("Rock", self.placa)
        print(f"8. Subgenero: {datosR[1]}\n9. la tocaron en conciertos: {datosR[2]}\n10. Pais de Origen: {datosR[3]}\n11. Letra: {datosR[4]}\n12. Musica: {datosR[5]}")
        print("============================")
                
    def ActualizarDatos(self, datoAct,datoCambio):
        """
            Actualiza los datos usando el numero de dato a cambiar y el dato dependiendo de su tipo.
        """
        if datoAct-1 == 1:
            self.actualizar("Musica", datos[datoAct-1], datoCambio, self.id_musica)
            self.actualizar("Rock", datos[datoAct-1], datoCambio, self.id_musica)
        elif datoAct-1 == 2 or datoAct-1 == 4 or datoAct-1 == 5 or datoAct-1 == 6:
            self.actualizar("Musica", datos[datoAct-1], datoCambio, self.id_musica)
        elif datoAct-1 == 3:
            self.actualizar("Musica", datos[datoAct-1], int(datoCambio), self.id_musica)
        elif datoAct-1 == 7:
            self.actualizar("Musica", datos[datoAct-1], float(datoCambio), self.id_musica)
        elif datoAct-1 == 8 or datoAct-1 == 10:
            self.actualizar("Rock", datos[datoAct-1], int(datoCambio), self.id_musica)
        elif datoAct-1 == 9:
            self.actualizar("Rock", datos[datoAct-1], bool(datoCambio), self.id_musica)
        elif datoAct-1 == 11 or datoAct-1 == 12:
            self.actualizar("Rock", datos[datoAct-1], datoCambio, self.id_musica)
        print("Datos actualizados.")

    def getId(self):
        """Retorna la id de la Cancion"""
        return self.id_musica
    
    def getTitulo(self):
        """Retorna el titulo de la cancion"""
        return self.titulo
    def getArtistaBanda(self):
        """Retorna el artista o la banda"""
        return self.artista_banda
    def getDuracion(self):
        """Retorna la duracion de la cancion"""
        return self.duracion
    def getAnoLanzamiento(self):
        """Retorna el ano de lanzamiento de la cancion"""
        return self.ano_lanzamiento
    def getFormato(self):
        """Retorna el formato de la cancion"""
        return self.formato
    def getGenero(self):
        """Retorna el genero de la cancion"""
        return self.genero

    # SETTERS
    def setId(self, id_musica):
        """Asigna La ID de la cancion"""
        self.id_musica = id_musica

    def setTitulo(self, titulo):
        """Asigna el Titulo de la Cancion"""
        self.titulo = titulo
    
    def setArtistaBanda(self, artista_banda):
        """Asigna el artista o banda"""
        self.artista_banda = artista_banda

    def setDuracion(self, duracion):
        """Asigna la duracion de la cancion"""
        self.duracion = duracion
    
    def setAnoLanzamiento(self, ano_lanzamiento):
        """Asigna el ano de lanzamiento de la cancion"""
        self.ano_lanzamiento = ano_lanzamiento

    def setFormato(self, formato):
        """Asigna el formato de la cancion"""
        self.formato = formato

    def setGenero(self, genero):
        """Asigna el genero de la cancion"""
        self.genero = genero