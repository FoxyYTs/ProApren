var g_tierra = 9.8, g_marte = 3.7, g_jupiter = 24.7,peso_f=0;
var eleccion = parseInt(prompt("Elige un planeta"));//Entrada en String
var peso = prompt("Cual es el peso a calcular?")//Entrada en String
peso = parseInt(peso); //Casteo de un valor = de String a Entero
if (eleccion == 1) {
    peso_f = peso * g_tierra / g_tierra;
    peso_f = parseInt(peso_f);//Casteo de un valor = de Float a Entero
    document.write(peso_f);//Mostrar el mensaje en el Body
} else if (eleccion == 2) {
    peso_f = peso * g_marte / g_tierra;
    peso_f = parseInt(peso_f);//Casteo de un valor = de Float a Entero
    document.write(peso_f);//Mostrar el mensaje en el Body
} else if (eleccion == 3) {
    peso_f = peso * g_jupiter / g_tierra;
    peso_f = parseInt(peso_f);//Casteo de un valor = de Float a Entero
    document.write(peso_f);//Mostrar el mensaje en el Body
} else {
    document.write("No valido");//Mostrar el mensaje en el Body

}
