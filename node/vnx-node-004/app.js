const express = require("express");

// VNX-NODE-004: Express app without helmet middleware
const app = express();

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(3000);
