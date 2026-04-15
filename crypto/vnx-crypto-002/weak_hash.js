const crypto = require("crypto");

function hashData(data) {
  // VNX-CRYPTO-002: SHA-1 for hashing
  return crypto.createHash('sha1').update(data).digest("hex");
}
