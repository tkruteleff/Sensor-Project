<?php
include("/var/www/html/phpgraphlib/phpgraphlib.php");
$graph=new PHPGraphLib(1000,500);

$link = mysqli_connect('10.208.0.12', 'quaria', 'debiancolasininen')
   or die('Could not connect: ' . mysqli_error());

mysqli_select_db($link, 'sensor_data') or die('Could not select database');

//$dataArray=array();

//get data from database
$sql="SELECT time, state FROM raw_data ORDER BY time DESC LIMIT 25";
$result = mysqli_query($link, $sql) or die('Query failed: ' . mysqli_error());
if ($result) {
  while ($row = mysqli_fetch_assoc($result)) {
        $state=$row["state"];
        $time=$row["time"];
      //add to data array
      $dataArray[$time]=$state;
 }
}
//configure grap;
$graph->addData(array_reverse($dataArray));
$graph->setTitle("Lassin ja Kaapon Motivaatiokayra");
$graph->setRange(160,0);
//$graph->setupXAxis(40);
$graph->setBars(false);
$graph->setLine(true);
$graph->setDataPoints(true);
$graph->setDataPointColor('maroon');
$graph->setDataValues(true);
$graph->setDataValueColor('maroon');
$graph->setGoalLine(19.9, "green", "solid");
$graph->setGoalLine(20, "green", "solid");
$graph->setGoalLine(20.1, "green", "solid");
$graph->setGoalLine(39.9, "yellow", "solid");
$graph->setGoalLine(40, "yellow", "solid");
$graph->setGoalLine(40.1, "yellow", "solid");
$graph->setGoalLine(69.9, "red", "solid");
$graph->setGoalLine(70, "red", "solid");
$graph->setGoalLine(70.1, "red", "solid");
$graph->setGoalLine(100, "black", "solid");
$graph->createGraph();
?>


