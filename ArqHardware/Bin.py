import pickle
import struct

def guardar_datos_huffman(diccionario, cadena_bits, nombre_archivo):
    """Guarda los datos de Huffman en un archivo binario.

    Args:
        diccionario: Diccionario con el código Huffman.
        longitud_cadena: Longitud de la cadena de bits codificada.
        cadena_bits: Cadena de bits codificada.
        nombre_archivo: Nombre del archivo a crear.
    """

    # Serializar el diccionario
    datos_diccionario = pickle.dumps(diccionario)

    # Convertir la cadena de bits a bytes
    bytes_cadena = bytes(int(cadena_bits[i:i+8], 2) for i in range(0, len(cadena_bits), 8))

    # Escribir los datos en el archivo
    with open(nombre_archivo, 'wb') as f:
        f.write(datos_diccionario)
        f.write(bytes_cadena)

# Ejemplo de uso:
diccionario = {"e": "00", "l": "01", " ": "100", "a": "1010", "h": "1011", "s": "11"}
cadena_bits = "1110110010011000101111001100101010011101100010111"

guardar_datos_huffman(diccionario, cadena_bits, "datos_huffmasn.bin")