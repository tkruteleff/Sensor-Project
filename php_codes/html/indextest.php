<?php
$link = mysqli_connect('10.208.0.12', 'quaria', 'debiancolasininen')
   or die('Could not connect: ' . mysqli_error());

mysqli_select_db($link, 'sensor_data') or die('Could not select database');

//$dataArray=array();

//get data from database
$sql="SELECT state FROM raw_data ORDER BY time DESC LIMIT 1";
$result = mysqli_query($link, $sql) or die('Query failed: ' . mysqli_error());
if ($result) {
  while ($row = mysqli_fetch_assoc($result)) {
        $state=$row["state"];
        $time=$row["time"];
	echo "ruokailijoita atm:",  $row["state"];
 }
}
?>
<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php echo '<p>Hello World</p>';
?>

<img src="indexg.php" alt="graphi">
 </body>
</html>

