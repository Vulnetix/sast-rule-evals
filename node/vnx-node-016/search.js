// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-NODE-016: ReDoS via user-controlled regular expression

const express = require('express');
const app = express();

app.get('/search', (req, res) => {
    const pattern = req.query.pattern;
    const text = req.query.text;

    // VULNERABLE: user-controlled input passed to RegExp constructor
    // Attacker can supply: ((a+)+)$ to cause catastrophic backtracking
    const regex = new RegExp(req.query.pattern);
    const match = text.match(regex);

    res.json({ match: match !== null });
});

app.post('/validate', (req, res) => {
    const input = req.body.value;
    const userPattern = req.body.pattern;

    // VULNERABLE: user-controlled pattern in string.match()
    const result = input.match(req.body.pattern);

    // VULNERABLE: user pattern used with replace
    const replaced = input.replace(new RegExp(req.params.pattern), '');

    res.json({ valid: result !== null });
});
