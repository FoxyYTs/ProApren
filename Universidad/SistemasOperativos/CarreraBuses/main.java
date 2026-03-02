package CarreraBuses;

public class main {
    public static void main(String[] args) {
        // Crear y mostrar la ventana en el hilo de eventos de Swing
        javax.swing.SwingUtilities.invokeLater(() -> {
            new ventana();
        });
    }
}