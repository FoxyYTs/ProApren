package Repositorio.CursoPOO.Java;

public class Car {
    private String placa;
    private Account conductor;
    protected int pasajeros;

    public Car(String placa, Account conductor){
        this.placa = placa;
        this.conductor = conductor;
    }
    
    public void dataCar(){
        System.out.println("Carro [Conductor: " + conductor.getNombre() + ", Placa: " + placa + ", Pasajeros: " + pasajeros + "]");
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public void setConductor(Account conductor) {
        this.conductor = conductor;
    }

    public void setPasajeros(int pasajeros) {
        if (pasajeros == 4){
            this.pasajeros = pasajeros;
        } else {
            System.out.println("Deben ser 4");
        }
    }

    public String getPlaca() {
        return placa;
    }

    public Account getConductor() {
        return conductor;
    }

    public int getPasajeros() {
        return pasajeros;
    }    
}
