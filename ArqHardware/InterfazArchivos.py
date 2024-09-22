import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from collections import Counter

def seleccionar_archivo():
    """
    Abre un diálogo de selección de archivos y devuelve la ruta del archivo seleccionado.
    """

    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    archivo_seleccionado = filedialog.askopenfilename()

    print("Archivo seleccionado:", archivo_seleccionado)
    if archivo_seleccionado:
        with open(archivo_seleccionado, 'r') as archivo:
            return archivo.read()
        
    else:
        messagebox.showerror("Error", "No se seleccionó ninguño archivo.")

def guardar_archivo(contenido):
    """
    Abre un diálogo para seleccionar una carpeta y permite al usuario ingresar el nombre del archivo.
    """

    # Crear una ventana raíz (oculta)
    root = tk.Tk()
    root.withdraw()

    # Abrir un diálogo para seleccionar una carpeta
    carpeta_seleccionada = filedialog.askdirectory()

    if carpeta_seleccionada:
        # Pedir al usuario el nombre del archivo
        nombre_archivo = simpledialog.askstring("Nombre de archivo", "Ingrese el nombre del archivo (sin extensión):")

        # Agregar la extensión si el usuario no la incluyó (por defecto .txt)
        if not nombre_archivo.endswith(".txt"):
            nombre_archivo += ".txt"

        ruta_completa = f"{carpeta_seleccionada}/{nombre_archivo}"

        # Guardar el archivo
        with open(ruta_completa, "w") as archivo:
            archivo.write(contenido)

        messagebox.showinfo("Información", f"Archivo guardado en: {ruta_completa}")
    else:
        messagebox.showerror("Error", "No se seleccionó ninguna carpeta.")

print(seleccionar_archivo())
#guardar_archivo("Esto se compone" + seleccionar_archivo())