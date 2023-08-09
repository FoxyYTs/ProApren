package AlgoritmosYProgramacion.TercerSemestre.Taller1.EJercicio1;

public class Nodo {
    String elemento;
    Nodo next, back;

    public Nodo(String elemento){
        this.elemento = elemento;
        this.next = null;
        this.back = null;
    }
}
