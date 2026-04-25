// VNX-NODE-014: NoSQL injection in MongoDB
const express = require("express");
const app = express();
app.use(express.json());

app.post("/login", async (req, res) => {
  const user = await db.collection("users").findOne(req.body);
  res.json(user);
});
