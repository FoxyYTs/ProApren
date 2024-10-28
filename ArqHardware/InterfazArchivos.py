import pickle
import struct

with open('archivo_binario.bin', 'rb') as f:
    

    datos_leidos = f.read()
    entero_leido = struct.unpack('>I', datos_leidos)[0]
    cadena_binaria_recuperada = bin(entero_leido)[2:].zfill()  # Ajustar la longitud si es necesario
    print(cadena_binaria_recuperada)

    