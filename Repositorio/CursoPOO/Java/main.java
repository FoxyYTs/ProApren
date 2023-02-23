package Repositorio.CursoPOO.Java;

public class Main {
    public static void main(String[] args) {

        try {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        } catch (Exception e){

        }
        System.out.println("Carro");
        Car car = new Car("QWE123", new Account("Foxy", "Fox","foxy@gmail.com","1234"));  
        car.setPassenger(4);
        car.printDataCar();

        System.out.print("UberX");
        UberX uberx = new UberX("PEP023", new Account("Freddy","Bear","freddy@gmail.com","1234"),"Toyota","Corolla");
        uberx.setPassenger(4); 
        uberx.printDataCar();
        
    }
}   