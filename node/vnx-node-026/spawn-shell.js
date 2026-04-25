// Triggers VNX-NODE-026: Child process spawn with shell:true
const { spawn, spawnSync } = require('child_process');
const express = require('express');
const app = express();

app.get('/run', (req, res) => {
    const filename = req.query.filename;

    // UNSAFE: shell:true passes command through shell, enabling injection
    // Attacker can pass filename=file.txt; cat /etc/passwd
    const proc = spawn('cat', [filename], { shell: true });
    let output = '';
    proc.stdout.on('data', (d) => output += d);
    proc.on('close', () => res.send(output));
});

app.post('/convert', (req, res) => {
    // UNSAFE: shell:true with user-controlled arguments via child_process
    const result = spawnSync('convert', [req.body.input, req.body.output], {
        shell: true,
        encoding: 'utf8'
    });
    res.json({ output: result.stdout });
});

app.listen(3000);
