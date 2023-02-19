package Repositorio.CursoPOO.Java;

public class UberPool extends Car {//UberPool hereda de Car
    String brand;
    String model;

    public UberPool(String license, Account driver, String brand, String model){
        super(license,driver);
        this.brand = brand;
        this.model = model;
    }
}
