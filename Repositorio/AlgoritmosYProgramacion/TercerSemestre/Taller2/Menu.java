package AlgoritmosYProgramacion.TercerSemestre.Taller2;

import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {

        Funciones fun = new Funciones();
        Scanner leer = new Scanner(System.in);

        String opcion = "",nombre,vip="N";
        Boolean seguir = true, vipB = false;

        System.out.println("Bienvenido al programa de Aerolinea");
        leer.nextLine();
        while (seguir){
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.print("Que operacion quiere realizar\n1) Comprar Tiquete\n2) Mostrar Ocupacion del Avion\n3) Mostrar Valor a Pagar por Asiento\n4) Salir\nEleccion: ");
            opcion = leer.nextLine();
            switch (opcion) {
                case "1":
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    System.out.println("Cargando Registro...");
                    leer.nextLine();
                    System.out.print("Ingrese el nombre de la persona que tendra este asiento: ");
                    nombre = leer.nextLine();
                    if (fun.contadorVip < 5) {
                        System.out.print("Quiere Comprar un Tiquete VIP (Y/N): ");
                        vip = leer.nextLine();
                        if (vip != "Y" || vip != "N") {
                            System.out.println("OPCION NO VALIDA");
                            leer.nextLine();
                            break;
                        } else if(vip == "Y"){
                            vipB = true;
                        } else {
                            vipB = false;
                        }
                    } else {
                        System.out.println("Los Asientos VIP estan llenos");
                    }
                    fun.compra(nombre, vipB);
                    break;
                
                case "2":
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    System.out.println("Verificando Puestos...");
                    leer.nextLine();
                    fun.disponibilidad();
                    leer.nextLine();
                    break;

                case "3":
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    System.out.println("Calculando Precios...");
                    leer.nextLine();
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    System.out.println(fun.valor());
                    leer.nextLine();
                    break;

                case "4":
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    System.out.println("Saliendo...");
                    seguir = false;
                    leer.nextLine();
                    break;
            
                default:
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    System.out.println("Opcion no valida");
                    leer.nextLine();
                    break;
            }
        }
    }
}
