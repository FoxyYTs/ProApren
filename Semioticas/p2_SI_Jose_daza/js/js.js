// Define la función que se ejecutará cuando la página termine de cargar
function cargaPagina() {
    // Genera un número aleatorio entre 1 y 100
    var numeroAleatorio = Math.floor(Math.random() * 100) + 1;
   
    // Crea un nuevo párrafo con el número aleatorio
    var nuevoParrafo = document.createElement('p');
    var contenidoParrafo = document.createTextNode('Número aleatorio: ' + numeroAleatorio);
    nuevoParrafo.appendChild(contenidoParrafo);
   
    // Añade el nuevo párrafo al body de la página
    document.body.appendChild(nuevoParrafo);
   
    console.log('La página ha terminado de cargar');
   }
   
   // Añade un event listener al objeto window para el evento "DOMContentLoaded"
   window.addEventListener('DOMContentLoaded', cargaPagina);