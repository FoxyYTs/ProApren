
package Taller1;

import java.util.Scanner;

public class pilaE1 {
	static pila pila=new pila();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el polinomio");
        String poli = sc.nextLine();
        char[] caracter = poli.toCharArray();
        for (int i = 0; i <= caracter.length; i++) {
            char x = caracter[i];
            if (x == '(' || x == ')' || x == '[' || x == ']' || x == '{' || x == '}') {
                if (x == '(' || x == '[' || x == '{') {
                    pila.push(x);
                } else if (pila.isEmpty()||!(pila.pop().caracter=='('&&x==')'||pila.pop().caracter=='['&&x==']'||pila.pop().caracter=='{'&& x=='}')){
                	System.out.println("La pila no está balanceada");
                }else {
                	pila.push(x);
                	System.out.println("La pila está balanceada");
                }
            }else {
            	System.out.println("Pila vacía: "+pila.isEmpty());
            }
        }
    }
}
