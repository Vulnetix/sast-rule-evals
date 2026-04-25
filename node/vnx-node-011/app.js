// VNX-NODE-011: Server-side template injection
const express = require("express");
const ejs = require("ejs");
const app = express();

app.get("/render", (req, res) => {
  const html = ejs.render(req.query.template, { user: "test" });
  res.send(html);
});
