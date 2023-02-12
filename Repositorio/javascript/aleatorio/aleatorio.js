numeritogrande = document.getElementById("numeromax");
numeritochiquito = document.getElementById("numeromin");
botoncito = document.getElementById("boton");
botoncito.addEventListener("click", imprimir)

function imprimir() {
    max = parseInt(numeritogrande.value);
    min = parseInt(numeritochiquito.value);
    z = aleatorio(max,min);
    console.log(min,max,z);
}

function aleatorio(maxi,mini) {
    resultado = Math.floor(Math.random() * (maxi-mini + 1)) + mini;
    return resultado;
}