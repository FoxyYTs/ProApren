import re

def es_usuario_valido(usuario):

  patron = r'^[A-Z]{1}[a-z]{2,9}[#?.,](0[1-9]|2[0-9]|3[0-1])(1[0-2]{1}|0[0-9]{1})$'

  regex = re.compile(patron)

  match = regex.match(usuario)

  return match is not None

usuario = "Aliriaar#0606"

print(f"El usuario {usuario} es un usuario válido: {es_usuario_valido(usuario)}\n")

def es_correo_valido(correo):

  patron = r'^([aA][lL][gG][oO][rR][iI][tT][mM][oO][sS]|[aA][yY][pP])([1-4]{1})poli@([a-zA-Z]{1,8})(.edu.co|.com)$'

  regex = re.compile(patron)

  match = regex.match(correo)

  return match is not None

correo = "Algoritmos4poli@elpoli.edu.co"

print(f"El correo {correo} es un correo electrónico: {es_correo_valido(correo)}\n")

def es_numero_valido(numero):

  patron = r'^([+]([0-9]{1,3})[^20]|[^32]|[^1]|[^40]|[^92])([(](1|3|4|6)[0-9]{2}[)])([0-9]{7})$'

  regex = re.compile(patron)

  match = regex.match(numero)

  return match is not None

numero = "+18(413)1234567"

print(f"El numero {numero} es un número valido: {es_numero_valido(numero)}\n")
