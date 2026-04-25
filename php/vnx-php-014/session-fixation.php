<?php
// vnx-php-014 eval target: session fixation via user-controlled session ID
session_id($_GET['sessid']);  // TRIGGERS rule
session_start();

$sid = $_COOKIE['session'];
session_id($sid);  // Not directly triggered (variable, not superglobal)

session_id($_POST['sid']);  // TRIGGERS rule
session_start();
