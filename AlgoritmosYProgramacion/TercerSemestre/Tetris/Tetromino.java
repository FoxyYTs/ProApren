package AlgoritmosYProgramacion.TercerSemestre.Tetris;
import java.util.Random;

public class Tetromino {
    enum Tetrominoes {
        VACIO, Z_FIGURA, S_FIGURA, I_FIGURA, T_FIGURA, O_FIGURA, L_FIGURA, J_FIGURA
    };

    private Tetrominoes tetrominoes;
    private int coords[][];                
    private int tablaTetrominoes[][][];

    public Tetromino() {
        coords = new int[4][2];
        tablaTetrominoes = new int[][][]{
                {{0, 0}, {0, 0}, {0, 0}, {0, 0}},        // VACIO
                {{0, -1}, {0, 0}, {-1, 0}, {-1, 1}},    // Z_FIGURA
                {{0, -1}, {0, 0}, {1, 0}, {1, 1}},    // S_FIGURA
                {{0, -1}, {0, 0}, {0, 1}, {0, 2}},    // I_FIGURA
                {{-1, 0}, {0, 0}, {1, 0}, {0, 1}},    // T_FIGURA
                {{0, 0}, {1, 0}, {0, 1}, {1, 1}},    // O_FIGURA
                {{-1, -1}, {0, -1}, {0, 0}, {0, 1}},    // L_FIGURA
                {{1, -1}, {0, -1}, {0, 0}, {0, 1}}    // J_FIGURA
        };

        setFigura(Tetrominoes.VACIO);
    }
    public void setFigura(Tetrominoes tetromino) {

        for (int i = 0; i < coords.length; i++) {
            for (int j = 0; j < coords[i].length; j++) {
                coords[i][j] = tablaTetrominoes[tetromino.ordinal()][i][j];
            }
        }

        tetrominoes = tetromino;
    }

    public void setRandomFigura() {
        Random r = new Random();
        int x = Math.abs(r.nextInt()) % 7 + 1;
        setFigura(Tetrominoes.values()[x]);
    }

    public Tetrominoes getFigura() {
        return tetrominoes;
    }

    // coordinate transform functions
    public void setX(int idx, int x) {
        coords[idx][0] = x;
    }

    public void setY(int idx, int y) {
        coords[idx][1] = y;
    }

    public int getX(int idx) {
        return coords[idx][0];
    }

    public int getY(int idx) {
        return coords[idx][1];
    }

    public int minX() {
        int ret = 0;
        for (int i = 0; i < coords.length; i++) {
            ret = Math.min(ret, coords[i][0]);
        }
        return ret;
    }

    public int minY() {
        int ret = 0;
        for (int i = 0; i < coords.length; i++) {
            ret = Math.min(ret, coords[i][1]);
        }
        return ret;
    }

    public Tetromino rotateLeft() {
        if (tetrominoes == Tetrominoes.O_FIGURA) {
            return this;
        }

        Tetromino ret = new Tetromino();
        ret.tetrominoes = tetrominoes;

        for (int i = 0; i < coords.length; i++) {
            ret.setX(i, getY(i));
            ret.setY(i, -getX(i));
        }

        return ret;
    }

    public Tetromino rotateRight() {
        if (tetrominoes == Tetrominoes.O_FIGURA) {
            return this;
        }

        Tetromino ret = new Tetromino();
        ret.tetrominoes = tetrominoes;

        for (int i = 0; i < coords.length; i++) {
            ret.setX(i, -getY(i));
            ret.setY(i, getX(i));
        }

        return ret;
    }
}
