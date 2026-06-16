<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Soup</title>
  </head>
  <body>
    <hi>Mmmm...soups</h1>
    <?php
      $soups = [
        'Monday' => 'Clam Chowder',
        'Tuesday' => 'White Chicken Chili',
        'Wednesday' => 'Vegetarian',
        'Sunday' => 'CLOSED'
      ];
      
      $count1 = count($soups);
      print "<p>The soup array originally had $count1 elements.</p>";
      
      $soups['Thursday'] = 'Potsticker Soup';
      $soups['Friday'] = 'Chicken Noodle';
      $soups['Saturday'] = 'Tomato';
      
      $count2 = count($soups);
      print "<p>The soup array now has $count2 elements.</p>";
      
      print_r($soups); 
    ?>
  </body>
</html>