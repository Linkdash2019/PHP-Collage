<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Fourm Post</title>
  </head>
  <body>
    <?php
      $fName = trim($_POST['fName']);
      $lName = trim($_POST['lName']);
      $posting = trim(nl2br($_POST['posting'], false));

      $fullName = $fName . ' ' . $lName;
      
      $wordCnt = str_word_count($posting);
      $posting = str_ireplace('secretBadWord', '[HIDDEN]', $posting);
      
      print "
        <p>Thank you $fullName for your post:</p>
        <p>$posting</p>
        <p>($wordCnt words)</p>
      ";
    ?>
  </body>
</html>