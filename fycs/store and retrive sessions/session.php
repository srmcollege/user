

<?php
// Start the session
session_start();

// Check if form is submitted to set session data
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['username']) && isset($_POST['color'])) {
    $_SESSION['username'] = $_POST['username'];
    $_SESSION['color'] = $_POST['color'];

    echo "Session started for user: " . $_SESSION['username'] . " with favorite color: " . $_SESSION['color'] . ".<br>";
    echo "<a href='session_form.html'>Go Back</a>";
}

// Retrieve session data if requested
if (isset($_POST['action']) && $_POST['action'] == 'retrieve') {
    if (isset($_SESSION['username']) && isset($_SESSION['color'])) {
        echo "Session Data:<br>";
        echo "Username: " . $_SESSION['username'] . "<br>";
        echo "Favorite Color: <span style='color:" . $_SESSION['color'] . "'>" . $_SESSION['color'] . "</span><br>";
    } else {
        echo "No session data found.<br>";
    }
    echo "<a href='session_form.html'>Go Back</a>";
}

// Destroy session if requested
if (isset($_POST['action']) && $_POST['action'] == 'destroy') {
    // Unset all session variables
    session_unset();

    // Destroy the session
    session_destroy();

    echo "Session ended and all data is cleared.<br>";
    echo "<a href='session_form.html'>Go Back</a>";
}
?>
