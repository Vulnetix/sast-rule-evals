// Triggers VNX-NODE-021: XXE via libxmljs with noent:true
const libxmljs = require('libxmljs');
const express = require('express');
const app = express();

app.post('/parse-xml', (req, res) => {
    const userXml = req.body.xml;

    // UNSAFE: noent:true enables XXE - attacker can read /etc/passwd
    // Malicious XML: <?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>
    const doc = libxmljs.parseXmlString(userXml, { noent: true, noblanks: true });
    res.send(doc.toString());
});

app.listen(3000);
