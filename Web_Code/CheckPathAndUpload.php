<!-- readdir() -->
<!-- scandir()  -->


<?php
	include_once 'dbconnect.php';
	
	$array = array();
	$query = mysql_query("SELECT Picture_Name FROM Clothing ");
	while($row = mysql_fetch_assoc($query))
	{
		// add each row returned into an array
		$array[] = $row;

	}

	// get each file's name in databse
	for($x=0;$x<count($array);$x++)
	{
		echo $array[$x][Picture_Name];
		echo "<br>";
	}
	
?>
