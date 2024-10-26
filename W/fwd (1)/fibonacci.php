<?php
if ($_SERVER["REQUEST_METHOD"]=="POST") {
$terms=$_POST['terms'];
function fibonacci($n) {
$fibseries=[];
$a=0;
$b=1;
for ($i=0;$i<$n;$i++) {
$fibseries[] = $a;
$next = $a + $b;
$a=$b;
$b=$next;
}
return $fibseries;
}
$result=fibonacci($terms);
echo "Fibonacci series of $terms terms: " . implode(", ", $result);
}
?>
