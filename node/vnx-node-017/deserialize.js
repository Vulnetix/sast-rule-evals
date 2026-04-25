// Triggers VNX-NODE-017: Deserialization of untrusted data via node-serialize
const serialize = require('node-serialize');
const express = require('express');
const app = express();

app.post('/restore', (req, res) => {
    // UNSAFE: deserializing user-supplied body with node-serialize
    // An attacker can send: {"rce":"_$$ND_FUNC$$_function(){require('child_process').execSync('id')}()"}
    const data = serialize.unserialize(req.body.data);
    res.json(data);
});

app.listen(3000);
