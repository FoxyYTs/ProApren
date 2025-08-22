import heapq
from collections import Counter
import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
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
    
def stringToByte(text):
    while len(text) % 8 != 0:
        text += "0"

    bytes = bytearray()
    for i in range(0, len(text), 8):
        byte = text[i:i+8]
        bytes.append(int(byte,2))

    return bytes

def byteToString(bytes):
    text = ""
    bits = bin(0)
    for byte in bytes:
        bits = bin(byte)[2:]
        bits = bits.zfill(8)
        text += bits

    return text

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
    reverse_huffman = {v: k for k, v in huffman_code.items()}  # invertir diccionario
    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_huffman:
            decoded_data += reverse_huffman[current_code]
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
            with open(archivo_seleccionado, 'rb') as archivo:
                diccionario = json.loads(archivo.readline().strip())

                segunda_linea = byteToString(archivo.readline().strip()) + "00001010" + byteToString(archivo.readline().strip())
            return diccionario, segunda_linea
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo seleccionado no existe o no se puede abrir.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {str(e)}")

def guardar_archivo(contenido, tipo):
    try:
        if tipo == "comprimir":
            archivo = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Archivos Binario", "*.bin")])
            with open(archivo, 'wb') as archivo:
                archivo.write(contenido)

        elif tipo == "descomprimir":
            archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
            with open(archivo, 'w') as archivo:
                archivo.write(contenido)
                
    except FileNotFoundError:
        messagebox.showerror("Error", "La ubicacion no se pudo encontrar.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {str(e)}")

def main():

    def comprimir():
        data = seleccionar_archivo("comprimir")

        tamano_original = len(data.encode('utf-8'))
        encoded_data, huffman_code = huffman_encoding(data)
        diccionario = json.dumps(huffman_code).encode('utf-8')
        datos = stringToByte(encoded_data)
        contenido = diccionario + b'\r\n' + datos
        tamano_codificado = len(contenido)
        tasa_compresion = (1 - (tamano_codificado / (tamano_original))) * 100
        messagebox.showinfo("Información", f"Archivo original: {tamano_original} bytes\n Aproximado Archivo codificado: {tamano_codificado} bits\nTasa de compresión: {tasa_compresion:.2f}%")

        
        print(huffman_code)
        print(encoded_data)
        print(tamano_codificado)
        

        guardar_archivo(contenido, "comprimir")

    def descomprimir():
        huffman_code, encoded_data = seleccionar_archivo("descomprimir")
        decode_data= huffman_decoding(encoded_data, huffman_code)
        guardar_archivo(decode_data, "descomprimir")

    ventana = tk.Tk() 
    ventana.title("Comprimir/Descomprimir") 
    ventana.geometry("300x200") 
    ventana.configure(bg='lightgrey') # Crear un marco para los botones 
    marco_botones = ttk.Frame(ventana, padding="10") 
    marco_botones.pack(padx=20, pady=20, fill=tk.BOTH, expand=True) # Botón Comprimir 
    boton_comprimir = ttk.Button(marco_botones, text="Comprimir", command=comprimir) 
    boton_comprimir.pack(side=tk.LEFT, padx=10, pady=10, expand=True) # Botón Descomprimir 
    boton_descomprimir = ttk.Button(marco_botones, text="Descomprimir", command=descomprimir) 
    boton_descomprimir.pack(side=tk.RIGHT, padx=10, pady=10, expand=True)

    ventana.mainloop()

if __name__ == "__main__":
    main()  