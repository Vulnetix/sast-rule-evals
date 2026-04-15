<?php
$input = $_GET['cmd'];

// VNX-PHP-002: exec() with user input
exec($input, $output);

// VNX-PHP-002: system() with user input
system($input);
?>
