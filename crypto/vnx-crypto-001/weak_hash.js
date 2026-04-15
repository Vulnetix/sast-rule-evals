const crypto = require("crypto");

function hashData(data) {
  // VNX-CRYPTO-001: MD5 for hashing
  return crypto.createHash('md5').update(data).digest("hex");
}
