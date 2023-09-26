package AlgoritmosYProgramacion.TercerSemestre.Tetris;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;
import sun.audio.*;

import AlgoritmosYProgramacion.TercerSemestre.Tetris.Tetromino.Tetrominoes;

public class Funciones extends JPanel implements ActionListener {
    public static final int ALTO = 22, ANCHO = 10;

    private Timer tiempo;
    private boolean caida = false;
    private boolean iniciado = false;
    private boolean pausado = false;
    private int puntuacionActual;
    private int actX = 0;
    private int actY = 0;
    private Tetromino figuraActual;
    private Tetrominoes[] tablero;
    private Color[] paletaColores;
    private String estatusActual;
    private String nivelActual;
    private int velocidadActual;
    private AudioStream audio;

    public Funciones(int timerResolution){
        setFocusable(true);
        musica();
        setBackground(new Color(30, 0, 30));
        figuraActual = new Tetromino();
        tiempo = new Timer(timerResolution, this);
        tiempo.start();
        velocidadActual = timerResolution;

        tablero = new Tetrominoes[ANCHO * ALTO];

        paletaColores = new Color[]{
            new Color(0, 0, 0), Color.RED,
            Color.GREEN, Color.CYAN,
            Color.MAGENTA, Color.YELLOW,
            Color.ORANGE, Color.BLUE};
    
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (!iniciado || figuraActual.getFigura() == Tetrominoes.VACIO) {
                    return;
                }

                int keycode = e.getKeyCode();

                if (keycode == 'p' || keycode == 'P') {
                    pausa();
                    return;
                }

                if (pausado) {
                    return;
                }

                switch (keycode) {
                    case 'a':
                    case 'A':
                    case KeyEvent.VK_LEFT:
                        movimiento(figuraActual, actX - 1, actY);
                        break;
                    case 'd':
                    case 'D':
                    case KeyEvent.VK_RIGHT:
                        movimiento(figuraActual, actX + 1, actY);
                        break;
                    case 'w':
                    case 'W':
                    case KeyEvent.VK_UP:
                        movimiento(figuraActual.rotateRight(), actX, actY);
                        break;
                    case 's':
                    case 'S':
                    case KeyEvent.VK_DOWN:
                        advanceOneLine();
                        break;
                    case KeyEvent.VK_SPACE:
                        hastaElFondo();
                        
                        break;
                    case 'p':
                    case 'P':
                        pausa();
                        break;
                }

            }
        });
        initBoard();
    }

    private void setDificultad() {
        if (puntuacionActual / 10 == 10) {
            velocidadActual = 100;
        } else if (puntuacionActual / 10 == 9) {
            velocidadActual = 130;
        } else if (puntuacionActual / 10 == 8) {
            velocidadActual = 160;
        } else if (puntuacionActual / 10 == 7) {
            velocidadActual = 190;
        } else if (puntuacionActual / 10 == 6) {
            velocidadActual = 220;
        } else if (puntuacionActual / 10 == 5) {
            velocidadActual = 250;
        } else if (puntuacionActual / 10 == 4) {
            velocidadActual = 280;
        } else if (puntuacionActual / 10 == 3) {
            velocidadActual = 310;
        } else if (puntuacionActual / 10 == 2) {
            velocidadActual = 340;
        } else if (puntuacionActual / 10 == 1) {
            velocidadActual = 370;
        } else {
            velocidadActual = 370;
        }

        tiempo.setDelay(velocidadActual);

    }

    private void initBoard() {
        for (int i = 0; i < ANCHO * ALTO; i++) {
            tablero[i] = Tetrominoes.VACIO;
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (caida) {
            caida = !caida;
            nuevaPieza();
        } else {
            advanceOneLine();
        }
    }

    public void musica() {
        try {
            String sonido = "D:/programacion/Github/ProApren/AlgoritmosYProgramacion/TercerSemestre/Tetris/song.wav";
            InputStream in = new FileInputStream(sonido);
            audio = new AudioStream(in);
            
        } catch (Exception e) {
            // TODO: handle exception
        }
    }

    public void inicio() {
        if (pausado) {
            return;
        }
        iniciado = true;
        caida = false;
        puntuacionActual = 0;
        initBoard();
        AudioPlayer.player.start(audio);
        nuevaPieza();
        tiempo.start();
    }

    public void pausa() {
        if (!iniciado) {
            return;
        }

        pausado = !pausado;
        if (pausado) {
            tiempo.stop();
            AudioPlayer.player.stop(audio);
        } else {
            tiempo.start();
            AudioPlayer.player.start(audio);
        }

        repaint();
    }

    private int anchoBloque() {
        return (int) getSize().getWidth() / ANCHO;
    }

    private int altoBloque() {
        return (int) getSize().getHeight() / ALTO;
    }

    Tetrominoes posActTetromino(int x, int y) {
        return tablero[(y * ANCHO) + x];
    }

    @Override
    public void paint(Graphics g) {

        super.paint(g);

        if (!pausado) {
            estatusActual = "Puntuacion: " + puntuacionActual;
            nivelActual = "Nivel: " + (puntuacionActual / 10 + 1);
        } else {
            estatusActual = "PAUSA";
            nivelActual = "";
        }

        g.setColor(Color.WHITE);
        g.setFont(new Font("Consolas", Font.PLAIN, 28));
        g.drawString(estatusActual, 15, 35);
        g.drawString(nivelActual, 15, 70);

        Dimension size = getSize();
        int boardTop = (int) size.getHeight() - ALTO * altoBloque();

        int tempY = actY;
        while (tempY > 0) {
            if (!movimientoValido(figuraActual, actX, tempY - 1, false))
                break;
            tempY--;
        }
        for (int i = 0; i < 4; i++) {
            int x = actX + figuraActual.getX(i);
            int y = tempY - figuraActual.getY(i);
            colocaTetromino(g, 0 + x * anchoBloque(), boardTop + (ALTO - y - 1) * altoBloque(), figuraActual.getFigura(),
                    true);
        }

        for (int i = 0; i < ALTO; i++) {
            for (int j = 0; j < ANCHO; j++) {
                Tetrominoes shape = posActTetromino(j, ALTO - i - 1);
                if (shape != Tetrominoes.VACIO)
                    colocaTetromino(g, 0 + j * anchoBloque(), boardTop + i * altoBloque(), shape, false);
            }
        }
        if (figuraActual.getFigura() != Tetrominoes.VACIO) {
            for (int i = 0; i < 4; i++) {
                int x = actX + figuraActual.getX(i);
                int y = actY - figuraActual.getY(i);
                colocaTetromino(g, 0 + x * anchoBloque(), boardTop + (ALTO - y - 1) * altoBloque(),
                        figuraActual.getFigura(), false);
            }
        }
    }

    private void colocaTetromino(Graphics g, int x, int y, Tetrominoes bs, boolean sombra) {
        Color curColor = paletaColores[bs.ordinal()];

        if (!sombra) {
            g.setColor(curColor);
            g.fillRect(x + 1, y + 1, anchoBloque() - 2, altoBloque() - 2);
        } else {
            g.setColor(curColor.darker().darker());
            g.fillRect(x + 1, y + 1, anchoBloque() - 2, altoBloque() - 2);
        }
    }

    private void completarFila() {
        int fullLines = 0;

        for (int i = ALTO - 1; i >= 0; i--) {
            boolean completo = true;

            for (int j = 0; j < ANCHO; j++) {
                if (posActTetromino(j, i) == Tetrominoes.VACIO) {
                    completo = false;
                    break;
                }
            }

            if (completo) {
                ++fullLines;
                for (int k = i; k < ALTO - 1; k++) {
                    for (int l = 0; l < ANCHO; ++l)
                        tablero[(k * ANCHO) + l] = posActTetromino(l, k + 1);
                }
            }
        }

        if (fullLines > 0) {
            puntuacionActual += fullLines;
            caida = true;
            figuraActual.setFigura(Tetrominoes.VACIO);
            setDificultad();
            repaint();
        }

    }

    private boolean movimientoValido(Tetromino chkBlock, int chkX, int chkY, boolean flag) {
        for (int i = 0; i < 4; i++) {
            int x = chkX + chkBlock.getX(i);
            int y = chkY - chkBlock.getY(i);
            if (x < 0 || x >= ANCHO || y < 0 || y >= ALTO)
                return false;
            if (posActTetromino(x, y) != Tetrominoes.VACIO) {
                return false;
            }
        }

        if (flag) {
            figuraActual = chkBlock;
            actX = chkX;
            actY = chkY;
            repaint();
        }

        return true;
    }

    private boolean movimiento(Tetromino revFig, int revX, int revY) {
        return movimientoValido(revFig, revX, revY, true);
    }

    private void nuevaPieza() {
        figuraActual.setRandomFigura();
        actX = ANCHO / 2 + 1;
        actY = ALTO - 1 + figuraActual.minY();

        if (!movimiento(figuraActual, actX, actY)) {
            figuraActual.setFigura(Tetrominoes.VACIO);
            tiempo.stop();
            iniciado = false;
            GameOver(puntuacionActual);
        }
    }

    private void tetrominoColocado() {
        for (int i = 0; i < 4; i++) {
            int x = actX + figuraActual.getX(i);
            int y = actY - figuraActual.getY(i);
            tablero[(y * ANCHO) + x] = figuraActual.getFigura();
        }

        completarFila();

        if (!caida) {
            nuevaPieza();
        }
    }

    private void advanceOneLine() {
        if (!movimiento(figuraActual, actX, actY - 1)) {
            tetrominoColocado();
        }
    }

    private void hastaElFondo() {
        int tempY = actY;
        while (tempY > 0) {
            if (!movimiento(figuraActual, actX, tempY - 1))
                break;
            --tempY;
        }
        tetrominoColocado();
    }

    private void GameOver(int tbpuntos) {
        int maxpuntos = readTB();
        String showD = "";
        if (tbpuntos > maxpuntos) {
            writeTB(tbpuntos);
            showD = String.format("%nFELICIDADES! %nNuevo Record: %d", tbpuntos);
        } else {
            showD = String.format("Puntuacion: %d %nMaxima Puntuacion: %d", tbpuntos, maxpuntos);
        }
        UIManager.put("OptionPane.okButtonText", "Nuevo Juego");
        JOptionPane.showMessageDialog(null, showD, "Game Over!", JOptionPane.OK_OPTION);
        setDificultad();
        inicio();
    }

    private int readTB() {
        try {
            BufferedReader input = new BufferedReader(new FileReader("Tetris.score"));
            String tbMaxScore = input.readLine();
            input.close();
            return Integer.parseInt(tbMaxScore);
        } catch (IOException e) {
            return -1;
        } catch (NumberFormatException e) {
            return -1;
        }
    }

    private void writeTB(int tbScore) {
        try {
            File UIFile = new File("Tetris.score");
            if (!UIFile.exists()) {
                UIFile.createNewFile();
            }
            FileWriter filewriter = new FileWriter(UIFile.getAbsoluteFile());
            BufferedWriter outputStream = new BufferedWriter(filewriter);
            outputStream.write(String.valueOf(tbScore));
            outputStream.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
