<?php
// signup.php
$servername = "localhost";
$username = "root";  // Change according to your phpMyAdmin settings
$password = "";      // Your phpMyAdmin password
$dbname = "recipie"; // Replace with your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the POST data from the request
$name = $_POST['username'];
$email = $_POST['E-mail'];
$user_password = $_POST['pass'];
$gender = $_POST['gender'];

// Check if email already exists
$sql = "SELECT * FROM users WHERE email = '$email'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "Email already exists.";
} else {
    // Hash the password before saving to the database

    

    // Insert data into the database
    $sql = "INSERT INTO users (user_name, email, gender, pass) VALUES ('$name', '$email', '$gender', '$user_password')";

    if ($conn->query($sql) === TRUE) {
        echo "Sign up successful!";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}
$conn->close();
?>
