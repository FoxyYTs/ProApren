import sqlite3
import json


conn = sqlite3.connect("Parcial1\cine.db")

# Crea las tablas
c = conn.cursor()
c.execute("""CREATE TABLE Cine (
  id INTEGER PRIMARY KEY,
  nombre VARCHAR(255),
  direccion VARCHAR(255),
  capacidadTotal INT,
  numeroSalas INT,
  telefono VARCHAR(255),
  correoElectronico VARCHAR(255)
);""")
c.execute("""CREATE TABLE Pelicula (
  id INTEGER PRIMARY KEY,
  titulo VARCHAR(255),
  director VARCHAR(255),
  duracion INT,
  genero VARCHAR(255),
  clasificacion VARCHAR(255),
  añoProduccion INT
);""")
c.execute("""CREATE TABLE Espectador (
  id INTEGER PRIMARY KEY,
  nombre VARCHAR(255),
  apellido VARCHAR(255),
  dni VARCHAR(255),
  fechaNacimiento DATE,
  telefono VARCHAR(255),
  correoElectronico VARCHAR(255)
);""")
c.execute("""CREATE TABLE Proyeccion (
  id INTEGER PRIMARY KEY,
  sala INT,
  horaInicio TIME,
  cine VARCHAR(255),
  pelicula VARCHAR(255),
  espectador VARCHAR(255),
  precio FLOAT
);""")
conn.close()

conn = sqlite3.connect("Parcial1\cine.db")
c = conn.cursor()
c.execute("""INSERT INTO Cine (nombre, direccion, capacidadTotal, numeroSalas, telefono, correoElectronico)
  VALUES ('PoliCine', 'Calle 123', 100, 5, '555-555-5555', 'PoliCine@example.com');""")
c.execute("""INSERT INTO Cine (nombre, direccion, capacidadTotal, numeroSalas, telefono, correoElectronico)
  VALUES ('UcoPoli', 'Calle 456', 200, 10, '666-666-6666', 'UcoPoli@example.com');""")
conn.commit()
conn.close()

conn = sqlite3.connect("Parcial1\cine.db")
c = conn.cursor()
c.execute("SELECT * FROM Cine;")
for row in c:
  print(row)
conn.close()
