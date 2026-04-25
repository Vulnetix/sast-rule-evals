// Triggers VNX-NODE-020: Deprecated crypto.createCipher without IV
const crypto = require('crypto');

const password = 'user_password';
const data = 'sensitive data';

// UNSAFE: createCipher derives the same IV every time from the password
// For CTR/GCM/CCM modes this completely breaks confidentiality
const cipher = crypto.createCipher('aes-256-cbc', password);
let encrypted = cipher.update(data, 'utf8', 'hex');
encrypted += cipher.final('hex');

// UNSAFE: createDecipher is similarly deprecated
const decipher = crypto.createDecipher('aes-256-cbc', password);
let decrypted = decipher.update(encrypted, 'hex', 'utf8');
decrypted += decipher.final('utf8');

// SAFE alternative (not flagged):
// const iv = crypto.randomBytes(16);
// const safeCipher = crypto.createCipheriv('aes-256-cbc', key, iv);
