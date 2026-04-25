<?php
// VNX-PHP-009: preg_replace /e modifier
$input = $_GET['input'];
$result = preg_replace('/(\w+)/e', 'strtoupper("$1")', $input);
echo $result;
