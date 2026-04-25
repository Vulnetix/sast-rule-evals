// VNX-NODE-013: Command injection via child_process
const { exec } = require("child_process");

function runCommand(req, res) {
  const filename = req.query.file;
  exec(`ls -la ${filename}`, (err, stdout) => {
    res.send(stdout);
  });
}
