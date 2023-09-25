package AlgoritmosYProgramacion.TercerSemestre.TetrisPru;

import java.awt.*;

import javax.swing.*;

public class Interfaz extends JFrame{

    public Interfaz(){
        setTitle("Tetris :D");
        setSize(400, 814);
        setResizable(true);

        setLayout(new GridLayout(1, 2));

        Funciones tablero = new Funciones(400);
        add(tablero);
        tablero.start();

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setVisible(true);
    }
    
}
