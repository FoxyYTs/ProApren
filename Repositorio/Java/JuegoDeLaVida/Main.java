package Repositorio.Java.JuegoDeLaVida;

import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        int filas = 50;
        int columnas = 50;
        
        JFrame frame = new JFrame("Juego de la Vida");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JuegoDeLaVida02 juegoDeLaVida = new JuegoDeLaVida02(filas, columnas);
        frame.add(juegoDeLaVida);
        
        frame.pack();
        frame.setVisible(true);
    }
}

