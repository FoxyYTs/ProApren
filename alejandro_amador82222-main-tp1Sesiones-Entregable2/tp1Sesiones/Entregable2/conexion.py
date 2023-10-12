import sqlite3
import json

class DataBase:
    def __init__(self):
        """
            Se conecta con la base de datos .sqlite y lee lo que tenga en el query.json
        """
        self.database = sqlite3.connect("/Entregable2/database.sqlite")
        self.pointer = self.database.cursor()    

        with open("/Entregable2/Query.json","r") as consultas:
            self.queries = json.load(consultas)

    def CrearTabla(self, nombreTabla="",Columnas=""):
        """
            Crea la tabla en la base de datos
        """
        if nombreTabla!="" and Columnas!="":
            info = self.queries["CrearTabla"].format(nombreTabla,self.queries[Columnas])
            self.pointer.execute(info)
            self.database.commit()
            print(f"Base de datos, tabla {nombreTabla} se ha creado correctamente.")
    
    def InsertarDato(self,tabla="",interrogantes="",valores=""): #Crear
        """
            Inserta el dato en cada campo
        """
        if tabla!="" and valores!="":
            info = self.queries["InsertarDato"].format(tabla,interrogantes)
            self.pointer.executemany(info,valores)
            self.database.commit()

    def LeerDato(self, tabla = "", id=""):
        """
            Lee el dato dependiendo de su clave primaria
        """
        if tabla!= "" and id!="":
            info = self.queries["LeerDato"].format(tabla,id)
            self.pointer.execute(info)
            self.database.commit()
            return self.pointer.fetchone()

    def ActualizarDato(self, tabla = "", datoAct = "", datoCambio = "", id = ""):
        """
            Actualiza el dato dependiendo el numero, cambio de dato y clave primaria
        """
        if tabla!= "" and datoAct != "" and datoCambio!="":
            info = self.queries["ActualizarDato"].format(tabla,datoAct,datoCambio,id)
            self.pointer.execute(info)
            self.database.commit()
            
    def EliminarDato(self, tabla = "", id = ""):
        """
            Elimina el dato dependiendo su clave primaria
        """
        if tabla!= "" and id!="":
            info = self.queries["EliminarDato"].format(tabla,id)
            self.pointer.execute(info)
            self.database.commit()