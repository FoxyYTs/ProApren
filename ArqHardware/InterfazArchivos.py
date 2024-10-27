from os import strerror

cadena_a_codificar ="Unas"
data = bytearray(len(cadena_a_codificar))

for i in cadena_a_codificar:
                     
        data.append(ord(i))


try:
    binary_file = open('file.bin', 'wb')
    binary_file.write(data)
    binary_file.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

# Ingresa aquí el código que lee los bytes del stream.

data2 = bytearray(len(cadena_a_codificar))
try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data2)
    binary_file.close()

    for b in data2:
        print(hex(b), end=' ')

    for b in data2:
        print(chr(b)+'-', end=' ')
        
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))