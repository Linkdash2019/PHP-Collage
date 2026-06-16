<?php
  define('TITLE', 'Home');
  include('header.html');
?>

<?php
  require('dbConnect.php');
  $pdo = dbConnect();
  $stmt = $pdo->query("SELECT * FROM users");
  $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<h2>Home</h2>
<br>
<h3>People</h3>
<p>You can press on an id to delete that person from the database FOREVER. If a user is registered it will also deregister that user.</p>

  <table border="1" cellpadding="10">
  <thead>
    <tr>
      <th>Id</th>
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
        <td><?php 
          print '<p><a href=delete.php?id='.$user['id'].'>'.$user['id'].'</a></p>'; 
        ?></td>
        <td><?php 
          print '<p>'.$user['first_name'].' '.$user['last_name'].'</p>'; 
        ?></td>
        <td><?php echo htmlspecialchars($user['email']); ?></td>
        <td><?php echo htmlspecialchars($user['home_address']); ?></td>
        <td><?php echo htmlspecialchars($user['city']); ?></td>
        <td><?php echo htmlspecialchars($user['state']); ?></td>
        <td><?php echo htmlspecialchars($user['phone_number']); ?></td>
      </tr>
    <?php endforeach; ?>
  </tbody>
</table>
<p><a href=add-person.php>Add a person to the database</a></p>
<p><a href=areaCodeMatch.php>Sort by area code</a></p>

<?php 
  include('footer.html'); 
?>