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
    
    datoss = f.readline()
    print(pickle.loads(datoss))
    datos = f.readline()
    print(byteToString(datos))

    