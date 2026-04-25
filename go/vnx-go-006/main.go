package main

import "net/http"

// VNX-GO-006: Server-side request forgery
func handler(w http.ResponseWriter, r *http.Request) {
	url := r.FormValue("url")
	resp, _ := http.Get(r.FormValue("target"))
	defer resp.Body.Close()
}
