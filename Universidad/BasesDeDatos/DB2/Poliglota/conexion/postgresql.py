import psycopg2

def conectar():
    try:
        # Conectarse a la base de datos
        conn = psycopg2.connect(
            dbname="poliglota",
            user="poliglota",
            password="Statue3@Untaxed@Cost",
            host="10.144.253.101",
            port="5432"
        )
        
        print("Conexión exitosa a la base de datos PostgreSQL.")
        return conn
        
    except Exception as e:
        print("Error al conectar a PostgreSQL:", e)
        return None