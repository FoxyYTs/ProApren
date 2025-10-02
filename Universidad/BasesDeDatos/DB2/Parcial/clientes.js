db.clientes.insertMany([
  {
    _id: 1,
    nombre: "Laura",
    apellido: "Gómez",
    correo: "laura.gomez@mail.com",
    direccion: {
      calle: "Avenida Principal 123",
      ciudad: "Bogotá",
      pais: "Colombia"
    }
  },
  {
    _id: 2,
    nombre: "Carlos",
    apellido: "Rodríguez",
    correo: "carlos.rodriguez@mail.com",
    direccion: {
      calle: "Calle Falsa 45",
      ciudad: "Madrid",
      pais: "España"
    }
  },
  {
    _id: 3,
    nombre: "Ana",
    apellido: "Díaz",
    correo: "ana.diaz@mail.com",
    direccion: {
      calle: "Carrera 10 #20-30",
      ciudad: "Lima",
      pais: "Perú"
    }
  }
]);