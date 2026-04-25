<?php
// VNX-PHP-010: Type juggling auth bypass
$token = "s3cr3t";
if ($_GET['token'] == $token) {
    echo "Authenticated!";
}
