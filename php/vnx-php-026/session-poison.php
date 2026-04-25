<?php
// Triggers VNX-PHP-026: PHP session poisoning via user-controlled session key

session_start();

// UNSAFE: user-controlled key used to write session variable
// Attacker can overwrite $_SESSION['is_admin'], $_SESSION['role'], etc.
$key = $_GET['key'];
$value = $_GET['value'];
$_SESSION[$_GET['key']] = $value;

// UNSAFE: variant where key comes from POST
$_SESSION[$_POST['field']] = $_POST['data'];

// UNSAFE: indirect user-controlled key
$sessionKey = $_REQUEST['session_var'];
$_SESSION[$sessionKey] = 'injected_value';
