package AlgoritmosYProgramacion.SegundoSemestre.listasligadascirculares;

public class Nodo {
    public String dato;
    public Nodo siguiente;
    public Nodo atras;
    
    public Nodo(String dato){
        this.dato = dato;
        this.siguiente = null;
        this.atras = null;
    }
}

