package CursoPOO.Java;

public class Main {
    public static void main(String[] args) {
        System.out.print("\033[H\033[2J");
        UberX car = new UberX("XMS532", new Account("Pedro", "12345", "pedro@gmail.com", "pass"), "Carro", "Mamalon" );
        car.setPasajeros(4);
        car.dataCar();

        UberVan uber = new UberVan("FKY", new Account("Fernando", "54321", "fer@gmail.com", "pass2"));
        uber.setPasajeros(6);
        uber.dataCar();
    }
}
