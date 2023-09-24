package AlgoritmosYProgramacion.TercerSemestre.Tetris;

import javax.swing.BorderFactory;
import javax.swing.JPanel;

import javafx.scene.paint.Color;



public class Funciones {
    
    public static final int ALTO = 20, ANCHO = 10;
    
    JPanel[][] juego = new JPanel[ALTO][ANCHO];
        for(int i = 0; i < ALTO; i++){
            for(int j = 0; j < ANCHO; j++){
                juego[i][j] = new JPanel();
                juego[i][j].setBorder(BorderFactory.createLineBorder(new Color(0, 30, 30)));
                juego[i][j].setBackground(new Color(30, 0, 30));
                juego[i][j].setPreferredSize(new Dimension(50, 50));
            }
        }
        
        for(JPanel[] fila: juego){
            for(JPanel panel: fila){
                ventana.add(panel);
            }
        }
}
