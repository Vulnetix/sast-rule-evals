// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JWT-002: JWT token signed without expiration

const jwt = require('jsonwebtoken');

const SECRET = process.env.JWT_SECRET;

function createUserToken(userId) {
    // VULNERABLE: no expiresIn option - token never expires
    const token = jwt.sign({ userId: userId, role: 'user' }, SECRET);
    return token;
}

function createAdminToken(adminId) {
    // VULNERABLE: hardcoded secret and no expiration
    const token = jwt.sign({ adminId: adminId, role: 'admin' }, 'hardcoded-secret-key');
    return token;
}

function createSessionToken(user) {
    // VULNERABLE: missing expiry - sessions last forever
    return jwt.sign(
        { id: user.id, email: user.email },
        SECRET
    );
}
