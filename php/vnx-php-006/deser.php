<?php
// VNX-PHP-006: PHP object injection
$data = $_POST['data'];
$obj = unserialize($data);
echo $obj->name;
