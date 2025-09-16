import mysql.connector

import redis
import json

from conexion import conectar

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
            

conexion = conectar()
if conexion:
    mycursor = conexion.cursor()
    print(consulta("usuario"))
    print(consulta("productos"))
    print(consulta_g())
    
