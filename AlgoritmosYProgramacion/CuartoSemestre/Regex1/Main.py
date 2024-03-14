import re

def es_correo_valido(correo):

  patron = r'^[a-zA-Z0-9_.+-]+@elpoli.edu.co$'

  regex = re.compile(patron)

  match = regex.match(correo)

  return match is not None

def es_telefono_fijo_colombia(numero):

  patron = r'^(\(?[7-9]\d{2}\)?\s)?(\d{7})+$'

  regex = re.compile(patron)

  match = regex.match(numero)

  return match is not None

def es_contraseña_valida(contraseña):
  
  patron = r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$'
  
  regex = re.compile(patron)

  match = regex.match(contraseña) 

  return match is not None

contraseñas = ["$Poli1", "contraseña", "Contraseña1234", "contraseña123456789"]

numeros = ["3202020", "3022173922", "2998772", "604299877"]

correos = ["mruiz.elpoli.edu.co", "jose_daza82222@elpoli.edu.co", "luzjaramillo@elpoli.edu.co", "labintegradorio@elpoli.edu.co"]

for contraseña in contraseñas:
  print(f"{contraseña} es una contraseña válida: {es_contraseña_valida(contraseña)}\n")
print("\n")
for numero in numeros:
  print(f"{numero} es un teléfono fijo de Colombia: {es_telefono_fijo_colombia(numero)}\n")
print("\n")
for correo in correos:
  print(f"{correo} es un correo válido: {es_correo_valido(correo)}\n")
