<?php
include("/var/www/html/phpgraphlib/phpgraphlib.php");
$graph=new PHPGraphLib(1000,500);

$link = mysqli_connect('10.208.0.12', 'quaria', 'debiancolasininen')
   or die('Could not connect: ' . mysqli_error());

mysqli_select_db($link, 'sensor_data') or die('Could not select database');

$dataArray=array();

//get data from database
$sql="SELECT time,  COUNT(*) AS 'state' FROM raw_data GROUP BY time";
$result = mysqli_query($link, $sql) or die('Query failed: ' . mysqli_error());
if ($result) {
  while ($row = mysqli_fetch_assoc($result)) {
	$id=$row["id"];
	$state=$row["state"];
	$time=$row["time"];
      //add to data areray
      $dataArray[$time]=$state;
  }
}

//configure graph
$graph->addData($dataArray);
//$graph->setTitle("Lassin ja Kaapon Motivaatiokayra");
//$graph->setGradient("lime", "green");
//$graph->setBarOutlineColor("black");
//$graph->createGraph();
$graph->setupXAxis(50);
$graph->setBars(false);
$graph->setLine(true);
$graph->setDataPoints(true);
$graph->setDataPointColor('maroon');
$graph->setDataValues(true);
$graph->setDataValueColor('maroon');
$graph->setGoalLine(.0025);
$graph->setGoalLineColor('red');
$graph->createGraph();
?>
