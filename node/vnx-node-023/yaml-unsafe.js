// Triggers VNX-NODE-023: Unsafe YAML.load() with untrusted input
const yaml = require('js-yaml');
const express = require('express');
const app = express();

app.post('/config', (req, res) => {
    // UNSAFE: yaml.load() executes !!js/eval and custom constructors
    // Attacker can send: "exploit: !!js/eval 'require(\"child_process\").execSync(\"id\")'"
    const config = yaml.load(req.body.yaml);
    res.json(config);
});

app.post('/settings', (req, res) => {
    // UNSAFE: YAML.load without safe schema
    const settings = YAML.load(req.body.data);
    res.json(settings);
});

// SAFE alternative (not flagged):
// const safeConfig = yaml.safeLoad(req.body.yaml);
// const safeConfig2 = yaml.load(req.body.yaml, { schema: yaml.FAILSAFE_SCHEMA });

app.listen(3000);
