package AlgoritmosYProgramacion.CuartoSemestre.Conjuntos1;

public class Nodo {
    private String dato;
    private Nodo next;
    private Nodo prev;

    public Nodo(String dato){
        this.dato = dato;
        this.next = null;
        this.prev = null;
    }

    public String getDato() {
        return dato;
    }

    public void setDato(String dato) {
        this.dato = dato;
    }

    public Nodo getNext() {
        return next;
    }

    public void setNext(Nodo next) {
        this.next = next;
    }

    public Nodo getPrev() {
        return prev;
    }

    public void setPrev(Nodo prev) {
        this.prev = prev;
    }

    
}
