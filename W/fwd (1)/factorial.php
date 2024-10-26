<?php
if ($_SERVER["REQUEST_METHOD"]=="POST") {
$number=$_POST['number'];
function factorial($n) {
if ($n<0) {
return "Factorial is not defined for negative numbers.";
}
if ($n===0 || $n===1) {
return 1;
}
return $n*factorial($n-1);
}
$result=factorial($number);
echo "Factorial of $number is $result.";
}
?>
