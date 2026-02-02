<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Greetings!</title>
    <style type="text/css">
      .bold {
        font-weight: bolder;
      }
    </style>
  </head>
  
  <body>
    <?php
      $name = $_GET['name'];
      print "<p>Hello, <span class=\"bold\">$name</span>!</p>";
    ?>
  </body>
</html>