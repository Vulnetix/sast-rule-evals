// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-GO-012: Go HTTP response header injection (CRLF)

package main

import (
	"net/http"
)

func handleRedirect(w http.ResponseWriter, r *http.Request) {
	// VULNERABLE: user-controlled query param passed directly to response header
	redirectURL := r.URL.Query().Get("redirect")
	w.Header().Set("Location", r.URL.Query().Get("redirect"))

	// VULNERABLE: form value injected into custom header
	w.Header().Add("X-Custom-Header", r.FormValue("header_value"))

	_ = redirectURL
	w.WriteHeader(http.StatusFound)
}
