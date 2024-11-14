<?php
// signup.php
$servername = "localhost";
$username = "root";  // Change according to your phpMyAdmin settings
$password = "";      // Your phpMyAdmin password
$dbname = "recipie"; // Replace with your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
if($conn)
{
    echo "UnSuccessful";
}
else{
    echo "Fail";
}
$conn->close();
?>
