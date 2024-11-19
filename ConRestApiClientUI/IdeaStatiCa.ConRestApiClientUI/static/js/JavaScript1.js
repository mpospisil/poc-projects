function showMessage() {
  alert("Button was clicked!");
  window.chrome.webview.hostObjects.clientHost.Run("xxx");
}
