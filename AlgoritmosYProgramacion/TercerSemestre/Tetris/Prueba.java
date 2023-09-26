import java.io.File;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.Clip;
import javax.swing.*;
import java.awt.*;

public class Prueba extends JPanel {
    // Resto del código...

    private Tetromino siguienteTetromino;

    public Prueba(int timerResolution) {
        // Resto del código...

        siguienteTetromino = new Tetromino();
    }

    public void paint(Graphics g) {
        // Resto del código...

        // Dibujar el siguiente tetromino
        g.setColor(Color.BLACK);
        g.setFont(new Font("Consolas", Font.PLAIN, 18));
        g.drawString("Siguiente Tetromino:", 15, 120);
        siguienteTetromino.draw(g, 15, 150);
    }

    // Resto del código...

    public static void main(String[] args) {
        // Resto del código...

        JFrame frame = new JFrame("Tetris");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 600);
        frame.setLocationRelativeTo(null);

        Prueba tetris = new Prueba(500);
        frame.add(tetris);

        frame.setVisible(true);
    }
}