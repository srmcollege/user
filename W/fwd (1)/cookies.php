
<?php
//Set cookies if the form is submitted

if ($_SERVER["REQUEST_METHOD"]=="POST" && isset($_POST['username']) && isset($_POST['color'])){
$username=$_POST['username'];
$color=$_POST['color'];

//Set the cookies(valid for 1 minute)
setcookie("username", $username,time()+60,"/");
setcookie("color",$color,time()+60,"/");
echo "Cookies are set for user: $username with favorite color: $color.<br>";
echo "<a href="cookie_form.html">Go Back</a>";
}

// Retrieve cookies if requested
if(isset($_POST['retrieve']) && $_POST['retrieve']=="yes") {
if(isset($_COOKIE ['username']) && isset($_COOKIE ['color'])) {
$username= $_COOKIE['username'];
$color= $_COOKIE['color'];
echo "Welcome back, $username! Your favorite color is: <span style='color:$color;'>$color</span>.<br>";
}else{
echo "No cookies found.<br>";
}
echo "<a href='cookie_form.html'>Go Back</a>";
}
?>