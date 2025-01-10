import sqlite3
import json

class Conexion:
    def __init__(self):
        """
        Inicializa el objeto estableciendo una conexión con una base de datos SQLite y cargando un archivo JSON que contiene consultas SQL.

        Parámetros:
            Ninguno

        Retorna:
            Nada
        """
        self.DB = sqlite3.connect("Universidad/Taller_Programacion/3er_Entregable/DB.sqlite")
        self.iterador = self.DB.cursor()
        with open("Universidad/Taller_Programacion/3er_Entregable/Queries.json", "r") as queries:
            self.Querys = json.load(queries)
    
    def buscar_id(self, id, tabla):
        """
        Recupera un registro específico de una tabla específica basado en el ID proporcionado.

        Parámetros:
            id (int): El ID del registro a recuperar.
            tabla (str): El nombre de la tabla desde la cual se recuperará el registro.

        Retorna:
            int: El ID del registro recuperado.
        """
        seleccionar = self.Querys["select"].format(tabla, "ID", id)
        self.iterador.execute(seleccionar)
        resultado = self.iterador.fetchone()[0]
        return resultado
    
    def read(self, tabla):
        """
        Lee todos los registros de la tabla especificada.

        Parámetros:
            tabla (str): El nombre de la tabla de la que se leerán los registros.

        Retorna:
            list: Una lista que contiene todos los registros de la tabla.
        """
        seleccionar = self.Querys["select_all"].format(tabla)
        self.iterador.execute(seleccionar)
        resultado = self.iterador.fetchall()
        return resultado
    
    def create(self, nombre = "", query = ""):
        """
        Crea un nuevo registro en la base de datos.

        Parámetros:
            nombre (str): El nombre del registro.
            query (str): La consulta a ejecutar.

        Retorna:
            None
        """
        if nombre != "" and query != "":
            info = self.Querys["create"].format(nombre, self.Querys[query])
            self.iterador.execute(info)
            self.DB.commit()
        else:
            print("DB :: No puede dejar un campo vacio.")

    def insert(self, tabla = "", columnas = 0, valores = ""):        
        """
        Inserta un nuevo registro en la tabla especificada.

        Parámetros:
            tabla (str): El nombre de la tabla en la que se insertará el registro.
            columnas (int): El número de columnas en la tabla.
            valores (str): Los valores que se insertarán en la tabla.

        Retorna:
            None
        """
        if tabla != "" and valores != "":
            info = self.Querys["insert"].format(tabla, ', '.join(['?'] * columnas))
            self.iterador.executemany(info, valores)
            self.DB.commit()
        else:
            print("DB :: No puede dejar un campo vacio.")
    
    def update(self, nuevo_dato, tabla = "", columna = "", id = 0):
        """
        Actualiza un registro en la base de datos.

        Args:
            nuevo_dato (any): Los nuevos datos a actualizar.
            tabla (str, optional): El nombre de la tabla. Por defecto es "".
            columna (str, optional): El nombre de la columna. Por defecto es "".
            id (int, optional): El ID del registro. Por defecto es 0.

        Returns:
            bool: True si la actualización es exitosa, False de lo contrario.
        """        
        if tabla != "" and id != 0:
            if self.buscar_id(id, tabla):
                info = self.Querys["update"].format(tabla, columna, nuevo_dato, "ID", id)
                self.iterador.execute(info)
                self.DB.commit()
                return True
            else:
                return False
        else:
            return False
        
    def delete(self, tabla = "", id = 0):
        """
        Elimina un registro de la tabla especificada en la base de datos.

        Parámetros:
            tabla (str): El nombre de la tabla desde la que se eliminará el registro. El valor predeterminado es una cadena vacía.
            id (int): El ID del registro que se va a eliminar. El valor predeterminado es 0.

        Retorna:
            bool: True si se eliminó el registro correctamente, False en caso contrario.
        """
        if tabla != "" and id != 0:
            if self.buscar_id(id, tabla):
                info = self.Querys["delete"].format(tabla, "ID", id)
                self.iterador.execute(info)
                self.DB.commit()
                return True
            else:
                return False
        else:
            return False
        
    def deleteAll(self, tabla, zooID = 0):
        """
        Elimina todos los registros de la tabla especificada.

        Args:
            tabla (str): El nombre de la tabla desde la cual se eliminarán los registros.
            zooID (int, opcional): El ID del registro a eliminar. Por defecto es 0.

        Returns:
            None
        """
        Info = self.Querys["delete_all"].format(tabla, "ZOO_ID", zooID)
        self.iterador.execute(Info)              
        self.DB.commit()
    
    def cerrar_db(self):
        """
        Confirma los cambios pendientes en la base de datos y cierra la conexión.

        Esta función se utiliza para cerrar la conexión con la base de datos después de realizar cambios en ella. Primero, confirma los cambios pendientes en la base de datos utilizando el método `commit()` del objeto `DB`. Luego, cierra la conexión con la base de datos utilizando el método `close()` del objeto `DB`.

        Parámetros:
            self (objeto): La instancia de la clase.

        Retorna:
            Ninguno
        """
        self.DB.commit()
        self.DB.close()