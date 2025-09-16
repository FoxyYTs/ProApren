from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def conectar_mongodb():
    try:
        client = MongoClient(
            'mongodb://10.144.253.101:27017/',
            serverSelectionTimeoutMS=5000  # 5 segundos de timeout
        )
        client.admin.command('ping') # Verifica la conexión
        print("Conexión exitosa a la base de datos MongoDB.")
        return client
    except ConnectionFailure as e:
        print(f"Error al conectar a la base de datos MongoDB: {e}")
        return None