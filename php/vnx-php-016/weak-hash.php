<?php
// vnx-php-016 eval target: weak hash function used for password
$password = $_POST['password'];
$hash = md5($password);  // TRIGGERS rule
$stored_password_hash = md5($user_input);  // TRIGGERS rule

$sha1_password = sha1($password);  // TRIGGERS rule

// Correct approach (not triggered):
// $hash = password_hash($password, PASSWORD_BCRYPT);
