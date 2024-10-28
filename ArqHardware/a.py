import json
import pickle
import struct

huffman_code = {"e": "00", "l": "01", " ": "100", "a": "1010", "h": "1011", "s": "11"}
cadena_bits = "01010110101100011111100111000110"


entero = hex(int(cadena_bits, 2))

diccionario = json.dumps(huffman_code)

guardado = [str(diccionario), str(len(cadena_bits)), str(entero)]

test = "\n".join(guardado)

datos = pickle.dumps(guardado)

print(datos)


# Escribir los datos en un archivo binario
with open('archivo_binario.bin', 'wb') as f:

    f.write(datos)
    