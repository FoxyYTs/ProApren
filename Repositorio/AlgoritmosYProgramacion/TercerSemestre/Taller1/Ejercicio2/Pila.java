package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio2;

public class Pila {
    Nodo top1, top2, top3;
    
    public Pila() {
        top1 = null;
        top2 = null;
        top3 = null;
    }
        
    public void push1(int elemento) {
        Nodo nuevoNodo = new Nodo(elemento);
        if (top1 == null) {
            top1 = nuevoNodo;
        } else {
            top1.back = nuevoNodo;
            nuevoNodo.next = top1;
            top1 = top1.back;
        }
    }
        
    public int pop1() {
        if (top1 == null) {
            return '0' ;
        }
        int caracter = top1.elemento;
        top1 = top1.next;
        return caracter;
    }

    public void push2(int elemento) {
        Nodo nuevoNodo = new Nodo(elemento);
        if (top2 == null) {
            top2 = nuevoNodo;
        } else {
            top2.back = nuevoNodo;
            nuevoNodo.next = top2;
            top2 = top2.back;
        }
    }
        
    public int pop2() {
        if (top2 == null) {
            return '0' ;
        }
        int caracter = top2.elemento;
        top2 = top2.next;
        return caracter;
    }

    public void push3(int elemento) {
        Nodo nuevoNodo = new Nodo(elemento);
        if (top3 == null) {
            top3 = nuevoNodo;
        } else {
            top3.back = nuevoNodo;
            nuevoNodo.next = top3;
            top3 = top3.back;
        }
    }
        
    public int pop3() {
        if (top3 == null) {
            return '0' ;
        }
        int caracter = top3.elemento;
        top3 = top3.next;
        return caracter;
    }

    public void print() {
        
    }

}
