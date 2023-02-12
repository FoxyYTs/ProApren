var bttn = document.getElementById("botoncito");
var txt = document.getElementById("textito");
bttn.addEventListener("click", dibujoporclick); 


var d = document.getElementById("holi");
var ancho = d.width;
var lienzo = d.getContext("2d"); 

document.write("X Inicial = "+xi+" Y Inicial = "+yi+" X Final = "+xf+" Y Final = "+yf+" I = "+i);


function dibuja(color, x1,y1,x2,y2) {
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo(x1,y1);
    lienzo.lineTo(x2,y2);
    lienzo.stroke();
    lienzo.closePath;
}
function dibujoporclick() {
    var texto = txt.value;
    texto = parseInt(texto);
    var espacio = ancho / texto;
    
    var xi=0,yi=0,xf=0,yf=0;

    xi=0,yi=0,xf=0,yf=1000;
    for (var i = 0; i < texto; i++) {
        dibuja("pink",xi,yi,xf,yf);
        yi += espacio
        xf += espacio
    }
}