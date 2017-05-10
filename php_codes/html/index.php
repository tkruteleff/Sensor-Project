<?php
// public_html/index.php - Read MySQL from PHP
// (c) 2016 Tero Karvinen http://TeroKarvinen.com

// MySQL Login
$user='quaria';
$password='debiancolasininen';

// Data Source Name i.e. connection details
$database=sensor_data;
$dsn="mysql:host=10.208.0.12;charset=UTF8;dbname=$database;";

// Open Connection, create new object of PDO class
$pdo=new PDO($dsn, $user, $password);

// Perform SQL Query
$pdoStatement=$pdo->prepare('SELECT * FROM raw_data;');
$pdoStatement->execute();
$hits=$pdoStatement->fetchAll();

// Print the $hits Array
foreach($hits as $row) {
 echo "<p>".$row['id']." ".$row['state']." ".$row['time']."</p>\n";
}
?>
