package AlgoritmosYProgramacion.CuartoSemestre.SegundoTrabajo2;

public class NodoLg {
    private int tag;
    private char dato;
    NodoLg subList;
    NodoLg next;
    NodoLg head;

    public NodoLg(char dato) {
        this.dato = dato;
    }

    public int getTag() {
        return tag;
    }

    public void setTag(int tag) {
        this.tag = tag;
    }

    public char getDato() {
        return dato;
    }

    public void setDato(char dato) {
        this.dato = dato;
    }

    public NodoLg getNext() {
        return next;
    }

    public void setNext(NodoLg next) {
        this.next = next;
    }

}
