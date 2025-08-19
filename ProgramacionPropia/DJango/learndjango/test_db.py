import psycopg2

try:
    # 🔗 Estableciendo la conexión a la base de datos PostgreSQL
    conexion = psycopg2.connect(
        host='10.144.253.101',
        database='lean_django',
        user='postgres',
        password='1987',
        port='5432'
    )
    
    # 📌 Verificando si la conexión fue exitosa
    print("✅ Conexión exitosa a la base de datos PostgreSQL")
    
    # 📝 Creando un cursor para ejecutar consultas
    cursor = conexion.cursor()
    
    #  Ejemplo de consulta: listar las tablas de la base de datos
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tablas = cursor.fetchall()
    
    print("\nEstas son las tablas en la base de datos:")
    for tabla in tablas:
        print(f"- {tabla[0]}")
        
except psycopg2.OperationalError as e:
    # ❌ Manejo de errores en caso de que la conexión falle
    print(f"❌ Error al conectar a la base de datos PostgreSQL: {e}")
    
finally:
    # 🚪 Cerrando el cursor y la conexión para liberar recursos
    if 'conexion' in locals() and not conexion.closed:
        cursor.close()
        conexion.close()
        print("\n✅ Conexión a PostgreSQL cerrada.")