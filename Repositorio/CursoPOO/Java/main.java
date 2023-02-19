package Repositorio.CursoPOO.Java;

public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.license = "QWE123";
        car.driver = "Foxy";
        car.passegenger = 4;
        System.out.println("Placa: " + car.license);
    }
}