db.productos.insertMany([
  {
    _id: 1,
    nombre: "Laptop Pro",
    descripcion: "Portátil de alto rendimiento con 16GB RAM",
    precio: NumberDecimal("1200.00"),
    cantidad: 15
  },
  {
    _id: 2,
    nombre: "Mouse Inalámbrico",
    descripcion: "Mouse ergonómico con conexión Bluetooth",
    precio: NumberDecimal("25.50"),
    cantidad: 50
  },
  {
    _id: 3,
    nombre: "Monitor LED 27\"",
    descripcion: "Pantalla Full HD con baja emisión de luz azul",
    precio: NumberDecimal("180.99"),
    cantidad: 30
  }
]);