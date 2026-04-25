// VNX-NODE-008: Open redirect
const express = require("express");
const app = express();

app.get("/redirect", (req, res) => {
  res.redirect(req.query.url);
});
