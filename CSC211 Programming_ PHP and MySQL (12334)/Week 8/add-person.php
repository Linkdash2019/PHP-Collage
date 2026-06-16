<?php
  define('TITLE', 'Add Person');
  include('header.html');
?>

<h2>Add person</h2>

<?php
//Handle input
$problem = false;
$passMatch = true;
$showForm = true;

if ($_SERVER['REQUEST_METHOD'] == 'POST') { 
	if (empty($_POST['fName'])) {
		$problem = true;
	}
  
  if (empty($_POST['lName'])) {
		$problem = true;
	}
  
  if (empty($_POST['email']) || (substr_count($_POST['email'], '@') != 1) ) {
		$problem = true;
	}
  
    if (empty($_POST['address'])) {
		$problem = true;
	}
  
  if (empty($_POST['city'])) {
		$problem = true;
	}
  
  if (empty($_POST['state'])) {
		$problem = true;
	}
  
  if (empty($_POST['phone'])) {
		$problem = true;
	}
	
	if (!$problem) { 
    require('dbConnect.php');
    $pdo = dbConnect();
    $sql = "INSERT INTO users (first_name, last_name, email, home_address, city, state, phone_number) 
            VALUES (:fName, :lName, :email, :address, :city, :state, :phone)";
    $stmt = $pdo->prepare($sql);
    
    $stmt->execute([
      'fName'   => $_POST['fName'],
      'lName'   => $_POST['lName'],
      'email'   => $_POST['email'],
      'address' => $_POST['address'],
      'city'    => $_POST['city'],
      'state'   => $_POST['state'],
      'phone'   => $_POST['phone']
    ]);
    
  
		$body = "Successfully added {$_POST['fName']} to the database.";
    print '<p class="text--success">'.$body.'</p>';
    print '<p><a href=index.php>Go Home</a></p>';
    
    $showForm = false;
		$_POST = [];
	
	} 
  else { 
		print '<p class="text--error">Please try again!</p>';	
	}

}
?>

<?php if ($showForm): ?>
  <form action="add-person.php" method="post">
    First Name: <input type="text" name="fName"><br>
    <?php if (empty($_POST['fName']) & ($problem)) { print '<p class="text--error">Please enter a first name!</p>'; } ?>
    
    Last Name: <input type="text" name="lName"><br>
    <?php if (empty($_POST['lName']) & ($problem)) { print '<p class="text--error">Please enter a last name!</p>'; } ?>
    
    Email: <input type="email" name="email" placeholder="example@example.com"><br>
    <?php if (empty($_POST['email']) & ($problem)) { print '<p class="text--error">Please enter a email!</p>'; } ?>
    
    Home Address: <input type="text" name="address"><br>
    <?php if (empty($_POST['address']) & ($problem)) { print '<p class="text--error">Please enter a address!</p>'; } ?>
    
    City: <input type="text" name="city"><br>
    <?php if (empty($_POST['city']) & ($problem)) { print '<p class="text--error">Please enter a home city!</p>'; } ?>
    
    State: <input type="text" name="state"><br>
    <?php if (empty($_POST['state']) & ($problem)) { print '<p class="text--error">Please enter a state!</p>'; } ?>
    
    Phone Number: <input type="tel" name="phone" placeholder="123-456-7890" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"><br>
    <?php if (empty($_POST['phone']) & ($problem)) { print '<p class="text--error">Please enter a phone number</p>'; } ?>
    <br>
    
    <button type="submit">Add Person</button>
  </form>
<?php endif; ?>


<?php include('footer.html'); ?>