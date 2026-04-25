// Triggers VNX-NODE-018: JWT decoded without signature verification
const jwt = require('jsonwebtoken');
const express = require('express');
const app = express();

app.get('/profile', (req, res) => {
    const token = req.headers.authorization.split(' ')[1];

    // UNSAFE: jwt.decode() does not verify signature, expiry, or issuer
    // An attacker can craft any payload and it will be accepted
    const payload = jwt.decode(token);
    res.json({ user: payload.sub, role: payload.role });
});

// Also bad: accepting 'none' algorithm
app.post('/login', (req, res) => {
    const token = req.body.token;
    const payload = jwt.verify(token, 'secret', { algorithms: ['HS256', 'none'] });
    res.json(payload);
});

app.listen(3000);
