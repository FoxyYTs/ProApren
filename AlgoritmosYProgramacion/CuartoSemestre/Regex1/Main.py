import re

def es_correo_valido(correo):
  patron = r'^[a-z]+[_-]+[a-z]+[0-9]{5}+@elpoli.edu.co$'

  regex = re.compile(patron)

  match = regex.match(correo)

  return match is not None

import re

def es_telefono_fijo_colombia(numero):

  patron = r'^(\(?[2-9]\d{2}\)?\s)?(\d{7})+$'

  regex = re.compile(patron)

  match = regex.match(numero)

  return match is not None

def es_contraseña_valida(contraseña):
  
  patron = r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$'
  
  regex = re.compile(patron)

  match = regex.match(contraseña)

  return match is not None

contraseña1 = "contraseña"
contraseña2 = "Contraseña"
contraseña3 = "Contraseña1234"

numero1 = "604 2998772"
numero2 = "3713777"
numero3 = "2998772"

correo1 = "juan.perez@gmail.com"
correo2 = "jose_daza82222@elpoli.edu.co"

print(f"{contraseña1} es una contraseña válida: {es_contraseña_valida(contraseña1)}")
print(f"{contraseña2} es una contraseña válida: {es_contraseña_valida(contraseña2)}")
print(f"{contraseña3} es una contraseña valida: {es_contraseña_valida(contraseña3)}")

print(f"{numero1} es un teléfono fijo de Colombia: {es_telefono_fijo_colombia(numero1)}")
print(f"{numero2} es un teléfono fijo de Colombia: {es_telefono_fijo_colombia(numero2)}")
print(f"{numero3} es un teléfono fijo de Colombia: {es_telefono_fijo_colombia(numero3)}")

print(f"{correo1} es un correo válido: {es_correo_valido(correo1)}")
print(f"{correo2} es un correo válido: {es_correo_valido(correo2)}")
