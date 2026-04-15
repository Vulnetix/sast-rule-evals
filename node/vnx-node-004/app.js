const express = require("express");

// VNX-NODE-004: Express app missing security header middleware
const app = express();

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(3000);
