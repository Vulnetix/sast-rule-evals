// Triggers VNX-NODE-022: Shell injection via shelljs exec()
const shell = require('shelljs');
const express = require('express');
const app = express();

app.get('/ping', (req, res) => {
    const host = req.query.host;

    // UNSAFE: shell.exec with user-controlled input
    // Attacker can pass host=8.8.8.8; cat /etc/passwd
    const result = shell.exec('ping -c 1 ' + host);
    res.send(result.stdout);
});

app.post('/process', (req, res) => {
    // UNSAFE: exec with request body data
    shell.exec(req.body.command);
    res.send('done');
});

app.listen(3000);
