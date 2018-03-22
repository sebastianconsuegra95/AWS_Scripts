<?php
// Conectando, seleccionando la base de datos
$conn = new mysqli("mydbdiseno2.crn0fxtqoene.us-east-1.rds.amazonaws.com", "root", "123456789", "dbsyrus"); // conecta al servidor con user, contraseña

$range_1=$_COOKIE['range_1'];
$range_2=$_COOKIE['range_2'];
// Realizar una consulta MySQL
$query = "SELECT * FROM syrus WHERE ID> $range_1 AND ID< $range_2"; // ultimo valor de la tabla llamada datos
$resultado = mysqli_query($conn, $query) or die("Consulta fallida: " . mysqli_error()); // guardo en resultado lo que saqué de query
$windows = mysqli_fetch_all($resultado); // guardo en un array lo que está en resultado, como string
$row_lat=array_column($windows,1); 
$row_lon=array_column($windows,2);
$var = array_merge($row_lat,$row_lon);
echo implode(" ",$var);
   mysqli_close($conn);

?>
