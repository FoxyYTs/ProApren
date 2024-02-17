package AlgoritmosYProgramacion.CuartoSemestre.SegundoTrabajo;

public class Pila {
    Nodo top;
    int tam = 0;

    public Pila(){
        this.top = null;
    }

    public void push(int dato) {
        Nodo nuevo = new Nodo(dato);
        if (top == null) {
            top = nuevo;
        } else {
            nuevo.next = top;
            top = nuevo;
        }
        tam++;
    }

    public Nodo pop(){
        if (top != null) {
            Nodo aux = top;
            top = top.next;
            tam--;
            return aux;
        }
        tam--;
        return null;
    }

    public int fill(){
        return tam;
    }
}
