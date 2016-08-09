<?php
    ini_set('mysql.connect_timeout',10);
    ini_set('default_socket_timeout',5);

	include_once 'dbconnect.php';


?>



    <?php
    if(isset($_POST['btn_Upload_Image']))
    {	
    	if(getimagesize($_FILES['image']['tmp_name']) == FALSE)
        {
            // echo "Please select an image.";
            ?>
                    <script>alert('Please select an image.');</script>
            <?php
        }
        else
        {
            $image= addslashes($_FILES['image']['tmp_name']);
			$Name= addslashes($_FILES['image']['name']);
			$image= file_get_contents($image);
			$image= base64_encode($image);
            saveimage($Name,$image);
         }
        
    }
    //displayimage();



    function saveimage($Name,$Image)
            {
	
				$qry="Insert into Clothing (Picture_Name,Picture_Storage) values ( '$Name','$Image')";
				
                // echo "$qry" ."</br>";
                $result=mysql_query($qry);
                if($result)
                {	
                	?>
                	<script>alert('Image uploaded.');</script>
                	<?php
                }
                else
                {	
                	?>
                	<script>alert('Image not uploaded.');</script>
                	<?php
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
    	<form method="post" enctype="multipart/form-data">
    		<center>
    		<table align="center" width="40%" border="0">


			<tr>
			<td>
				<input type="file" name="image" />
	            <br/>
	            <br/>
	            <input type="submit" name="btn_Upload_Image" value="Upload" />

			</td>	
			</tr>
			<center>
        	</table>


        	<br>
			<br>
			<br>
			<br>
			<br>
			<br>


		</form>	

		    <?php
        		displayimage();
        	?>

		<br> 
		<br>
		<br>
		<br>


		<hr>


	</div>
</div>




</body>
</html>