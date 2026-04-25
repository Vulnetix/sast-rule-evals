<?php
// VNX-PHP-005: Server-side request forgery
$url = $_GET['url'];
$content = file_get_contents($_GET['target']);
echo $content;
