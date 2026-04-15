const { exec, execSync } = require("child_process");

function runCommand(userInput) {
  // VNX-NODE-003: exec with template literal interpolation
  exec(`ls -la ${userInput}`, (err, stdout) => {
    console.log(stdout);
  });
}

function runSync(filename) {
  // VNX-NODE-003: execSync with string concatenation
  const output = execSync("cat " + filename);
  return output.toString();
}
