<?php
// Conectando, seleccionando la base de datos
$conn = new mysqli("mydbdiseno2.crn0fxtqoene.us-east-1.rds.amazonaws.com", "root", "123456789", "dbsyrus"); // conecta al servidor con user, contraseña
$timems_1=$_COOKIE['timems_1'];
$timems_2=$_COOKIE['timems_2'];
$timems_1=239;
$timems_2=251;
// Realizar una consulta MySQL
$query = "SELECT * FROM syrus WHERE ID< $timems_2 AND ID> $timems_1 ORDER BY ID ASC"; // Ventana de valores con respecto a timems
$resultado = mysqli_query($conn, $query) or die("Consulta fallida: " . mysqli_error()); // guardo en resultado lo que saqué de query
$windows = mysqli_fetch_all($resultado); // guardo en un array lo que está en resultado, como string
$row_lat=array_column($windows,1); 
$row_lon=array_column($windows,2);
$var = array_merge($row_lat,$row_lon);
echo implode(" ",$var);
  mysqli_close($conn);

?>
