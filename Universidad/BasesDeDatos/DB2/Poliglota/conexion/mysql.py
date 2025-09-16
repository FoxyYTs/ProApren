import mysql.connector

def conectar():  # Nombre más descriptivo
    try:
        mydb = mysql.connector.connect(
            host="10.144.253.101",
            user="poliglota",
            passwd="Statue3@Untaxed@Cost",
            database="poliglota"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error al conectar a MySQL: {err}")
        return None