var vp = document.getElementById("villaplatzi");
var villa = vp.getContext("2d");
var cantidadvaca=5, cantidadpollo=50, cantidadcerdo=5;
var fondo = {
    url: "tile.png",
    cargaOK: false
}
var vaca = {
    url: "vaca.png",
    cargaOK: false
}
var pollo = {
    url: "pollo.png",
    cargaOK: false
}
var cerdo = {
    url: "cerdo.png",
    cargaOK: false
}

fondo.imagen = new Image();
fondo.imagen.src = fondo.url;
fondo.imagen.addEventListener("load", cargarfondo);

vaca.imagen = new Image();
vaca.imagen.src = vaca.url;
vaca.imagen.addEventListener("load", cargarvaca);

pollo.imagen = new Image();
pollo.imagen.src = pollo.url;
pollo.imagen.addEventListener("load", cargarpollo);

cerdo.imagen = new Image();
cerdo.imagen.src = cerdo.url;
cerdo.imagen.addEventListener("load", cargarcerdo);

function cargarfondo() {
    fondo.cargaOK = true;
    dibuja();
}
function cargarvaca() {
    vaca.cargaOK = true;
    dibuja();
}
function cargarpollo() {
    pollo.cargaOK = true;
    dibuja();
}
function cargarcerdo() {
    cerdo.cargaOK = true;
    dibuja();
}
function dibuja() {
    if (fondo.cargaOK) {
        villa.drawImage(fondo.imagen,0,0);
    }
    if (vaca.cargaOK){
        for (var i = 0; i < cantidadvaca; i++) {
            var x = aleatorio(0,5);
            var y = aleatorio(0,5);
            x = x * 80;
            y = y * 80;
            villa.drawImage(vaca.imagen,x,y);
        }
    } 
    if (pollo.cargaOK) {
        for (var i = 0; i < cantidadpollo; i++) {
            var x = aleatorio(0,5);
            var y = aleatorio(0,5); 
            x = x * 80;
            y = y * 80;
            villa.drawImage(pollo.imagen,x,y);  
        }
    }
    if (cerdo.cargaOK){
        for (var i = 0; i < cantidadcerdo; i++) {
            var x = aleatorio(0,5);
            var y = aleatorio(0,5);
            x = x * 80;
            y = y * 80;
            villa.drawImage(cerdo.imagen,x,y);
        }
    }
}

function aleatorio(mini,maxi) {
    var resultado = Math.floor(Math.random() * (maxi-mini + 1)) + mini;
    return resultado;
}