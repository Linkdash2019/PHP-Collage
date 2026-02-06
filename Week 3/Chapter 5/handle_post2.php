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
      
      $htmlEntity = nl2br(htmlentities($_POST['posting']));
      $htmlStrip = nl2br(strip_tags($_POST['posting']));
      
      print "
        <p>Thank you $fullName for your posting:</p>
        <p>Original: $posting</p>
        <p>Entity: $htmlEntity</p>
        <p>Stripped: $htmlStrip</p>
      ";
    ?>
  </body>
</html>