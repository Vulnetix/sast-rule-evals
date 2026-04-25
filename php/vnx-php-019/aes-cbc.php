<?php
// Triggers VNX-PHP-019: PHP insecure cipher mode (AES-CBC)

$key = openssl_random_pseudo_bytes(32);
$iv = openssl_random_pseudo_bytes(16);
$data = 'sensitive data';

// UNSAFE: AES-CBC is unauthenticated; vulnerable to padding oracle attacks
$encrypted = openssl_encrypt($data, 'AES-256-CBC', $key, 0, $iv);
$decrypted = openssl_decrypt($encrypted, 'AES-128-CBC', $key, 0, $iv);

// SAFE alternative:
// $encrypted = openssl_encrypt($data, 'AES-256-GCM', $key, 0, $iv, $tag);
