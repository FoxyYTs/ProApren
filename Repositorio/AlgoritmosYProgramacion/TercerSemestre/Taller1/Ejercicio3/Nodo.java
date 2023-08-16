package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio3;

public class Nodo {
    boolean embarazo;
    int edad;
    Nodo next,back;

    public Nodo(boolean embarazo, int edad){
        this.embarazo = embarazo;
        this.edad = edad;
        this.next = null;
        this.back = null;
    }
}
