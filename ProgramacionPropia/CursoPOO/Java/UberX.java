package CursoPOO.Java;

public class UberX extends Car{
    private String marca;
    private String modelo;

    public UberX(String license, Account driver, String marca, String modelo){
        super(license, driver);
        this.marca = marca;
        this.modelo = modelo;
    }

    @Override
    public void dataCar() {
        super.dataCar();
        System.out.println("UberX [Marca: " + marca + ", Modelo: " + modelo + "]");
    }
}
