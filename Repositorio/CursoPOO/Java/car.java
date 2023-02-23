package Repositorio.CursoPOO.Java;

public class Car {
    Integer id;
    String license;
    Account driver;
    private Integer passegenger;

    public Car(String license, Account driver){
        this.license = license;
        this.driver = driver;   
    }

    
    void printDataCar(){
        System.out.println("\nID: " + id + "\nLicense: " + license + "\nNombre Conductor: " + driver.name + "\nPasajeros: " + passegenger);
    }

    public Integer getPassenger(){
        return passegenger;
    }

    public void setPassenger(Integer passenger){
        if(passenger == 4){
            this.passegenger = passenger;
        }else{
            System.out.println("Necesitas 4 pasajeros");
        }
    }
}
