// VNX-NODE-007: Node.js SQL injection
const mysql = require("mysql2");
const conn = mysql.createConnection({ host: "localhost" });

function getUser(req, res) {
  const id = req.params.id;
  conn.query("SELECT * FROM users WHERE id = " + id, (err, rows) => {
    res.json(rows);
  });
}
