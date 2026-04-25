const _ = require("lodash");
const express = require("express");

// VNX-NODE-006: Prototype pollution via lodash merge
const app = express();
app.use(express.json());

app.post("/config", (req, res) => {
  const config = {};
  _.merge(config, req.body);
  res.json(config);
});

app.listen(3000);
