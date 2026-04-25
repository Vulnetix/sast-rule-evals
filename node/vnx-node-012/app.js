// VNX-NODE-012: Client-side XSS
function displayMessage(msg) {
  document.getElementById("output").innerHTML = msg;
  document.write(msg);
}
