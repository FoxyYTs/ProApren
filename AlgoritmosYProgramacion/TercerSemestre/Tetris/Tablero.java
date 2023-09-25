package AlgoritmosYProgramacion.TercerSemestre.Tetris;

import java.awt.*;

import javax.swing.*;

public class Tablero {

    private JFrame ventana = new JFrame("Tetris");
    
    public Tablero(){
        ventana.setSize(500, 1000);

        Funciones tablero = new Funciones(400);
        ventana.add(tablero);
        tablero.inicio();
        
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setResizable(false);
        ventana.setVisible(true);
    }
}
