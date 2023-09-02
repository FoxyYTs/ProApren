var a = document.getElementById("terreno");
var lienzo = a.getContext("2d");
document.addEventListener("keydown",dibujoTecla);
var xi=500,yi=500,xf=500,yf=500;

var teclas = {
    LEFT:37,UP:38,RIGHT:39,DOWN:40,A:65,W:87,D:68,S:83
};


function dibujoTecla(evento) {
    var color = "White",color2 = "red",movimiento = 50;

    if (evento.keyCode == teclas.LEFT) {
        xi-=movimiento;
        dibuja(color,xi,yi,xf,yf);
        console.log(color,xi,yi,xf,yf);
        xf=xi;
    } else if(evento.keyCode == teclas.UP) {
        yi-=movimiento;
        dibuja(color,xi,yi,xf,yf);
        console.log(color,xi,yi,xf,yf);
        yf=yi;
    } else if(evento.keyCode == teclas.RIGHT) {
        xi+=movimiento;
        dibuja(color,xi,yi,xf,yf);
        console.log(color,xi,yi,xf,yf);
        xf=xi;
    } else if(evento.keyCode == teclas.DOWN) {
        yi+=movimiento;
        dibuja(color,xi,yi,xf,yf);
        console.log(color,xi,yi,xf,yf);
        yf=yi;
    } else if(evento.keyCode == teclas.A) {
        xi-=movimiento;
        dibuja(color2,xi,yi,xf,yf);
        console.log(color2,xi,yi,xf,yf);
        xf=xi;
    } else if(evento.keyCode == teclas.W) {
        yi-=movimiento;
        dibuja(color2,xi,yi,xf,yf);
        console.log(color2,xi,yi,xf,yf);
        yf=yi;
    } else if(evento.keyCode == teclas.D) {
        xi+=movimiento;
        dibuja(color2,xi,yi,xf,yf);
        console.log(color2,xi,yi,xf,yf);
        xf=xi;
    } else if (evento.keyCode == teclas.S) {
        yi+=movimiento;
        dibuja(color2,xi,yi,xf,yf);
        console.log(color2,xi,yi,xf,yf);
        yf=yi;
    }else{
        console.log(evento.keyCode,evento.key);
    }
}

function dibuja(color, x1,y1,x2,y2) {
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo(x1,y1);
    lienzo.lineTo(x2,y2);
    lienzo.stroke();
    lienzo.closePath;
}