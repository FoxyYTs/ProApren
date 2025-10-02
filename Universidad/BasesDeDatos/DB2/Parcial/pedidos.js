db.pedidos.insertMany([
  {
    _id: 1,
    fk_cliente_id: 1, // Referencia a Laura Gómez
    fecha_hora: ISODate("2025-10-01T15:30:00Z"), // Se usa formato ISODate para MongoDB
    estado: "Completado",
    precio_total: NumberDecimal("1225.50"),
    productos_comprados: [
      {
        fk_producto_id: 1,
        nombre: "Laptop Pro",
        cantidad: 1,
        precio_unitario: NumberDecimal("1200.00")
      },
      {
        fk_producto_id: 2,
        nombre: "Mouse Inalámbrico",
        cantidad: 1,
        precio_unitario: NumberDecimal("25.50")
      }
    ]
  },
  {
    _id: 2,
    fk_cliente_id: 2, // Referencia a Carlos Rodríguez
    fecha_hora: ISODate("2025-10-01T20:45:00Z"),
    estado: "En Proceso",
    precio_total: NumberDecimal("361.98"),
    productos_comprados: [
      {
        fk_producto_id: 3,
        nombre: "Monitor LED 27\"",
        cantidad: 2,
        precio_unitario: NumberDecimal("180.99")
      }
    ]
  },
  {
    _id: 3,
    fk_cliente_id: 3, // Referencia a Ana Díaz
    fecha_hora: ISODate("2025-10-02T13:00:00Z"),
    estado: "Pendiente",
    precio_total: NumberDecimal("25.50"),
    productos_comprados: [
      {
        fk_producto_id: 2,
        nombre: "Mouse Inalámbrico",
        cantidad: 1,
        precio_unitario: NumberDecimal("25.50")
      }
    ]
  }
]);