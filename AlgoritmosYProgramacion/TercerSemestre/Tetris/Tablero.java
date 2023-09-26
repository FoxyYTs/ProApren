package AlgoritmosYProgramacion.TercerSemestre.Tetris;

import java.awt.*;

import javax.swing.*;

public class Tablero {

    private JFrame ventana = new JFrame("Tetris");
    int x = 0;
    public Tablero(){
        ventana.setSize(500, 1000);

        Funciones tablero = new Funciones(400);
        while (x < 3) {
            ventana.add(tablero);
            x++;
        }
        tablero.inicio();
        
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setResizable(false);
        ventana.setVisible(true);
    }
}
