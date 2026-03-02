package CarreraBuses;

import javax.sound.sampled.*;
import java.net.URL;

public class Sonido {

    private Clip clip;

    public void reproducir() {
        try {
            URL audioURL = getClass().getResource("bus.wav");

            if (audioURL == null) {
                System.out.println("ERROR: No se encontró bus.wav");
                return;
            }

            AudioInputStream audioStream =
                    AudioSystem.getAudioInputStream(audioURL);

            clip = AudioSystem.getClip();
            clip.open(audioStream);
            clip.start();

        } catch (Exception e) {
            System.out.println("Error reproduciendo sonido: " + e.getMessage());
        }
    }

    public void detener() {
        if (clip != null && clip.isRunning()) {
            clip.stop();
            clip.close();
        }
    }
}