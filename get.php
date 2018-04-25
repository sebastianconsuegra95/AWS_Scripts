<?php
// Conectando, seleccionando la base de datos
$conn = new mysqli("mydbdiseno2.crn0fxtqoene.us-east-1.rds.amazonaws.com", "root", "123456789", "dbsyrus"); // conecta al servidor con user, contraseña


// Realizar una consulta MySQL
$query = "SELECT * FROM syrus_00_ ORDER BY id DESC LIMIT 1"; // ultimo valor de la tabla llamada datos
$resultado = mysqli_query($conn, $query) or die("Consulta fallida: " . mysqli_error()); // guardo en resultado lo que saqué de query

$fila = mysqli_fetch_row($resultado); // guardo en un array lo que está en resultado, como string

$var = $fila[1]."\n".$fila[2]."\n".$fila[3]."\n".$fila[4]."\n";

 echo $var;
   mysqli_close($conn);

?>
