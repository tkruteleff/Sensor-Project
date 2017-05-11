<!DOCTYPE html>
<html>
<div1>
<p>Kulunseuranta graaffi</p>
</div1>
<div2>
<p>Ruokailijoita </p>
</div2>
<div3>
<?php
$link = mysqli_connect('10.208.0.12', 'quaria', 'debiancolasininen')
   or die('Could not connect: ' . mysqli_error());

mysqli_select_db($link, 'sensor_data') or die('Could not select database');

//$dataArray=array();
//This code uses PHPgraphlib http://www.ebrueggeman.com/phpgraphlib
//get data from database
$sql="SELECT state FROM raw_data ORDER BY time DESC LIMIT 1";
$result = mysqli_query($link, $sql) or die('Query failed: ' . mysqli_error());
if ($result) {
  while ($row = mysqli_fetch_assoc($result)) {
        $state=$row["state"];
        $time=$row["time"];
        echo " ",  $row["state"];
 }
}
?>
</div3>
 <head>
<link rel="stylesheet" href="styles.css">
        <title>Ruokalan kulunseuranta</title>
        <meta http-equiv="refresh" content="10" >
 </head>
 <body>
<img src="indexg.php" alt="graphi">
<svg height="210" width="500">
        <line x1="10" y1="30" x2="100" y2="30" style="stroke:rgb(255,0,0);stroke-width:5" />
        <text x="120" y="30">Täynnä (yli 70 henkilöä)</text>
        <line x1="10" y1="60" x2="100" y2="60" style="stroke:rgb(255,255,0);stroke-width:5" />
        <text x="120" y="60">Hieman ahdasta (40-100 henkilöä)</text>
        <line x1="10" y1="90" x2="100" y2="90" style="stroke:rgb(0,128,0);stroke-width:5" />
        <text x="120" y="90">Hyvin tilaa (alle 20 henkilöä)</text>
</svg>
 </body>
</html>

