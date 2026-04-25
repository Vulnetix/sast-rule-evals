// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-SEC-024: OAuth token stored in localStorage

async function handleOAuthCallback(code) {
    const response = await fetch('/api/auth/token', {
        method: 'POST',
        body: JSON.stringify({ code }),
    });
    const data = await response.json();

    // VULNERABLE: access token stored in localStorage - accessible to XSS
    localStorage.setItem("access_token", data.access_token);

    // VULNERABLE: refresh token stored in localStorage
    localStorage.setItem("refresh_token", data.refresh_token);

    // VULNERABLE: ID token stored in localStorage
    localStorage.setItem("id_token", data.id_token);
}

function logout() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("id_token");
}

function getAuthHeader() {
    // VULNERABLE: token retrieved from insecure storage
    const token = localStorage.getItem("access_token");
    return `Bearer ${token}`;
}
