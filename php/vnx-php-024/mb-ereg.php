<?php
// Triggers VNX-PHP-024: PHP mb_ereg_replace with variable options enabling eval modifier

$pattern = $_GET['pattern'];
$replacement = $_GET['replacement'];
$string = "Hello World";

// UNSAFE: options parameter is a variable - attacker can supply 'e' for eval
$options = $_GET['options'];
$result = mb_ereg_replace($pattern, $replacement, $string, $options);
echo $result;

// UNSAFE: hardcoded options with 'e' modifier - evaluates replacement as PHP code
$result2 = mb_ereg_replace('(\w+)', 'system("id")', $string, 'ieg');
echo $result2;

// UNSAFE: mb_eregi_replace with variable options
$result3 = mb_eregi_replace($pattern, $replacement, $string, $options);
