import json
import redis

r = redis.Redis(host="localhost", port=6379, db = 0, decode_responses = True)

def crear_usuario():
    user_id = input("ID del usuario:")
    nombre = input("Nombre Usuario:")
    email = input("Correo Usuario:")
    usuario = {"nombre":nombre, "email":email}
    r.set(user_id,json.dump(usuario))
    print("Usuario ha sido creado")
    
def leer_usuario():
    user_id = input("ID usuario a leer:")
    data = r.get(user_id)
    if data:
        usuario = json.load(data)
        print("Usuario encontrado")
    else:
        print("Usuario no encontrado")