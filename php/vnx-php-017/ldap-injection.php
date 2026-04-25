<?php
// vnx-php-017 eval target: LDAP injection via user-controlled filter
$username = $_GET['username'];
$conn = ldap_connect("ldap://ldap.example.com");
$results = ldap_search($conn, "dc=example,dc=com", "(uid=" . $_GET['username'] . ")");  // TRIGGERS rule

// Another variant:
$filter = "(cn=" . $_POST['name'] . ")";
ldap_search($conn, "ou=users,dc=example,dc=com", $filter . $_REQUEST['extra']);  // TRIGGERS rule
