<?php

$db = mysqli_connect('10.207.3.0', 'asari', 'debiancolasininen', 'quaria')
or die('Error connecting to MySQL server!');
?>

<html>
    <head>
    </head>
    <body>
    <h1>PHP connect to MySQL</h1>
    
<?php
$query = "SELECT * FROM id, state, time";
        mysqli_query($db, $query) or die('Error querying database!');
        
$result = mysqli_query($dbm $query);
$row = mysqli_fetch_array($result);
mysqli_close($db);
?>
        
</body>
</html>