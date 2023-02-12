var d = document.getElementById("holi");
var lienzo = d.getContext("2d"); 

var xi=0,yi=0,xf=0,yf=0;

xi=0,yi=0,xf=0,yf=500;
for (var i = 0; i < 50; i++) {
    dibuja("Orange",xi,yi,xf,yf);
    yi += 10
    xf += 10
    dibuja("blue",xi,yi,xf,yf);
    yi += 10
    xf += 10
}
xi=0,yi=500,xf=500,yf=500;
for (var i = 0; i < 50; i++) {
    dibuja("red",xi,yi,xf,yf);
    xi += 10
    yf -= 10
    dibuja("green",xi,yi,xf,yf);
    xi += 10
    yf -= 10
}
xi=500,yi=500,xf=500,yf=0;
for (var i = 0; i < 50; i++) {
    dibuja("yellow",xi,yi,xf,yf);
    yi -= 10
    xf -= 10
    dibuja("purple",xi,yi,xf,yf);
    yi -= 10
    xf -= 10
}
xi=500,yi=0,xf=0,yf=0;
for (var i = 0; i < 50; i++) {
    dibuja("brown",xi,yi,xf,yf);
    xi -= 10
    yf += 10
    dibuja("white",xi,yi,xf,yf);
    xi -= 10
    yf += 10
}

document.write("X Inicial = "+xi+" Y Inicial = "+yi+" X Final = "+xf+" Y Final = "+yf+" I = "+i);


function dibuja(color, x1,y1,x2,y2) {
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo(x1,y1);
    lienzo.lineTo(x2,y2);
    lienzo.stroke();
    lienzo.closePath;
}