<?php
// vnx-php-015 eval target: unrestricted file upload via move_uploaded_file
$target = '/var/www/uploads/' . $_FILES['file']['name'];
move_uploaded_file($_FILES['file']['tmp_name'], $target);  // TRIGGERS rule

// No MIME type validation, no extension whitelist, no path sanitization
