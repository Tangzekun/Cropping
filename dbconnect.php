<?php
error_reporting( E_ALL & ~E_DEPRECATED & ~E_NOTICE );
if(!mysql_connect("ix.cs.uoregon.edu:3366","hotel","hotel"))
{
	die('oops connection problem ! --> '.mysql_error());
}
if(!mysql_select_db("Hotel_Data"))
{
	die('oops database selection problem ! --> '.mysql_error());
}

?>