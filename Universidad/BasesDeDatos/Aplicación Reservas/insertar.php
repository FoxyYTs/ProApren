<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Inserción de Reserva - Aerolínea</title>
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
        <a class="nav-link" href="insertar.html">INSERTAR RESERVA</a>
      </li>
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

<div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-6">
      <form action="insertar.php" method="post">
        <div class="form-group">
          <label for="numeroReserva">Número de Reserva</label>
          <input type="text" class="form-control" id="numeroReserva" name="numeroReserva" required>
        </div>
        <div class="form-group">
          <label for="fechaReserva">Fecha de Reserva</label>
          <input type="date" class="form-control" id="fechaReserva" name="fechaReserva" required>
        </div>
        <div class="form-group">
          <label for="horaReserva">Hora de Reserva</label>
          <input type="time" class="form-control" id="horaReserva" name="horaReserva" required>
        </div>
        <div class="form-group">
          <label for="cantidadAsientos">Cantidad de Asientos</label>
          <input type="number" class="form-control" id="cantidadAsientos" name="cantidadAsientos" required>
        </div>
        <div class="form-group">
          <label for="numeroPasaporte">Número de Pasaporte</label>
          <input type="text" class="form-control" id="numeroPasaporte" name="numeroPasaporte" required>
        </div>
        <div class="form-group">
          <label for="numeroVuelo">Número de Vuelo</label>
          <select class="form-control" id="numeroVuelo" name="numeroVuelo" required>
          <?php
           include_once("db.php");
           while(){
             echo "<option value='$num_vuelo'>$num_vuelo</option>";
           } 
          
            <option value="CD456">CD456</option>
            <option value="EF789">EF789</option>
            <option value="GH012">GH012</option>
            <option value="IJ345">IJ345</option>
          </select>
        </div>
        <div class="form-group">
          <label for="tipoPago">Tipo de Pago</label>
          <select class="form-control" id="tipoPago" name="tipoPago" required>
            <option value="Pago en efectivo">Pago en efectivo</option>
            <option value="Pago con Tarjeta">Pago con Tarjeta</option>
            <option value="Pago con Transferencia">Pago con Transferencia</option>
          </select>
        </div>

        <button type="submit" class="btn btn-danger btn-block">RESERVAR</button>
      </form>
    </div>
  </div>
</div>

<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

</body>
</html>