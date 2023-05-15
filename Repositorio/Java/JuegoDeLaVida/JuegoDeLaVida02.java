package Repositorio.Java.JuegoDeLaVida;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class JuegoDeLaVida02 extends JPanel {
    private static final int CELDA_TAMANIO = 10;
    private static final int FILAS = 50;
    private static final int COLUMNAS = 50;
    private boolean[][] celulas;
    private boolean juegoIniciado;

    public JuegoDeLaVida02() {
        celulas = new boolean[FILAS][COLUMNAS];
        juegoIniciado = false;

        setPreferredSize(new Dimension(COLUMNAS * CELDA_TAMANIO, FILAS * CELDA_TAMANIO));

        MouseAdapter mouseAdapter = new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (!juegoIniciado) {
                    int fila = e.getY() / CELDA_TAMANIO;
                    int columna = e.getX() / CELDA_TAMANIO;

                    celulas[fila][columna] = !celulas[fila][columna];
                    repaint();
                }
            }

            @Override
            public void mouseDragged(MouseEvent e) {
                if (!juegoIniciado) {
                    int fila = e.getY() / CELDA_TAMANIO;
                    int columna = e.getX() / CELDA_TAMANIO;

                    celulas[fila][columna] = true;
                    repaint();
                }
            }
        };

        addMouseListener(mouseAdapter);
        addMouseMotionListener(mouseAdapter);
    }

    public void iniciarJuego() {
        juegoIniciado = true;
        while (juegoIniciado) {
            actualizarEstado();
            repaint();
            try {
                Thread.sleep(500); // Ajusta la velocidad del juego aquí (en milisegundos)
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private void actualizarEstado() {
        boolean[][] nuevoEstado = new boolean[FILAS][COLUMNAS];

        for (int fila = 0; fila < FILAS; fila++) {
            for (int columna = 0; columna < COLUMNAS; columna++) {
                int vecinosVivos = contarVecinosVivos(fila, columna);

                if (celulas[fila][columna]) {
                    // Regla 1: Una célula viva con menos de 2 vecinos vivos muere (subpoblación)
                    if (vecinosVivos < 2) {
                        nuevoEstado[fila][columna] = false;
                    }
                    // Regla 2: Una célula viva con 2 o 3 vecinos vivos sobrevive
                    else if (vecinosVivos == 2 || vecinosVivos == 3) {
                        nuevoEstado[fila][columna] = true;
                    }
                    // Regla 3: Una célula viva con más de 3 vecinos vivos muere (sobrepoblación)
                    else if (vecinosVivos > 3) {
                        nuevoEstado[fila][columna] = false;
                    }
                } else {
                    // Regla 4: Una célula muerta con exactamente 3 vecinos vivos se convierte en una célula viva (reproducción)
                    if (vecinosVivos == 3) {
                        nuevoEstado[fila][columna] = true;
                    }
                }
            }
        }

        celulas = nuevoEstado;
    }

    private int contarVecinosVivos(int fila, int columna) {
        int contador = 0;

        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                if (i == 0 && j == 0) {
                    continue; // Saltar la celda actual
                }

                int vecinaFila = fila + i;
                int vecinaColumna = columna + j;

                if (vecinaFila >= 0 && vecinaFila < FILAS && vecinaColumna >= 0 && vecinaColumna < COLUMNAS) {
                    if (celulas[vecinaFila][vecinaColumna]) {
                        contador++;
                    }
                }
            }
        }

        return contador;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        for (int fila = 0; fila < FILAS; fila++) {
            for (int columna = 0; columna < COLUMNAS; columna++) {
                if (celulas[fila][columna]) {
                    g.setColor(Color.BLACK);
                } else {
                    g.setColor(Color.WHITE);
                }

                g.fillRect(columna * CELDA_TAMANIO, fila * CELDA_TAMANIO, CELDA_TAMANIO, CELDA_TAMANIO);
                g.setColor(Color.GRAY);
                g.drawRect(columna * CELDA_TAMANIO, fila * CELDA_TAMANIO, CELDA_TAMANIO, CELDA_TAMANIO);
            }
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Juego de la Vida");
        JuegoDeLaVida02 juegoDeLaVida = new JuegoDeLaVida02();
        frame.add(juegoDeLaVida);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);

        juegoDeLaVida.iniciarJuego();
    }
}

