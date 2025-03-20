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

    public AbrirArchivoTexto() {
        // Para poder cerrar la ventana
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Se agrega un layout
        setLayout(new BorderLayout());

        // Se crea el editor de texto y se agrega a un scroll
        txp = new JTextPane();
        JScrollPane jsp = new JScrollPane();
        jsp.setViewportView(txp);

        add(jsp, BorderLayout.CENTER);

        // Se crea un boton para abrir el archivo
        JButton btn = new JButton("Abrir");
        btn.addActionListener(this);

        add(btn, BorderLayout.NORTH);

        // Tamano de la ventana
        setSize(500, 500);

        // Esto sirve para centrar la ventana
        setLocationRelativeTo(null);

        // Hacemos visible la ventana
        setVisible(true);
    }

    // ------------------------------Action Performed-------------------------------//
    public void actionPerformed(ActionEvent e) {
        JButton btn = (JButton) e.getSource();
        if (btn.getText().equals("Abrir")) {
            if (abrirArchivo == null) abrirArchivo = new JFileChooser();
            // Con esto solamente podamos abrir archivos
            abrirArchivo.setFileSelectionMode(JFileChooser.FILES_ONLY);

            int seleccion = abrirArchivo.showOpenDialog(this);

            if (seleccion == JFileChooser.APPROVE_OPTION) {
                File f = abrirArchivo.getSelectedFile();
                try {
                    String nombre = f.getName();
                    String path = f.getAbsolutePath();
                    String contenido = getArchivo(path);
                    // Colocamos en el titulo de la aplicacion el
                    // nombre del archivo
                    this.setTitle(nombre);
                    // En el editor de texto colocamos su contenido
                    txp.setText(contenido);

                } catch (Exception exp) {
                }
            }
        }
    }
    // ------------------------------------------------------------------------------//

    // -------------------------Se obtiene el contenido del Archivo----------------//
    public String getArchivo(String ruta) {
        FileReader fr = null;
        BufferedReader br = null;
        // Cadena de texto donde se guardara el contenido del archivo
        String contenido = "";
        String lineaToken[] = new String[200];
        boolean programaEncontrado = false;
        boolean inicioEncontrado = false;
        boolean finEncontrado = false;

        try {
            // ruta puede ser de tipo String o tipo File
            fr = new FileReader(ruta);
            br = new BufferedReader(fr);

            String linea;
            int numLinea = 0;
            // Obtenemos el contenido del archivo linea por linea
            while ((linea = br.readLine()) != null) {
                contenido += linea + "\n";
                numLinea += 1;
                lineaToken = anaLex(linea);
                System.out.println("Linea: " + numLinea);
                for (int x = 0; x < lineaToken.length; x++) {
                    if (lineaToken[x] == null) {
                        break;
                    }
                    System.out.println("Token posicion " + x + ": " + lineaToken[x]);
                }

                // Verificamos si la primera línea comienza con "programa"
                if (numLinea == 1 && !linea.trim().equals("programa")) {
                    contenido += "Error: La primera línea debe comenzar con la palabra clave 'programa'\n";
                }

                // Verificamos si la línea contiene "programa"
                if (linea.trim().equals("programa")) {
                    programaEncontrado = true;
                }

                // Verificamos si la línea siguiente a "programa" es vacía o "inicio"
                if (programaEncontrado && !inicioEncontrado) {
                    String siguienteLinea = br.readLine();
                    if (siguienteLinea != null) {
                        contenido += siguienteLinea + "\n";
                        numLinea += 1;
                        if (!siguienteLinea.trim().isEmpty() && !siguienteLinea.trim().equals("inicio")) {
                            contenido += "Error: Después de 'programa' debe haber una línea vacía o 'inicio'\n";
                        } else {
                            inicioEncontrado = true;
                        }
                    }
                }

                // Verificamos si la línea contiene "fin"
                if (linea.trim().equals("fin")) {
                    finEncontrado = true;
                }
            }

            // Verificamos si se encontró la palabra "fin" al final del archivo
            if (!finEncontrado) {
                contenido += "Error: El archivo debe terminar con la palabra 'fin'\n";
            }

        } catch (Exception e) {
            System.out.println(e);
        }
        // finally se utiliza para que si todo ocurre correctamente o si ocurre
        // algun error se cierre el archivo que anteriormente abrimos
        finally {
            try {
                br.close();
            } catch (Exception ex) {
            }
        }
        return contenido;
    }
    // ------------------------------------------------------------------------------//

    public String[] anaLex(String lineas) {
        // ----------------------------------------------------
        // Analisis lexico
        String token = ""; // almacena cada token
        String tokens[] = new String[200]; // vector para almacenar los tokens de cada línea
        int t = 0; // puntero de tokens
        char palabra[] = lineas.toCharArray();

        // Verificación de líneas vacías o que comiencen con palabras clave
        if (!lineas.trim().isEmpty()) {
            String primeraPalabra = obtenerPrimeraPalabra(lineas);
            if (!esPalabraClave(primeraPalabra)) {
                tokens[t] = "Error: La línea debe comenzar con una palabra clave (programa, inicio, imprimir, leer, fin)";
                t += 1;
            }

            // Verificación de terminación con ; si no es inicio o fin
            if (!primeraPalabra.equals("inicio") && !primeraPalabra.equals("fin")) {
                if (!lineas.trim().endsWith(";")) {
                    tokens[t] = "Error: La línea debe terminar con ;";
                    t += 1;
                }
            }
        }

        for (int i = 0; i < palabra.length; i++) {
            if (palabra[i] == ' ') {
                // Ignorar espacios
            } else if (palabra[i] == '<') {
                if (i + 1 < palabra.length && palabra[i + 1] == '=') {
                    tokens[t] = "<=";
                    t += 1;
                    i += 1;
                } else if (i + 1 < palabra.length && palabra[i + 1] == '>') {
                    tokens[t] = "<>";
                    t += 1;
                    i += 1;
                } else {
                    tokens[t] = "<";
                    t += 1;
                }
            } else if (palabra[i] == '=') {
                tokens[t] = "=";
                t += 1;
            } else if (palabra[i] == '>') {
                if (i + 1 < palabra.length && palabra[i + 1] == '=') {
                    tokens[t] = ">=";
                    t += 1;
                    i += 1;
                } else {
                    tokens[t] = ">";
                    t += 1;
                }
            } else if (Character.isDigit(palabra[i])) {
                int j = i;
                token = "";
                while (j < palabra.length && (Character.isDigit(palabra[j]) || palabra[j] == '.')) {
                    token += palabra[j];
                    j += 1;
                }
                tokens[t] = token;
                t += 1;
                i = j - 1;
            } else if (Character.isLetter(palabra[i])) {
                int j = i;
                token = "";
                while (j < palabra.length && Character.isLetter(palabra[j])) {
                    token += palabra[j];
                    j += 1;
                }
                tokens[t] = token;
                t += 1;
                i = j - 1;
            } else if (palabra[i] == '"') {
                token = "";
                token += palabra[i];
                int j = i + 1;
                while (j < palabra.length && palabra[j] != '"') {
                    token += palabra[j];
                    j += 1;
                }
                if (j >= palabra.length) {
                    tokens[t] = "Error: Cadena de texto no cerrada correctamente con comillas dobles";
                    t += 1;
                } else {
                    token += palabra[j];
                    tokens[t] = token;
                    t += 1;
                    i = j;
                }
            } else {
                tokens[t] = "" + palabra[i];
                t += 1;
            }
        }

        // Fin analisis lexico
        // ----------------------------------------------------

        return tokens;
    }

    private String obtenerPrimeraPalabra(String lineas) {
        String[] palabras = lineas.trim().split("\\s+");
        return palabras.length > 0 ? palabras[0] : "";
    }

    private boolean esPalabraClave(String palabra) {
        return palabra.equals("programa") || palabra.equals("inicio") || palabra.equals("imprimir") || palabra.equals("leer") || palabra.equals("fin");
    }

    public static void main(String[] arg) {
        try {
            // Cambiamos el Look&Feel
            JFrame.setDefaultLookAndFeelDecorated(true);
        } catch (Exception e) {
        }
        new AbrirArchivoTexto();
    }

    JTextPane txp;
    JFileChooser abrirArchivo;
}