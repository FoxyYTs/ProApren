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

with open('ArqHardware/Pruebas/wi.bin', 'rb') as f:
    
    datos = f.readline().strip()
    code = byteToString(datos)
    print(code)



    