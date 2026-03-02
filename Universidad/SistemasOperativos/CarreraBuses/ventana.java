package CarreraBuses;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.io.File;

public class ventana extends JFrame implements GanadorListener {
    
    private JLabel titulo, subtitulo;
    private JLabel labelBus1, labelBus2, labelBus3, labelBus4;
    private JLabel labelPos1, labelPos2, labelPos3, labelPos4;
    private JLabel imagenBus1, imagenBus2, imagenBus3, imagenBus4;
    private JProgressBar barraBus1, barraBus2, barraBus3, barraBus4;
    private JButton btnIniciar, btnReiniciar;
    private JLabel mensajeEstado, mensajeGanador;
    private ArrayList<bus> buses = new ArrayList<>();
    private boolean carreraIniciada = false;
    private Timer actualizadorPosiciones;
    private Sonido sonidoInicio;
    
    public ventana() {
        setUIFont(new Font("Segoe UI Emoji", Font.PLAIN, 12));
        sonidoInicio = new Sonido();
        initComponents();
        iniciarActualizadorPosiciones();
    }
    
    // Método para configurar la fuente de toda la interfaz
    private void setUIFont(Font font) {
        UIManager.put("Label.font", font);
        UIManager.put("Button.font", font);
        UIManager.put("ProgressBar.font", font);
    }
    
    private void initComponents() {
        setTitle("Carrera de Buses - Práctica de Hilos");
        setSize(950, 750);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());
        
        // Panel principal
        JPanel mainPanel = new JPanel(new BorderLayout());
        mainPanel.setBackground(new Color(240, 248, 255));
        
        // Panel superior con títulos (usando caracteres en lugar de emojis)
        JPanel topPanel = new JPanel(new GridLayout(2, 1));
        topPanel.setBackground(new Color(240, 248, 255));
        
        titulo = new JLabel(">>> CARRERA DE BUSES - CARRIL DE CARRERA <<<", JLabel.CENTER);
        titulo.setFont(new Font("Arial", Font.BOLD, 24));
        titulo.setForeground(new Color(0, 102, 204));
        topPanel.add(titulo);
        
        subtitulo = new JLabel("Distancia total: 100 km", JLabel.CENTER);
        subtitulo.setFont(new Font("Arial", Font.PLAIN, 16));
        topPanel.add(subtitulo);
        
        mainPanel.add(topPanel, BorderLayout.NORTH);
        
        // Panel central con la carrera
        JPanel carreraPanel = new JPanel();
        carreraPanel.setLayout(new BoxLayout(carreraPanel, BoxLayout.Y_AXIS));
        carreraPanel.setBackground(new Color(240, 248, 255));
        carreraPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        
        // Crear los carriles para cada bus
        carreraPanel.add(crearCarril("BUS 1", new Color(255, 99, 71), 
                        labelBus1 = new JLabel(), barraBus1 = new JProgressBar(0, 100),
                        labelPos1 = new JLabel("-", JLabel.CENTER), 
                        imagenBus1 = new JLabel()));
        
        carreraPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        
        carreraPanel.add(crearCarril("BUS 2", new Color(60, 179, 113), 
                        labelBus2 = new JLabel(), barraBus2 = new JProgressBar(0, 100),
                        labelPos2 = new JLabel("-", JLabel.CENTER), 
                        imagenBus2 = new JLabel()));
        
        carreraPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        
        carreraPanel.add(crearCarril("BUS 3", new Color(30, 144, 255), 
                        labelBus3 = new JLabel(), barraBus3 = new JProgressBar(0, 100),
                        labelPos3 = new JLabel("-", JLabel.CENTER), 
                        imagenBus3 = new JLabel()));
        
        carreraPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        
        carreraPanel.add(crearCarril("BUS 4", new Color(255, 165, 0), 
                        labelBus4 = new JLabel(), barraBus4 = new JProgressBar(0, 100),
                        labelPos4 = new JLabel("-", JLabel.CENTER), 
                        imagenBus4 = new JLabel()));
        
