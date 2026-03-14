<?php
  define('TITLE', 'Register');
  include('header.html');
?>


<form action="calculator.php" method="post">

  <input type="number" name="num1"></input><br><br>
  
  <select name="operator">
    <option value="add">&ensp; &plus;</option>
    <option value="sub">&ensp; &minus;</option>
    <option value="mult">&ensp; &times;</option>
    <option value="div">&ensp; &divide;</option>
  </select><br><br>
  
  <input type="number" name="num2"></input><br><br>
  
  <button type="submit">Calculate</button>
  
</form>

<?php
  if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (is_numeric($_POST['num1']) && is_numeric($_POST['num2']) && isset($_POST['operator'])) {
      if ($_POST['operator'] == 'add'){$result = $_POST['num1']+$_POST['num2'];}
      elseif ($_POST['operator'] == 'sub') {$result = $_POST['num1']-$_POST['num2'];}
      elseif ($_POST['operator'] == 'mult') {$result = $_POST['num1']*$_POST['num2'];}
      elseif ($_POST['operator'] == 'div') {$result = $_POST['num1']/$_POST['num2'];}
      else {$result = 'Error';}
      
      print '<p>'.$result.'</p>';
    }
  }
?>

<?php 
  include('footer.html'); 
?>