import heapq
from collections import Counter
import json
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from collections import Counter

def seleccionar_archivo():
    """
    Abre un diálogo de selección de archivos y devuelve la ruta del archivo seleccionado.
    """

    archivo_seleccionado = filedialog.askopenfilename()

    print("Archivo seleccionado:", archivo_seleccionado)
    if archivo_seleccionado:
        with open(archivo_seleccionado, 'r') as archivo:
            return archivo.read()
        
    else:
        messagebox.showerror("Error", "No se seleccionó ninguño archivo.")


def main():
    def comprimir():
        print(seleccionar_archivo())
    def descomprimir():
        print("Descomprimiendo...")

    ventana = tk.Tk()
    ventana.title("Comprimir/Descomprimir")

    boton_comprimir = tk.Button(ventana, text="Comprimir", command=comprimir)
    boton_comprimir.pack()

    boton_descomprimir = tk.Button(ventana, text="Descomprimir", command=descomprimir)
    boton_descomprimir.pack()

    ventana.mainloop()

if __name__ == "__main__":
    main()