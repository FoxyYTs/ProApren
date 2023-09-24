package AlgoritmosYProgramacion.TercerSemestre.Tetris;

import java.awt.*;

import javax.swing.*;

public class Tablero {

    private JFrame ventana = new JFrame("Tetris");
    
    public Tablero(){
        ventana.setSize(500, 1000);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setResizable(false);
        ventana.setVisible(true);
    }
}
