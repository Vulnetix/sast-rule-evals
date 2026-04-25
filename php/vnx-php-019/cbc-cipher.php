<?php
// vnx-php-019 eval target: insecure AES-CBC cipher mode
$encrypted = openssl_encrypt($data, 'AES-256-CBC', $key, 0, $iv);  // TRIGGERS rule
$decrypted = openssl_decrypt($data, 'aes-128-cbc', $key, 0, $iv);  // TRIGGERS rule

// Standalone cipher string reference also flagged:
$cipher = 'AES-256-CBC';  // TRIGGERS rule

// Correct approach (not triggered):
// $encrypted = openssl_encrypt($data, 'AES-256-GCM', $key, 0, $iv, $tag);
