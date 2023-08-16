package Taller1;

public class pila {
    public node top = null;

    public void push(char caracter) {
        node nuevo = new node(caracter);
        nuevo.next = top;
        top = nuevo;
    }

    public node pop() {
        node temp = null;
        temp = top;
        top = top.next;
        return temp;
    }

    public boolean isEmpty() {
        return top == null;
    }
}