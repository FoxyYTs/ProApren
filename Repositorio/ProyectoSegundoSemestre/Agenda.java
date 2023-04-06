package Repositorio.ProyectoSegundoSemestre;

import java.util.Scanner;

public class Agenda {
    public static Contacto hContacto;
    private static Grupo hGrupo;
    private static String formatoFechaHora = "dd/MM/yyyy", idioma = "es";
    public static Configuracion configuracion = new Configuracion(formatoFechaHora, idioma);
    public static Scanner leer = new Scanner (System.in);

    public Agenda(){
        Agenda.hContacto = null;
    }
    
    public void menu(){
        String nameG,nameC,lastname,email,phone;
        System.out.print("creando nuevo Grupo\nIngresa el nombre del Grupo: ");
        agregarGrupos(leer.nextLine());
        System.out.println("Ahora vamos a crear los contactos");
        for (int i = 1; i <= 5; i++) {
            nameC = "nombre" + i;
            lastname = "apellido" + i;
            phone = "telefono" + i;
            email = "correo" + i;
            insertarContacto(nameC, lastname, phone, email);
        }
        System.out.println("La lista de contactos es: ");
        mostrarContacto();
        System.out.println("Ingresa el Nombre de Grupo: ");
        nameG = leer.nextLine();
        System.out.println("ingresa el Nombre: ");
        nameC = leer.nextLine();
        System.out.print("Ingresa el Apellido: ");
        lastname = leer.nextLine();
        insertarAGrupo(nameG, nameC, lastname);

        System.out.println("Lista de grupos");
        mostrarGrupos();
        System.out.println("ingrese el grupo que quiera ver: ");
        nameG = leer.nextLine();
        mostrarGrupo(nameG);
        


    }
    //Funciones Contactos
    public static void insertarContacto(String nombre, String apellido, String correo, String telefono) {
        Contacto nuevo = new Contacto(nombre, apellido, correo, telefono);
        if (hContacto == null) {
            hContacto = nuevo;
        } else {
            Contacto pContacto = hContacto;
            while (pContacto.next != null) {
                pContacto = pContacto.next;
            }
            pContacto.next = nuevo;
        }
    }

    public static void eliminarContacto(String nombre) {
        if (hContacto == null) {
            return;
        }
        if (hContacto.getNombre() == nombre) {
            hContacto = hContacto.next;
            return;
        }
        Contacto pContacto = hContacto;
        while (pContacto.next.getNombre() != nombre && pContacto.next != null) {
            pContacto = pContacto.next;
        }
        if (pContacto.next != null) {
            pContacto.next = pContacto.next.next;
        }
    }

    public static void mostrarContacto() {
        Contacto pContacto = hContacto;
        while (pContacto != null) {
            configuracion.imprimirMostrarContactos(pContacto.getNombre(), pContacto.getApellido(), pContacto.getTelefono(), pContacto.getCorreo());
            pContacto = pContacto.next;
        }
        System.out.println();
    }

    public static Contacto buscarContacto(String nombre, String apellido){
        Contacto pContacto = hContacto;
        while (pContacto != null) {
            if(pContacto.getNombre().equals(nombre) && pContacto.getApellido().equals(apellido)){
                return pContacto;
            }
            pContacto = pContacto.next;
        }
        return null;
    }

    //Funciones Grupos

    public static void agregarGrupos(String nombre) {
        Grupo nuevo = new Grupo(nombre);
        if (hGrupo == null) {
            hGrupo = nuevo;
        } else {
            Grupo pointerGrupos = hGrupo;
            while (pointerGrupos.next != null) {
                pointerGrupos = pointerGrupos.next;
            }
            pointerGrupos.next = nuevo;
        }
    }

    public static void eliminarGrupos(String nombre) {
        if (hGrupo == null) {
            return;
        }
        if (hGrupo.getNombre() == nombre) {
            hGrupo = hGrupo.next;
            return;
        }
        Grupo pointerGrupos = hGrupo;
        while (pointerGrupos.next.getNombre() != nombre && pointerGrupos.next != null) {
            pointerGrupos = pointerGrupos.next;
        }
        if (pointerGrupos.next != null) {
            pointerGrupos.next = pointerGrupos.next.next;
        }
    }

    public static void mostrarGrupos() {
        Grupo pointerGrupos = hGrupo;
        while (pointerGrupos != null) {
            configuracion.agendaMostrarGrupo(pointerGrupos.getNombre());
            pointerGrupos = pointerGrupos.next;
        }
        System.out.println();
    }

    public static void insertarAGrupo(String nombreG, String nombreC, String apellido){
        Grupo pGrupo = hGrupo;
        while (pGrupo != null) {
            if(pGrupo.getNombre().equals(nombreG)){
                pGrupo.agregarContactoGrupo(buscarContacto(nombreC, apellido)); 
                return;
            }
            pGrupo = pGrupo.next;
        }
        return;
    }
    
    public static void mostrarGrupo(String nombreG){
        Grupo pGrupo = hGrupo;
        while (pGrupo != null) {
            if(pGrupo.getNombre().equals(nombreG)){
                pGrupo.mostrarContactoGrupo();
                return;
            }
            pGrupo = pGrupo.next;
        }
        return;
    } 
}
