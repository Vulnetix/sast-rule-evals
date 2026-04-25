// VNX-NODE-009: Server-side request forgery
const express = require("express");
const app = express();

app.get("/proxy", async (req, res) => {
  const resp = await fetch(req.query.url);
  const data = await resp.json();
  res.json(data);
});
