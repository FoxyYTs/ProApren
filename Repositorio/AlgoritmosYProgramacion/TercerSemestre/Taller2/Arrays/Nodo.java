package AlgoritmosYProgramacion.TercerSemestre.Taller2.Arrays;

public class Nodo {
    String dueño = "VACIO";
    Boolean vip = false;
    double precio = 0;

    public Nodo(String dueño, boolean vip, double precio){
        this.dueño = dueño;
        this.vip = vip;
        this.precio = precio;
    }
}
