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
      if (is_numeric($_POST['year'])) {
        $age = 2026 - $_POST['year'];
      }
      else{
        print '<p class ="error">Please enter the year you were born as four digits.</p>';
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