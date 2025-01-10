package CursoPOO.Java;

public class UberPool extends Car{
    private String marca;
    private String modelo;

    public UberPool(String license, Account driver, String marca, String modelo){
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