        JScrollPane scrollPane = new JScrollPane(carreraPanel);
        scrollPane.setBorder(BorderFactory.createTitledBorder("CARRILES DE CARRERA"));
        mainPanel.add(scrollPane, BorderLayout.CENTER);
        
        // Panel inferior con botones y mensajes
        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new BoxLayout(bottomPanel, BoxLayout.Y_AXIS));
        bottomPanel.setBackground(new Color(240, 248, 255));
        bottomPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        
        // Panel de botones
        JPanel buttonPanel = new JPanel(new FlowLayout());
        buttonPanel.setBackground(new Color(240, 248, 255));
        
        btnIniciar = new JButton("INICIAR CARRERA");
        btnIniciar.setFont(new Font("Arial", Font.BOLD, 16));
        btnIniciar.setBackground(new Color(0, 153, 76));
        btnIniciar.setForeground(Color.WHITE);
        btnIniciar.addActionListener(e -> iniciarCarrera());
        
        btnReiniciar = new JButton("REINICIAR CARRERA");
        btnReiniciar.setFont(new Font("Arial", Font.BOLD, 16));
        btnReiniciar.setBackground(new Color(204, 102, 0));
        btnReiniciar.setForeground(Color.WHITE);
        btnReiniciar.setEnabled(false);
        btnReiniciar.addActionListener(e -> reiniciarCarrera());
        
        buttonPanel.add(btnIniciar);
        buttonPanel.add(btnReiniciar);
        
        // Mensajes
        mensajeEstado = new JLabel("Presiona INICIAR para comenzar la carrera", JLabel.CENTER);
        mensajeEstado.setFont(new Font("Arial", Font.ITALIC, 14));
        mensajeEstado.setForeground(Color.GRAY);
        mensajeEstado.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        mensajeGanador = new JLabel("", JLabel.CENTER);
        mensajeGanador.setFont(new Font("Arial", Font.BOLD, 20));
        mensajeGanador.setForeground(new Color(204, 0, 0));
        mensajeGanador.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        bottomPanel.add(buttonPanel);
        bottomPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        bottomPanel.add(mensajeEstado);
        bottomPanel.add(Box.createRigidArea(new Dimension(0, 5)));
        bottomPanel.add(mensajeGanador);
        
        mainPanel.add(bottomPanel, BorderLayout.SOUTH);
        
        add(mainPanel);
        setVisible(true);
    }
    
    private JPanel crearCarril(String nombreBus, Color color, JLabel labelInfo, 
                               JProgressBar barra, JLabel labelPos, JLabel imagen) {
        JPanel carril = new JPanel();
        carril.setLayout(new BorderLayout());
        carril.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1));
        carril.setBackground(Color.WHITE);
        
        // Panel izquierdo con información del bus
        JPanel infoPanel = new JPanel();
        infoPanel.setLayout(new BoxLayout(infoPanel, BoxLayout.Y_AXIS));
        infoPanel.setBackground(new Color(240, 248, 255));
        infoPanel.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        infoPanel.setPreferredSize(new Dimension(120, 100));
        
        // Nombre del bus
        JLabel nombreLabel = new JLabel(nombreBus);
        nombreLabel.setFont(new Font("Arial", Font.BOLD, 14));
        nombreLabel.setForeground(color);
        nombreLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        // Posición
        labelPos.setFont(new Font("Arial", Font.BOLD, 18));
        labelPos.setForeground(Color.GRAY);
        labelPos.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        // Información de distancia
        labelInfo.setText("0 km");
        labelInfo.setFont(new Font("Arial", Font.PLAIN, 12));
        labelInfo.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        infoPanel.add(nombreLabel);
        infoPanel.add(Box.createRigidArea(new Dimension(0, 5)));
        infoPanel.add(labelPos);
        infoPanel.add(Box.createRigidArea(new Dimension(0, 5)));
        infoPanel.add(labelInfo);
        
        // Panel central con la pista y el bus
        JPanel pistaPanel = new JPanel(null);
        pistaPanel.setBackground(new Color(169, 169, 169)); // Color gris como la pista
        pistaPanel.setPreferredSize(new Dimension(500, 100));
        
        // Meta
        JLabel meta = new JLabel("META");
        meta.setFont(new Font("Arial", Font.BOLD, 18));
        meta.setForeground(Color.RED);
        meta.setBounds(520, 50, 60, 20);
        pistaPanel.add(meta);
        
        // Línea de meta
        JLabel lineaMeta = new JLabel();
        lineaMeta.setBounds(454, 0, 2, 150);
        lineaMeta.setOpaque(true);
        lineaMeta.setBackground(Color.RED);
        pistaPanel.add(lineaMeta);
        
        // Cargar la imagen del bus desde el sistema de archivos
        ImageIcon iconoBus = cargarImagenBus();
        if (iconoBus != null) {
            imagen.setIcon(iconoBus);
        } else {
            // Si no encuentra la imagen, muestra texto como respaldo
            imagen.setText("[BUS]");
            imagen.setFont(new Font("Arial", Font.BOLD, 12));
            imagen.setForeground(color);
            imagen.setHorizontalAlignment(JLabel.CENTER);
            imagen.setVerticalAlignment(JLabel.CENTER);
            imagen.setOpaque(true);
            imagen.setBackground(color);
            imagen.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        }
        
        imagen.setBounds(10, 30, 50, 40);
        pistaPanel.add(imagen);
        
        // Panel derecho con barra de progreso
        JPanel barraPanel = new JPanel(new BorderLayout());
        barraPanel.setBackground(new Color(240, 248, 255));
        barraPanel.setBorder(BorderFactory.createEmptyBorder(40, 5, 40 , 5));
        barraPanel.setPreferredSize(new Dimension(150, 100));
        
        JLabel barraLabel = new JLabel("Progreso:", JLabel.CENTER);
        barraLabel.setFont(new Font("Arial", Font.BOLD, 12));
        
        barra.setStringPainted(true);
        barra.setForeground(color);
        barra.setBackground(Color.LIGHT_GRAY);
        barra.setFont(new Font("Arial", Font.BOLD, 12));
        barra.setValue(0);
        
        barraPanel.add(barraLabel, BorderLayout.NORTH);
        barraPanel.add(barra, BorderLayout.CENTER);
        
        carril.add(infoPanel, BorderLayout.WEST);
        carril.add(pistaPanel, BorderLayout.CENTER);
        carril.add(barraPanel, BorderLayout.EAST);
        
        return carril;
    }
    
    private ImageIcon cargarImagenBus() {
        try {
            java.net.URL imgURL = getClass().getResource("bus.png");

            if (imgURL == null) {
                System.out.println("ERROR: No se encontró bus.png en el classpath");
                return null;
            }

            ImageIcon iconoOriginal = new ImageIcon(imgURL);
            Image imagenEscalada = iconoOriginal.getImage()
                    .getScaledInstance(50, 40, Image.SCALE_SMOOTH);

            return new ImageIcon(imagenEscalada);

        } catch (Exception e) {
            System.out.println("Error cargando imagen: " + e.getMessage());
            return null;
        }
    }
    
    private void iniciarActualizadorPosiciones() {
        actualizadorPosiciones = new Timer(100, e -> actualizarPosiciones());
        actualizadorPosiciones.start();
    }
    
    private void actualizarPosiciones() {
        if (!buses.isEmpty() && carreraIniciada) {
            // Ordenar buses por distancia recorrida (mayor a menor)
            ArrayList<bus> busesOrdenados = new ArrayList<>(buses);
            busesOrdenados.sort((b1, b2) -> 
                Integer.compare(b2.getDistanciaRecorrida(), b1.getDistanciaRecorrida()));
            
            // Asignar posiciones
            for (int i = 0; i < busesOrdenados.size(); i++) {
                bus b = busesOrdenados.get(i);
                b.setPosicion(i + 1);
            }
        }
    }
    
    private void iniciarCarrera() {
        if (!carreraIniciada) {
            carreraIniciada = true;
            sonidoInicio.reproducir();
            btnIniciar.setEnabled(false);
            btnReiniciar.setEnabled(true);
            mensajeEstado.setText(">> ¡Carrera en progreso! <<");
            mensajeGanador.setText("");
            bus.reiniciarGanador();
            
            // Reiniciar valores
            barraBus1.setValue(0);
            barraBus2.setValue(0);
            barraBus3.setValue(0);
            barraBus4.setValue(0);
            labelBus1.setText("0 km");
            labelBus2.setText("0 km");
            labelBus3.setText("0 km");
            labelBus4.setText("0 km");
            labelPos1.setText("-");
            labelPos2.setText("-");
            labelPos3.setText("-");
            labelPos4.setText("-");
            
            // Reiniciar posición de las imágenes
            imagenBus1.setLocation(10, 30);
            imagenBus2.setLocation(10, 30);
            imagenBus3.setLocation(10, 30);
            imagenBus4.setLocation(10, 30);
            
            // Crear y iniciar los buses
            buses.clear();
            

            bus bus1 = new bus("BUS 1", barraBus1, labelBus1, labelPos1, imagenBus1, this);
            bus bus2 = new bus("BUS 2", barraBus2, labelBus2, labelPos2, imagenBus2, this);
            bus bus3 = new bus("BUS 3", barraBus3, labelBus3, labelPos3, imagenBus3, this);
            bus bus4 = new bus("BUS 4", barraBus4, labelBus4, labelPos4, imagenBus4, this);
            
            buses.add(bus1);
            buses.add(bus2);
            buses.add(bus3);
            buses.add(bus4);
            
            // Iniciar todos los hilos
            for (bus b : buses) {
                b.start();
            }
        }
    }
    
    private void reiniciarCarrera() {
        // Detener todos los buses
        for (bus b : buses) {
            b.detenerCarrera();
            b.interrupt();
        }
        
        carreraIniciada = false;
        sonidoInicio.detener();
        btnIniciar.setEnabled(true);
        btnReiniciar.setEnabled(false);
        mensajeEstado.setText("Carrera reiniciada. Presiona INICIAR para comenzar");
        mensajeGanador.setText("");
        
        // Reiniciar valores visuales
        barraBus1.setValue(0);
        barraBus2.setValue(0);
        barraBus3.setValue(0);
        barraBus4.setValue(0);
        labelBus1.setText("0 km");
        labelBus2.setText("0 km");
        labelBus3.setText("0 km");
        labelBus4.setText("0 km");
        labelPos1.setText("-");
        labelPos2.setText("-");
        labelPos3.setText("-");
        labelPos4.setText("-");
        
        // Reiniciar posición de las imágenes
        imagenBus1.setLocation(10, 30);
        imagenBus2.setLocation(10, 30);
        imagenBus3.setLocation(10, 30);
        imagenBus4.setLocation(10, 30);
        
        bus.reiniciarGanador();
        buses.clear();
    }
    
    public void mostrarGanador(String nombreBus) {
        // Detener todos los buses
        for (bus b : buses) {
            b.detenerCarrera();
        }
        
        // Actualizar posiciones finales
        actualizarPosiciones();
        
        mensajeGanador.setText("!!! GANADOR: " + nombreBus + " !!!");
        mensajeEstado.setText(">>> ¡Carrera finalizada! <<<");
        carreraIniciada = false;
        btnReiniciar.setEnabled(true);
    }

    @Override
    public void hayGanador(String nombreBus) {
        SwingUtilities.invokeLater(() -> mostrarGanador(nombreBus));
    }
}