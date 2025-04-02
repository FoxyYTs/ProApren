import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTextPane;

public class AbrirArchivoTexto extends JFrame implements ActionListener {

    private JTextPane txp;
    private JFileChooser abrirArchivo;

    public AbrirArchivoTexto() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        txp = new JTextPane();
        JScrollPane jsp = new JScrollPane(txp);
        add(jsp, BorderLayout.CENTER);

        JButton btn = new JButton("Abrir");
        btn.addActionListener(this);
        add(btn, BorderLayout.NORTH);

        setSize(500, 500);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() instanceof JButton && ((JButton) e.getSource()).getText().equals("Abrir")) {
            if (abrirArchivo == null) {
                abrirArchivo = new JFileChooser();
                abrirArchivo.setFileSelectionMode(JFileChooser.FILES_ONLY);
            }

            if (abrirArchivo.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
                File f = abrirArchivo.getSelectedFile();
                try {
                    String nombre = f.getName();
                    String contenido = getArchivo(f.getAbsolutePath());
                    this.setTitle(nombre);
                    txp.setText(contenido);
                } catch (Exception ex) {
                    txp.setText("Error al leer el archivo: " + ex.getMessage());
                }
            }
        }
    }

    public String getArchivo(String ruta) {
        StringBuilder contenido = new StringBuilder();
        boolean inicioEncontrado = false;
        boolean finEncontrado = false;

        try (BufferedReader br = new BufferedReader(new FileReader(ruta))) {
            String linea;
            int numLinea = 0;

            while ((linea = br.readLine()) != null) {
                contenido.append(linea).append("\n");
                numLinea++;

                if (numLinea == 1) {
                    if (!linea.trim().startsWith("programa ")) {
                        contenido.append("Error: La primera línea debe comenzar con 'programa' seguido de un identificador válido\n");
                    } else {
                        String[] partes = linea.trim().split("\\s+");
                        if (partes.length < 2 || !esIdentificadorValido(partes[1])) {
                            contenido.append("Error: El identificador después de 'programa' debe comenzar con una letra y no contener números ni símbolos\n");
                        }
                    }
                } else if (numLinea > 1 && linea.trim().startsWith("programa")) {
                    contenido.append("Error: La palabra 'programa' solo puede aparecer en la primera línea\n");
                }

                if (!linea.trim().isEmpty()) {
                    String primeraPalabra = obtenerPrimeraPalabra(linea);
                    if (primeraPalabra.equals("inicio")) {
                        inicioEncontrado = true;
                    }
                    if (primeraPalabra.equals("fin")) {
                        finEncontrado = true;
                    }
                    if (!esPalabraClave(primeraPalabra)) {
                        contenido.append("Error: La línea debe comenzar con una palabra clave (inicio, imprimir, leer, fin)\n");
                    }
                }

                String erroresLexicos = anaLex(linea);
                if (!erroresLexicos.isEmpty()) {
                    contenido.append(erroresLexicos).append("\n");
                }
            }

            if (!inicioEncontrado) {
                contenido.append("Error: La palabra 'inicio' no fue encontrada\n");
            }
            if (!finEncontrado) {
                contenido.append("Error: La palabra 'fin' no fue encontrada\n");
            }

        } catch (Exception e) {
            contenido.append("Error al leer el archivo: ").append(e.getMessage()).append("\n");
        }

        return contenido.toString();
    }

    public String anaLex(String lineas) {
        StringBuilder errores = new StringBuilder();
        char[] palabra = lineas.toCharArray();

        if (!lineas.trim().isEmpty()) {
            String primeraPalabra = obtenerPrimeraPalabra(lineas);
            if (!primeraPalabra.equals("inicio") && !primeraPalabra.equals("fin") && !lineas.trim().endsWith(";")) {
                errores.append("Error: La línea debe terminar con ;\n");
            }
        }

        for (int i = 0; i < palabra.length; i++) {
            if (palabra[i] == ' ') {
                continue;
            } else if (Character.isDigit(palabra[i]) || Character.isLetter(palabra[i])) {
                int j = i;
                while (j < palabra.length && (Character.isLetterOrDigit(palabra[j]) || palabra[j] == '.')) {
                    j++;
                }
                i = j - 1;
            } else if (palabra[i] == '"') {
                int j = i + 1;
                while (j < palabra.length && palabra[j] != '"') {
                    j++;
                }
                if (j >= palabra.length) {
                    errores.append("Error: Cadena de texto no cerrada correctamente con comillas dobles\n");
                } else {
                    i = j;
                }
            } else if (palabra[i] != ';') {
                errores.append("Error: Carácter no válido: ").append(palabra[i]).append("\n");
            }
        }

        return errores.toString();
    }

    private String obtenerPrimeraPalabra(String lineas) {
        String[] palabras = lineas.trim().split("\\s+");
        return palabras.length > 0 ? palabras[0] : "";
    }

    private boolean esPalabraClave(String palabra) {
        return palabra.equals("programa") || palabra.equals("inicio") || palabra.equals("imprimir") || palabra.equals("leer") || palabra.equals("fin");
    }

    private boolean esIdentificadorValido(String identificador) {
        if (identificador == null || identificador.isEmpty()) {
            return false;
        }
        if (!Character.isLetter(identificador.charAt(0))) {
            return false;
        }
        for (int i = 1; i < identificador.length(); i++) {
            if (!Character.isLetterOrDigit(identificador.charAt(i)) && identificador.charAt(i) != ';') {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] arg) {
        try {
            JFrame.setDefaultLookAndFeelDecorated(true);
        } catch (Exception e) {
        }
        new AbrirArchivoTexto();
    }
}
=======
if (a < b) { 
	System.out.println("a es menor que b"); 
} else if (num > 5) { 
	System.out.println("num es mayor que 5"); 
} else if (nombre != "juan") { 
	System.out.println("el nombre no es juan"); 
} else { 
	System.out.println("ninguna de las condiciones se cumplio"); }
>>>>>>> Stashed changes
