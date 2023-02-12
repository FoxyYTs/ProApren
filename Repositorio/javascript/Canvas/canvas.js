var d = document.getElementById("osito"); //Metodo del document para traer un objeto por su ID
var lienzo = d.getContext("2d"); 
var xi=0,yi=0,xf=0,yf=0;
/*
lienzo.beginPath(); //Iniciar el camino
lienzo.strokeStyle = "blue"; //define el color del trazo
lienzo.moveTo(0,x); //mueve el lapiz al punto sin dibujar una linea
lienzo.lineTo(x,500); //mueves el lapiz al punto dibujando una linea
lienzo.stroke(); //Dibuja
lienzo.closePath; //Cerrar el camino
*/
xi=0,yi=0,xf=0,yf=500;
for (var i = 0; i < 50; i++) {
    lienzo.beginPath();
    lienzo.strokeStyle = "orange";
    lienzo.moveTo(xi,yi); 
    lienzo.lineTo(xf,yf); 
    lienzo.stroke(); 
    lienzo.closePath; 
    yi += 10
    xf += 10
    lienzo.beginPath();
    lienzo.strokeStyle = "blue";
    lienzo.moveTo(xi,yi); 
    lienzo.lineTo(xf,yf); 
    lienzo.stroke(); 
    lienzo.closePath; 
    yi += 10
    xf += 10
}
xi=0,yi=500,xf=500,yf=500;
for (var i = 0; i < 50; i++) {
    lienzo.beginPath();
    lienzo.strokeStyle = "red";
    lienzo.moveTo(xi,yi); 
    lienzo.lineTo(xf,yf); 
    lienzo.stroke(); 
    lienzo.closePath;
    xi += 10
    yf -= 10
    lienzo.beginPath();
    lienzo.strokeStyle = "green";
    lienzo.moveTo(xi,yi); 
    lienzo.lineTo(xf,yf); 
    lienzo.stroke(); 
    lienzo.closePath;
    xi += 10
    yf -= 10
}
xi=500,yi=500,xf=500,yf=0;
for (var i = 0; i < 50; i++) {
    lienzo.beginPath();
    lienzo.strokeStyle = "yellow";
    lienzo.moveTo(xi,yi); 
    lienzo.lineTo(xf,yf); 
    lienzo.stroke(); 
    lienzo.closePath;
    yi -= 10
    xf -= 10
    lienzo.beginPath();
    lienzo.strokeStyle = "purple";
    lienzo.moveTo(xi,yi); 
    lienzo.lineTo(xf,yf); 
    lienzo.stroke(); 
    lienzo.closePath;
    yi -= 10
    xf -= 10
}
xi=500,yi=0,xf=0,yf=0;
for (var i = 0; i < 50; i++) {
    lienzo.beginPath();
    lienzo.strokeStyle = "brown";
    lienzo.moveTo(xi,yi); 
    lienzo.lineTo(xf,yf); 
    lienzo.stroke(); 
    lienzo.closePath;
    xi -= 10
    yf += 10
    lienzo.beginPath();
    lienzo.strokeStyle = "white";
    lienzo.moveTo(xi,yi); 
    lienzo.lineTo(xf,yf); 
    lienzo.stroke(); 
    lienzo.closePath;
    xi -= 10
    yf += 10
}

document.write(" Hola ");