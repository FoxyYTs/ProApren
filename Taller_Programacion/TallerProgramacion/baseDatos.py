import sqlite3

conn=sqlite3.connect('TallerProgramacion/musicadb.db')

c=conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS musica (
        id INT PRIMARY KEY,
        titulo VARCHAR(45)NOT NULL,
        artista_banda VARCHAR(45) NOT NULL,
        duracion VARCHAR (45) NOT NULL,
        ano_lanzamiento INT NOT NULL,
        formato VARCHAR(5) NOT NULL,
        genero VARCHAR(45) NOT NULL
)""")
c.execute("""CREATE TABLE IF NOT EXISTS rock(
          id INT PRIMARY KEY,
          subgenero VARCHAR(45) NOT NULL,
          conciertos_dados INT NOT NULL,
          pais_origen VARCHAR(45) NOT NULL,
          letra TEXT NOT NULL,
          album VARCHAR(45),
          musica INT NOT NULL,
          FOREIGN KEY (musica) REFERENCES musica (id_musica)
)""")

conn.close()