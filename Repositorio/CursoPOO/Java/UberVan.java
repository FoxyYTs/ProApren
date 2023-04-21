package Repositorio.CursoPOO.Java;


import java.util.*;

public class UberVan extends Car{
    private Map<String, Map<String, Integer>> typeCarAccepted;
    private ArrayList<String> seatsMaterial;
    public UberVan(String license, Account driver, Map<String, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatsMaterial){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }

    @Override
    public void setPasajeros(int pasajeros) {
        if ( pasajeros == 6){
            this.pasajeros = pasajeros;
        } else {
            System.out.println("Deben ser 6");
        }
    }

    public Map<String, Map<String, Integer>> getTypeCarAccepted() {
        return typeCarAccepted;
    }

    public void setTypeCarAccepted(Map<String, Map<String, Integer>> typeCarAccepted) {
        this.typeCarAccepted = typeCarAccepted;
    }

    public ArrayList<String> getSeatsMaterial() {
        return seatsMaterial;
    }

    public void setSeatsMaterial(ArrayList<String> seatsMaterial) {
        this.seatsMaterial = seatsMaterial;
    }

    
}
