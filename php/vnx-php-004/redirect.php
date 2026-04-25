<?php
// VNX-PHP-004: Open redirect
$url = $_GET['url'];
header("Location: " . $_GET['next']);
exit;
