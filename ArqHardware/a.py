import json
import pickle
import struct

huffman_code = {"e": "00", "l": "01", " ": "100", "a": "1010", "h": "1011", "s": "11"}
text = "01010110101100011111100111000110"

while len(text) % 8 == 0:
    text += '0'

byteArray = bytearray()
for i in range(0, len(text), 8):
    byte = text[i:i+8]
    byteArray.append(int(byte,2))

print(byteArray)

    