// VNX-SEC-012: CORS wildcard misconfiguration
const express = require("express");
const cors = require("cors");
const app = express();

app.use(cors({origin: true}));

app.get("/api/data", (req, res) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.json({ secret: "data" });
});
