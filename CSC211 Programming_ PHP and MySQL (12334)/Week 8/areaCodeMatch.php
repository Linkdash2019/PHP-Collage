<?php
  define('TITLE', 'Area Code check');
  include('header.html');
?>


<?php
  require('dbConnect.php');
  $pdo = dbConnect();
  $stmt = $pdo->query("SELECT * FROM users");
  $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
  
  $organizedData = [];
  foreach ($users as $user){
    $userArea = substr($user['phone_number'], 0, 3);
    if (isset($organizedData[$userArea])) {
      $organizedData[$userArea][] = $user['first_name'].' '.$user['last_name'];
    }
    else{
      $organizedData[$userArea] = [];
      $organizedData[$userArea][] = $user['first_name'].' '.$user['last_name'];
    }
  }
  
  ksort($organizedData, SORT_NUMERIC);
  
  foreach ($organizedData as $code => $names) {
    print('<h2>'.$code.'</h2>');
    foreach ($names as $name) {
      print('<p>'.$name .'</p>');
    }
    echo ("<br>");
  }
?>

<?php 
  include('footer.html'); 
?>