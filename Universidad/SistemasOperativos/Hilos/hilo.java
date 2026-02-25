package Hilos;

public class hilo extends Thread {

    hiloVentan ventana;

    public hilo(hiloVentan ventana) {
        this.ventana = ventana;
    }

    public void run() {
        while (true) {
            try {
                for (int hora = 0; hora < 24; hora++) {
                    for (int min = 0; min < 60; min++) {
                        for (int seg = 0; seg < 60; seg++) {

                            ventana.jLabel1.setText("Hora: " + hora);
                            ventana.jLabel2.setText("Min: " + min);
                            ventana.jLabel3.setText("Seg: " + seg);

                            Thread.sleep(1000);
                        }
                    }
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}