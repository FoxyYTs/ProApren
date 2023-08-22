package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio3;

public class Nodo {
    String nombre;
    int edad;
    boolean embarazada;
    Nodo next, back;

    public Nodo(String nombre, int edad, boolean embarazada) {
        this.nombre = nombre;
        this.edad = edad;
        this.embarazada = embarazada;
        this.next = null;
    }
}
