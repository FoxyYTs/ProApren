package AlgoritmosYProgramacion.TercerSemestre.Tetris;

import java.io.*;

import sun.audio.*;
public class Sonido {
    public static void main(String[] args) throws Exception {
        playMusic("D:/programacion/Github/ProApren/AlgoritmosYProgramacion/TercerSemestre/Tetris/song.wav");        
    }

    public static void playMusic(String filepath){
        try {
            AudioData data = new AudioStream(new FileInputStream(filepath)).getData();
            ContinuousAudioDataStream sound = new ContinuousAudioDataStream(data);
            AudioPlayer.player.start(sound);

            AudioPlayer.player.stop(sound);
        } catch (Exception e) {
            System.out.println("No dio");
        }
    }
}
