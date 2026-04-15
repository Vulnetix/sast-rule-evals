import React from "react";

function UnsafeComponent({ htmlContent }) {
  // VNX-NODE-005: dangerouslySetInnerHTML
  return <div dangerouslySetInnerHTML={{ __html: htmlContent }} />;
}

function DirectInnerHTML() {
  const el = document.getElementById("target");
  // VNX-NODE-005: innerHTML assignment
  el.innerHTML = userInput;
}
