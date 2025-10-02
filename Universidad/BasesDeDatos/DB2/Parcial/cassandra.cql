-- ========================================================
-- 1. CREACIÓN DEL KEYSPACE
-- ========================================================

-- Creamos el KeySpace con replicación SimpleStrategy (para un nodo de desarrollo)
CREATE KEYSPACE IF NOT EXISTS parcial_tienda_ks
WITH replication = {
    'class': 'SimpleStrategy', 
    'replication_factor': '1'
};

USE parcial_tienda_ks;

-- ========================================================
-- 2. DEFINICIÓN DE UUIDs DE EJEMPLO
-- Usamos las funciones de Cassandra para generar UUIDs.
-- Estos UUIDs se usarán para los IDs de entidad y las referencias.
-- ========================================================

-- IDs de Cliente (UUIDs generados para replicar IDs 1, 2, 3)
SET client_uuid_1 = 490a6e0e-4340-4f9e-8798-888888888801; 
SET client_uuid_2 = 490a6e0e-4340-4f9e-8798-888888888802;
SET client_uuid_3 = 490a6e0e-4340-4f9e-8798-888888888803;

-- IDs de Producto (UUIDs generados para replicar IDs 1, 2, 3)
SET prod_uuid_1 = a3b4c1d5-6789-4b3e-a1b2-111111111101; -- Laptop Pro
SET prod_uuid_2 = a3b4c1d5-6789-4b3e-a1b2-111111111102; -- Mouse Inalámbrico
SET prod_uuid_3 = a3b4c1d5-6789-4b3e-a1b2-111111111103; -- Monitor LED 27"

-- IDs de Pedido (UUIDs generados para replicar IDs 1, 2, 3)
SET order_uuid_1 = 7c8d9e0f-1234-4a5b-c6d7-222222222201; 
SET order_uuid_2 = 7c8d9e0f-1234-4a5b-c6d7-222222222202;
SET order_uuid_3 = 7c8d9e0f-1234-4a5b-c6d7-222222222203;

-- ========================================================
-- 3. CREACIÓN DE TIPOS DE DATOS PERSONALIZADOS (UDTs)
-- Para incrustar los detalles del producto de manera estructurada.
-- ========================================================

-- Tipo para los detalles de un producto en un pedido
CREATE TYPE IF NOT EXISTS detalle_producto (
    fk_producto_id uuid,
    nombre_producto text,
    cantidad int,
    precio_unitario decimal
);

-- ========================================================
-- 4. CREACIÓN DE TABLAS
-- ========================================================

-- Tabla 1: clientes
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id uuid,
    nombre text,
    apellido text,
    correo text,
    direccion_calle text,
    direccion_ciudad text,
    direccion_pais text,
    PRIMARY KEY (cliente_id)
);

-- Tabla 2: productos_por_id
CREATE TABLE IF NOT EXISTS productos_por_id (
    producto_id uuid,
    nombre text,
    descripcion text,
    precio decimal,
    cantidad_inventario int,
    PRIMARY KEY (producto_id)
);

-- Tabla 3: pedidos_por_cliente
-- PARTITION KEY: cliente_id (permite agrupar todos los pedidos por cliente)
-- CLUSTERING KEYS: fecha_hora (para ordenar cronológicamente) y pedido_id (para unicidad)
CREATE TABLE IF NOT EXISTS pedidos_por_cliente (
    cliente_id uuid,
    pedido_id uuid,
    fecha_hora timestamp,
    estado text,
    precio_total decimal,
    -- Datos del cliente incrustados (desnormalización)
    cliente_nombre text,
    cliente_apellido text,
    -- Detalles del pedido incrustados
    detalles list<frozen<detalle_producto>>,
    PRIMARY KEY (cliente_id, fecha_hora, pedido_id)
) WITH CLUSTERING ORDER BY (fecha_hora DESC);


-- ========================================================
-- 5. INSERCIÓN DE DATOS DE EJEMPLO
-- ========================================================

