import pickle
import struct

def leer_datos_huffman(nombre_archivo):
    """Lee los datos de Huffman desde un archivo binario.

    Args:
        nombre_archivo: Nombre del archivo a leer.

    Returns:
        tuple: Una tupla con el diccionario Huffman, la longitud de la cadena original
               y la cadena de bits decodificada.
    """

    with open(nombre_archivo, 'rb') as f:
        # Leer el diccionario
        datos_diccionario = f.read(4)  # Leer los primeros 4 bytes (tamaño estimado)
        while True:
            try:
                diccionario = pickle.loads(datos_diccionario)
                break
            except EOFError:
                datos_diccionario += f.read(4)

        # Leer la longitud de la cadena
        longitud_bytes = f.read(4)
        longitud_cadena = struct.unpack('>I', longitud_bytes)[0]

        # Leer la cadena de bits
        bytes_cadena = f.read()
        cadena_bits = ''.join(format(byte, '08b') for byte in bytes_cadena)

    # Decodificar la cadena (implementación básica)
    cadena_decodificada = ""
    codigo_actual = ""
    for bit in cadena_bits:
        codigo_actual += bit
        if codigo_actual in diccionario:
            cadena_decodificada += diccionario[codigo_actual]
            codigo_actual = ""

    return diccionario, longitud_cadena, cadena_decodificada

# Ejemplo de uso
diccionario, longitud, cadena_decodificada = leer_datos_huffman("datos_huffman.bin")
print(diccionario)
print(longitud)
print(cadena_decodificada)