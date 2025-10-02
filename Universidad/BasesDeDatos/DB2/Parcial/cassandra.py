from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import util
import uuid

CASSANDRA_HOSTS = ['127.0.0.1']
KEYSPACE = "parcial_tienda_ks"

CLIENTE_UUID_ANA = uuid.UUID('490a6e0e-4340-4f9e-8798-888888888803')
PRODUCTO_UUID_LAPTOP = uuid.UUID('a3b4c1d5-6789-4b3e-a1b2-111111111101')

try:
    cluster = Cluster(CASSANDRA_HOSTS)
    session = cluster.connect(KEYSPACE)
    print("Conexión a Cassandra exitosa.")

    def get_pedidos_by_cliente_uuid(cliente_uuid):
        print(f"\n--- Consultando Pedidos para el Cliente UUID: {cliente_uuid} ---")

        query = "SELECT pedido_id, fecha_hora, estado, precio_total FROM pedidos_por_cliente WHERE cliente_id = %s"
        
        try:
            rows = session.execute(query, [cliente_uuid])
            if rows:
                print(f"Pedidos encontrados para el cliente {cliente_uuid}:")
                for row in rows:
                    fecha_str = row.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
                    print(f"  Pedido ID: {row.pedido_id}, Fecha: {fecha_str}, Estado: {row.estado}, Total: ${row.precio_total}")
            else:
                print("No se encontraron pedidos.")
        except Exception as e:
            print(f"Error al consultar pedidos en Cassandra: {e}")

    def get_producto_by_uuid(producto_uuid):
        print(f"\n--- Consultando Producto por UUID: {producto_uuid} ---")
        
        query = "SELECT nombre, descripcion, precio, cantidad_inventario FROM productos_por_id WHERE producto_id = %s"
        
        try:
            row = session.execute(query, [producto_uuid]).one()
            if row:
                print(f"Producto Encontrado:")
                print(f"  Nombre: {row.nombre}")
                print(f"  Descripción: {row.descripcion}")
                print(f"  Precio: ${row.precio}")
                print(f"  Stock: {row.cantidad_inventario}")
            else:
                print("Producto no encontrado.")
        except Exception as e:
            print(f"Error al consultar producto en Cassandra: {e}")

    def get_clientes_by_ciudad(ciudad):
        print(f"\n--- Consultando Clientes en la ciudad: {ciudad} ---")
        
        query = "SELECT cliente_id, nombre, apellido, correo FROM clientes WHERE direccion_ciudad = %s"
        
        try:
            rows = session.execute(query, [ciudad])
            clientes_encontrados = list(rows)
            if clientes_encontrados:
                print(f"Clientes encontrados en {ciudad}:")
                for row in clientes_encontrados:
                    print(f"  Cliente ID: {row.cliente_id}, Nombre: {row.nombre} {row.apellido}, Correo: {row.correo}")
            else:
                print(f"No se encontraron clientes en {ciudad}.")
        except Exception as e:
            print(f"Error al consultar clientes por ciudad (¿Falta el Índice?): {e}")
            print("Intenta crear el índice en CQLSH: CREATE INDEX IF NOT EXISTS on clientes (direccion_ciudad);")

    get_pedidos_by_cliente_uuid(CLIENTE_UUID_ANA) 
    get_producto_by_uuid(PRODUCTO_UUID_LAPTOP)
    get_clientes_by_ciudad("Lima") 

except Exception as e:
    print(f"Error de conexión o ejecución en Cassandra: {e}")
finally:
    if 'cluster' in locals() and cluster:
        cluster.shutdown()