package AlgoritmosYProgramacion.TercerSemestre.Quiz1;

public class Puesto {
    private String cliente = "VACIO";
    private String tipo;
    private String ocupado;
    private double precio = 0;

    public Puesto(String cliente, String tipo, String ocupado, double precio){
        this.cliente = cliente;
        this.tipo = tipo;
        this.ocupado = ocupado;
        this.precio = precio;
    }

    public String getCliente() {
        return cliente;
    }

    public void setCliente(String cliente) {
        this.cliente = cliente;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getOcupado() {
        return ocupado;
    }

    public void setOcupado(String ocupado) {
        this.ocupado = ocupado;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }


}
