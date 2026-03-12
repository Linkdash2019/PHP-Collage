<?php
  define('TITLE', 'Login');
  include('header.html');
?>

<h2>Login</h2>
<h4>Welcome Back!</h4>

<?php
//Handle input
$problem = false;
$passMatch = true;
$showForm = true;

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  require('dbConnect.php');
  $sql = "SELECT * FROM users WHERE email = :email LIMIT 1";
  $stmt = $pdo->prepare($sql);
  $stmt->execute(['email' => $_POST['email']]);
  $user = $stmt->fetch(PDO::FETCH_ASSOC);
  
  if (isset($user['email'])){
    if (($_POST['email']) != ($user['email']) OR !password_verify($_POST['password'], $user['password'])) {
  		$problem = true;
  	}
  }
  else{ $problem = true; }
	
	if (!$problem) {  
    print '<p class="text--success">Success! Redirecting...</p>';
    
    $showForm = false;
		$_POST = [];
	
	} 
  else { 
		print '<p class="text--error">Invalid email or password.</p>';	
	}
}
?>

<?php if ($showForm): ?>
  <form action="login.php" method="post">
    Email: <input type="email" name="email" placeholder="example@example.com"><br>
    Password: <input type="password" name="password"><br><br>
    <button type="submit">Login</button>
  </form>
<?php endif; ?>
<?php include('footer.html'); ?>