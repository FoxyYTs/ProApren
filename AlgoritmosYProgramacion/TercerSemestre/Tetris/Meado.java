package AlgoritmosYProgramacion.TercerSemestre.Tetris;



import java.io.IOException;
import java.io.InputStream;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;

public class Meado extends Thread{
    Clip audio;
    InputStream ruta;


    @Override
    public void run(){

        try {
            ruta = getClass().getResourceAsStream("/Sonidos/SonidoJuego.wav");
            audio = AudioSystem.getClip();
            audio.open(AudioSystem.getAudioInputStream(ruta)) ;
            audio.start();
        } catch (Exception e) {
        }
    }  
}