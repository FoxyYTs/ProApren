package Hilos;

public class hiloAbecedario extends Thread {

    hiloVentan ventana;
    private final String abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public hiloAbecedario(hiloVentan ventana) {
        this.ventana = ventana;
    }

    public void run() {
        try {
            while (true) {
                for (int i = 0; i < abecedario.length(); i++) {
                    ventana.jLabel4.setText(
                            "Letra: " + abecedario.charAt(i)
                    );
                    Thread.sleep(500);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}