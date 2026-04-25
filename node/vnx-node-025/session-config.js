// Triggers VNX-NODE-025: Insecure express-session configuration
const express = require('express');
const session = require('express-session');
const app = express();

// UNSAFE: secure:false means cookie is sent over plain HTTP
app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: true,
    saveUninitialized: true,
    cookie: {
        secure: false,      // triggers VNX-NODE-025: cookie sent over HTTP
        httpOnly: false,    // triggers VNX-NODE-025: JS can read session cookie
        maxAge: 86400000,
    }
}));

app.get('/', (req, res) => {
    res.send('Hello');
});

app.listen(3000);
