package Repositorio.CursoPOO.Java;

import java.util.ArrayList;
import java.util.Map;

public class UberVan extends Car{//UberVan hereda de Car
    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;

    public UberVan(String license, Account driver, String brand, String model, Map<String, Map<String,Integer>> typeCarAccepted, ArrayList<String> seatsMaterial){
        super(license,driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
}
