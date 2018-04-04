<?php
// Conectando, seleccionando la base de datos
$conn = new mysqli("mydbdiseno2.crn0fxtqoene.us-east-1.rds.amazonaws.com", "root", "123456789", "dbsyrus"); // conecta al servidor con user, contraseña
$timems_1=intval($_POST['posttimems1']);
$timems_2=intval($_POST['posttimems2']);
// Realizar una consulta MySQL
$query = "SELECT * FROM syrus WHERE timems<= $timems_2 AND timems>= $timems_1 ORDER BY timems ASC"; // Ventana de valores con respecto a timems
$resultado = mysqli_query($conn, $query) or die("Consulta fallida: " . mysqli_error()); // guardo en resultado lo que saqué de query
$windows = mysqli_fetch_all($resultado); // guardo en un array lo que está en resultado, como string
$row_lat=array_column($windows,1); 
$row_lon=array_column($windows,2);
$var = array_merge($row_lat,$row_lon);

echo implode(" ",$var);
  mysqli_close($conn);

?>
