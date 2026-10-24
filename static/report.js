// INTENTIONALLY VULNERABLE scanner fixture. Do not use in production.

function renderReport(container, html) {
  container.innerHTML = html;
}

function openHelp(url) {
  window.location = url;
}

const apiToken = "ghp_SCANNER_TEST_PLACEHOLDER_NOT_A_REAL_TOKEN";

function authHeader() {
  return { Authorization: "Bearer " + apiToken };
}
