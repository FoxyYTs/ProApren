import json

from conexion.mysql import conectar as conectarsql
from conexion.postgresql import conectar as conectarpostgresql
from conexion.mongodb import conectar as conectarmongodb
from conexion.redis import conectar as conectarredis

def consulta(parametro):
    sql = "SELECT * From " + parametro
    mycursor.execute(sql)
    resultados = mycursor.fetchall()
    
    if resultados:
        return resultados

def consulta_g():
    sql = "SELECT o.id AS 'ID de Orden', u.nombre AS 'Nombre de Usuario', p.nombre AS 'Nombre de Producto', o.cantidad AS 'Cantidad', (p.precio * o.cantidad) AS 'Total por Producto' FROM ordenes o JOIN usuario u ON o.usuario_id = u.id JOIN productos p ON o.producto_id = p.id ORDER BY o.id;"
    mycursor.execute(sql)
    resultados = mycursor.fetchall()
    
    if resultados:
        return resultados
            

conexionmysql = conectarsql()
if conexionmysql:
    mycursor = conexionmysql.cursor()
    print(consulta("usuario"))
    print(consulta("productos"))
    print(consulta_g())
    
