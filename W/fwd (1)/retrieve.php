<?php
if($_SERVER["REQUEST_METHOD"]=="POST"){
$name=$_POST['name'];
$email=$_POST['email'];
$age=$_POST['age'];

echo "<h2>Submitted Data</h2>";
echo "Name: ".htmlspecialchars($name)."<br>";
echo "Email: ".htmlspecialchars($email)."<br>";
echo "Age: ".htmlspecialchars($age)."<br>";
}else{
echo "Values not found!";
}
?>