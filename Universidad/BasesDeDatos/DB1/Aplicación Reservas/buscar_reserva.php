<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Inicio - Aerolínea</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Aerolínea</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="buscar_reserva.html">BUSCAR RESERVA</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="disponibilidad.html">DISPONIBILIDAD DE ASIENTOS</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="vuelos.html">VUELOS DISPONIBLES</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="aerolineas.html">AEROLÍNEAS</a>
      </li>
    </ul>
  </div>
</nav>

<?php

include_once("db.php");

// Obtener el número de tiquete enviado por POST
if(isset($_POST['reserva'])) {
    $num_reserva = $_POST['reserva'];

    // Consulta SQL
    $sql = "SELECT reservas.numero_reserva, reservas.cantidad_asientos, pasajeros.nombre_pasajero, pasajeros.correo_pasajero, vuelos.fecha_salida, vuelos.fecha_llegada, aeropuertos.nombre_aeropuerto as aeropuerto_origen, ad.nombre_aeropuerto AS aeropuerto_destino 
            FROM reservas 
            JOIN pasajeros ON pasajeros.numero_pasaporte = reservas.numero_pasaporte_reserva 
            JOIN vuelos ON vuelos.numero_vuelo = reservas.numero_vuelo_reserva 
            JOIN aeropuertos ON aeropuertos.IATA = vuelos.aeropuerto_origen 
            JOIN aeropuertos ad ON ad.IATA = vuelos.aeropuerto_destino 
            WHERE reservas.numero_reserva = '$num_reserva'";

        $conectar=conn();//crear la conexión a la b.d.
        $result=mysqli_query($conectar,$sql) or trigger_error("Error:",mysqli_error($conectar));    
        //$result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Mostrar los datos obtenidos de la consulta
        
        while($row = $result->fetch_assoc()) {
            echo "Reserva de ".$row['nombre_pasajero']." <br>";
            echo "# Reserva: ".$row['numero_reserva']." <br>";
            echo "Cantidad Asientos: ".$row['cantidad_asientos']."<br>";
            echo "Correo del pasajero: ".$row['correo_pasajero']."<p>";

    ?>

    <div class="row">
    <div class="col-md-6">
      <div class="card">
        <img src="https://www.colombia.co/wp-content/uploads/2019/10/Cartagena-Cortes%C2%A1a-Charly-Boillot-2-768x397.jpg" width="1%"class="card-img-top" alt="Aeropuerto 1">
        <div class="card-body">
          <h5 class="card-title">AEROPUERTO ORIGEN</h5>
          <p class="card-text"><?php echo $row["aeropuerto_origen"]; ?></p>
          <a href="#" class="btn btn-primary">Más información</a>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card">
        <img src="aeropuerto2.jpg" class="card-img-top" alt="Aeropuerto 2">
        <div class="card-body">
          <h5 class="card-title">AEROPUERTO DESTINO</h5>
          <p class="card-text"><?php echo $row["aeropuerto_destino"]; ?></p>
          <a href="#" class="btn btn-primary">Más información</a>
        </div>
      </div>
    </div>
  </div>
</div>

<?php
        }
    } else {
        echo "No se encontraron resultados para el número de reserva proporcionado.";
    }
}
?>


<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

</body>
</html>