import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

archivo = "AlgoritmosYProgramacion/CuartoSemestre/Estadistica3/LaInformacion.xlsx"

tabla = pd.read_excel(archivo, sheet_name='Data')
df = pd.DataFrame(tabla)

df.replace('..', np.nan, inplace=True)

df.iloc[:, 4:] = df.iloc[:, 4:].apply(pd.to_numeric, errors='coerce')

numeric_columns = df.select_dtypes(include=[np.number])
df[numeric_columns.columns] = numeric_columns.fillna(numeric_columns.mean())

df.replace(np.nan, 0, inplace=True)

def graficar(pais,version):
    pais = df.loc[df.iloc[:, 0] == pais]
    filas = pais.loc[df.iloc[:, 3] == version]
    fig, ax = plt.subplots()

    for columna in range(6, 24):
        ax.plot(filas.iloc[:, 4], filas.iloc[:, columna], label=f'Columna {columna-5}')

    ax.set_xlabel('Fechas')
    ax.set_ylabel('Valores')
    ax.legend(title='Nombre de las columnas', bbox_to_anchor=(1, 1))
    plt.show()

pais = ["Colombia","Bulgaria","Brazil","Bolivia","Australia","Argentina","Mexico","Chile","Peru","Espana","Bolivia"]
version = ["FPN 1.0","FPN 1.1","FPN 2.0","FPN 2.1"]

p = input("Menu de Grafica\nElige el Pais\n1) Colombia\n2) Bulgaria\n3) Brazil\n4) Bolivia\n5) Australia\n6) Argentina\n7) Mexico\n8) Chile\n9) Peru\n10) España\n11) Bolivia\nEleccion: ")
v = input("Elige la Version\n1) FPN 1.0\n2) FPN 1.1\n3) FPN 2.0\n4) FPN 2.1\nEleccion: ")
graficar(pais[int(p)-1],version[int(v)-1])
