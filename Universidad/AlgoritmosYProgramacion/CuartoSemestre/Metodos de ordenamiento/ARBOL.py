class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.izquierda = None
    self.derecha = None

class ArbolBinario:
  def __init__(self):
    self.raiz = None

  # Insertar dato en el árbol
  def insertar(self, dato):
    if self.raiz is None:
      self.raiz = Nodo(dato)
      return
    else:
      actual = self.raiz
      while True:
        if dato < actual.dato:
          if actual.izquierda is None:
            actual.izquierda = Nodo(dato)
            break
          else:
            actual = actual.izquierda
        else:
          if actual.derecha is None:
            actual.derecha = Nodo(dato)
            break
          else:
            actual = actual.derecha

  # Buscar dato en el árbol 
  def buscar(self, dato):
    actual = self.raiz
    while actual is not None:
      if actual.dato == dato:
        return True
      elif dato < actual.dato:
        actual = actual.izquierda
      else:
        actual = actual.derecha
    return False

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)

dato_buscado = 12
encontrado = arbol.buscar(dato_buscado)

if encontrado:
  print(f"El dato {dato_buscado} se encuentra en el árbol")
else:
  print(f"El dato {dato_buscado} no se encuentra en el árbol")
