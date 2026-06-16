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
      
      $wordCnt = str_word_count($posting);
      $posting = substr($posting,0,50);
      
      print "
        <p>Thank you $fullName for your post:</p>
        <p>$posting...</p>
        <p>($wordCnt words)</p>
      ";
    ?>
  </body>
</html>