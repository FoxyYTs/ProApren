import pickle
import struct

with open('archivo_binario.bin', 'rb') as f:
    

    datos = f.read()
    datos_leidos = pickle.loads(datos)
    print(datos_leidos)

    