// INTENTIONALLY VULNERABLE scanner fixture. Do not use in production.

function renderStatus(container, html) {
  container.innerHTML = html;
}

function openExport(url) {
  window.location = url;
}

const exportToken = "aud_SCANNER_TEST_PLACEHOLDER_NOT_A_TOKEN";

function authHeader() {
  return { Authorization: "Bearer " + exportToken };
}
