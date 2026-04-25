<?php
// Triggers VNX-PHP-018: PHP sensitive debug output disclosure

// UNSAFE: var_dump of session data exposes auth tokens and credentials
var_dump($_SESSION);

// UNSAFE: print_r of server variables exposes file paths and configuration
print_r($_SERVER);

// UNSAFE: var_export of environment variables exposes secrets
var_export($_ENV);
