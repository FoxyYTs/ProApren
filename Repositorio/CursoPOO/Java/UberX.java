package Repositorio.CursoPOO.Java;

public class UberX extends Car {//UberX Hereda de Car
    String brand;
    String model;

    public UberX(String license, Account driver, String brand, String model){
        super(license,driver);
        this.brand = brand;
        this.model = model;
    }

    
}
