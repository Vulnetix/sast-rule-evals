<?php
// Triggers VNX-PHP-020: PHP curl SSL certificate verification disabled

$url = 'https://api.example.com/data';
$ch = curl_init($url);

// UNSAFE: disabling SSL certificate verification enables MITM attacks
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);
echo $response;
