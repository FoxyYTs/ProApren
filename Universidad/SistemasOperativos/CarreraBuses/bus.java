package CarreraBuses;

import javax.swing.*;
import java.awt.*;

public class bus extends Thread {
    private String nombreBus;
    private int distanciaRecorrida = 0;
    private int posicion = 0;
    private JProgressBar barraProgreso;
    private JLabel labelBus;
    private JLabel labelPosicion;
    private JLabel imagenBus;
    private boolean carreraActiva = true;
    private GanadorListener listener;
    private static final Object lock = new Object();
    private static boolean hayGanador = false;
    
    public bus(String nombre, JProgressBar barra, JLabel label, JLabel labelPos,
            JLabel imagen, GanadorListener listener) {
        this.nombreBus = nombre;
        this.barraProgreso = barra;
        this.labelBus = label;
        this.labelPosicion = labelPos;
        this.imagenBus = imagen;
        this.listener = listener;
    }
    
    @Override
    public void run() {
        while (carreraActiva && distanciaRecorrida < 100) {
            try {
                int avance = (int)(Math.random() * 10) + 1;
                distanciaRecorrida = Math.min(distanciaRecorrida + avance, 100);

                final int progreso = distanciaRecorrida;
                SwingUtilities.invokeLater(() -> {
                    barraProgreso.setValue(progreso);
                    labelBus.setText(nombreBus + ": " + progreso + " km");
                    int movimiento = (progreso * 400) / 100;
                    imagenBus.setLocation(10 + movimiento, imagenBus.getY());
                });

                if (distanciaRecorrida >= 100) {
                    synchronized (lock) {
                        if (!hayGanador) {
                            hayGanador = true;
                            carreraActiva = false;
                            listener.hayGanador(nombreBus);
                        }
                    }
                    break;
                }

                Thread.sleep((long)(Math.random() * 400) + 100);

            } catch (InterruptedException e) {
                return;
            }
        }
    }
    
    public void detenerCarrera() {
        carreraActiva = false;
    }
    
    public static void reiniciarGanador() {
        hayGanador = false;
    }
    
    public int getDistanciaRecorrida() {
        return distanciaRecorrida;
    }
    
    public void setPosicion(int posicion) {
        this.posicion = posicion;
        SwingUtilities.invokeLater(() -> {
            labelPosicion.setText("#" + posicion);
            // Cambiar color según la posición
            switch(posicion) {
                case 1:
                    labelPosicion.setForeground(new Color(255, 215, 0)); // Oro
                    break;
                case 2:
                    labelPosicion.setForeground(new Color(192, 192, 192)); // Plata
                    break;
                case 3:
                    labelPosicion.setForeground(new Color(205, 127, 50)); // Bronce
                    break;
                default:
                    labelPosicion.setForeground(Color.GRAY);
            }
        });
    }
    
    public String getNombreBus() {
        return nombreBus;
    }
}