-- 5.1. Inserción en 'clientes' (3 Registros)
INSERT INTO clientes (cliente_id, nombre, apellido, correo, direccion_calle, direccion_ciudad, direccion_pais) VALUES (490a6e0e-4340-4f9e-8798-888888888801, 'Laura', 'Gómez', 'laura.gomez@mail.com', 'Avenida Principal 123', 'Bogotá', 'Colombia');
INSERT INTO clientes (cliente_id, nombre, apellido, correo, direccion_calle, direccion_ciudad, direccion_pais) VALUES (490a6e0e-4340-4f9e-8798-888888888802, 'Carlos', 'Rodríguez', 'carlos.rodriguez@mail.com', 'Calle Falsa 45', 'Madrid', 'España');
INSERT INTO clientes (cliente_id, nombre, apellido, correo, direccion_calle, direccion_ciudad, direccion_pais) VALUES (490a6e0e-4340-4f9e-8798-888888888803, 'Ana', 'Díaz', 'ana.diaz@mail.com', 'Carrera 10 #20-30', 'Lima', 'Perú');

-- 5.2. Inserción en 'productos_por_id' (3 Registros)
INSERT INTO productos_por_id (producto_id, nombre, descripcion, precio, cantidad_inventario) VALUES (a3b4c1d5-6789-4b3e-a1b2-111111111101, 'Laptop Pro', 'Portátil de alto rendimiento con 16GB RAM', 1200.00, 15);
INSERT INTO productos_por_id (producto_id, nombre, descripcion, precio, cantidad_inventario) VALUES (a3b4c1d5-6789-4b3e-a1b2-111111111102, 'Mouse Inalámbrico', 'Mouse ergonómico con conexión Bluetooth', 25.50, 50);
INSERT INTO productos_por_id (producto_id, nombre, descripcion, precio, cantidad_inventario) VALUES (a3b4c1d5-6789-4b3e-a1b2-111111111103, 'Monitor LED 27"', 'Pantalla Full HD con baja emisión de luz azul', 180.99, 30);

-- 5.3. Inserción en 'pedidos_por_cliente' (3 Registros)
-- Los detalles del pedido se incrustan usando el tipo 'detalle_producto' (list<frozen<detalle_producto>>)

-- Pedido 1: Cliente Laura Gómez
INSERT INTO pedidos_por_cliente (cliente_id, pedido_id, fecha_hora, estado, precio_total, cliente_nombre, cliente_apellido, detalles) VALUES (
    490a6e0e-4340-4f9e-8798-888888888801,
    7c8d9e0f-1234-4a5b-c6d7-222222222201,
    '2025-10-01 10:30:00-0500', -- Hora y fecha del pedido
    'Completado',
    1225.50,
    'Laura', 'Gómez',
    [ 
        {fk_producto_id: a3b4c1d5-6789-4b3e-a1b2-111111111101, nombre_producto: 'Laptop Pro', cantidad: 1, precio_unitario: 1200.00},
        {fk_producto_id: a3b4c1d5-6789-4b3e-a1b2-111111111102, nombre_producto: 'Mouse Inalámbrico', cantidad: 1, precio_unitario: 25.50}
    ]
);

-- Pedido 2: Cliente Carlos Rodríguez
INSERT INTO pedidos_por_cliente (cliente_id, pedido_id, fecha_hora, estado, precio_total, cliente_nombre, cliente_apellido, detalles) VALUES (
    490a6e0e-4340-4f9e-8798-888888888802,
    7c8d9e0f-1234-4a5b-c6d7-222222222202,
    '2025-10-01 15:45:00-0500',
    'En Proceso',
    361.98,
    'Carlos', 'Rodríguez',
    [
        {fk_producto_id: a3b4c1d5-6789-4b3e-a1b2-111111111103, nombre_producto: 'Monitor LED 27"', cantidad: 2, precio_unitario: 180.99}
    ]
);

-- Pedido 3: Cliente Ana Díaz
INSERT INTO pedidos_por_cliente (cliente_id, pedido_id, fecha_hora, estado, precio_total, cliente_nombre, cliente_apellido, detalles) VALUES (
    490a6e0e-4340-4f9e-8798-888888888803,
    7c8d9e0f-1234-4a5b-c6d7-222222222203,
    '2025-10-02 08:00:00-0500',
    'Pendiente',
    25.50,
    'Ana', 'Díaz',
    [
        {fk_producto_id: a3b4c1d5-6789-4b3e-a1b2-111111111102, nombre_producto: 'Mouse Inalámbrico', cantidad: 1, precio_unitario: 25.50}
    ]
);