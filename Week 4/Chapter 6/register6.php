<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <p>Please complete this form to register:</p>
    <form action="handle_reg.php" method="post">
      <p>Email Adress: <input type="email" name="email" size="30"></p>
      <p>Password: <input type="password" name="password" size="20"></p>
      <p>Confirm Password: <input type="password" name="confirm" size="20"></p>
      <p>Date of birth: 
        <select name="month">
          <option value="">Month</option>
          <option value="1">January</option>
          <option value="2">Febuary</option>
          <option value="3">March</option>
          <option value="4">April</option>
          <option value="5">May</option>
          <option value="6">June</option>
          <option value="7">July</option>
          <option value="8">August</option>
          <option value="9">September</option>
          <option value="10">October</option>
          <option value="11">November</option>
          <option value="12">December</option>
        </select>
        <select name="day">
          <option value="">Day</option>
          <?php
            for ($lc = 1; $lc <= 31; $lc++) {
              print "<option value=\"$lc\">$lc</option>\n";
            }
          ?>
        </select>
      </p>
      <p>Favorite Color: <select name="color">
        <option value="">Pick One</option>
        <option value="red">Red</option>
        <option value="yellow">Yellow</option>
        <option value="green">Green</option>
        <option value="blue">Blue</option>
        <option value="pink">Pink</option>
        <option value="purple">Purple</option>
      </select></p>
      <p><input type="checkbox" name="terms"> Accept the secret terms?</p>
      <input type="submit" name="submit" value="Register">
    </form>
  </body>
</html>