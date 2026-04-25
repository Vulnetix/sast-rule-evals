// VNX-SEC-022: Sensitive data in logs
function authenticate(user, password) {
  console.log("Login attempt with password: " + password);
  logger.info("Using api_key: " + config.api_key);
}
