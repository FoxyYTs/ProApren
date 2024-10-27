import heapq
from collections import Counter
import json
from os import strerror
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, Node)):
            return False
        return self.freq == other.freq

def build_huffman_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        heap.append(Node(char, freq))
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)
    return heap[0]

def huffman_encoding(data):
    freq_dict = Counter(data)
    huffman_tree = build_huffman_tree(freq_dict)
    huffman_code = {}
    def dfs(node, code):
        if node.char:
            huffman_code[node.char] = code
            return
        dfs(node.left, code + "0")
        dfs(node.right, code + "1")
    dfs(huffman_tree, "")
    encoded_data = "".join([huffman_code[char] for char in data])
    return encoded_data, huffman_code

def huffman_decoding(encoded_data, huffman_code):
    print(encoded_data)
    decoded_data = ""
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        for clave, valor in huffman_code.items():
            if valor == current_code:
                decoded_data += clave
                current_code = ""
    return decoded_data

def seleccionar_archivo(tipo):
    try:
        if tipo == "comprimir":
            archivo_seleccionado = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
            with open(archivo_seleccionado, 'r') as archivo:
                return archivo.read()

        elif tipo == "descomprimir":
            archivo_seleccionado = filedialog.askopenfilename(defaultextension=".bin", filetypes=[("Archivos Binario", "*.bin")])
            binary_file = open('archivo_seleccionado', 'rb')

            # esto lee un objeto bytes, si necesitás que sea mutable, envolvelo con bytearray
            data2 = binary_file.read()

            binary_file.close()

            for b in data2:
                print(chr(b)+'-', end=' ')
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo seleccionado no existe o no se puede abrir.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {str(e)}")

def guardar_archivo(contenido, tipo):
    # Abrir un diálogo para seleccionar una carpeta
    if tipo == "comprimir":
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

        if archivo:
            # Guardar el archivo
            with open(archivo, "w") as archivo:
                archivo.write(contenido)

            messagebox.showinfo("Información", f"Archivo guardado en: {archivo}")
        else:
            messagebox.showerror("Error", "No se seleccionó ninguna carpeta.")
    
    elif tipo == "descomprimir":
        archivo = filedialog.askopenfilename(defaultextension=".bin", filetypes=[("Archivos Binario", "*.bin")])

        if archivo:
            binary_file = open(archivo, 'wb')

            # creo un objeto bytes a partir de una cadena utf-8
            binary_file.write(contenido.encode())

            binary_file.close()
        else:
            messagebox.showerror("Error", "No se seleccionó ninguño archivo.")

def main():

    def comprimir():
        data = seleccionar_archivo("comprimir")

        tamano_original = len(data.encode('utf-8'))
        encoded_data, huffman_code = huffman_encoding(data)
        tamano_codificado = len(encoded_data)
        tasa_compresion = (1 - (tamano_codificado / (tamano_original * 7))) * 100
        messagebox.showinfo("Información", f"Archivo original: {tamano_original*7} bytes\nArchivo codificado: {tamano_codificado} bits\nTasa de compresión: {tasa_compresion:.2f}%")

        diccionario_str = json.dumps(huffman_code)
        datos = [diccionario_str, encoded_data]
        contenido = "\n".join(datos)

        guardar_archivo(contenido, "comprimir")
        ventana.destroy()

    def descomprimir():
        huffman_code, encoded_data = seleccionar_archivo("descomprimir")
        decode_data= huffman_decoding(encoded_data, huffman_code)
        guardar_archivo(decode_data, "descomprimir")

    ventana = tk.Tk()
    ventana.title("Comprimir/Descomprimir")

    boton_comprimir = tk.Button(ventana, text="Comprimir", command=comprimir)
    boton_comprimir.pack()

    boton_descomprimir = tk.Button(ventana, text="Descomprimir", command=descomprimir)
    boton_descomprimir.pack()

    ventana.mainloop()

if __name__ == "__main__":
    main()