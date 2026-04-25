package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	// G107: URL provided to HTTP request as taint input (SSRF risk)
	url := r.FormValue("url")
	resp, err := http.Get(url)
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	defer resp.Body.Close()
	fmt.Fprintf(w, "status: %d", resp.StatusCode)
}

func main() {
	http.HandleFunc("/fetch", handler)
	http.ListenAndServe(":8080", nil)
}
