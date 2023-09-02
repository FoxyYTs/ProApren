var e = document.getElementById("tablero1");
var f = document.getElementById("tablero2");
var lienzo1 = e.getContext("2d");
var lienzo2 = f.getContext("2d");
var xi=0,yi=0,xf=0,yf=0;

xi=0,yi=250,xf=250,yf=250;
for (var i = 0;i <= 25;i++) {
    dibujo1("red",xi,yi,xf,yf);
    xi+=10
    yf-=10
}
xi=250,yi=0,xf=250,yf=250;
for (var i = 0;i <= 25;i++) {
    dibujo1("green",xi,yi,xf,yf);
    yi+=10
    xf+=10
}
xi=500,yi=250,xf=250,yf=250;
for (var i = 0;i <= 25;i++) {
    dibujo1("blue",xi,yi,xf,yf);
    xi-=10
    yf+=10
}
xi=250,yi=500,xf=250,yf=250;
for (var i = 0;i <= 25;i++) {
    dibujo1("yellow",xi,yi,xf,yf);
    yi-=10
    xf-=10
}

xi=0,yi=500,xf=250,yf=0;
for (var i = 0;i <= 25;i++) {
    dibujo2("blue",xi,yi,xf,yf);
    yf+=10
    xf+=5
    xi+=5
}
xi=500,yi=500,xf=250,yf=0;
for (var i = 0;i <= 25;i++) {
    dibujo2("red",xi,yi,xf,yf);
    yf+=10
    xf-=5
    xi-=5
}
xi=125.5,yi=250,xf=0,yf=500;
for (var i = 0;i <= 25;i++) {
    dibujo2("red",xi,yi,xf,yf);

}
xi=0,yi=0,xf=500,yf=0;
for (var i = 0;i <= 25;i++) {
    dibujo2("white",xi,yi,xf,yf);
    yi+=125.5
    yf+=125.5
}
xi=0,yi=0,xf=0,yf=500;
for (var i = 0;i <= 25;i++) {
    dibujo2("white",xi,yi,xf,yf);
    xi+=125.5
    xf+=125.5
}





function dibujo1(color, x1,y1,x2,y2) {
    lienzo1.beginPath();
    lienzo1.strokeStyle = color;
    lienzo1.moveTo(x1,y1);
    lienzo1.lineTo(x2,y2);
    lienzo1.stroke();
    lienzo1.closePath;
}

function dibujo2(color, x1,y1,x2,y2) {
    lienzo2.beginPath();
    lienzo2.strokeStyle = color;
    lienzo2.moveTo(x1,y1);
    lienzo2.lineTo(x2,y2);
    lienzo2.stroke();
    lienzo2.closePath;
}

