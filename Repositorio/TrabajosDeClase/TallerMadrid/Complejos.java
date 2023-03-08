package Repositorio.TrabajosDeClase.TallerMadrid;

import java.util.Scanner;
import java.lang.Math;

public class Complejos {
    public static void main(String[] args) {
        Complejo2 z1 = new Complejo2(2, 4);
        Scanner leer = new Scanner(System.in);

        double numA = 0,numB = 0;


        System.out.println("Introduce un numero");
        numA = Double.parseDouble(leer.nextLine());

        System.out.println("Ingresa Otro numero");
        numB = Double.parseDouble(leer.nextLine());

        System.out.println("Suma: " + sumar(numA,numB) + "\nResta: 1.2");
        
    }
    static double sumar (double num1, double num2){
        return num1+num2;
    }

    static double restar (double num1, double num2){
        return num1-num2;
    }

    static double multiplicar (double num1, double num2){
        return num1*num2;
    }

    static double dividir (double num1, double num2){
        return num1/num2;
    }


    
}
