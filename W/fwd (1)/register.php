<?php
$servername = "localhost";
$username = "root";
$password= ""; 
$dbname="sycs";
$conn=new mysqli($servername, $username, $password, $dbname);
if($conn->connect_error){
die("Connection failed: ".$conn->connect_error);
}
$name=$_POST['name'];
$email=$_POST['email'];
$password=password_hash ($_POST['password'],PASSWORD_DEFAULT);

$sql="INSERT INTO students (name, email, password) VALUES ('$name', '$email', '$password')";
if($conn->query($sql)===TRUE) {
echo "Registration successful!";
}else{
echo "Error: ".$sql."<br>".$conn->error;
}
$conn->close();
?>