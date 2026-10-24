// INTENTIONALLY VULNERABLE scanner fixture. Do not use in production.

function renderWelcome(container, html) {
  container.innerHTML = html;
}

function openWorkspace(url) {
  window.location = url;
}

const inviteToken = "inv_SCANNER_TEST_PLACEHOLDER_NOT_A_TOKEN";

function authHeader() {
  return { Authorization: "Bearer " + inviteToken };
}
