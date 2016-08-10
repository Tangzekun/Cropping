
<?php
	ini_set('mysql.connect_timeout',10);
	ini_set('default_socket_timeout',5);

	include_once 'dbconnect.php';


?>



<?php
	if(isset($_FILES['files']))
	{
		$errors= array();
		$extensions = array("jpeg","jpg","png"); 
		foreach($_FILES['files']['tmp_name'] as $key => $tmp_name )
		{
			
			$file_name = $key.$_FILES['files']['name'][$key];
			$file_size =$_FILES['files']['size'][$key];
			$file_tmp =$_FILES['files']['tmp_name'][$key];
			$file_type=$_FILES['files']['type'][$key];
			
			$image= addslashes($_FILES['files']['tmp_name'][$key]);
			$image= file_get_contents($image);
			$image= base64_encode($image);
			
			$query="Insert into Clothing (Picture_Name,Picture_Storage) values ( '$file_name','$image')";
			
			$desired_dir="user_data";
			if(empty($errors)==true)
			{
				if(is_dir($desired_dir)==false)
				{
					mkdir("$desired_dir", 0700);		// Create directory if it does not exist
				}
				if(is_dir("$desired_dir/".$file_name)==false)
				{
					move_uploaded_file($file_tmp,"user_data/".$file_name);
				}
				else
				{									//rename the file if another one exist
					$new_dir="user_data/".$file_name.time();
					 rename($file_tmp,$new_dir) ;				
				}
				mysql_query($query);			
			}
			else
			{
					print_r($errors);
			}
		}
		if(empty($error)){
			echo "Success";
		}
		
		
		
	}


	function displayimage()
	{	
		$qry = "Select * from Clothing";

		$result=mysql_query($qry);

		while($row = mysql_fetch_array($result))
		{
			echo '<img height="200" width="200" src="data:image;base64,'.$row[Picture_Storage].' "> ';
		}
	}

?>












<html>

	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Hello PeekABuy</title>
		<link rel="stylesheet" href="style.css" type="text/css" />
	</head>
	
	
	<body>
	
	<div id="header">
		<div id="left">
	    <label>Cropped Images </label>
	    </div>
	</div>


<div id="body">
    <div id="Hotel-InfoForm">
			<form action="" method="POST" enctype="multipart/form-data">
				<center>
					<input type="file" name="files[]" multiple="" />
					<input type="submit"/>
				<center>	
			</form>
			
			<br> 
			<br>
			<br>

		    <?php
        		displayimage();
        	?>


		<br>


		<hr>


	</div>
</div>




</body>
</html>
