import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import javax.swing.ImageIcon; // no se usa
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTextPane;
import javax.swing.UIManager; //No se usa

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
		// btn.setIcon( new ImageIcon( getClass().getResource( "Abrir.png" ) ) );

		add(btn, BorderLayout.NORTH);

		// Tamano de la ventana
		setSize(500, 500);

		// Esto sirve para centrar la ventana
		setLocationRelativeTo(null);

		// Hacemos visible la ventana
		setVisible(true);
	}

	// ------------------------------Action
	// Performed-------------------------------//
	public void actionPerformed(ActionEvent e) {
		JButton btn = (JButton) e.getSource();
		if (btn.getText().equals("Abrir")) {
			if (abrirArchivo == null)
				abrirArchivo = new JFileChooser();
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
					// txp.setText(texto);
					txp.setText(contenido);

				} catch (Exception exp) {
					System.out.println(exp); // imprimir el error para poder verlo
				}
			}
		}
	}
	// -----------------------------------------------------------------------------//

	// -------------------------Se obtiene el contenido del
	// Archivo----------------//
	public String getArchivo(String ruta) {
		FileReader fr = null;
		BufferedReader br = null;
		// Cadena de texto donde se guardara el contenido del archivo
		String contenido = "";
		String lineaToken[] = new String[200];
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
						break; // faltaba indentar
					}
					System.out.println("Token posicion " + x + ": " + lineaToken[x]);
				}
			}

		} catch (Exception e) {
			System.out.println(e); // faltaba indentar
		}
		// finally se utiliza para que si todo ocurre correctamente o si ocurre
		// algun error se cierre el archivo que anteriormente abrimos
		finally {
			try {
				// antes solo cerraba el br ahora cierra los 2 solo cuando no eran nulos
				if (br != null)
					br.close();
				if (fr != null)
					fr.close();

			} catch (Exception ex) {
				System.out.println(ex);// visualiar el error
			}
		}
		return contenido;
	}
	// -----------------------------------------------------------------------------//

	public String[] anaLex(String lineas) {
		// ----------------------------------------------------
		// Analisis lexico
		String token = ""; // almacena cada token
		String tokens[] = new String[200]; // vector para almacenar los tokens de cada l�nea
		int t = 0; // puntero de tokens
		char palabra[] = new char[200];
		palabra = lineas.toCharArray();
		// System.out.println(lineas);
		for (int i = 0; i < palabra.length; i++) {
			// System.out.println(palabra[i]);

			if (palabra[i] == ' ') {
				// System.out.println("Espacio");
				// System.out.println("Posicion: "+ i);
			} else if (palabra[i] == '<') {
				if (palabra[i + 1] == '=') {
					// System.out.println("Es el simbolo <=");
					i = i + 1;
					tokens[t] = "<=";
					t += 1;
				} else if (palabra[i] == '>') {
					// System.out.println("Es simbolo <>");
					i = i + 1;
					tokens[t] = "<>";
					t += 1;
				} else {
					// System.out.println("Es el simbolo <");
					tokens[t] = "<";
					t += 1;
				}
			} // else if
			else if (palabra[i] == '=') {
				// System.out.println("Es el simbolo =");
				tokens[t] = "=";
				t += 1;

			} // else if
			else if (palabra[i] == '>') {
				if (palabra[i + 1] == '=') {
					// System.out.println("Es el simbolo >=");
					i = i + 1;
					tokens[t] = ">=";
					t += 1;
				} else {
					// System.out.println("Es el simbolo >");
					tokens[t] = ">";
					t += 1;
				}
			} else if (Character.isDigit(palabra[i])) {
				System.out.println("Es un numero: " + Character.isDigit(palabra[i]));

				int j = i;
				token = "";
				while (Character.isDigit(palabra[j]) || palabra[j] == '.') {
					token += palabra[j];
					j += 1;
					if (j == palabra.length) {
						break;
					} // Si llego al fin, se lee el next char
				}
				// System.out.println(token);
				tokens[t] = token;
				t += 1;
				i = j - 1;// Para que continue en la siguiente palabra
			} else if (Character.isLetter(palabra[i])) {
				System.out.println("Es una letra: " + Character.isLetter(palabra[i]));

				int j = i;
				token = "";
				while (Character.isLetter(palabra[j])) {
					token += palabra[j];
					j += 1;
					if (j == palabra.length) {
						break;
					} // Si llego al fin, se lee el next char
				}
				System.out.println(token);
				tokens[t] = token;
				t += 1;
				i = j - 1;// Para que continue en la siguiente palabra

			} else if (palabra[i] == '\"') {
				token = "";
				token += palabra[i];
				int j = i + 1;
				while (j < palabra.length && palabra[j] != '\"') {
					token += palabra[j];
					j += 1;
				}
				if (j == palabra.length) {
					System.out.println("Error: Cadena no cerrada.");
					return null;  // O manejar el error de otra manera
				}
				token += palabra[j];  // Agregar la comilla de cierre
				tokens[t] = token;
				t += 1;
				i = j;
			} else {
				// System.out.println("Es otro caracter");
				tokens[t] = "" + palabra[i];
				t += 1;
			}
		}

		// Fin analisis lexico
		// ----------------------------------------------------

		return tokens;
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