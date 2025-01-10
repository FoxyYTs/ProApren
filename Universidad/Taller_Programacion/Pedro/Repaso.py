# 1)
print("Hola Mundo")
# 2,3)
int2 = 5
string2 = "Pepe"
double2 = 2.5
boolean2 = True
# 4)
int4 = 5
print(int4 + 5)
print(int4 * 3)
print(int4 - 2)
# 5)
string5 = "2"
int5 = int(string5)
print (int5)
# 6)
int6 = int(input())
print (int6+5)
# 7, 8, 9)
int7 = int(input("Ingrese un numero: "))
if int7 > 5:
    print(str(int7) + " Es mayor a 5")
elif int7 == 5:
    print(str(int7) + " Es igual a 5")
else:
    print(str(int7) + " Es menor a 5")
# 10
for i in range (0,21, 2) :
    print (i)
# 11
i = 0
while (i < 10):
    print(str(i) + " veces")
    i += 1
# 12
for i in range (1,11):
    if i==0 or i==5:
        continue
    elif i==8:
        break
    print(i)
#13
lista = ["A", "C", "/", "D", "C"]
for i in range (0, 5):
    print(lista[i])
print("=======================")
for i in range (-1,-6,-1):
    print(lista[i])

lista[2] = "|"
print(lista)
# 14
tupla = (1, 8, 3, 6, 5, 4, 7, 2, 9)
print(tupla)
print(tupla.count(8))
print(tupla.index(4))
# 15
primos = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
par = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
impar = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
print(par | impar)
print(primos - impar)
print(impar & primos)
# 16
dic = {"A" : 1,
       "B" : 2,
       "C" : 3,
       "D" : 4,
       "E" : 5,
       "F" : 6,
       "G" : 7,
       "H" : 8,
       "I" : 9,
       "J" : 10}
for i in dic:
    print(i, end = ", ")
print("\n=================")
for j in dic:
    print(dic[i], end = ", ")
print("\n=================")
for x, y in dic.items():
    print(x, y ,end = ", ")
print("\n=================")
print(dic.keys())
print(dic.values())
# 17
lista = ["C","B"]
lista2 = ["D", "/", "C", "A"]
num = [2,4,6,8,1,3,5,7,9]
print(lista)
lista.extend("C")
print(lista)
print(lista2)
lista.extend(lista2)
print(lista)
lista.insert(0 , "C")
print(lista)
del lista[1: 3]
print(lista)
lista.remove("C")
print(lista)
print(num)
lista.reverse()
num.reverse()
print(lista)
print(num)
num.sort()
print(sorted(lista))
print(num)
num.sort(reverse=True)
print(lista)
print(num)
# 18
with open("hoja.txt", "r") as archivo:
    print(archivo.read())
# 19
with open("hoja.txt", "w") as archivo:
    archivo.write("Texto predeterminado")
# 18 y 19
for i in range (0, 10):
    with open("hoja.txt", "r") as archivo:
        print(archivo.read())
    with open("hoja.txt", "w") as archivo:
        archivo.write("Texto predeterminado" + str(i))
# 20
#r:leer,w:escribir,a:añadir,rb:leer imagenes, wb:escribir imagenes
# 21
import pandas as pd
df = pd.DataFrame()

nombres = ["Ana", "Alejandro", "Andres" ,"Jose"]
edades = [20, 19, 21, 21]

df['Nombre'] = nombres
df['Edad'] = edades

print(df)
# 22
import csv
with open("arhivoCSV.csv", newline="") as archivo:
    lector = csv.reader(archivo, delimiter=" ", quotechar="|")
    for i in lector:
        print(", ".join(i))
# 23
import pandas as pd
Documento = pd.read_csv("taller1.txt",sep=";") 
Filtrar=Documento[Documento["Fecha"]=="16/08/2023"]
print(Filtrar.to_string(index=False))
# 24
import numpy as np 
numeros=[10,20,30,40,50]
print(f"Numeros: {numeros}")
sum=np.sum(numeros)
print(f"Suma: {sum}")
mean=np.mean(numeros)
print(f"Mitad: {mean}")
max=np.max(numeros)
print(f"Maximo: {max}")
min=np.min(numeros)
print(f"Minimo: {min}")
# 25
import pandas as pd

df = pd.DataFrame()

nombres = ["Ana", "Alejandro", "Andres" ,"Jose"]
edades = [20, 19, 21, 21]

df['Nombre'] = nombres
df['Edad'] = edades

print(f"Iloc:\n{df.iloc[0]}")
print("Loc:\n",df.loc[df["Edad"]==19])
print("Casilla:\n",df.loc[df["Edad"]==21,"Nombre"])
# 26
import pandas as pd

df = pd.DataFrame()

nombres = ["Ana", "Alejandro", "Andres" ,"Jose"]
edades = [20, 20, 21, 21]

df['Nombre'] = nombres
df['Edad'] = edades

df.groupby("Edad")
for name in df.groupby("Edad"):
    print(name)
# 27
import pandas as pd

df1 = pd.DataFrame({'A':['A0', 'A1', 'A2','A3'],
	'B':['B0', 'B1', 'B2','B3'],
	'C':['C0', 'C1', 'C2','C3'],
	'D':['D0', 'D1', 'D2','D3']})


df2 = pd.DataFrame({'A':['A4', 'A5', 'A6','A7'],
	'B':['B4', 'B5', 'B6','B7'],
	'C':['C4', 'C5', 'C6','C7'],
	'D':['D4', 'D5', 'D6','D7']})

con = pd.concat([df1, df2],ignore_index=True)
print(con)

con = df1.merge(df2, on="B")
print(con)
# 28
import pandas as pd

Valores = ("A", "B", "C", "D", "E")
series = pd.Series(Valores)

print(series)
# 29
import pandas as pd

df = pd.DataFrame({'A':['A0', 'A1', 'A2','A3'],
	'B':['B0', 'B1', 'B2','B3'],
	'C':['C0', 'C1', 'C2','C3'],
	'D':['D0', 'D1', 'D2','D3']})

print(df)
df.to_csv("arhivoCSV.csv")

# 30
import pandas as pd

df = pd.DataFrame({'A':['A0', 'A1', 'A2','A3'],
	'B':['B0', 'B1', 'B2','B3'],
	'C':['C0', 'C1', 'C2','C3'],
	'D':['D0', 'D1', 'D2','D3']})

print(df.to_json())
df.to_json("archivojson.json")

# 31 y 32
import pandas as pd

tabla = pd.read_html("https://es.wikipedia.org/wiki/Estatura")[1]
tablaDF = pd.DataFrame(tabla)

tablaDF.to_excel("archivoXLSX.xlsx")

# 33
import pandas as pd

tabla = pd.read_html("https://es.wikipedia.org/wiki/Estatura")[1]
tablaDF = pd.DataFrame(tabla)
primeros10 = tablaDF.head(11)
primeros10.to_csv("archivoCSV.csv")
# 34
import pandas as pd

Hoja1=pd.read_html("https://es.wikipedia.org/wiki/Estatura")[1]
Hoja2=pd.read_html("https://www.cuandoenelmundo.com/herramientas/codigos-para-llamadas-internacionales")[0]
Hoja3=pd.read_html("https://minecraft-ids.grahamedgecombe.com")[0]

with pd.ExcelWriter("archivoXLSX.xlsx") as writer:
    Hoja1.to_excel(writer,sheet_name="Altura")
    Hoja2.to_excel(writer,sheet_name="Codigo llamada")
    Hoja3.to_excel(writer,sheet_name="Minecraft")
# 35


