from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["dbempleado"]
coleccion1 = db["persona"]
coleccion2 = db["estudiante"]

for i in range(1):
    persona = {
        "nombre": f"Persona {i}",
        "edad": i + 20,
        "ciudad": "Ciudad" + str(i),
        "lenguajes": ["Python", "Java", "C++"]
    }
    estudiante = {
        "nombre": f"Estudiante {i}",
        "edad": i + 18,
        "carrera": "Carrera" + str(i),
        "lenguajes": ["JavaScript", "Ruby"]
    }
    coleccion1.insert_one(persona)
    coleccion2.insert_one(estudiante)
    
for doc in coleccion1.find():
    print(doc)
    
for doc in coleccion2.find():
    print(doc)