package TrabajosDeClase.Pruebas;

public class Complejo {
    private double real;
    private double imaginario;

    // Constructor por defecto
    public Complejo() {
        this.real = 0;
        this.imaginario = 0;
    }

    // Constructor parametrizado
    public Complejo(double real, double imaginario) {
        this.real = real;
        this.imaginario = imaginario;
    }

    // Accesores
    public double getReal() {
        return real;
    }

    public double getImaginario() {
        return imaginario;
    }

    // Mutadores
    public void setReal(double real) {
        this.real = real;
    }

    public void setImaginario(double imaginario) {
        this.imaginario = imaginario;
    }

    // Suma de números complejos
    public Complejo suma(Complejo otroComplejo) {
        double nuevaParteReal = this.real + otroComplejo.real;
        double nuevaParteImaginaria = this.imaginario + otroComplejo.imaginario;
        Complejo resultado = new Complejo(nuevaParteReal, nuevaParteImaginaria);
        return resultado;
    }

    // Resta de números complejos
    public Complejo resta(Complejo otroComplejo) {
        double nuevaParteReal = this.real - otroComplejo.real;
        double nuevaParteImaginaria = this.imaginario - otroComplejo.imaginario;
        Complejo resultado = new Complejo(nuevaParteReal, nuevaParteImaginaria);
        return resultado;
    }

    // Multiplicación de números complejos
    public Complejo multiplicacion(Complejo otroComplejo) {
        double nuevaParteReal = this.real * otroComplejo.real - this.imaginario * otroComplejo.imaginario;
        double nuevaParteImaginaria = this.real * otroComplejo.imaginario + this.imaginario * otroComplejo.real;
        Complejo resultado = new Complejo(nuevaParteReal, nuevaParteImaginaria);
        return resultado;
    }

    // División de números complejos
    public Complejo division(Complejo otroComplejo) {
        double divisor = otroComplejo.real * otroComplejo.real + otroComplejo.imaginario * otroComplejo.imaginario;
        double nuevaParteReal = (this.real * otroComplejo.real + this.imaginario * otroComplejo.imaginario) / divisor;
        double nuevaParteImaginaria = (this.imaginario * otroComplejo.real - this.real * otroComplejo.imaginario) / divisor;
        Complejo resultado = new Complejo(nuevaParteReal, nuevaParteImaginaria);
        return resultado;
    }

    // Acumulación de números complejos
    public void acumulacion(Complejo otroComplejo) {
        this.real += otroComplejo.real;
        this.imaginario += otroComplejo.imaginario;
    }

    // Método para imprimir el número complejo
    public void print() {
        System.out.println(real + " + " + imaginario + "i");
    }
}

