import json


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


diccionario = {"e": "00", "l": "01", " ": "100", "a": "1010", "h": "1011", "s": "11"}

dic = json.dumps(diccionario)

print(dic)

# Codificar la cadena en UTF-8
cadena_codificada = dic.encode()

# Imprimir la cadena codificada como bytes
print(cadena_codificada)