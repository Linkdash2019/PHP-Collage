<?php
  define('TITLE', 'Home');
  include('header.html');
?>

  <?php
    require('dbConnect.php');
    $stmt = $pdo->query("SELECT * FROM users");
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
  ?>
  
  <h2>Home</h2>
  <br>
  <h3>People</h3>

  <table border="1" cellpadding="10">
      <thead>
          <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Home Address</th>
              <th>City</th>
              <th>State</th>
              <th>Phone Number</th>
          </tr>
      </thead>
      <tbody>
          <?php foreach ($users as $user): ?>
              <tr>
                  <td><?php echo htmlspecialchars($user['first_name']." ".$user['last_name']); ?></td>
                  <td><?php echo htmlspecialchars($user['email']); ?></td>
                  <td><?php echo htmlspecialchars($user['home_address']); ?></td>
                  <td><?php echo htmlspecialchars($user['city']); ?></td>
                  <td><?php echo htmlspecialchars($user['state']); ?></td>
                  <td><?php echo htmlspecialchars($user['phone_number']); ?></td>
              </tr>
          <?php endforeach; ?>
      </tbody>
  </table>
  
<?php 
  include('footer.html'); 
?>