<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Regestration</title>
    <style type="text/css" media="screen">
      .error { color: red; }
    </style>
  </head>
  <body>
    <h1>Regestration Results</h1>
    <?php
      $okay = true;
      
      //Check email
      if (empty($_POST['email'])) {
        print '<p class="error">Please enter your email address.</p>';
        $okay=false;
      }
      
      //Check Password
      if (empty($_POST['password'])) {
        print '<p class="error">Please enter a password.</p>';
        $okay=false;
      }
      else if ($_POST['password'] != $_POST['confirm']) {
        print '<p class="error">Passwords do not match.</p>';
        $okay=false;
      }
      
      //Check Year 
      if (is_numeric($_POST['year']) AND (strlen($_POST['year']) == 4)) {
        if ($_POST['year'] < 2026) {
          $age = 2026 - $_POST['year'];
        } 
        else {
          print '<p class ="error">Invalid year! Website may need an update or you are from the future.</p>';
          $okay = false;
        }
      }
      else {
        print '<p class ="error">Invalid year! Please enter a 4 digit year.</p>';
        $okay = false;
      }
      
      if (!isset($_POST['terms'])) {
        print '<p class="error">You must accept the terms.</p>';
        $okay = false;
      }
      
      //Output
      if ($okay) {
        print '<p>Your registration is valid.</p>';
        print "<p>You will be $age this year. (2026)</p>";
      }
      else{
        print '<p>Your registration contains errors please take a look above and try again.</p>';
      }
    ?>
  </body>
</html>