package AlgoritmosYProgramacion.TercerSemestre.Quiz1;

public class Puesto {
    String cliente = "VACIO";
    String tipo;
    Boolean ocupado = false;
    double precio = 0;

    public Puesto(String cliente, String tipo, boolean ocupado, double precio){
        this.cliente = cliente;
        this.tipo = tipo;
        this.ocupado = ocupado;
        this.precio = precio;
    }
}
