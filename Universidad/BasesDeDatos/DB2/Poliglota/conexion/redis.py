import redis

def conectar():
    """
    Establece una conexión a Redis con autenticación.
    """
    try:
        r = redis.StrictRedis(
            host='10.144.253.101',
            port=6379,
            db=0,
            password='Statue3@Untaxed@Cost' # <-- Agrega esta línea con tu contraseña
        )
        r.ping()  # Verifica la conexión
        print("Conexión exitosa a la base de datos Redis.")
        return r
    except redis.exceptions.AuthenticationError as e:
        print(f"Error de autenticación: la contraseña es incorrecta. {e}")
        return None
    except redis.exceptions.ConnectionError as e:
        print(f"Error al conectar a la base de datos Redis: {e}")
        return None