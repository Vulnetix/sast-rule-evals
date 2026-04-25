<?php
// Triggers VNX-PHP-023: PHP anonymous LDAP bind without password

$ldap = ldap_connect('ldap://ldap.example.com');
ldap_set_option($ldap, LDAP_OPT_PROTOCOL_VERSION, 3);

// UNSAFE: anonymous bind with empty string password
ldap_bind($ldap, 'cn=admin,dc=example,dc=com', '');

// UNSAFE: anonymous bind with NULL password
ldap_bind($ldap, 'cn=admin,dc=example,dc=com', NULL);

// UNSAFE: bind with only one argument (anonymous)
ldap_bind($ldap);

$results = ldap_search($ldap, 'dc=example,dc=com', '(objectClass=person)');
$entries = ldap_get_entries($ldap, $results);
