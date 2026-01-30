<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Your Feedback</title>
  </head>
  
  <body>
    <?php
      //Enable error showing
      ini_set('display_errors', 1);
    
      //Put recived data into variables
      $title = $_POST['title'];
      $fName = $_POST['fName'];
      $lName = $_POST['lName'];
      $response = $_POST['response'];
      $comments = $_POST['comments'];
      
      //Show the recived data
      print 
        "<p>
          Thank you $title $fName $lName for your feedback of: <br>
          $response <br>
          $comments
        </p>"
    ?>
  </body>
</html>