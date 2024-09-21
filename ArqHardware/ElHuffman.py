import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from collections import Counter



def descomprimir_huffman(texto_comprimido, arbol):
    # Descomprime un texto comprimido utilizando el árbol de Huffman
    nodo = arbol
    texto_descomprimido = ""
    for bit in texto_comprimido:
        if bit == '0':
            nodo = nodo[0]
        else:
            nodo = nodo[1]
        if isinstance(nodo, str):
            texto_descomprimido += nodo
            nodo = arbol
    return texto_descomprimido

def construir_arbol_huffman(frecuencias):
    # Construye un árbol de Huffman a partir de un diccionario de frecuencias
    nodos = [(peso, simbolo) for simbolo, peso in frecuencias.items()]
    while len(nodos) > 1:
        (peso1, simbolo1) = heappop(nodos)
        (peso2, simbolo2) = heappop(nodos)
        nodo = (peso1 + peso2, (simbolo1, simbolo2))
        heappush(nodos, nodo)
    return nodos[0][1]

def recorrer_arbol(nodo, codigo, codigos):
    # Recorre el árbol de Huffman para asignar códigos a los símbolos
    if isinstance(nodo, str):
        codigos[nodo] = codigo
    else:
        recorrer_arbol(nodo[0], codigo + "0", codigos)
        recorrer_arbol(nodo[1], codigo + "1", codigos)

def comprimir_huffman(texto):
    # Comprime un texto utilizando el algoritmo de Huffman
    frecuencias = Counter(texto)
    arbol = construir_arbol_huffman(frecuencias)
    codigos = {}
    recorrer_arbol(arbol, "", codigos)
    texto_comprimido = "".join(codigos[simbolo] for simbolo in texto)
    return texto_comprimido, codigos



def seleccionar_archivo():
    """
    Abre un diálogo de selección de archivos y devuelve la ruta del archivo seleccionado.
    """

    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    archivo_seleccionado = filedialog.askopenfilename()

    if archivo_seleccionado:
        return archivo_seleccionado
    else:
        return "No se seleccionó ningún archivo."

# Ejemplo de uso:
ruta_archivo = seleccionar_archivo()
print(ruta_archivo)

def guardar_archivo():
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

        # Contenido del archivo (puedes cambiarlo)
        contenido = "Este es el contenido del archivo de texto."

        # Guardar el archivo
        with open(ruta_completa, "w") as archivo:
            archivo.write(contenido)

        print(f"Archivo guardado en: {ruta_completa}")
    else:
        print("No se seleccionó ninguna carpeta.")

# Llamar a la función para iniciar el proceso
guardar_archivo()