<?php
  require('dbConnect.php');
  $pdo = dbConnect();
  $sql = "DELETE FROM users WHERE id=:id;";
  $stmt = $pdo->prepare($sql);   
  $stmt->execute([
    'id'   => $_GET['id'],
  ]);
  
  header('Location: '."index.php");
?>
