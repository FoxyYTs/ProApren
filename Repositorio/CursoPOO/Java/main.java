package Repositorio.CursoPOO.Java;

public class Main {
    public static void main(String[] args) {

        try {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        } catch (Exception e){

        }
        
        Car car = new Car("QWE123", new Account("Foxy", "Fox","foxy@gmail.com","1234"));
        car.passegenger = 4;
        car.printDataCar();

        Car car2 = new Car("PEP023", new Account("Freddy","Bear","freddy@gmail.com","1234"));
        car2.passegenger = 4;
        car2.printDataCar();
        
    }
}