var color = document.getElementById("colorea");
var a = document.getElementById("terreno");
var lienzo = a.getContext("2d");
a.addEventListener("mousemove",dibujoTecla);

var teclas = {
    RIGHT:1,LEFT:2,MIDDLE:4
};

function dibujoTecla(evento) {
    var x=evento.layerX,y=evento.layerY;
    var xf=x-5,yf=y-5;
    if (evento.buttons == 1) {
        dibuja(color.value,x,y,xf,yf);
        console.log(color,x,y,xf,yf,evento);
    } 
}
function dibuja(color, x1,y1,x2,y2) {
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.lineWidth = 5;
    lienzo.moveTo(x1,y1);
    lienzo.lineTo(x2,y2);
    lienzo.stroke();
    lienzo.closePath;
}