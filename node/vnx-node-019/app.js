// Triggers VNX-NODE-019: Hardcoded JWT or session secret
const jwt = require('jsonwebtoken');
const session = require('express-session');
const crypto = require('crypto');
const express = require('express');
const app = express();

// UNSAFE: hardcoded JWT secret in source code
app.post('/login', (req, res) => {
    const token = jwt.sign({ user: req.body.username }, 'my_super_secret_key_123');
    res.json({ token });
});

// UNSAFE: hardcoded session secret
app.use(session({
    secret: 'keyboard_cat_secret',
    resave: false,
    saveUninitialized: false,
}));

// UNSAFE: hardcoded HMAC key
const hmac = crypto.createHmac('sha256', 'hardcoded_hmac_key_value');

app.listen(3000);
