<?php
// Get form data from POST request
$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

// Hardcoded valid credentials
$valid_username = 'admin';
$valid_password = 'admin1234';

// Check credentials
if ($username === $valid_username && $password === $valid_password) {
    echo "<h2>Login successful!</h2>";
    echo "Welcome, " . htmlspecialchars($username) . "!";
} else {
    echo "<h2>Login failed!</h2>";
    echo "Invalid username or password.";
}
?>
