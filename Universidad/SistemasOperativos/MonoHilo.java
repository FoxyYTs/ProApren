public class MonoHilo {
    public static void main(String[] args) {
        System.out.print("Iniciando Tarea 1...");
        hacerTrabajo(2000);
        System.out.print("Finalizando Tarea 1...");

        System.out.print("Iniciando Tarea 2...");
        hacerTrabajo(1000);
        System.out.print("Finalizando Tarea 2...");
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
