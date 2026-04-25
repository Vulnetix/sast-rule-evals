<?php
// vnx-php-012 eval target: reflected XSS via echo/print of user input
echo $_GET['name'];  // TRIGGERS rule
echo "Hello " . $_POST['username'];  // TRIGGERS rule
print($_REQUEST['search']);  // TRIGGERS rule
printf("Welcome %s", $_GET['user']);  // TRIGGERS rule
