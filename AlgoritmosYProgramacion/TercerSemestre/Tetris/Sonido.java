package AlgoritmosYProgramacion.TercerSemestre.Tetris;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;


import sun.audio.AudioPlayer;
import sun.audio.AudioStream;


public class Sonido {

    public static void main(String[] args) throws Exception {

        String sonido = "D:/programacion/Github/ProApren/AlgoritmosYProgramacion/TercerSemestre/Tetris/song.wav";
        InputStream in = new FileInputStream(sonido);
        AudioStream audio = new AudioStream(in);
        //AudioPlayer.player.start(audio);


        File archivoAudio = new File("D:/programacion/Github/ProApren/AlgoritmosYProgramacion/TercerSemestre/Tetris/song.wav");

        // Crear un objeto AudioInputStream a partir del archivo de audio
        AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(archivoAudio);

        // Crear un objeto Clip
        Clip clip = AudioSystem.getClip();

        // Cargar el archivo de audio en el objeto Clip
        clip.open(audioInputStream);

        clip.setLoopPoints(1500, 2000);

        // Iniciar la reproducción del archivo de audio en bucle
        clip.loop(3);

        clip.start();

        // Esperar a que termine la reproducción del archivo de audio
    

    }
}