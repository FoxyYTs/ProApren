import json
import pickle
import struct

def stringToByte(text):
    while len(text) % 8 != 0:
        text += "0"

    bytes = bytearray()
    for i in range(0, len(text), 8):
        byte = text[i:i+8]
        bytes.append(int(byte,2))

    print(bytes)
    return bytes

def byteToString(bytes):
    text = ""
    bits = bin(0)
    for byte in bytes:
        bits = bin(byte)[2:]
        bits = bits.zfill(8)
        text += bits

    print(text)


def guardar_datos_huffman(diccionario, cadena_bits, nombre_archivo):
    """Guarda los datos de Huffman en un archivo binario.

    Args:
        diccionario: Diccionario con el código Huffman.
        longitud_cadena: Longitud de la cadena de bits codificada.
        cadena_bits: Cadena de bits codificada.
        nombre_archivo: Nombre del archivo a crear.
    """

    papa = pickle.dumps(diccionario)
    # Serializar el diccionario
    cadena_bits = stringToByte(cadena_bits)

    a = pickle.loads(papa)

    print(a)    

    # Escribir los datos en el archivo
    with open(nombre_archivo, 'wb') as f:
        f.write(cadena_bits + b'\r\n')
        f.write(papa)

# Ejemplo de uso:
diccionario = {"e": "00", "l": "01", " ": "100", "a": "1010", "h": "1011", "s": "11"}

a = json.dumps(diccionario)

test = a.encode("")

print(test)

cadena_bits = "1110110010011000101111001100101010011101100010111"

guardar_datos_huffman(diccionario, cadena_bits, "datos_huffmasn.bin")
