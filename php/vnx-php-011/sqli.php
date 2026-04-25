<?php
// vnx-php-011 eval target: SQL injection via string concatenation
$id = $_GET['id'];
$result = mysql_query("SELECT * FROM users WHERE id = " . $id);  // TRIGGERS rule

$name = $_POST['name'];
$res = mysqli_query($conn, "SELECT * FROM products WHERE name = '" . $name . "'");  // TRIGGERS rule

$email = $_REQUEST['email'];
pg_query($conn, "SELECT * FROM accounts WHERE email = '" . $email . "'");  // TRIGGERS rule
