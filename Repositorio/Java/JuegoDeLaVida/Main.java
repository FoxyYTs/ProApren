package Repositorio.Java.JuegoDeLaVida;

import javax.swing.JFrame;

public class Main {
    public static void main(String[] args) {

        JFrame ventana = new JFrame("Juego de La Vida");

        ventana.setSize(1000, 1000);


        ventana.setVisible(true);

        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
