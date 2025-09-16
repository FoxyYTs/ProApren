import redis

def conectar():
    try:
        r = redis.StrictRedis(
            host='10.144.253.101',
            port=6379,
            db=0
        )
        r.ping()  # Verifica la conexión
        print("Conexión exitosa a la base de datos Redis.")
        return r
    except redis.exceptions.ConnectionError as e:
        print(f"Error al conectar a la base de datos Redis: {e}")
        return None