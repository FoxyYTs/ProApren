package Hilos;

import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.GridLayout;

public class hiloVentan extends JFrame {

    public JLabel jLabel1;
    public JLabel jLabel2;
    public JLabel jLabel3;
    public JLabel jLabel4;

    public hiloVentan() {
        initComponents();
    }

    private void initComponents() {
        setTitle("Práctica de Hilos");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridLayout(3, 1));

        jLabel1 = new JLabel("Hora", JLabel.CENTER);
        jLabel2 = new JLabel("Minutos", JLabel.CENTER);
        jLabel3 = new JLabel("Segundos", JLabel.CENTER);
        jLabel4 = new JLabel("Abecedario", JLabel.CENTER);

        add(jLabel1);
        add(jLabel2);
        add(jLabel3);
        add(jLabel4);

        setVisible(true);
    }
}
