from pymongo import MongoClient, DECIMAL128
from bson.objectid import ObjectId

MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "parcial_tienda"

try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    clientes_coll = db["clientes"]
    pedidos_coll = db["pedidos"]
    productos_coll = db["productos"]
    print("Conexión a MongoDB exitosa.")

    def get_pedidos_by_cliente_email(email_cliente):
        print(f"\n--- Consultando Pedidos para el correo: {email_cliente} ---")
        
        cliente = clientes_coll.find_one({"correo": email_cliente}, {"_id": 1, "nombre": 1, "apellido": 1})
        
        if not cliente:
            print(f"Error: No se encontró ningún cliente con el correo {email_cliente}")
            return []
            
        cliente_id = cliente["_id"]
        print(f"Cliente encontrado: {cliente['nombre']} {cliente['apellido']} (ID: {cliente_id})")
        
        pedidos = pedidos_coll.find({"fk_cliente_id": cliente_id})
        
        pedidos_list = list(pedidos)
        if pedidos_list:
            for pedido in pedidos_list:
                print(f"  Pedido ID: {pedido['_id']}, Fecha: {pedido['fecha_hora'].strftime('%Y-%m-%d %H:%M')}, Total: ${pedido['precio_total']}")
        else:
            print(f"  No se encontraron pedidos para este cliente.")
        return pedidos_list

    def get_productos_bajo_stock(stock_minimo=15):
        print(f"\n--- Consultando Productos con stock menor a {stock_minimo} ---")
        productos = productos_coll.find({"cantidad": {"$lt": stock_minimo}})
        
        productos_list = list(productos)
        if productos_list:
            for producto in productos_list:
                precio_str = str(producto.get('precio', 'N/A'))
                print(f"  ID: {producto['_id']}, Nombre: {producto['nombre']}, Stock Actual: {producto['cantidad']}, Precio: ${precio_str}")
        else:
            print("  Todos los productos tienen stock suficiente.")
        return productos_list

    def calcular_total_pedidos_pendientes():
        print("\n--- Calculando Valor Total de Pedidos 'Pendiente' ---")
        
        pipeline = [
            {"$match": {"estado": "Pendiente"}},
            {"$group": {
                "_id": None,
                "total_acumulado": {"$sum": "$precio_total"}
            }}
        ]
        
        resultado = pedidos_coll.aggregate(pipeline)
        
        try:
            total_doc = next(resultado)
            total = str(total_doc['total_acumulado'])
            print(f"El valor total de los pedidos 'Pendiente' es: ${total}")
            return total
        except StopIteration:
            print("No hay pedidos 'Pendiente' o el total es $0.00.")
            return "0.00"

    get_pedidos_by_cliente_email("laura.gomez@mail.com")
    get_productos_bajo_stock(stock_minimo=35)
    calcular_total_pedidos_pendientes()

except Exception as e:
    print(f"Error de conexión o ejecución en MongoDB: {e}")
finally:
    if 'client' in locals() and client:
        client.close()