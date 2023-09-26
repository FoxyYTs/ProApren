package AlgoritmosYProgramacion.TercerSemestre.Tetris;

import java.awt.*;

import javax.swing.*;

public class Tablero {

    private JFrame ventana = new JFrame("Tetris");
    public Tablero(){
        ventana.setSize(1000, 1000);
        

        ventana.setLayout(new GridLayout(1, 2));

        Prueba prueba = new Prueba();
        Funciones tablero = new Funciones(400);
        
        ventana.add(tablero);
        
        ventana.add(prueba);

        tablero.inicio();
        
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setResizable(false);
        ventana.setLocationRelativeTo(null);
        ventana.setVisible(true);
    }

}
