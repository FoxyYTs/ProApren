package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio1;

public class Pila {
    Nodo top;
    
    public Pila() {
        top = null;
    }
        
    public void push(char elemento) {
        Nodo nuevoNodo = new Nodo(elemento);
        nuevoNodo.next = top;
        top = nuevoNodo;
    }
        
    public char pop() {
        if (top == null) {
            return '0' ;
        }
        char caracter = top.elemento;
        top = top.next;
        return caracter;
    }
        
    public boolean isEmpty() {
        return top == null;
    }
}
