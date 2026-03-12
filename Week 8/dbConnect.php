<?php
$host = 'localhost';
$db   = 'infoninjadb';
$user = 'root';
$pass = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
} catch (PDOException $e) {
    echo "Action failed: " . $e->getMessage();
}
?>