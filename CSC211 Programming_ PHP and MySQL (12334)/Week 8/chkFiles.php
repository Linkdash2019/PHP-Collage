<?php
  define('TITLE', 'Check Files');
  include('header.html');
?>

<?php
  $files = scandir('files');
  foreach ($files as $file) {
    if (($file != ".") && ($file != '..')){
      print '<p>'.$file.'<br></p>';
    }
  }
?>

<?php include('footer.html'); ?>