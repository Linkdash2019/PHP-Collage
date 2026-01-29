<?php
  $aNumber = 12;
  $bNumber = 98437589720872345;

  $aString = "I am a string! 😀";
  $bString = "Spaghetti!";

  $aArray = array(
    "KEY1" => 1234,
    "KEY2" => 9876,
  );
  $bArray = array(
    "KEYa" => "The key to unlock this door is KEYa!",
    "KEYb" => "=> looks like a happy face.",
  );
  
  echo "Number Variables:<br>
    $aNumber<br>
    $bNumber<br>
    <br>
    String Variables:<br>
    $aString<br>
    $bString<br>
    <br>
    Arrays:<br>";
  print_r($aArray); 
  echo "<br>";
  print_r($bArray);
?>