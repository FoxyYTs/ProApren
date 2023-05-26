package Java.JuegoDeLaVida;

import java.util.Arrays;

public class JuegoDeLaVida03 {
    private int filas;
    private int columnas;
    private boolean[][] celulas;

    public JuegoDeLaVida03(int filas, int columnas) {
        this.filas = filas;
        this.columnas = columnas;
        celulas = new boolean[filas][columnas];
    }

    public void iniciarJuego() {
        // Configurar el estado inicial del juego
        configurarEstadoInicial();

        // Ejecutar el juego
        while (true) {
            imprimirEstado();
            actualizarEstado();
            esperar(1000); // Ajusta la velocidad del juego aquí (en milisegundos)
            limpiarConsola();
        }
    }

    private void configurarEstadoInicial() {
        // Configurar el estado inicial del juego según tus preferencias
        // Aquí se muestra un ejemplo con algunas células vivas

        celulas[2][3] = true;
        celulas[3][3] = true;
        celulas[4][3] = true;
    }

    private void imprimirEstado() {
        for (int fila = 0; fila < filas; fila++) {
            for (int columna = 0; columna < columnas; columna++) {
                if (celulas[fila][columna]) {
                    System.out.print("█ ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }

    private void actualizarEstado() {
        boolean[][] nuevoEstado = new boolean[filas][columnas];

        for (int fila = 0; fila < filas; fila++) {
            for (int columna = 0; columna < columnas; columna++) {
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

                // Comprobar si la celda vecina está dentro de los límites del tablero
                if (vecinaFila >= 0 && vecinaFila < filas && vecinaColumna >= 0 && vecinaColumna < columnas) {
                    if (celulas[vecinaFila][vecinaColumna]) {
                        contador++;
                    }
                }
            }
        }

        return contador;
    }

    private void esperar(int milisegundos) {
        try {
            Thread.sleep(milisegundos);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void limpiarConsola() {
        try {
            final String os = System.getProperty("os.name");
            if (os.contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        JuegoDeLaVida03 juego = new JuegoDeLaVida03(9, 9);
        juego.iniciarJuego();
    }
}

