<?php
// VNX-PHP-003: File inclusion with user-controlled path
$page = $_GET['page'];
include($page . '.php');
