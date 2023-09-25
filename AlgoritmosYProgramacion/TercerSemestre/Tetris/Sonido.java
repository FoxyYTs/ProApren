package AlgoritmosYProgramacion.TercerSemestre.Tetris;
import java.io.*;

import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;

import sun.audio.*;
public class Sonido {
    public static void main(String[] args) throws Exception {

        Clip clip = AudioSystem.getClip();
        String sonido = "D:/programacion/Github/ProApren/AlgoritmosYProgramacion/TercerSemestre/Tetris/song.wav";
        InputStream in = new FileInputStream(sonido);
        AudioStream s = new AudioStream(in);
        AudioData audiodata = s.getData();
        ContinuousAudioDataStream loop = new ContinuousAudioDataStream(audiodata);
        AudioPlayer.player.start(loop);
        
    }
}
