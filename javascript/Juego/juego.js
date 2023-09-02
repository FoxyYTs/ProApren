a = document.getElementById("plantilla");
lienzo = a.getContext("2d");
document.addEventListener("keydown",mover);

var letra = {
    IZQUIERDA: 37,ARRIBA: 38,DERECHA: 39,ABAJO: 40, A: 65,W: 87,D: 68,S: 83
}

function mover(evento) {
    if (evento.keyCode == letra.IZQUIERDA || evento.keyCode == letra.A) {
        console.log("Izquierda")
    } else if() {
        
    }
}