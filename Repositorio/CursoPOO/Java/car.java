package Repositorio.CursoPOO.Java;

public class Car {
    private Integer id;
    private String license;
    private Account driver;
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

    public Integer getId() {
        return id;
    }


    public void setId(Integer id) {
        this.id = id;
    }


    public String getLicense() {
        return license;
    }


    public void setLicense(String license) {
        this.license = license;
    }


    public Account getDriver() {
        return driver;
    }


    public void setDriver(Account driver) {
        this.driver = driver;
    }
        
}
