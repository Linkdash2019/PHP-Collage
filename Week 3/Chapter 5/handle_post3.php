<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Fourm Post</title>
  </head>
  <body>
    <?php
      $fName = $_POST['fName'];
      $lName = $_POST['lName'];
      $posting = nl2br($_POST['posting'], false);

      $fullName = $fName . ' ' . $lName;
      
      print "
        <p>Thank you $fullName for your posting:</p>
        <p>$posting</p>
      ";
      
      $fullName = urlencode($fullName);
      $email = urlencode($_POST['email']);
      
      print "<p>Click <a href=\"thanks.php?name=$fullName&email=$email\">here</a> to continue</p>";
    ?>
  </body>
</html>