package AlgoritmosYProgramacion.TercerSemestre.Tetris;


import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Main {
    public static void main(String[] args) {
        KeyAdapter keyAdapter = new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                char keyChar = e.getKeyChar();
                int keyCode = e.getKeyCode();

                System.out.println("Tecla presionada: " + keyChar);
                System.out.println("Código de tecla: " + keyCode);
            }
        };

        System.out.println("Presiona una tecla (Presiona Ctrl+C para salir)");

        // Agregar el KeyAdapter al sistema
        System.in.addKeyListener(keyAdapter);

        // Mantener el programa en ejecución
        try {
            System.in.read();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

