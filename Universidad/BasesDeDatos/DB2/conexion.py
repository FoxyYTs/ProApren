from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ejemplo"]
coleccion = db["persona"]

coleccion.drop()  # Limpiar la colección antes de insertar nuevos documentos

for i in range(1):
    documento = {
        "nombre": f"Persona {i}",
        "edad": i + 20,
        "ciudad": "Ciudad" + str(i),
        "lenguajes": ["Python", "Java", "C++"]
    }
    coleccion.insert_one(documento)
    
for doc in coleccion.find():
    print(doc)
    
coleccion.update_one({"nombre": "Persona 0"}, {"$set": {"edad": 30}})

for doc in coleccion.find():
    print(doc)