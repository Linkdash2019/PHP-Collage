<?php
  define('TITLE', 'Register');
  include('header.html');
?>

<h2>Registration form</h2>

<?php
//Handle input
$problem = false;
$passMatch = true;
$showForm = true;

if ($_SERVER['REQUEST_METHOD'] == 'POST') { //I wonder if using the array $_POST counts?
	if (empty($_POST['fName'])) {
		$problem = true;
	}
  
  if (empty($_POST['lName'])) {
		$problem = true;
	}
  
  if (empty($_POST['email']) || (substr_count($_POST['email'], '@') != 1) ) {
		$problem = true;
	}
  
  if (empty($_POST['password'])) {
		$problem = true;
	}

	if ($_POST['password'] != $_POST['cpassword']) {
		$problem = true;
    $passMatch = false;
	} 
	
	
	if (!$problem) { 
    $hashPass = password_hash($_POST['password'], PASSWORD_DEFAULT);
    
    require('dbConnect.php');
    $sql = "INSERT INTO users (first_name, last_name, email, home_address, city, state, phone_number, password) 
            VALUES (:fName, :lName, :email, :address, :city, :state, :phone, :pass)";
    $stmt = $pdo->prepare($sql);
    
    $stmt->execute([
      'fName'   => $_POST['fName'],
      'lName'   => $_POST['lName'],
      'email'   => $_POST['email'],
      'address' => $_POST['address'],
      'city'    => $_POST['city'],
      'state'   => $_POST['state'],
      'phone'   => $_POST['phone'],
      'pass'    => $hashPass
    ]);
    
  
		$body = "Thank you, {$_POST['fName']}, for registering!.";
    print '<p class="text--success">'.$body.'</p>';
    
    $showForm = false;
		$_POST = [];
	
	} 
  else { 
		print '<p class="text--error">Please try again!</p>';	
	}

}
?>

<?php if ($showForm): ?>
  <form action="register.php" method="post">
    First Name: <input type="text" name="fName"><br>
    <?php if (empty($_POST['fName']) & ($problem)) { print '<p class="text--error">Please enter your first name!</p>'; } ?>
    
    Last Name: <input type="text" name="lName"><br>
    <?php if (empty($_POST['lName']) & ($problem)) { print '<p class="text--error">Please enter your last name!</p>'; } ?>
    
    Email: <input type="email" name="email" placeholder="example@example.com"><br>
    <?php if (empty($_POST['email']) & ($problem)) { print '<p class="text--error">Please enter your email!</p>'; } ?>
    
    Home Address: <input type="text" name="address"><br>
    <?php if (empty($_POST['address']) & ($problem)) { print '<p class="text--error">Please enter your home address!</p>'; } ?>
    
    City: <input type="text" name="city"><br>
    <?php if (empty($_POST['city']) & ($problem)) { print '<p class="text--error">Please enter your home city!</p>'; } ?>
    
    State: <input type="text" name="state"><br>
    <?php if (empty($_POST['state']) & ($problem)) { print '<p class="text--error">Please enter your home state!</p>'; } ?>
    
    Phone Number: <input type="tel" name="phone" placeholder="123-456-7890" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"><br>
    <?php if (empty($_POST['phone']) & ($problem)) { print '<p class="text--error">Please enter your phone number</p>'; } ?>
    
    Password: <input type="password" name="password"><br>
    <?php if (empty($_POST['password']) & ($problem)) { print '<p class="text--error">Please enter a password!</p>'; } ?>
    
    Retype Password: <input type="password" name="cpassword"><br>
    <?php if (!$passMatch & ($problem)) { print '<p class="text--error">Passwords did not match!</p>'; } ?>
    <br>
    
    <button type="submit">Register</button>
  </form>
<?php endif; ?>


<?php include('footer.html'); ?>