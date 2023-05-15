package Repositorio.Java;

import javax.swing.*;

public class VentanaHolaMundo {
    public static void main(String[] args) {
        // Crear una instancia de JFrame
        JFrame ventana = new JFrame("PERRRRRROOOOOOO");

        // Crear una instancia de JLabel con el texto "Hola Mundo"
        JLabel etiqueta = new JLabel("Hola Mundo");

        // Agregar el JLabel a la ventana
        ventana.add(etiqueta);

        // Configurar el tamaño de la ventana
        ventana.setSize(300, 100);

        // Hacer que la ventana sea visible
        ventana.setVisible(true);

        // Configurar la acción al cerrar la ventana
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
