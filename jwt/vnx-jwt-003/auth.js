// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JWT-003: JWT signing with hardcoded secret

const jwt = require('jsonwebtoken');

// VULNERABLE: hardcoded JWT secret in variable
const JWT_SECRET = "my-super-secret-key-that-is-hardcoded";

function signToken(payload) {
    // VULNERABLE: hardcoded string literal as signing secret
    return jwt.sign(payload, "hardcoded-jwt-secret-value-here", { expiresIn: '1h' });
}

function verifyToken(token) {
    // VULNERABLE: hardcoded secret in verify call
    return jwt.verify(token, "hardcoded-jwt-secret-value-here");
}

function createToken(user) {
    // VULNERABLE: secret string literal
    const token = jwt.sign(
        { id: user.id, email: user.email },
        "my-static-signing-key",
        { expiresIn: '24h' }
    );
    return token;
}
