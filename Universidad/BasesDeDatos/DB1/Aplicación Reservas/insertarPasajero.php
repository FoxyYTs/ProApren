<?php
$pasaporte = $_POST["pasaporte"];
$nombre = $_POST["nombre"];
$correo = $_POST["correo"];
$telefono = $_POST["telefono"]; 
include_once ("db.php");
$sql = "INSERT INTO pasajero (pasaporte,nombre,correo,telefono) VALUES ('$pasaporte','$nombre','$correo','$telefono')";
$conexion = conn();
$consulta = mysqli_query($conexion, $sql) or trigger_error("Error:", mysqli_error($conexion));

echo "<META HTTP-EQUIV='REFRESH' CONTENT='0; URL=insertarPasajero.html'>";
?>