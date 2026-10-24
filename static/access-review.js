// INTENTIONALLY VULNERABLE scanner fixture. Do not use in production.

function renderDecision(container, html) {
  container.innerHTML = html;
}

function followLink(url) {
  window.location = url;
}

const reviewToken = "eyJ_SCANNER_TEST_PLACEHOLDER_NOT_A_JWT";

function authHeader() {
  return { Authorization: "Bearer " + reviewToken };
}
