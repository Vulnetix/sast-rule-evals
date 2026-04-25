// VNX-SEC-013: Insecure cookie settings
const express = require("express");
const session = require("express-session");
const app = express();

app.use(session({
  secret: "keyboard cat",
  cookie: { secure: false, httpOnly: false }
}));
