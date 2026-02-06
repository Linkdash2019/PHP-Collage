<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
      $toungeTwister = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?";
      
      //Replace all instances of "wood" with "would"
      echo str_replace("wood", "would", $toungeTwister);
      
      //Count words
      echo "<br><br>Words in woodchuck toungetwister: " . str_word_count($toungeTwister) . "<br><br>";
      
      //Get the next 29 characters from string starting at offset 40 
      echo substr($toungeTwister, 40, 29);
    ?>
  </body>
</html>