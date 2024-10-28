import json
import pickle
import struct

diccionario = {"e": "00", "l": "01", " ": "100", "a": "1010", "h": "1011", "s": "11"}
cadena_bits = "01010110101100011111100111000110"

diccionario_str = pickle.dumps(diccionario)
entero = int(cadena_bits, 2)
datos_empaquetados = struct.pack('>I', entero)



# Escribir los datos en un archivo binario
with open('archivo_binario.bin', 'wb') as f:
    f.write(datos_empaquetados)
    