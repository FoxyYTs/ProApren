package AlgoritmosYProgramacion.TercerSemestre.TetrisPru;

import javax.swing.JFrame;
import java.awt.GridLayout; 

public class Interfaz extends JFrame{

    public Interfaz(){
        setTitle("Tetris :D");
        setSize(400, 814);
        setResizable(true);

        setLayout(new GridLayout(1, 2));

        Funciones gameBoard = new Funciones(this, 400);
        add(gameBoard);
        gameBoard.start();

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setVisible(true);
    }
    
}
