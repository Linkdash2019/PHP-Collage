<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Caculation Results</title>
    <style type="text/css">.number {font-weight:bold;}</style>
  </head>
  <body>
    <?php
      //Recived variables
      $price = $_POST['price'];
      $quantity = $_POST['quantity'];
      $discount = $_POST['discount'];
      $tax = $_POST['tax'];
      $shipping = $_POST['shipping'];
      $payments = $_POST['payments'];
      
      //Total cost caculation
      $total = $price * $quantity;
      $total = $total + $shipping;
      $total = $total - $discount;
      //Plus tax
      $taxrate = $tax / 100;
      $taxrate = $taxrate + 1;
      $total = $total * $taxrate;
      //Monthly payment calculation
      $monthly = $total / $payments;
      
      //Formatting
      $total = number_format($total, 2);
      $monthly = number_format($monthly, 2);
      
      print "<p>
        You have selected to purchase:<br>
        <span class=\"number\">$quantity</span> software licence for<br>
        $<span class=\"number\">$price</span> each plus a<br>
        $<span class=\"number\">$shipping</span> shipping cost at a<br>
        <span class=\"number\">$tax%</span> tax rate.<br>
        After your $<span class=\"number\">$discount</span> discount,<br> 
        the total cost is $<span class=\"number\">$total</span><br>
        Divided over <span class=\"number\">$payments</span> monthly payments,<br>
        that would be $<span class=\"number\">$monthly</span> each month.
      </p>"
    ?>
  </body>
</html>