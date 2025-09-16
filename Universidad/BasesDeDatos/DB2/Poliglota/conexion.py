import mysql.connector
import pymongo

def conectarSQL():  # Nombre más descriptivo
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="tienda"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None  # Importante retornar None en caso de error

def conectarMongo():
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    