public class MultiHilo {
    public static void main(String[] args) {
        // Crear el primer Hilo
        Thread hilo1 = new Thread(() -> {
            System.out.println("Iniciando Tarea 1...");
            hacerTrabajo(2000);
            System.out.println("Finalizando Tarea 1...");
        });
        // Crear el segundo Hilo
        Thread hilo2 = new Thread(() -> {
            System.out.println("Iniciando Tarea 2...");
            hacerTrabajo(1000);
            System.out.println("Finalizando Tarea 2...");
        });
        //.start() Lanza los hilos en paralelo
        hilo1.run();
        hilo2.run();
        System.out.println("El hilo principal sigue funcionando mientras los hilos 1 y 2 siguen corriendo...");
    }

        private static void hacerTrabajo(int i) {
        try{
            Thread.sleep(i);
        } catch(InterruptedException e){
            e.printStackTrace();
            System.out.println("Error");
        }
    }

}
