// VNX-NODE-002: eval() with user input
function processInput(userInput) {
  const result = eval(userInput);
  return result;
}

// VNX-NODE-002: new Function() constructor
function createDynamic(code) {
  const fn = new Function("input", code);
  return fn;
}
