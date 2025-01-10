package AlgoritmosYProgramacion.CuartoSemestre.Conjuntos2;

public class Nodo {
    private String name;
    private float[] nota = {0,0,0,0};
    private Nodo next;

    public Nodo(){
        this.name = null;
        this.nota = null;
        this.next = null;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public float[] getNota() {
        return nota;
    }

    public void setNota(float[] nota) {
        this.nota = nota;
    }

    public Nodo getNext() {
        return next;
    }

    public void setNext(Nodo next) {
        this.next = next;
    }
}