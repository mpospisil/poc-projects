function showMessage() {  
 alert("Button was clicked!");  
 window.chrome.webview.hostObjects.clientHost.Run("xxx");  
}

function onPageLoad() {  
   console.log("Page loaded successfully!");  
   alert("onPageLoad 2");  
  window.chrome.webview.hostObjects.clientHost.PageLoaded();
}
