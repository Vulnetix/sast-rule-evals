<?php
// Triggers VNX-PHP-025: PHP deprecated mcrypt encryption functions

$key = 'secret_key_12345';
$data = 'sensitive data to encrypt';

// UNSAFE: mcrypt was deprecated in PHP 7.1, removed in PHP 7.2
// Uses outdated algorithms and has not been maintained
$iv = mcrypt_create_iv(
    mcrypt_get_iv_size(MCRYPT_RIJNDAEL_256, MCRYPT_MODE_CBC),
    MCRYPT_DEV_URANDOM
);

$encrypted = mcrypt_encrypt(
    MCRYPT_RIJNDAEL_256,
    $key,
    $data,
    MCRYPT_MODE_CBC,
    $iv
);

$decrypted = mcrypt_decrypt(
    MCRYPT_RIJNDAEL_256,
    $key,
    $encrypted,
    MCRYPT_MODE_CBC,
    $iv
);

// Also triggers
mdecrypt_generic($handle, $encrypted);
