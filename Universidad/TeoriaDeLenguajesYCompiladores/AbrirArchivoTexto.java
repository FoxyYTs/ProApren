<<<<<<< Updated upstream
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
        boolean inicioEncontrado = false;
        boolean finEncontrado = false;

        try {
            // ruta puede ser de tipo String o tipo File
            fr = new FileReader(ruta);
            br = new BufferedReader(fr);

            String linea;
            int numLinea = 0;
            // ----------------------------------------------------
            // Analisis lexico
            // Obtenemos el contenido del archivo linea por linea
            while ((linea = br.readLine()) != null) {
                contenido += linea + "\n";
                numLinea += 1;

                // Verificamos si es la primera línea
                if (numLinea == 1) {
                    if (!linea.trim().startsWith("programa ")) {
                        contenido += "Error: La primera línea debe comenzar con 'programa' seguido de un identificador válido\n";
                    } else {
                        String[] partes = linea.trim().split("\\s+");
                        if (partes.length < 2 || !esIdentificadorValido(partes[1])) {
                            contenido += "Error: El identificador después de 'programa' debe comenzar con una letra y no contener números ni símbolos\n";
                        } else {
                        }
                    }
                } else {
                    // Verificamos si la línea no está vacía y comienza con una palabra clave
                    if (!linea.trim().isEmpty()) {
                        String primeraPalabra = obtenerPrimeraPalabra(linea);
                        if (primeraPalabra.equals("inicio")) {
                            inicioEncontrado = true;
                        }
                        if (primeraPalabra.equals("fin")) {
                            finEncontrado = true;
                        }
                        if (!esPalabraClave(primeraPalabra)) {
                            contenido += "Error: La línea debe comenzar con una palabra clave (inicio, imprimir, leer, fin)\n";
                        }
                    }
                }

                // Verificamos si la palabra "programa" aparece en otra línea
                if (numLinea > 1 && linea.trim().startsWith("programa")) {
                    contenido += "Error: La palabra 'programa' solo puede aparecer en la primera línea\n";
                }

                // Llamamos a anaLex para detectar errores léxicos
                String erroresLexicos = anaLex(linea);
                if (!erroresLexicos.isEmpty()) {
                    contenido += erroresLexicos + "\n";
                }
            }
            if (!inicioEncontrado) {
                contenido += "Error: La palabra 'inicio' no fue encontrada\n";
            }
            if (!finEncontrado) {
                contenido += "Error: La palabra 'fin' no fue encontrada\n";
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

    public String anaLex(String lineas) {
        
        String errores = ""; // almacena los errores léxicos
        char palabra[] = lineas.toCharArray();

        // Verificación de líneas vacías
        if (!lineas.trim().isEmpty()) {
            String primeraPalabra = obtenerPrimeraPalabra(lineas);
            // Verificación de terminación con ; si no es inicio o fin
            if (!primeraPalabra.equals("inicio") && !primeraPalabra.equals("fin")) {
                if (!lineas.trim().endsWith(";")) {
                    errores += "Error: La línea debe terminar con ;\n";
                }
            }
        }

        for (int i = 0; i < palabra.length; i++) {
            if (palabra[i] == ' ') {
                // Ignorar espacios
            }  else if (Character.isDigit(palabra[i])) {
                int j = i;
                while (j < palabra.length && (Character.isDigit(palabra[j]) || palabra[j] == '.')) {
                    j += 1;
                }
                i = j - 1;
            } else if (Character.isLetter(palabra[i])) {
                int j = i;
                while (j < palabra.length && Character.isLetter(palabra[j])) {
                    j += 1;
                }
                i = j - 1;
            } else if (palabra[i] == '"') {
                int j = i + 1;
                while (j < palabra.length && palabra[j] != '"') {
                    j += 1;
                }
                if (j >= palabra.length) {
                    errores += "Error: Cadena de texto no cerrada correctamente con comillas dobles\n";
                } else {
                    i = j;
                }
            } else {
                if (palabra[i] != ';') {
                    errores += "Error: Carácter no válido: " + palabra[i] + "\n";
                }
                
            }
        }

        return errores;
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
        // Verifica que el primer carácter sea una letra
        if (!Character.isLetter(identificador.charAt(0))) {
            return false;
        }
        // Verifica que el resto de los caracteres sean letras o números
        for (int i = 1; i < identificador.length(); i++) {
            if (!Character.isLetterOrDigit(identificador.charAt(i))) {
                if (identificador.charAt(i) != ';') {
                    return false;
                }
            }
        }
        return true;
    }

    // Fin analisis lexico
    // ----------------------------------------------------

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
