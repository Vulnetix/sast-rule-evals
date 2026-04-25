// Triggers VNX-NODE-024: postMessage without origin validation
// Browser-side code that lacks origin checks

// UNSAFE: addEventListener('message') without checking event.origin
window.addEventListener('message', function(event) {
    // No origin check - any window can send messages here
    const data = JSON.parse(event.data);
    if (data.action === 'setToken') {
        localStorage.setItem('authToken', data.token);
    }
    document.getElementById('content').innerHTML = data.html;
});

// UNSAFE: postMessage to wildcard origin - any frame can receive this
function sendToFrame(data) {
    const iframe = document.getElementById('myframe');
    iframe.contentWindow.postMessage(JSON.stringify(data), "*");
}
