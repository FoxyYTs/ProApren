import java.util.Scanner;
public class array {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int x = 10;
        int[] array1 = new int[x];
        int[] array2 = new int[x];
        int[] array3 = new int[x];

        for (int i = 0; i < x; i++) {
            System.out.print("ingresa un numero para la primera lista: ");
            array1[i] = Integer.parseInt(leer.nextLine()); 
            System.out.print("ingresa un numero para la segunda lista: ");
            array2[i] = Integer.parseInt(leer.nextLine()); 
        }
        System.out.println("las listas quedaron de la siguiente forma\n|\tlista 1\t|\tlista2\t|");
        for (int i = 0; i < x; i++){
            System.out.println("|\t" + array1[i] + "\t|\t" + array2[i] + "\t|");
        }
        for (int i = 0; i < x; i++){
            if(array1[i] > array2[i]){
                array3[i] = array1[i];
            }else if(array2[i] >= array1[i]){
                array3[i] = array2[i];
            }
        }
        for (int i = 0; i < x; i++) {
            System.out.println(array3[i]);
        }
    }
}
