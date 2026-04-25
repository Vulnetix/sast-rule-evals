// VNX-NODE-010: Path traversal
const express = require("express");
const fs = require("fs");
const path = require("path");
const app = express();

app.get("/file/:name", (req, res) => {
  const data = fs.readFileSync(req.params.name);
  res.send(data);
});
