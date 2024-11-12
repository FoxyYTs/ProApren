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
    print(len(bytes))
    return bytes

def byteToString(bytes):
    text = ""
    bits = bin(0)
    for byte in bytes:
        bits = bin(byte)[2:]
        bits = bits.zfill(8)
        text += bits

    return text


def guardar_datos_huffman(diccionario, cadena_bits, nombre_archivo):
    """Guarda los datos de Huffman en un archivo binario.

    Args:
        diccionario: Diccionario con el código Huffman.
        longitud_cadena: Longitud de la cadena de bits codificada.
        cadena_bits: Cadena de bits codificada.
        nombre_archivo: Nombre del archivo a crear.
    """

    papa = json.dumps(diccionario).encode('utf-8')
    # Serializar el diccionario
    cadena_bits = stringToByte(cadena_bits)



    

    # Escribir los datos en el archivo
    with open(nombre_archivo, 'wb') as f:
        f.write(cadena_bits)

# Ejemplo de uso:
diccionario = {'e': '00', 'l': '01', ' ': '100', 'a': '1010', 'h': '1011', 's': '11'}

print(len(str(diccionario)+"\n"))

cadena_bits = "1110110010011000101111001100101010011101100010111"
print(stringToByte(cadena_bits))
guardar_datos_huffman(diccionario, cadena_bits, "ArqHardware/Pruebas/wi.bin")
