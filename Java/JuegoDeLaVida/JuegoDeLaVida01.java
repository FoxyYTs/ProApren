package Java.JuegoDeLaVida;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class JuegoDeLaVida01 extends JPanel implements ActionListener {
    private int tamañoCelula = 20;
    private int filas;
    private int columnas;
    private boolean[][] celulas;
    private Timer timer;

    public JuegoDeLaVida01(int filas, int columnas) {
        this.filas = filas;
        this.columnas = columnas;
        celulas = new boolean[filas][columnas];
        
        // Inicializar el estado del juego de la vida

        // Configurar el temporizador para actualizar el juego
        timer = new Timer(100, this);
        timer.start();
    }

    public void actionPerformed(ActionEvent e) {
        // Actualizar el estado del juego
        actualizarEstado();
        repaint();
    }

    private void actualizarEstado() {
        // Lógica para actualizar el estado del juego de la vida
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        
        // Dibujar las celdas en el panel
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (celulas[i][j]) {
                    g.setColor(Color.BLACK);
                } else {
                    g.setColor(Color.WHITE);
                }
                g.fillRect(j * tamañoCelula, i * tamañoCelula, tamañoCelula, tamañoCelula);
                g.setColor(Color.GRAY);
                g.drawRect(j * tamañoCelula, i * tamañoCelula, tamañoCelula, tamañoCelula);
            }
        }
    }

    @Override
    public Dimension getPreferredSize() {
        return new Dimension(columnas * tamañoCelula, filas * tamañoCelula);
    }

    public static void main(String[] args) {
        int filas = 50;
        int columnas = 75;
        
        JFrame frame = new JFrame("Juego de la Vida");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JuegoDeLaVida01 juegoDeLaVida = new JuegoDeLaVida01(filas, columnas);
        frame.add(juegoDeLaVida);
        
        frame.pack();
        frame.setVisible(true);
    }
}
