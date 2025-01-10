# 3
jadg_s = "12345"
print(int(jadg_s))
# 13
jadg_s = "jadg"
print(jadg_s.upper())
# 23
jadg_lista = [1,2,3,4,5,6,7,8,9,10]
jadg_listaPar = []
for i in range (0,10) :
    if ((jadg_lista[i] % 2)==0):
        jadg_listaPar.append(jadg_lista[i]) 

print(jadg_listaPar)
# 33
jadg_lista_principal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jadg_sublista = [3, 4, 5]

for i in range(len(jadg_lista_principal) - len(jadg_sublista) + 1):
        if jadg_lista_principal[i:i + len(jadg_sublista)] == jadg_sublista:
            print("Si es")
# 43
import pandas as pd
jadg_tabla = pd.read_csv("Quiz/archivoCSV.csv")
jadg_tablaDF = pd.DataFrame(jadg_tabla)
jadg_tablaDF.to_excel("Quiz/archivoXLSX.xlsx")       