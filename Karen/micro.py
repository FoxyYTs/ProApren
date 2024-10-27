def facturacion(n,i):
  while(n.lower() =="si"):
    servicios = ["Consulta","Vacunación","Radiografía", "Desparacitación", "Baño"]
    costo = [50000, 30000, 80000, 60000, 40000]
    servicio = input("Los servicios que presta la veterinaria son:" "\n-Consulta" "\n-Vacunación" "\n-Radiografía" "\n-Desparacitación" "\n-Baño" "\nIngrese servicio requerido: ")
    tipo = input("Ingrese tipo de mascota: ")
    nombre=input("Ingrese nombre de la mascota: ")
    if (servicio.lower() == "consulta"):
      valor = costo[0]
    elif (servicio.lower() == "vacunacion"):
      valor = costo[1]
    elif (servicio.lower() == "radiografia"):
      valor = costo[2]
    elif (servicio.lower() ==  "desparacitacion"):
      valor = costo[3]
    elif (servicio.lower() == "baño"):
      valor = costo[4]
    else:
      print("Servicio no disponible")
      continue
    iva = float(valor*0.19)
    total = float(valor+iva)
    i+=1
    Nombre.append(nombre)
    Tipo.append(tipo)
    visita.append(valor)
    Iva.append(iva)
    totalVisita.append(total)
    print("FACTURA",i,"" "\nTipo mascota: ", tipo,"\nNombre mascota: ", nombre, "\nMotivo visita: ", servicio, "\nValor: ${}".format(valor), "\nIVA: ${}".format(iva), "\nValor total: ${}".format(total), "\n**FIN")
    n=input("Ingrese SI: para ingresar datos o NO: para cerrar facturación""\n¿Desea facturar el servicio de una mascota?: ")

def promedio(Nombre,Tipo,totalVisita,Iva):
  for i in range(len(Tipo)):
    print("Nombre Mascota: ",Nombre[i], "Tipo Mascota: ",Tipo[i], "Valor: ${}".format(visita[i]), "IVA: ${}".format(Iva[i]), "Valor Total: ${}".format(totalVisita[i]))
  sumaValor=sum(visita)
  sumaIva=sum(Iva)
  sumaTotal=sum(totalVisita)
  print("Total Valor: ${}".format(sumaValor), "\nTotal IVA: ${}".format(sumaIva), "\nValor Total: ${}".format(sumaTotal))
  promedioValor = sumaValor/len(Tipo)
  promedioIva = sumaIva/len(Tipo)
  promedioTotal = sumaTotal/len(Tipo)
  print("Promedio Valor: ${}".format(promedioValor), "\nPromedio IVA: ${}".format(promedioIva), "\nPromedio Valor Total: ${}".format(promedioTotal))

#Programa Principal
n = input("Ingrese SI: para ingresar datos o NO: para cerrar facturación""\n¿Desea facturar el servicio de una mascota?: " )
i=0
Nombre = []
Tipo = []
visita = []
totalVisita =[]
Iva = []
facturacion(n,i)
promedio(Nombre,Tipo,totalVisita,Iva)