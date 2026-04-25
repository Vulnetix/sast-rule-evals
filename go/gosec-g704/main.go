package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	// G704: SSRF — user input flows into http.Get
	target := r.URL.Query().Get("url")
	resp, err := http.Get(target)
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	defer resp.Body.Close()
	fmt.Fprintf(w, "status: %d", resp.StatusCode)
}

func main() {
	http.HandleFunc("/proxy", handler)
	http.ListenAndServe(":8080", nil)
}
