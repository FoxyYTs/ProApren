package Repositorio.CursoPOO.Java;


import java.util.*;

public class UberVan extends Car{
    private Map<String, Map<String, Integer>> typeCarAccepted;
    private ArrayList<String> seatsMaterial;
    //Map<String, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatsMaterial
    public UberVan(String license, Account driver){
        super(license, driver);
        // this.typeCarAccepted = typeCarAccepted;
        // this.seatsMaterial = seatsMaterial;
    }

    @Override
    public void setPasajeros(int pasajeros) {
        if ( pasajeros == 6){
            this.pasajeros = pasajeros;
        } else {
            System.out.println("Deben ser 6");
        }
    }
}
