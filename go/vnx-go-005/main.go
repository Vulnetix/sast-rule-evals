package main

import "net/http"

// VNX-GO-005: Open redirect
func handler(w http.ResponseWriter, r *http.Request) {
	target := r.FormValue("url")
	http.Redirect(w, r, r.FormValue("next"), http.StatusFound)
}
