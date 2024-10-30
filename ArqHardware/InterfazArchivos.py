import pickle
import struct

def byteToString(bytes):
    text = ""
    bits = bin(0)
    for byte in bytes:
        bits = bin(byte)[2:]
        bits = bits.zfill(8)
        text += bits

    return text


with open('datos_huffmasn.bin', 'rb') as f:
    datos = f.readline()
    print(datos)
    print(byteToString(datos))
    datoss = f.readline()
    print(datoss)
    print(pickle.loads(datoss))

    