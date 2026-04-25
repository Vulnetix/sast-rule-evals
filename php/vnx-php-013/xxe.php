<?php
// vnx-php-013 eval target: XXE via LIBXML_NOENT flag
$xml = file_get_contents('php://input');
$data = simplexml_load_string($xml, 'SimpleXMLElement', LIBXML_NOENT);  // TRIGGERS rule

$doc = simplexml_load_file($_GET['file'], 'SimpleXMLElement', LIBXML_DTDLOAD);  // TRIGGERS rule
