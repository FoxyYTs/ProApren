import pandas as pd

archivo = "d:/programacion/Github/AlgoritmosYProgramacion/CuartoSemestre/Estadistica/Lainformacion.xlsx"

# Leemos el archivo directamente con Pandas
df = pd.read_excel(archivo, sheet_name='Data')

# Imprimimos la información del DataFrame

print("COUNT: " , df.iloc[:, 4].count())
print("Media: " , df.iloc[:, 4].mean())
print("Desviacion: " , df.iloc[:, 4].std())
print("Minimo: " , df.iloc[:, 4].min())
print("Maximo: " , df.iloc[:, 4].max())

print(df.iloc[:,5].describe())
# Imprimimos el número de filas en la hoja de trabajo
print(df.shape[0])