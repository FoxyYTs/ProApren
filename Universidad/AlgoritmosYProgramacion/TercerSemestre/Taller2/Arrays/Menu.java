package AlgoritmosYProgramacion.TercerSemestre.Taller2.Arrays;

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
                    if (fun.contadorOcupado < fun.cantSilla) {
                        System.out.print("Ingrese el nombre de la persona que tendra este asiento: ");
                        nombre = leer.nextLine();
                        vipB = false;
                        if (fun.contadorVip < fun.sillaVip) {
                            System.out.print("Quiere Comprar un Tiquete VIP (Y/N): ");
                            vip = leer.nextLine();
                            if (vip.equals("N")) {
                                vipB = false;
                                break;
                            } else if(vip.equals("Y")){
                                vipB = true;
                            } else {
                                System.out.println("OPCION NO VALIDA");
                                leer.nextLine();
                            }
                        } else {
                            System.out.println("Los Asientos VIP estan llenos");
                        }
                        fun.compra(nombre, vipB);
                    } else {
                        System.out.println("El Avion se encuentra lleno");
                    }
                    leer.nextLine();
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
