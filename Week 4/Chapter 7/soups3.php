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
        'Thursday' => 'Potsticker Soup',
        'Friday' => 'Chicken Noodle',
        'Saturday' => 'Tomato',
        'Sunday' => 'CLOSED'
      ];
      
      foreach ($soups as $day => $soup) {
        print "<p>$day:$soup</p>";
      }
    ?>
  </body>
</html>