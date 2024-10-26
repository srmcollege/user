<?php
$file = 'file.txt';
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$action = $_POST['action'] ?? '';
if ($action == 'write') {
$content = $_POST['content'] ?? '';
file_put_contents($file, $content);
echo "Content written to file.";
}
elseif ($action=='append') {
$content = $_POST['content'] ?? '';
file_put_contents($file, $content, FILE_APPEND);
echo "Content appended to file.";
}
elseif ($action=='read') {
if (file_exists($file)) {
$content = file_get_contents($file);
echo nl2br($content);
} else {
echo "File does not exist.";
}
}
elseif ($action=='delete') {
if (file_exists($file)) {
unlink($file);
echo "File deleted.";
} else {
echo "File does not exist.";
}
}
}
?>
