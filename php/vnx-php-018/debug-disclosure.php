<?php
// vnx-php-018 eval target: sensitive debug output disclosure
var_dump($_SESSION);  // TRIGGERS rule
print_r($_SERVER);  // TRIGGERS rule
var_export($_ENV, true);  // TRIGGERS rule
var_dump($_SERVER['DB_PASSWORD']);  // TRIGGERS rule
